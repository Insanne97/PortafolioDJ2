from django.shortcuts import render
from .models import Proyectos

# Create your views here.
def home(request):
    proyectos = Proyectos.objects.all()
    return render(request,'home.html',{'proyectos':proyectos})