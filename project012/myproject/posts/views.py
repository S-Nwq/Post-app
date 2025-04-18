from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms
# from django.http import HttpResponse    (1st style of rendering in web)

# Create your views here.
def posts_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', {'posts': posts})

def post_page(request, slug):
    # return HttpResponse(slug)     (1st style of rendering in web)
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_page.html', {'post': post})

@login_required(login_url="/users/sign_in")
def posts_new(request):
    # form = forms.CreatePost()
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts:list')
            
    else:
        form = forms.CreatePost()
    return render(request, 'posts/post-new.html' , {'form': form})