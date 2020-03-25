#install ngnix with puppet and configurate a server
exec { 'install':
  command  => 'sudo apt-get -y update && sudo apt-get -y install nginx && echo "Holberton School" > /var/www/html/index.nginx-debian.html && n_s="\\\trewrite ^/redirect_me https://www.youtube.com/ permanent;" && sudo sed -i "42i $n_s" /etc/nginx/sites-available/default && sudo service nginx start',
  provider => shell,
}