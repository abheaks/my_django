from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("My Second App")

def help(request):
    dict={'help_me':'I am here to help you'}
    return render(request,'help.html',context=dict)
