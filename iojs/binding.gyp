{
  "targets": [
    {
      "target_name": "Realm",
      "sources": [ 
        	"../src/object-store/object_accessor.cpp",
		    "../src/object-store/object_schema.cpp",
		    "../src/object-store/object_store.cpp",
		    "../src/object-store/results.cpp",
		    "../src/object-store/index_set.cpp",
		    "../src/object-store/schema.cpp",
		    "../src/object-store/transact_log_handler.cpp",
        "iorealm.cc",
        "realm.cc",
        "realmobject.cc",
        "realmresults.cc",
        "realmarray.cc",
        "realmschema.cc"
      ],
      "include_dirs": [ "../core/include", "../src/object-store" ],
      "cflags_cc": [ '-DREALM_ENABLE_REPLICATION', '-fexceptions', '-frtti', '-std=c++14' ],
      "ldflags": [ '-L../core/', '-lrealm' ],
      "xcode_settings" : {
        'OTHER_CFLAGS' : [ '-mmacosx-version-min=10.8', '-DREALM_ENABLE_REPLICATION', '-fexceptions', '-frtti', '-std=c++14', '-stdlib=libc++' ],
      },
    }
  ]
}