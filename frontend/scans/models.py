from django.db import models
from django.forms import ModelForm
from django import forms 

class Tag(models.Model):
    """ 
        >>> t = Tag.objects.create(name='joe')
        >>> t.name
        'joejsd'
    """
    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=20)
    

class Scan(models.Model):

    def __unicode__(self):
        line = self.ocr.split('\n')[0][:100]
        if line == '':
            line = self.ocr.split('\n')[1][:100]
        return line + u'...'

    def not_processed(self):
        if not self.processed:
            return True

    def pdf_link(self):
        return self._link('/static/pdfs') + '.pdf'

    def thumb_link(self):
        return self._link('/static/thumbs') + '.png'

    def preview_link(self):
        return self._link('/static/scans') + '.png'

    def _link(self, area):
        return '/'.join([area, self.datedir, self.timedir, self.filename])

    def before_break(self):
        return '\n'.join(self.ocr.split('\n')[:13]) # First 5 lines of OCR

    def after_break(self):
        return '\n'.join(self.ocr.split('\n')[13:])

    datedir = models.CharField(max_length=10)
    timedir = models.CharField(max_length=8)
    filename = models.CharField(max_length=100)
    ocr = models.TextField()
    processed = models.BooleanField()
    tags = models.ManyToManyField(Tag)

class ScanStatus(models.Model): 
    # Simple model to store scan status data.
    in_progress = models.BooleanField()
    percent = models.IntegerField() 
    message = models.TextField()


class Comment(models.Model):

    def __unicode__(self):
        txt = 'On %s, %s said: %s' % (self.pub_date, self.name, self.content[:10]+'...')
        return txt

    comments = models.ForeignKey(Scan)
    name = models.CharField(max_length=50)
    content = models.TextField()
    pub_date = models.DateField()


### MODELFORMS
class ScanTagForm(ModelForm):
    """ Used for managing tags associated to a specific scan """ 
    class Meta:
        model = Scan
        fields = ['tags']
        tags = forms.ModelMultipleChoiceField(
                queryset=Tag.objects.all(), widget=forms.SelectMultiple)

        Tag.name = forms.CharField(max_length=20)

class TagForm(ModelForm):
    """ Used for managing ALL tags. """ 
    class Meta:
        model = Tag
