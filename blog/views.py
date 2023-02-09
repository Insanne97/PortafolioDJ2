from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def blog(request):
    proyectos = Blog.objects.all()
    return render(request, 'blog.html',{'proyectos':proyectos})

def blog_extendido(request, id_blog):
    post = get_object_or_404(Blog, pk=id_blog)
    return render(request, 'blogExtendido.html',{'post':post})