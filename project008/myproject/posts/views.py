from django.shortcuts import render
from .models import Post
# from django.http import HttpResponse    (1st style of rendering in web)

# Create your views here.
def posts_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', {'posts': posts})

def post_page(request, slug):
    # return HttpResponse(slug)     (1st style of rendering in web)
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_page.html', {'post': post})
