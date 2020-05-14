from django.shortcuts import render ,get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import Createcontent
from django.shortcuts import redirect
from .models import Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required



def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


@login_required
def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def create_post(request):
    if request.method == "POST":
        form = Createcontent(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', post.slug)
    else:
        form = Createcontent()
    return render(request, 'blog/post_creator.html', {'form': form})

def cat_list(request):
    categories = Category.objects.all()
    return render(request, 'blog/categories.html', {'categories': categories})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render(request, 'blog/category_detail.html', {'category': category})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('post_list')
    else:
        regisform = UserCreationForm()
    return render(request, 'blog/register.html', {'regisform': regisform})

