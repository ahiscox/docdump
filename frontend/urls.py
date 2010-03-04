from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import djapian
djapian.load_indexes()

urlpatterns = patterns('',
    # Example:
    # (r'^frontend/', include('frontend.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^scan/', include('frontend.scans.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^tickets/', include('frontend.tickets.urls')),
    (r'^help/', include('frontend.help.urls')),
    (r'^search/', include('frontend.search.urls')),
    (r'^dojango/', include('frontend.dojango.urls')),

)
