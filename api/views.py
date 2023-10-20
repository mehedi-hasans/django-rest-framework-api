from django.shortcuts import render
from .models import *
from . import forms
# Create your views here.
def index(request):
    musicianList = Musician.objects.order_by('first_name')
    diction = {'musician': musicianList}
    return render(request, 'index.html', context= diction)

def form(request):
    djangoForm = forms.djangoForms()
    diction = {'newForm': djangoForm, 'heading': 'Form from Django Library'}
    return render(request, 'form.html', diction)