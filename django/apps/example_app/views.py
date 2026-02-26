# handles web requests

from django.shortcuts import render

from .models import ExampleModel # we want access to our newly created model

def home(request):
    examples = ExampleModel.objects.all() # load all example items
    return render(request, 'example_app/home.html', {"examples": examples})