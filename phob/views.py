from django.shortcuts import render
from . import views
def home(request):
    return render(request,'index.html')
# Create your views here.
def events(request):
    return render(request,'events.html')

def schedule(request):
    return render(request,'schedule.html')

def street(request):
    return render(request,'street.html')

def studio(request):
    return render(request,'studio.html')

def tours(request):
    return render(request,'tours.html')

def wedding(request):
    return render(request,'wedding.html')  

