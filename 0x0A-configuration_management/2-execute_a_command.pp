#executed a command (kill proccess)
exec { 'killmenow':
  command  => 'pkill killmenow',
  provider => 'shell'
}