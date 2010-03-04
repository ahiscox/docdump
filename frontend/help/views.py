# Create your views here.
# from django.shortcuts import render_to_response
# from django.http import HttpResponse
from frontend.help.models import Topic
from frontend.help.taconite import Taconite


def index (request):
    """ Help index """
    tac = _get_topic('nocontent')
    return tac.response()
    
def topic (request, topicid):
    """ Grab a topic from the database by ID """ 
    tac = _get_topic(topicid)
    return tac.response()

def _get_topic(topicslug):
    """
    Convenience method to grab a topic and return it to the as a taconite object. 
    Returns a simple response if topic does not exist.
    """
    
    try:
        """ 
        On success, return a Taconite xml document 
        """
        
        page = Topic.objects.get(slug=topicslug)
        tac = page.tac_load_page()
        # Don't need this updater, stupid, see .live() instead; 
        # tac.eval('helpUpdater();')
        return tac

        
    except Topic.DoesNotExist:
        """
        Return a taconite object xml doc informing the user we did not find topicslug
        """
        
        page = Topic.objects.get(slug='nocontent')
        tac = page.tac_load_page()
        # remove soon!
        # tac.eval('helpUpdater();')
        return tac
