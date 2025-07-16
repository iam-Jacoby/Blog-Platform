from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import PostForm
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User
from taggit.models import Tag
from django.db import models


def blog_list(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(
            models.Q(title__icontains=query) | models.Q(content__icontains=query)
        ).distinct()
    else:
        posts = Post.objects.all()
    return render(request, 'blog/blog_list.html', {'posts': posts, 'query': query})


def blog_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/blog_detail.html', {'post': post})

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog_detail', pk=post.pk)
        else:
            print("Form is invalid:", form.errors)  # <-- Add this line
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to edit this post.")

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_form.html', {'form': form, 'edit': True})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to delete this post.")

    if request.method == 'POST':
        post.delete()
        return redirect('blog_list')

    return render(request, 'blog/post_confirm_delete.html', {'post': post})

import markdown

def blog_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.content = markdown.markdown(post.content)
    return render(request, 'blog/blog_detail.html', {'post': post})

def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=user)
    return render(request, 'blog/user_profile.html', {'user_profile': user, 'posts': posts})

def tagged_posts(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = Post.objects.filter(tags__in=[tag])
    return render(request, 'blog/tagged_posts.html', {'tag': tag, 'posts': posts})