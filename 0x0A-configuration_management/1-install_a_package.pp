# Puppet installer
package { 'puppet-lint':
    source   => 'https://rubygems.org',
    ensure   => '2.5.0',
    provider => 'gem',
}
