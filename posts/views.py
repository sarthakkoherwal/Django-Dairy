from django.shortcuts import render,redirect
from .models import Post
from . import forms
from django.contrib.auth.decorators import login_required

# Create your views here.
app_name = 'posts'

@login_required(login_url="/accounts/login/")
def post_list(request):
    #articles = Article.objects.all().order_by('date');
    posts = Post.objects.filter(author=request.user)
    return render(request, 'posts/post_list.html', { 'posts': posts })

@login_required(login_url="/accounts/login/")
def post_detail(request,pk):
    post = Post.objects.get(pk=pk)
    return render(request,'posts/post_detail.html',{'post':post})

@login_required(login_url="/accounts/login/")
def post_create(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            # save article to db
            instance = form.save()
            instance.author = request.user
            instance.save()
            return redirect('posts:list')
    else:
        form = forms.CreatePost()
    return render(request, 'posts/post_create.html', {'form': form})

@login_required(login_url="/accounts/login/")
def post_edit(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        form = forms.CreatePost(request.POST, instance=post)
        # form = CreateArticle(request.POST, instance=cat)
        if form.is_valid():
            article = form.save(commit=False)
            article.save()
            return redirect('posts:list')
        else:
            form = forms.CreatePost(instance=post)
    else:
        form = forms.CreatePost(instance=post)
    #return render(request, 'articles/article_create.html', {'form': form})
    return render(request, 'posts/post_edit.html', {'form': form, 'post': post})

def post_delete(request, pk):
    post = Post.objects.get(pk=pk)  # Get your current cat
    if request.method == 'POST':         # If method is POST,
        post.delete()                     # delete the cat.
        return redirect('posts:list')            # Finally, redirect to the homepage.
    else:
        return redirect('posts:list')
    #return render(request, 'article_list.html', {'cat': arti})
    # If method is not POST, render the default template.
    # *Note*: Replace 'template_name.html' with your corresponding template name.
