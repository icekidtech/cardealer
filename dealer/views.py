from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

# Create your views here.

#index
def index(request):
    template=loader.get_template("index.html")
    return HttpResponse(template.render())