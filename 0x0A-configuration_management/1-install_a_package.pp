#!/usr/bin/pup
# Using Puppet, install flask from pip3.

package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['werkzeug'],
}
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
