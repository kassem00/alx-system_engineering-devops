# fix_apache_500_error

exec { 'fix_apache_500_error':
  provider => 'shell',
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
}
