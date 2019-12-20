#install ngnix with puppet and configurate a server
exce { 'config_server':
  provider => shell,
  command  => 'sudo apt-get update; sudo apt-get -y install nginx; echo "Holberton School" | sudo tee /var/www/html/index.nginx-debian.html; new="server_name _;\n\trewrite ^\/redirect_me https:\/\/www.youtube.com\/watch?v=x_WLgwoohSk&t=5s permanent ;"; sudo sed -i "s/server_name _;/$new/" /etc/nginx/sites-available/default; sudo nginx -t; sudo service nginx restart',
}