from django.db import models
from django.contrib.auth.models import User
from django.forms import ImageField
from django.urls import reverse
from ckeditor.fields import RichTextField



# Create your models here.



class Categoria(models.Model):
    name= models.CharField(max_length=50)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('Inicio')


class Blog(models.Model):
    titulo=models.CharField(max_length=200)
    subtitulo=models.CharField(max_length=200)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    image=models.ImageField(null=True, blank=True, upload_to='media/')
    categoria=models.CharField(max_length=50, default='Sin categoria')
    snippet=models.TextField(max_length=50, default='Click link above to read blog....')
    content=RichTextField(blank=True, null=True)
    created=models.DateField(auto_now_add=True)#para que agrege fehca automaticamente
    updated=models.DateField(auto_now_add=True)
    like=models.ManyToManyField(User, related_name='Blog_posts')
    def total_like(self):
        return self.like.count()
    def __str__(self):
        return f'{self.autor}: {self.titulo}'
    def get_absolute_url(self):
        return reverse('Inicio')

class Comment(models.Model):
    post=models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    curpo=models.TextField()
    created=models.DateField(auto_now_add=True)
    def __str__(self):
        return f'{self.post}'