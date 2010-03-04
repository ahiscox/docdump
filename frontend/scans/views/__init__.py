# TODO: Get rid of all these fucking imports!
# TODO: Read under TAG HANDLERS, I've got some todos that are priority
# TODO: Move some stuff over to scans.views.tags.AjaxTag and AjaxComment
# TODO: I want the tags list output in a multiple select element, not drop down.
#  


from django.shortcuts import render_to_response
from frontend.scans.models import Scan, ScanStatus, Comment, Tag
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.template import loader
from django.http import HttpResponse
from frontend.taconite import Taconite


def sort(request):
    """
        - Sort documents that have not been processed yet.
        - Quickly apply tags and comments to each scan.
    """
    unprocessed = Scan.objects.filter(processed__gt=0)


    response = { 'unprocessed' : unprocessed, }
    
    return render_to_response('scans/sort.html', response)

def excerpt(request, scanid):
    """ Return excerpt for article """
    scan = Scan.objects.get(pk=scanid)
    return _page('scans/get_excerpt.xml',
              {'id' : scanid, 'scan' : scan})

def _page (template, templatevars):
    page = loader.render_to_string(template, templatevars)
    return HttpResponse(page, mimetype="application/xml")


### TAG HANDLERS

def tag_form(request, scanid): 
    from frontend.scans.views.tags import AjaxTag
    
    tag = AjaxTag()
    taconite = tag.form(scanid)
    return HttpResponse(taconite, mimetype="application/xml") 

def tag_add(request, scanid, tagname): 
    from frontend.scans.views.tags import AjaxTag
    
    tag = AjaxTag()
    rtn = tag.add(scanid, tagname)
    return HttpResponse(rtn)

def tag_del(request, scanid, tagname):
    from frontend.scans.views.tags import AjaxTag

    tag = AjaxTag()
    rtn = tag.delete(scanid, tagname)
    return HttpResponse(rtn)

def status(request):
    """ Returns information on a running scan """ 

    s = ScanStatus.objects.get(pk=1)
    rtn = '%s:%s:%s' % (str(s.in_progress), str(s.percent), str(s.message))

    return HttpResponse(rtn)

def start(request): 
    """ Starts a scan, if it does not already exist """ 
    import xmlrpclib

    s = xmlrpclib.Server('http://localhost:9001')
    s.supervisor.startProcess('ddbackend')

    return HttpResponse('ok')

def scan(request): 
    """ Return a scan page """ 
    
    return render_to_response('scans/scan.html') 

