from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.
def index(request):
    User.objects.all()
    return render(request, 'index.html')


def list(request):
    return render(request, 'List.html')


def check(request):
    return render(request, 'update.html')


def num(request, id):
    return HttpResponse(f"num {id} page")
