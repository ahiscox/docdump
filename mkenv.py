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
    subprocess.call([easy_install, '-U', 'mysql-python'])
    subprocess.call(['git', 'clone', 'git@github.com:ahiscox/docdump.git', join(home_dir, 'docdump')])
"""))
f = open('setup_docdump.py', 'w').write(output)

# Apply a patch to output source to use --no-site-packages

patch = r"""
--- setup_docdump.py.old	2010-03-03 18:25:21.000000000 -0800
+++ setup_docdump.py	2010-03-03 18:27:33.000000000 -0800
@@ -446,11 +446,15 @@
         help="Clear out the non-root install and start from scratch")
 
     parser.add_option(
-        '--no-site-packages',
+        '--use-site-packages',
         dest='no_site_packages',
-        action='store_true',
-        help="Don't give access to the global site-packages dir to the "
-             "virtual environment")
+        action='store_false',
+        default=True,
+        help="Give access to the global site-packages. "
+             "This defaults to not using site packages. "
+             "This command used to be --no-site-packages "
+             "but was patch by docdump project to use "
+             "a isolated environment by default ")
 
     parser.add_option(
         '--unzip-setuptools',
"""
f = open('.setup_docdump.py.patch', 'w+').write(patch)
os.system('patch setup_docdump.py < .setup_docdump.py.patch') 
os.system('chmod +x setup_docdump.py') 
os.system('rm .setup_docdump.py.patch') 
