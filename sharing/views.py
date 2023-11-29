from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import SharedItem
from newsfeed.models import Post
from django.http import JsonResponse

@login_required
def shared_items(request):
    shared_items = SharedItem.objects.all()  # Retrieve all shared items
    return render(request, 'sharing/shared_items.html', {'shared_items': shared_items})

@login_required
def share_post(request, post_id):
    post = Post.objects.get(pk=post_id)

    # Check if the post is already shared
    if SharedItem.objects.filter(user=request.user, post=post).exists():
        return JsonResponse({'status': 'error', 'message': 'Post is already shared.'})
    else:
        SharedItem.objects.create(user=request.user, post=post)
        return JsonResponse({'status': 'ok', 'message': 'Post shared successfully.'})
