#!/usr/bin/python3
from __future__ import print_function
from subprocess import call
from os import path
import os

CURRENT_DIR = path.dirname(path.realpath(__file__))

os.chdir(CURRENT_DIR)
print('Setting up symlink for node_modules...')
os.makedirs('/home/ubuntu/.sympm/petreon/node_modules', exist_ok=True)
call(['ln', '-s', '/home/ubuntu/.sympm/petreon/node_modules', 'node_modules'])
call(['npm', 'install'])

os.chdir(path.join(CURRENT_DIR, 'api'))
call(['php', 'composer.phar', 'install'])

print('Setup done.')
