my_sql project DEVos

task.

0. install mysql in both my servers web.

$ echo 'deb http://repo.mysql.com/apt/ubuntu/ trusty mysql-5.7-dmr' | sudo tee -a /etc/apt/sources.list      # download repo
$ sudo apt-get update               # updates the packages
$ sudo apt-get install mysql-server-5.7   # install mysql 5.7.x