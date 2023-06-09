from django.shortcuts import redirect, render
from django.http import HttpResponse
import requests


def index(request):

    responce = requests.get('https://swapi.dev/api/')

    return render(request, 'api.html', {"responce": responce.json().items()})