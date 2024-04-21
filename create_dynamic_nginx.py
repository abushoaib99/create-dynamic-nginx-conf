# Replace placeholders in the template with actual values
import os


def generate_config(domain):
    with open('template.robo2mation.com', 'r') as f:
        template = f.read()
    # config = template.replace('{{DOMAIN}}', domain).replace('{{BACKEND_SERVER}}', backend_server)
    config = template.replace('{{DOMAIN}}', domain)
    with open(f'/etc/nginx/sites-available/{domain}', 'w') as f:
        f.write(config)
        # Reload Nginx configuration
        os.system(f'sudo ln -s /etc/nginx/sites-available/{domain} /etc/nginx/sites-enabled/')
        os.system('sudo systemctl reload nginx')
        # os.system(f'sudo certbot --nginx -d {domain}')
        print("Created nginx config")

# Example usage
generate_config('onebank.robo2mation.com', )
