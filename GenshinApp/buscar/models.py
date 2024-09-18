from django.db import models
from django.contrib.auth.models import User
from .enums import Vision,TipoArmas

from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='media/images')
# Create your models here.

class Personajes(models.Model):
    nombre=models.CharField(max_length=35)
    elemental=models.CharField(max_length=75)
    arma=models.CharField(max_length=15,choices=[(tag.value, tag.name) for tag in TipoArmas])
    vision=models.CharField(max_length=10,choices=[(tag.value, tag.name) for tag in Vision])
    ultimate=models.CharField(max_length=75)
    decripcion=models.TextField(blank=True)
    decripcion_elemental=models.TextField(blank=True)
    decripcion_ultimate=models.TextField(blank=True)
    img=models.ImageField(upload_to='images/', storage=fs)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.nombre
    

    