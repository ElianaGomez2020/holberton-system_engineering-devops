# Fix file .phpp to .php 
exec {'fix-file':
    command => 'sed -i "s/phpp/php/" /var/www/html/wp-settings.php',
    path    => ['/usr/bin', '/usr/sbin', '/usr/local/bin', '/usr/local/sbin'],
}
