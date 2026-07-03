from django.shortcuts import render
from django.shortcuts import render

def index(request):
    return render(request, 'Main/index.html')


def schedule(request):
    return render(request, 'main/schedule.html')

def login(request):
    return render(request, 'main/login.html')

# Create your views here.
