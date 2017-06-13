{
	'includes':
	[
		'../common.gypi',
	],
	
	'targets':
	[
		{
			'target_name': 'libcef',
			'type': 'none',
			
			'dependencies':
			[
				'fetch.gyp:fetch',
			],
			
			'direct_dependent_settings':
			{
				'defines':
				[
					'USING_CEF_SHARED=1',
				],
			},
						
			'conditions':
			[   
                [
				    'OS == "win"',
				    {
					    'copies':
					    [
						    {
							    'destination':'<(PRODUCT_DIR)/CEF/',
							    'files':
							    [
								    'lib/win32/<(target_arch)/CEF/cef.pak',
								    'lib/win32/<(target_arch)/CEF/cef_100_percent.pak',
								    'lib/win32/<(target_arch)/CEF/cef_200_percent.pak',
								    'lib/win32/<(target_arch)/CEF/cef_extensions.pak',
								    'lib/win32/<(target_arch)/CEF/d3dcompiler_43.dll',
								    'lib/win32/<(target_arch)/CEF/d3dcompiler_47.dll',
								    'lib/win32/<(target_arch)/CEF/devtools_resources.pak',
								    'lib/win32/<(target_arch)/CEF/icudtl.dat',
								    'lib/win32/<(target_arch)/CEF/libcef.dll',
								    'lib/win32/<(target_arch)/CEF/libEGL.dll',
								    'lib/win32/<(target_arch)/CEF/libGLESv2.dll',
								    'lib/win32/<(target_arch)/CEF/natives_blob.bin',
								    'lib/win32/<(target_arch)/CEF/snapshot_blob.bin',
								    'lib/win32/<(target_arch)/CEF/widevinecdmadapter.dll',
							    ],
						    },
                            {
                                'destination': '<(PRODUCT_DIR)/CEF/locales',
                                'files':
                                [
                                    'lib/win32/<(target_arch)/CEF/locales/am.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/ar.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/bg.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/bn.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/ca.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/cs.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/de.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/el.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/en-GB.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/en-US.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/es.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/es-419.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/et.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/fa.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/fi.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/fil.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/fr.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/gu.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/he.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/hi.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/hr.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/hu.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/id.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/it.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/ja.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/kn.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/ko.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/lt.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/lv.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/ml.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/mr.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/ms.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/nb.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/nl.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/pl.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/pt-BR.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/pt-PT.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/ro.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/ru.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/sk.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/sl.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/sr.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/sv.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/sw.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/ta.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/te.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/th.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/tr.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/uk.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/vi.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/zh-CN.pak',
                                    'lib/win32/<(target_arch)/CEF/locales/zh-TW.pak',
                                ],
                            },
                        ],

					    'all_dependent_settings':
					    {
						    'variables':
						    {
							    # Gyp will only use a recursive xcopy if the path ends with '/'
							    'dist_aux_files': [ 'lib/win32/<(target_arch)/CEF/', ],
						    },
					    },
				    },
				],
				
				[
				    'OS == "linux"',
                    {
                        'copies':
                        [
                            {
                                'destination': '<(PRODUCT_DIR)/',
                                'files':
                                [
                                    'lib/linux/<(target_arch)/CEF/natives_blob.bin',
                                    'lib/linux/<(target_arch)/CEF/snapshot_blob.bin',
                                    'lib/linux/<(target_arch)/CEF/icudtl.dat',
                                ],
                            },
                            {
                                'destination': '<(PRODUCT_DIR)/Externals/CEF',
                                'files':
                                [
                                    'lib/linux/<(target_arch)/CEF/cef.pak',
                                    'lib/linux/<(target_arch)/CEF/cef_100_percent.pak',
                                    'lib/linux/<(target_arch)/CEF/cef_200_percent.pak',
                                    'lib/linux/<(target_arch)/CEF/cef_extensions.pak',
                                    'lib/linux/<(target_arch)/CEF/devtools_resources.pak',
                                    'lib/linux/<(target_arch)/CEF/libcef.so',
                                ],
                            },
                            {
                                'destination': '<(PRODUCT_DIR)/Externals/CEF/locales',
                                'files':
                                [
                                    'lib/linux/<(target_arch)/CEF/locales/am.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/ar.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/bg.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/bn.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/ca.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/cs.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/de.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/el.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/en-GB.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/en-US.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/es.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/es-419.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/et.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/fa.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/fi.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/fil.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/fr.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/gu.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/he.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/hi.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/hr.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/hu.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/id.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/it.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/ja.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/kn.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/ko.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/lt.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/lv.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/ml.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/mr.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/ms.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/nb.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/nl.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/pl.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/pt-BR.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/pt-PT.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/ro.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/ru.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/sk.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/sl.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/sr.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/sv.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/sw.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/ta.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/te.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/th.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/tr.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/uk.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/vi.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/zh-CN.pak',
                                    'lib/linux/<(target_arch)/CEF/locales/zh-TW.pak',
                                ],
                            },
                        ],
                        
					    'all_dependent_settings':
					    {
						    'variables':
						    {
							    'dist_aux_files':
                                [
                                    '<(PRODUCT_DIR)/Externals/',
                                    '<(PRODUCT_DIR)/natives_blob.bin',
                                    '<(PRODUCT_DIR)/snapshot_blob.bin',
                                    '<(PRODUCT_DIR)/icudtl.dat',
                                ],
						    },
					    },
				    },
				],
			],
		},
	],
}
