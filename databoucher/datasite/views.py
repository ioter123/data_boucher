from django.shortcuts import render
from .models import Data
import json
# Create your views here.
from django.http import HttpResponse
from django.core import serializers


def index(request):

    data = Data.objects.all().values()
    #print(json.dumps(list(data)))
    return render(request, 'index.html', {'data_json': json.dumps(list(data))})