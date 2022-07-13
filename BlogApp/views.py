from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse
from .forms import  PostForm
from .models import *
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.http import HttpResponseRedirect

def handler404(request, exception):
    return render( request,"BlogApp/404.html")

class Inicio(ListView):
    model=Blog
    template_name= "BlogApp/inicio.html"
    cats=Categoria.objects.all()
    def get_context_data(self, *args, **kwargs):
        cat_menu=Categoria.objects.all()
        context=super(Inicio,self).get_context_data(*args, **kwargs)
        context['cat_menu']=cat_menu
        return context

#CRUD creacion

class blogCreacion(CreateView):
    model=Blog
    template_name= "BlogApp/blog_creacion.html"
    fields='__all__'

class postCreacion(CreateView):
    model=Comment
    form_class= PostForm
    template_name= "BlogApp/comentarios.html"
    def form_valid(self, form):
        form.instance.post_id=self.kwargs['pk']
        return super().form_valid(form)
    success_url= reverse_lazy('Inicio') 

class categoriaCreacion(CreateView):
    model=Categoria
    template_name='BlogApp/categoria_creacion.html'
    fields='__all__'
    success_url= reverse_lazy('blog_crear')

def LikeView(request,pk):
    blog=get_object_or_404(Blog, id=request.POST.get('blog_id'))
    like=False
    if blog.like.filter(id=request.user.id).exists():
        blog.like.remove(request.user)
        like=False
    else:
        blog.like.add(request.user)
        like=True
    return HttpResponseRedirect(reverse('blog_detalle', args=[str(pk)]))
#CRUD leer

class blogLista(ListView):
    model=Blog
    template_name= "BlogApp/blog_lista.html"
    orden=['-id']

class blogDetalle(DetailView):
    model=Blog
    template_name= "BlogApp/blog_detalle.html"
    def get_context_data(self, *args, **kwargs):
        cat_menu=Categoria.objects.all()
        
        stuff= get_object_or_404(Blog, id=self.kwargs['pk'])
        total_like= stuff.total_like()
        liked=False
        if stuff.like.filter(id=self.request.user.id).exists():
            liked=True
        context=super(blogDetalle,self).get_context_data(*args, **kwargs)
        context['cat_menu']=cat_menu
        context['total_like']=total_like
        context['liked']=liked
        return context

def CategoriaVista(request, cats):
    cat=Categoria.objects.filter(name=cats).exists()
    if cat==True:
        categoria = Categoria.objects.get(name=cats)
        categoria_blog=Blog.objects.filter(categoria_id=categoria.id)
        return render(request, 'BlogApp/categorias.html', {'cats':cats, 'categoria_blog':categoria_blog})
    else:
        return render(request, 'BlogApp/categorias.html', {'cats': cats})      


def about(request):
    about=About.objects.all()
    contexto={'about':about}
    return render(request, 'BlogApp/about.html', contexto)

def buscarCategoriaBlog(request):
    if request.GET['name']:
        name = request.GET['name']
        cat=Categoria.objects.filter(name=name).exists()
        if cat==True:
            categoria = Categoria.objects.get(name=name)
            blogs = Blog.objects.filter(categoria_id = categoria.id)
            return render(request, 'BlogApp/resultadosCategoriaBlog.html', {'blogs': blogs, 'name': name})
        else:
            return render(request, 'BlogApp/resultadosCategoriaBlog.html', {'name': name})

#CRUD update

class blogActualizar(LoginRequiredMixin, UpdateView):
    model=Blog
    template_name= "BlogApp/blog_form.html"
    fields='__all__'

#CRUD delete

class blogEliminar(LoginRequiredMixin, DeleteView):
    model=Blog
    template_name= "BlogApp/blog_confirm_delete.html"
    success_url= reverse_lazy('Inicio')