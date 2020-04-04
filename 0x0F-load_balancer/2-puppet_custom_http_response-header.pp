#!/usr/bin/env bash                                              
#configures a brand new Ubuntu machine

exec {'Install nginx':
command  => 'sudo apt-get -y update && sudo apt-get -y install nginx && sudo sed -i "15i add_header X-Served-By \$hostname;" /etc/nginx/nginx.conf && sudo service nginx restart',
provider => shell,
}