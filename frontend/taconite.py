from django.http import HttpResponse

class Taconite(object):
    """Support class to make taconite responses easier to format.
    
    The method names and arguments reflect those in the jQuery 
    aconite API.  These are the ones I personally needed. Feel
    free to add more methods as needed.
    """
    
    def __init__(self):
        self._xml = []

    def _add(self, stuff):
        # this could be more elaborate for debugging
        self._xml.append(stuff)

    def remove(self, select):
        self._add('<remove select="%s" />' % (select, ) )

    def hide(self, select):
        self._add('<hide select="%s" />' % (select, ) )

    def addClass(self, select, arg):
        self._add('<addClass select="%s" arg1="%s" />' % (select, arg ) )

    def replaceContent(self, select, data):
        self._add('<replaceContent select="%s"><![CDATA[%s]]></replaceContent>'
                            % (select, data,))

    def append(self, select, data):
        """ Added by <anthonyhiscox@gmail.com> """
        self._add('<append select="%s"><![CDATA[%s]]></append>'
                            % (select, data,))

    def eval(self, data):
        self._add("<eval><![CDATA[%s]]></eval>" % (data,))

    def fadein(self, select): 
        self._add('<fadeIn select="%s" />' % (select,))

    def fadeout(self, select):
        self._add('<fadeOut select="%s" />' % (select,))

    def render(self):
        # this could be more elaborate for logging/debugging
        ret = ('<taconite>' +  ''.join(self._xml) + '</taconite>')
        return ret

    def response(self):
        return HttpResponse(self.render(), mimetype='application/xml')
# class Taconite


