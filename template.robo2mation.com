server {
    listen 80;
    server_name {{DOMAIN}};
    location / {
        proxy_pass http://unix:/home/souyeb/{{DOMAIN}}.sock;;
    }
}