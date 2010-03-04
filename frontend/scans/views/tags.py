class AjaxTag:
    def form(self, scanid):
        """ Return Taconite XML to replace OCR excerpt with tag form for scanid """ 
        from frontend.scans.models import Scan, Tag
        from django.template import loader
        from frontend.taconite import Taconite

        tags = Scan.objects.get(pk=scanid).tags.all()

        template = loader.render_to_string('scans/tags/form.html', {'tags' : tags})
        
        tac = Taconite()

        # Create a list of all Tags on the page (used for autocompletion, updating multiple selects, etc.)
        alltags = []
        for i in Tag.objects.all():
            alltags.append(i.name)

        selector = 'div#alltags'
        tac.replaceContent(selector, ",".join(alltags))

        selector = 'div#ocr-' + str(scanid)
        tac.replaceContent(selector, template)

        # Handle clicking tags deletes them, handler.
        # tac.eval('updateTags();updateHandlers();')

        return tac.render()
        

    def add(self, scanid, tagname):
        """
        FIXME: This docstring is outdated, update it.
        Add a tag to Tag if it doesn't exist. 
        Attach a tag to a scan.
        Return a Taconite XML doc replacing div#ocr-<scanid> div.attached_tags with
        updated tags list for scanid. Eval JS to update all open tags multiple selects.
        """
        from frontend.scans.models import Scan, Tag
        
        # Create a tag if it doesn't exist. Grab tag. 
        try:
            tag = Tag.objects.get(name=tagname)
        except Tag.DoesNotExist:
            tag = Tag(name=tagname)
            tag.save()

        scan = Scan.objects.get(pk=scanid)
        try:
            scan.tags.get(name=tagname)
            return 'exists'
        except:
            scan.tags.add(tag)
            scan.save()
            return 'ok'

    def delete(self, scanid, tagname):
        """
        FIXME: This docstring is outdated, fix it.
        Detach a tag from a scan. 
        Does NOT remove tag from database!
        Return Taconite XML replacing div#ocr-<scanid> div.attached_tags with updated list.
        """ 
        from frontend.scans.models import Scan, Tag

        try:
            scan = Scan.objects.get(pk=scanid)
        
            # Detach tag
            scan.tags.remove(Tag.objects.get(name=tagname))
            scan.save()
            return 'ok'
           
        except:
            return 'fail'
