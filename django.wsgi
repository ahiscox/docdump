import os
import sys

sys.path.append('/home/dd/dd')
os.environ['DJANGO_SETTINGS_MODULE'] = 'frontend.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

