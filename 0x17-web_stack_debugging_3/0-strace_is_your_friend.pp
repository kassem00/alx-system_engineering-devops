# fix_apache_500_error

exec { 'fix_apache_500_error':
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  onlyif  => 'test -f /var/www/html/wp-settings.php',
  path    => ['/bin', '/usr/bin'],
}
