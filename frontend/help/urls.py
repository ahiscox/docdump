from django.conf.urls.defaults import *

urlpatterns = patterns('frontend.help.views',
    (r'^$', 'index'),
    (r'^topic/(?P<topicid>\w+)/$', 'topic'), 
)



