#automate the task of creating a custom HTTP
exec { 'setup-nginx':
  command  => 'apt-get -y update &&
      apt-get -y install nginx &&
          sudo sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default &&
	      service nginx restart',
	        provider => shell,
		}
		