from django.shortcuts import render_to_response
from django.http import HttpResponse 

from frontend.scans.models import Scan, Comment, Tag
from frontend.search.index import complete_indexer 

from django import forms 

from IPython import Shell

def _myshell():
    Shell.IPShellEmbed()()

MODEL_MAP = {
    'scan': Scan,
    'tag': Tag,
    'comment' : Comment
}

MODEL_CHOICES = [('', 'all')] + zip(MODEL_MAP.keys(), MODEL_MAP.keys())

class SearchForm(forms.Form):
    query = forms.CharField(required=True)
    models = forms.ChoiceField(choices=MODEL_CHOICES, required=False)


def query(request):
    results = []

    if request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            models = MODEL_MAP.get(form.cleaned_data['models'])
        if not models:
            indexer = complete_indexer
        else:
            indexer = models.search

        results = indexer.search(query).spell_correction()
        correct = results.get_corrected_query_string()
        if not correct:
            correct = False
        if results.count() == 0:
            noresults = True
            results = indexer.search(correct).prefetch()
        else: 
            noresults = False

    else:
        form = SearchForm()
        correct = False
        noresults = True
    return render_to_response('search/search.html', {'correct':correct, 'noresults':noresults, 'results': results, 'form':form})



