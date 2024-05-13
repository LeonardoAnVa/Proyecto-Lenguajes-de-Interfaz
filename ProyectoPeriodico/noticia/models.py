from datetime import date

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Reportero(User, models.Model):
    #nombre = models.CharField(max_length=80)
    #apellidos = models.CharField(max_length=80)
    telefono = models.CharField(max_length=10, blank=True)
    #email = models.EmailField()
    direccion = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField(default='1900-01-01')
    foto = models.ImageField(upload_to='fotos/', blank=True)
    acta_nacimiento = models.FileField(upload_to='actas/', blank=True)

    def getEdad(self):
        """Calcula la edad a partir de la fecha de nacimiento."""
        hoy = date.today()  # Obtiene la fecha actual
        edad = hoy.year - self.fecha_nacimiento.year  # Calcula la diferencia de años

        # Ajusta la edad si el cumpleaños no ha ocurrido este año
        if (hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day):
            edad -= 1

        return edad

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    autor =models.CharField(max_length=200)  # Vincula cada noticia a un usuario
    contenido = models.TextField()
    fecha_publicacion = models.DateField(auto_now_add=True)  # Fecha de publicación, establecida automáticamente en la creación
    imagen = models.ImageField(upload_to='imagenes_noticias/', blank=True, null=True)  # Opcional: para añadir una imagen a la noticia

    def __str__(self):
        return self.titulo  # Representación en string del modelo, útil en el admin de Django



