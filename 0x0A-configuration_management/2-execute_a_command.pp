#executed a command (kill process)
exec { 'killmenow':
  command  => 'pkill killmenow',
  provider => 'shell'
}