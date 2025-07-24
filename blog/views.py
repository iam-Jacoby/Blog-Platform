from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User
from taggit.models import Tag
from django.db import models
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm


def blog_list(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(
            models.Q(title__icontains=query) | models.Q(content__icontains=query)
        ).distinct()
    else:
        posts = Post.objects.all()

    paginator = Paginator(posts, 5)  # Show 5 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/blog_list.html', {
        'page_obj': page_obj,
        'query': query,
    })

def blog_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments_qs = Comment.objects.filter(post=post).order_by('-created_at')

    paginator = Paginator(comments_qs, 5)
    page_number = request.GET.get('page')
    comments = paginator.get_page(page_number)

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                return redirect('blog_detail', pk=pk)
            else:
                print("❌ Form errors:", form.errors)
        else:
            return redirect('login')
    else:
        form = CommentForm()

    return render(request, 'blog_detail.html', {
        'post': post,
        'comments': comments,
        'form': form
    })

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

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # or 'blog_list'
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})