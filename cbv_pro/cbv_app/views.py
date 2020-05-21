from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from . import models
# Create your views here.
#def index(request):
#    return render(request,'index.html')
class IndexView(TemplateView):
    template_name='index.html'

class SchoolListView(ListView):
    context_object_name='schools'
    model=models.School



class  SchoolDetailView(DetailView):
    context_object_name='school_details'
    model=models.School
    template_name='cbv_app/school_details.html'
class SchoolCreateView(CreateView):
    model=models.School
