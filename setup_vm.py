#!/usr/bin/python3
from __future__ import print_function
from subprocess import call
from os import path
import os

CURRENT_DIR = path.dirname(path.realpath(__file__))

os.chdir(CURRENT_DIR)
print('Setting up symlink for node_modules...')
os.makedirs('/home/ubuntu/.sympm/petreon/node_modules', exist_ok=True)
if path.islink('node_modules'):
    print('Looks like you already got a symlink setup! Skipping...')
elif path.isdir('node_modules'):
    print('Hmm, interesting, you already got a non-symlinked folder setup')
    print('I will just make sure it works if you made it on Windows...')
    call(['npm', 'rebuild', 'node-sass'])
else:
    call(['ln', '-s', '/home/ubuntu/.sympm/petreon/node_modules', 'node_modules'])

call(['npm', 'install'])

os.chdir(path.join(CURRENT_DIR, 'api'))

if path.isfile('composer.lock'):
    call(['php', 'composer.phar', 'update'])
else:
    call(['php', 'composer.phar', 'install'])

print('Setup done.')
