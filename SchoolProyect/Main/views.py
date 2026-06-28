from django.shortcuts import render
from django.shortcuts import render

def index(request):
    return render(request, 'Main/index.html')


def schedule(request):
    return render(request, 'main/schedule.html')
# Create your views here.
