from django.http import HttpResponse
from django.shortcuts import redirect, render
from polls.models import Feedback
from polls.models import Item

def index(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {})


def contacts(request):
    return render(request, 'contacts.html', {})


def hobbies(request):
    return HttpResponse("My hobbies")


def photo(request):
    return HttpResponse("My photo")


def services(request):
    return render(request, 'services.html', {})


def skills(request):
    return render(request, 'skills.html', {})


def partfolio(request):
    return render(request, 'partfolio.html', {})


def contact(request):
    return render(request, 'contact.html', {})



def index(request):
    item = Item.objects.all()
    return render(request, 'index.html', {'items': item})










