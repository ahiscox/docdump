#!/usr/bin/env python

# This simple script sets up a virtualenv 
# for docdumps python files.

import virtualenv, textwrap, os
output = virtualenv.create_bootstrap_script(textwrap.dedent("""
import os, subprocess
def after_install(options, home_dir):
    etc = join(home_dir, 'etc')
    if not os.path.exists(etc):
        os.makedirs(etc)

    easy_install = join(home_dir, 'bin', 'easy_install') 

    subprocess.call([easy_install, '-U', 'supervisor']) 
    subprocess.call([easy_install, '-U', 'django'])
    subprocess.call([easy_install, '-U', 'cherrypy'])
    subprocess.call(['git', 'clone', 'git@github.com:ahiscox/docdump.git', join(home_dir, 'docdump')])
"""))
f = open('setup_docdump.py', 'w').write(output)
os.system('chmod +x setup_docdump.py') 
