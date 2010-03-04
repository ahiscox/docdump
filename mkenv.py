#!/usr/bin/env python

# This script creates the 
# setup_docdump.py installer

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

# Simple patch to add header to top of generated setup script. 
# decode with patch.decode('base64').decode('zlib')
patch = """
eJxtkk+L2zAQxc/Np5gml5bEjp2yYTGlZMmh7SFLKKWlp6JIY1uLrBH6k62/fUdOUli2xmCQ5/dm
3tMURQEBY3K/FUmVBle6sSSj3myquiqqD/zCpmru7pt6W1a3B4rqvqpmy+XyFfwCrJvqrqk2r8Dd
Dop6tYVlvaq3sNvNYPF2nYJfn7Rdoz2DG2NPdlYsFvDz4dvj18fPDXzvdYBWGwT+dmjRi4iKa/6L
LhcXIEivXcxICqgg0mViEKDwjIbcgDbCGX3QF4pauLoBbbnsrH1MwmTpZx17eCfMQCG+B2EMazi0
Cq3UGCDTIkUaRNSS/47gMZA5o1qxlDRJaduxYsvHPXQslk4gDVnkphmOPYJhUyG+GI48DCJE9Kzn
KJRTo6MR1rIhNibgWYzZ2cvmkmyru+Rx0lVPwnY0jWgV7Hv0fjyOwLa0J5v7XIX/JTeQSpewnfAx
5zLpXLNxnp5QxhX8Ohx+lBk6ELfStiWfZyALUlg4IbSUuKOI0MfomvX6tiuS2GkpJbMZ35Mbve76
CHmD4MHmaxzhiw6S/sDHK7W7UZ8yBvP5fO+RI+MQ5tebmsNxWgGeJUROYhpmKp3B7C8KX/Dv"""
# print patch.decode('base64').decode('zlib')

# Open a tmp patch file and write the decoded patch to it.
f=open('.tmp_patch','w+').write(patch.decode('base64').decode('zlib'))

# apply the patch
os.system('patch setup_docdump.py < .tmp_patch') 

# remove the patch file. 
os.system('rm .tmp_patch')

# Make script executable. 
os.system('chmod +x setup_docdump.py') 
