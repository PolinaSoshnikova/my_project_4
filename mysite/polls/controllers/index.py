from django.http import HttpResponse
from django.shortcuts import redirect, render

def index(request):
    name = request.GET.get('name')
    return render(request, 'index.html', {'name': name})


def about(request):
    return HttpResponse("My name is Polina")


def aboutWork(request):
    return HttpResponse("Software engineer")


def interests(request):
    return render(request, 'interests.html', {'title': 'Интересы'})








