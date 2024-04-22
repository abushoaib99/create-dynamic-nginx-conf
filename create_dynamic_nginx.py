import os

template_name = 'template.robo2mation.com'
site_available_path = '/etc/nginx/sites-available/'
site_enabled_path = '/etc/nginx/sites-enabled/'
nginx_reload_command = 'sudo systemctl reload nginx'


def is_file_exists(file_path: str) -> bool:
    """
    Checks if the given file exists.
    :param file_path:
    :return: `True` if file exists, otherwise `False`
    """

    return os.path.exists(file_path)


def generate_config(domain):
    # Open template in read mode
    with open(template_name, 'r') as f:
        template = f.read()

    # Replace the domain into `template.robo2mation.com`
    config = template.replace('{{DOMAIN}}', domain)

    # create subdomain file
    with open(f'{site_available_path}{domain}', 'w') as f:
        # write into the created subdomain file
        f.write(config)

        file_path = f'{site_enabled_path}{domain}'
        # check given domain is exists in `sites-enabled` or not
        if is_file_exists(file_path) is False:
            # if file not exists, then create symbolic link
            os.system(f'sudo ln -s {site_available_path}{domain} {site_enabled_path}')

        # Reload Nginx configuration
        os.system(nginx_reload_command)

        print(f"Subdomain ({domain}) added to nginx configuration")


# Example usage
generate_config('onebank.robo2mation.com')
