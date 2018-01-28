#### Date, 20, 27-2018

## Configuration

### Configure ssh-open-client:

1. sudo apt install openssh-client
2. ssh root@IP
3. adduser ano
4. sudo usermod -a -G sudo ano

### Configure ngnix in Ubuntu 16.04 :	

1. which nginx

   - /usr/sbin/nginx

2. sudo apt-get install nginx

3. systemctl status nginx

4. systemctl start nginx

5. http://127.0.0.1

6. cd /etc/nginx/sites-available

   - default

7. touch default

   - default.bak
   - default

8. vi default

   ```c++
   server {
     	listen 80;
     	server_name ano;
     
       root /var/www/example;
       index ano.html;
       location / {
           #include    uwsgi_params;
           #uwsgi_pass http://localhost:8080;
           #proxy_pass http://localhost:8080;
       }

       location /images/ {
           root /home/ano/Pictures/LL3.jpg;
       }
   }
   ```

   9. cd /etc/nginx/sites-enabled

   - rm default

   10. ln -s /etc/nginx/sites-available/default  /etc/nginx/sites-enabled/default

   11. cd /var/www

       - mkdir example

       - cd example

       - ano.html

       - vi ano.html

         ``````html
         <html>
             <head>
                 <title>Hello World</title>
             </head>
             <body>            
                 <p><button>Hello World!</button></p>
             </body>
         </html>
         ``````

         ​

   12. nginx -s reload

   13. http://127.0.0.1

   ### References:

   1. https://help.ubuntu.com/lts/serverguide/openssh-server.html
   2. http://nginx.org/en/docs/beginners_guide.html
   3. https://linode.com/docs/web-servers/nginx/how-to-configure-nginx/
   4. https://www.nginx.com/resources/admin-guide/reverse-proxy/