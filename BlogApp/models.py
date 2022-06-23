from django.db import models
from django.contrib.auth.models import User
from django.forms import ImageField
from django.urls import reverse
# Create your models here.


class Blog(models.Model):
    titulo=models.CharField(max_length=50)
    subtitulo=models.CharField(max_length=50)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    image=ImageField()
    content=models.TextField()
    created=models.DateField(auto_now_add=True)#para que agrege fehca automaticamente
    updated=models.DateField(auto_now_add=True)
    def __str__(self):
        return f'{self.autor}: {self.titulo}'
    def get_absolute_url(self):
        return reverse('Inicio')