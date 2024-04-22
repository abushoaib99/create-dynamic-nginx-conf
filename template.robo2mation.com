server {
	server_name {{DOMAIN}};
	location = /favicon.ico { access_log off; log_not_found off; }

	location /static/ {
		root /opt/expo_DMSWF_v3;
	}

	location /media/ {
		alias /opt/expo_DMSWF_v3/media/;
	}
	location / {
		include proxy_params;
		proxy_pass http://unix:/opt/expo_DMSWF_v3/gunicorn.sock;
	}

    listen 443 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/robo2mation.com/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/robo2mation.com/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot
}

server {
    if ($host = {{DOMAIN}}) {
        return 301 https://$host$request_uri;
    } # managed by Certbot

server_name {{DOMAIN}};
    listen 80;
    return 404; # managed by Certbot
}