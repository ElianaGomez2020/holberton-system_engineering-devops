#puppet_ssh_config.pp
file_line { 'IdentityFile':
  ensure  => present,
  replace => true,
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/holberton',
}

file_line { 'PasswordAuthentication':
  ensure  => present,
  replace => true,
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
}
