from __future__ import print_function
from os import path
from string import Template
import subprocess
import webbrowser
import os
import sys
import shutil
import errno

class AtTemplate(Template):
    delimiter = '@'

VARIABLES = {
    'root': path.dirname(path.realpath(__file__)).replace('\\', '/'),
    'port': '8080' if os.name == 'nt' else '80',
    'fastcgi': '127.0.0.1:9000' if os.name == 'nt' else 'unix:/var/run/php/php7.0-fpm.sock'
}

print("Setting up nginx's configuration file...")
with open('conf/nginx.template.conf', 'r') as template, \
     open('conf/nginx.conf', 'w') as conf:
    conf.write(AtTemplate(template.read()).substitute(VARIABLES))

if os.name == 'posix':
    try:
        print("Overriding nginx's config files...")
        shutil.copyfile('conf/nginx.conf', '/etc/nginx/nginx.conf')
        print('Reloading nginx...')
        subprocess.call(['nginx', '-s', 'reload'])

        # We aren't reponsible for those :D
        php_cgi, nginx = (None,) * 2
    except IOError as e:
        if (e.errno == errno.EACCES):
            print('You need to run this script as root.', file=sys.stderr)
            sys.exit(1)
else:
    print('Running php-cgi...')
    php_cgi = subprocess.Popen(['php-cgi', '-b', '127.0.0.1:9000'])
    print('Running nginx...')
    nginx = subprocess.Popen(['nginx'])

print('Running npm run dev...')
npm_run = subprocess.Popen(['node', 'scripts/start.js'], stdout=subprocess.PIPE)

try:
    next(None for line in npm_run.stdout if line == b'The app is running at:\n')

    print('Done! Server running at localhost:' + VARIABLES['port'])
    webbrowser.open('http://localhost:' + VARIABLES['port'])

    npm_run.wait()
except KeyboardInterrupt:
    print('Killing everyone...')
    if php_cgi and nginx:
        php_cgi.kill()
        nginx.kill()
    npm_run.kill()
