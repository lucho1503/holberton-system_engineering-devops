# create a file in the path /tmp/holberton
file { '/tmp/holberton':
     mode	=> '0744',
     owner	=> 'www-data',
     group	=> 'www-data',
     content	=> 'I love Pupeet'
}
