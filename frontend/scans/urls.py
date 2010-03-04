from django.conf.urls.defaults import *

urlpatterns = patterns('frontend.scans.views',
    (r'^$', 'index'),
    (r'^sort/', 'sort'),
    (r'^comments/(?P<scanid>\d+)/$', 'comments'),
    (r'^tag_form/(?P<scanid>\d+)/$', 'tag_form'),
    (r'^tag_add/(?P<scanid>\d+)/(?P<tagname>\w+)/$', 'tag_add'),
    (r'^tag_del/(?P<scanid>\d+)/(?P<tagname>\w+)/$', 'tag_del'),
    (r'^excerpt/(?P<scanid>\d+)/$', 'excerpt'),
    (r'^addtag/(?P<scanid>\d+)/(?P<tags>\w+)/$', 'addtag'),
    (r'^addcomment/', 'addcomment'),
    (r'^status/', 'status'), 
    (r'^scan/', 'scan'), 
    (r'^start/', 'start'),
)
