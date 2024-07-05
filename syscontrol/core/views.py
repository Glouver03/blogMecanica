from django.shortcuts import render, redirect , get_object_or_404
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

# Create your views here.


def index (request):
    html = 'core/content.html'
    contexto= {}
    return render(request, html, contexto)


# def aulas(request):
#     html = 'core/aulas.html'
#     contexto= {}
#     return render(request, html, contexto)

def noticias(request):
    html = 'core/noticias.html'
    contexto= {}
    return render(request, html, contexto)

def oficina(request):
    html = 'core/oficina.html'
    contexto= {}
    return render(request, html, contexto)

def projetos(request):
    html = 'core/projetos.html'
    contexto= {}
    return render(request, html, contexto)

def loja(request):
    html = 'core/loja.html'
    contexto= {}
    return render(request, html, contexto)

def contato(request):
    html = 'core/contato.html'
    contexto= {}
    return render(request, html, contexto)



# from django.contrib.auth.decorators import login_required
# @login_required


# def criar_postagem(request):
#     if request.method == 'POST':
#         title = request.POST['title']
#         content = request.POST['content']
#         author = request.user  # O autor é o usuário logado
#         post = Post.objects.create(title=title, content=content, author=author, date_posted=timezone.now())
#         post.save()
#         return redirect('aulas')  # Redireciona para a página após criar a postagem
#     else:
#         return render(request, 'core/aulas.html')
    
def aulas(request):
    posts = Post.objects.all().order_by('-date_posted')[:3]  # Os 3 posts mais recentes para o carrossel
    recent_posts = Post.objects.all().order_by('-date_posted')[3:6]  # Próximos 3 posts mais recentes para a lista
    # posts = Post.objects.all().order_by('-date_posted')  # Ordena as postagens pela data de publicação, da mais recente para a mais antiga
    return render(request, 'core/post_list.html', {'posts': posts, 'recent_posts': recent_posts})

# Esta função busca uma postagem específica pelo ID
def post_detail(request, id):
    post = get_object_or_404(Post, id=id) 
    return render(request, 'core/post_detail.html', {'post': post}) # Em seguida, renderiza o template post_detail.html


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('aulas')
    else:
        form = PostForm()
    return render(request, 'core/create_post.html', {'form': form})

class PostListView(ListView):
    model = Post
    template_name = 'core/post_list.html'  # Certifique-se de que este caminho está correto
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'core/post_detail.html'  # Certifique-se de que este caminho está correto
    context_object_name = 'post'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'core/create_post.html'
    success_url = reverse_lazy('post_list')