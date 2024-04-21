import os
import environ

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env('.env')

password = env('PASSWORD')

os.system(f'echo {password} | sudo -S python3 create_dynamic_nginx.py')