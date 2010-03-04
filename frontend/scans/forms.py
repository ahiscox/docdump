from django import forms
from frontend.scans.models import Scan, Tag, Comment
from becommands.tag import tag


class TagForm(forms.Form):
    existing = forms.MultipleChoiceField(queryset=Tag.objects.all())
   


def testing():
    """ blah blah balh"""
    print 'Foo!'




































































testing()


