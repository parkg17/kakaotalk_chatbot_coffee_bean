from django.shortcuts import render
from community.forms import *
from django.http import JsonResponse
import json
# Create your views here.

def test(request):
    data = {
        'code':200
    }
    return JsonResponse(data)