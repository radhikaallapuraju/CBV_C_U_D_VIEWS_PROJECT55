from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from app.models import *

class home(TemplateView):
    template_name='app/home.html'

class school_list(ListView):
    model=School
    
    context_object_name='schools'

class School_Detail(DetailView):
    model=School
    context_object_name='sclobject'


class SchoolCreate(CreateView):
    model=School
    fields='__all__'

class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'

class SchoolDelete(DeleteView):
    model=School
    fields='__all__'
    success_url=reverse_lazy('school_list')
