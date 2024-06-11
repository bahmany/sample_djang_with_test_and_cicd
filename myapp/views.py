from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from myapp.models import Item


def index(request):
    items = Item.objects.all()
    return HttpResponse(', '.join(item.name for item in items))