{
	'includes':
	[
		'../common.gypi',
	],

    'variables':
    {
        'conditions':
        [
            [
                'host_os == "linux"',
                {
                    'server-engine': '<(PRODUCT_DIR)/server-community',
                    'dev-engine': '<(PRODUCT_DIR)/LiveCode-Community',
                    'standalone-engine': '<(PRODUCT_DIR)/standalone-community',     
                    'lc-run': '<(PRODUCT_DIR)/lc-run',                             
                },
            ],
            [
                'host_os == "mac"',
                {
                    'server-engine': '<(PRODUCT_DIR)/server-community',
                    'dev-engine': '<(PRODUCT_DIR)/LiveCode-Community.app/Contents/MacOS/LiveCode-Community',
                    'standalone-engine': '<(PRODUCT_DIR)/Standalone-Community.app/Contents/MacOS/Standalone-Community',   
                    'lc-run': '<(PRODUCT_DIR)/lc-run',
                },
            ],
            [
                'host_os == "win"',
                {
                    'server-engine': '<(PRODUCT_DIR)/server-community.exe',
                    'dev-engine': '<(PRODUCT_DIR)/LiveCode-Community.exe',
                    'standalone-engine': '<(PRODUCT_DIR)/standalone-community.exe',   
                    'lc-run': '<(PRODUCT_DIR)/lc-run.exe',
                },
            ],
        ],
    },
    
    'conditions':
    [
    	[
			'host_os == "win"',
			{
				'targets':
				[
					{
						'target_name': 'make-standalone-console',
						'type': 'none',			
					
						'dependencies':
						[
							'../engine/engine.gyp:standalone',
						],
					
						'actions':
						[
							{
								'action_name': 'editbin-standalone',

								'inputs':
								[
									'<(PRODUCT_DIR)/standalone-community.exe',
								],

								'outputs':
								[
									# hack because gyp wants an output
									'notarealfile.txt',
								],

								'message': 'Making standalone a console application',

								'action':
								[
									'EDITBIN.EXE',
									'/SUBSYSTEM:CONSOLE',
									'<(standalone-engine)'
								],
							},
						],											
					},
				],
			}, 
		], 	
    ],
    
    'targets':
    [
		{
			'target_name': 'tests-run-all',
			'type': 'none',

			'dependencies':
			[
			    '../livecode.gyp:LiveCode-all'
				'lcs-check',
				#'lcs-server-check',
				#'lcb-check',				
			],

		},	
		{
			'target_name': 'check-compile-modules',
			'type': 'none',

			'actions':
			[
				{
					'action_name': 'check-compile-modules',

					'inputs':
					[
						'test-extensions-utils.lc',
					],

					'outputs':
					[
						# hack because gyp wants an output
                        'notarealfile.txt',
					],

					'message': 'Compiling modules for tests',

					'action':
					[
						'<(server-engine)',
						'test-extensions-utils.lc',
						'$(not_a_real_variable)findandcompile',
						'../tests',
						'../_tests/_build',
					],
				},
			],			
		},	
		{
			'target_name': 'lcb-check',
			'type': 'none',

			'dependencies':
			[
				'check-compile-modules',
			],
			
			'actions':
			[
				{
					'action_name': 'lcb_check',

					'inputs':
					[
					    'test-extensions-utils.lc',
						'_testrunner.lcb',
						'_testlib.lcb',
					],

					'outputs':
					[
						# hack because gyp wants an output
                        'notarealfile.txt',
					],

					'message': 'Testing standalone engine',
					
					'action':
					[
						'<(server-engine)',
						'test-extensions-utils.lc',
						'$(not_a_real_variable)lcruntests',
						'../tests/lcb', # Must have 'tests' in it
						'../_tests/_build',
						'<(lc-run)',
						'../_tests/_build/_testrunner.lcm',
						'../_tests/_build/_testlib.lcm',
					],
				},
			],
		},				
		{
			'target_name': 'lcs-check-extensions-compile',
			'type': 'none',

			'actions':
			[
				{
					'action_name': 'build_extensions',

					'inputs':
					[
						'test-extensions-utils.lc',
					],

					'outputs':
					[
						# hack because gyp wants an output
                        'notarealfile.txt',
					],

					'message': 'Building extensions for lcs tests',

					'action':
					[
						'<(server-engine)',
						'test-extensions-utils.lc',
						'$(not_a_real_variable)findandbuild',
						'lcs/extensions',
						'dummy',
						'../_tests/_build/packaged_extensions',
						'$(not_a_real_variable)false',
						'>(lc-compile_host)',
						'<(PRODUCT_DIR)/modules/lci',
					],
				},
			],			
		},
		{
			'target_name': 'lcs-check-deps',
			'type': 'none',

			'dependencies':
			[
				'lcs-check-extensions-compile',
				'check-compile-modules',
			],		
			
			'conditions':
			[
				[
					'host_os == "win"',
					{
						'dependencies':            
						[
							'make-standalone-console',
						],
					},		
                ],		
			],				
		},
		{
			'target_name': 'lcs-check',
			'type': 'none',

			'dependencies':
			[
				'lcs-check-deps',
				'../engine/engine.gyp:standalone',
			],
			
			'actions':
			[
				{
					'action_name': 'lcs_check',

					'inputs':
					[
						'_testrunner.livecodescript',
					],

					'outputs':
					[
						# hack because gyp wants an output
                        'notarealfile.txt',
					],

					'message': 'Testing standalone engine',

					'action':
					[
						'<(standalone-engine)',
						'<@(_inputs)',
						'$(not_a_real_variable)run',
						'lcs',
					],
				},
			],
		},
		{
			'target_name': 'lcs-server-check',
			'type': 'none',

			'dependencies':
			[
				'lcs-check-deps',
			],
			
			'actions':
			[
				{
					'action_name': 'lcs_server_check',

					'inputs':
					[
						'_testrunner.lc',
					],

					'outputs':
					[
						# hack because gyp wants an output
                        'notarealfile.txt',
					],

					'message': 'Testing server engine',

					'action':
					[
						'<(server-engine)',
						'<@(_inputs)',
						'$(not_a_real_variable)run',
						'lcs',
					],
				},
			],
		},
	],
}