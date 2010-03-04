from django.conf.urls.defaults import *

urlpatterns = patterns('frontend.search.views',
    (r'^$', 'query'),
)
