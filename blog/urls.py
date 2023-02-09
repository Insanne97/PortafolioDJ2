from django.urls import path
from .views import blog, blog_extendido

app_name = 'blog'

urlpatterns = [
    path('', blog, name='blog'),
    path('<id_blog>',blog_extendido, name='blog_extendido'),
]
