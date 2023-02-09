import datetime
from django.db import models

# Create your models here.
class Blog(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='Blog/imagen/')
    fecha = models.DateField(datetime.date.today)
    
    def __str__(self) -> str:
        nombrePublicacion = 'Publicacion: ' + self.titulo
        return nombrePublicacion
