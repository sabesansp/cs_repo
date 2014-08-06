$oneHostNIOCv3VDS = {
    'vc' => {
       '[1]' => {
           'datacenter' => {
              '[1]' => {
                 'host' => 'host.[1].x.[x]'
              }
           },
          'dvportgroup' => {
             '[1]' => {
                'vds' => 'vc.[1].vds.[1]'
             }
          },
          'vds' => {
             '[1]' => {
                'datacenter' => 'vc.[1].datacenter.[1]',
                'vmnicadapter' => 'host.[1].vmnic.[1]',
                'configurehosts' => 'add',
                'host' => 'host.[1].x.[x]',
                'nioc' => 'enable',
                'niocversion'    => "version3",
                'version'        => "6.0.0",
             },
             '[2]' => {
                'datacenter' => 'vc.[1].datacenter.[1]',
                'nioc' => 'enable',
                'niocversion' => 'version3',
                'version' => '6.0.0',
             }
          },
       }
    },
};


