from django.shortcuts import render ,get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import Createcontent
from django.shortcuts import redirect
from .models import Category



def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})



def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})


#def create_post(request):
#    form = Createcontent
#    return render(request, 'blog/post_creator.html', {'form': form})


def create_post(request):
    if request.method == "POST":
        form = Createcontent(request.POST)
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

