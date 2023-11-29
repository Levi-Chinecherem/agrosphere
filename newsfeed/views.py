# newsfeed/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post
from .forms import PostForm 
from django.http import JsonResponse
from sharing.models import SharedItem
from django.views.decorators.http import require_POST

@login_required
def news_feed(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'newsfeed/news_feed.html', {'posts': posts})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            return redirect('feed')
    else:
        form = PostForm()

    return render(request, 'newsfeed/create_post.html', {'form': form})

@login_required
def profile_details(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'newsfeed/profile_details.html', {'user': user})

@login_required
def toggle_like(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post = get_object_or_404(Post, pk=post_id)

        if request.user in post.liked_by.all():
            post.liked_by.remove(request.user)
            is_liked = False
        else:
            post.liked_by.add(request.user)
            is_liked = True

        like_count = post.liked_by.count()
        return JsonResponse({'like_count': like_count, 'is_liked': is_liked})

    return JsonResponse({'error': 'Invalid request method'})


@login_required
def share_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    # Check if the post is already shared
    if SharedItem.objects.filter(user=request.user, post=post).exists():
        return JsonResponse({'status': 'error', 'message': 'Post is already shared.'})
    else:
        SharedItem.objects.create(user=request.user, post=post)
        return JsonResponse({'status': 'ok', 'message': 'Post shared successfully.'})


@login_required
def feed_details(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'newsfeed/feed_details.html', {'post': post})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('feed')

@login_required
@require_POST
def like_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.user in post.liked_by.all():
        post.liked_by.remove(request.user)
        is_liked = False
    else:
        post.liked_by.add(request.user)
        is_liked = True

    like_count = post.liked_by.count()
    return JsonResponse({'like_count': like_count, 'is_liked': is_liked})

# Update post
@login_required
def update_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('feed')
        else:
            return render(request, 'newsfeed/create_post.html', {'form': form})
    else:
        # Handle GET request, possibly render a form to update the post
        form = PostForm(instance=post)
        return render(request, 'newsfeed/update_post.html', {'form': form, 'post': post})
