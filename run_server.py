from os import path
import subprocess
import webbrowser
import os

CURRENT_PATH = path.dirname(path.realpath(__file__))

print("Setting up nginx's configuration file...")
with open('conf/nginx.template.conf', 'r') as template, open('conf/nginx.conf', 'w') as conf:
    conf.write(template.read().replace('$$root', CURRENT_PATH.replace('\\', '/')))

print('Running npm run dev...')
npm_run = subprocess.Popen(['node', 'scripts/start.js'], stdout=subprocess.PIPE)
print('Running php-cgi...')
php_cgi = subprocess.Popen(['php-cgi', '-b', '127.0.0.1:9000'])
print('Running nginx...')
nginx = subprocess.Popen(['nginx'])

try:
    next(None for line in npm_run.stdout if line == b'The app is running at:\n')

    print('Done! Server running at localhost:8080')
    webbrowser.open('http://localhost:8080')

    npm_run.wait()
except KeyboardInterrupt:
    print('Killing everyone...')
    php_cgi.kill()
    nginx.kill()
    npm_run.kill()
