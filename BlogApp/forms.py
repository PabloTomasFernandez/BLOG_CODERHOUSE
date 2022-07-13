from django import forms
from .models import *
from django.forms import ModelForm

choices=Categoria.objects.all().values_list('name')
choice_list=[]
for item in choices:
    choice_list.append(item)


class BlogForm(ModelForm):
    class Meta:
        model=Blog
        fields=('titulo','subtitulo','categoria','autor','categoria','content','snippet', 'like')
        widgets ={
            'titulo': forms.TextInput(),
            'subtitulo':forms.TextInput(),
            'categoria':forms.Select(choices=choice_list),
            'autor': forms.Select(),
            'content':forms.Textarea(attrs={'class':'form-control'}),
            'snippet':forms.Textarea(),
            'like':forms.Select()
        }
        


class PostForm(ModelForm):
    class Meta:
        model=Comment
        fields=('name','curpo')
        widgets ={
            'name': forms.TextInput(),
            'curpo':forms.Textarea(),
        }