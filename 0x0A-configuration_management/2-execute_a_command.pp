# create manifiest that kills
exec { 'killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin',
}
