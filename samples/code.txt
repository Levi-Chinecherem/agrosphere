# chat/views.py

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Group, Message
from django.contrib.auth.models import User
from django.http import HttpResponseBadRequest
from django.db.models import Q
from accounts.models import Profile
from django.db.models import F
from .forms import GroupForm

@login_required
def group_chat(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    messages = group.messages.all()

    return render(request, 'chat/group_chat.html', {'group': group, 'messages': messages})

@login_required
def private_chat(request, recipient_id):
    recipient = get_object_or_404(User, id=recipient_id)
    messages = Message.objects.filter(
        (Q(sender=request.user) & Q(recipient=recipient)) | 
        (Q(sender=recipient) & Q(recipient=request.user))
    ).order_by('timestamp')

    return render(request, 'chat/private_chat.html', {'recipient': recipient, 'messages': messages})


@login_required
def send_group_message(request):
    print("Received a POST request to send a group message.")
    if request.method == 'POST':
        print("Received a POST request to send a group message. in the if statement")
        content = request.POST.get('content')
        group_id = request.POST.get('group_id')
        image = request.FILES.get('image')

        if not content and not image:
            return JsonResponse({'status': 'error', 'message': 'Content or image is required for the message.'})

        try:
            group = Group.objects.get(pk=group_id)
        except Group.DoesNotExist:
            return HttpResponseBadRequest('Invalid group_id.')

        message = Message.objects.create(group=group, sender=request.user, content=content, image=image)

        return JsonResponse({'status': 'ok', 'content': message.content, 'image': message.image.url if message.image else None, 'sender': message.sender.username, 'timestamp': message.timestamp.strftime('%Y-%m-%d %H:%M:%S')})

    return JsonResponse({'status': 'error'})

@login_required
def send_private_message(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        recipient_id = request.POST.get('recipient_id')
        image = request.FILES.get('image')

        if not content and not image:
            return JsonResponse({'status': 'error', 'message': 'Content or image is required for the message.'})

        recipient = get_object_or_404(User, pk=recipient_id)
        message = Message.objects.create(sender=request.user, recipient=recipient, content=content, image=image)

        # If it's the first time, enable the communication feature
        if not recipient.profile.communicated_users:
            recipient.profile.communicated_users = True
            recipient.profile.save()

        return JsonResponse({'status': 'ok', 'content': message.content, 'image': message.image.url if message.image else None, 'sender': message.sender.username, 'timestamp': message.timestamp.strftime('%Y-%m-%d %H:%M:%S')})

    return JsonResponse({'status': 'error'})

@login_required
def create_group(request):
    if request.method == 'POST':
        group_name = request.POST.get('group_name')
        image = request.FILES.get('image')
        
        # Check if group name already exists
        if Group.objects.filter(name=group_name).exists():
            return JsonResponse({'status': 'error', 'message': 'Group name already exists. Please choose a different name or join the existing group.'})

        # Create the group
        group = Group.objects.create(name=group_name, created_by=request.user, image=image)
        group.members.add(request.user)
        group.admin.add(request.user)

        return redirect('group_chat', group_id=group.id)

    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

@login_required
def join_group(request):
    if request.method == 'POST':
        group_name = request.POST.get('group_name')

        # Check if the group exists
        try:
            group = Group.objects.get(name=group_name)
        except Group.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Group does not exist. Please check the group name and try again.'})

        # Add the user to the group
        group.members.add(request.user)

        return redirect('group_chat', group_id=group.id)

    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

@login_required
def communities(request):
    groups = Group.objects.all()
    return render(request, 'chat/communities.html', {'groups': groups})

@login_required
def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST, request.FILES)
        if form.is_valid():
            group = form.save(commit=False)
            group.created_by = request.user
            group.save()
            group.members.add(request.user)  # Automatically add the creator as a member
            group.admin.add(request.user)  # Automatically add the creator as an admin
            return redirect('communities')
    else:
        form = GroupForm()

    return render(request, 'chat/create_group.html', {'form': form})

@login_required
def view_group(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    return render(request, 'chat/view_group.html', {'group': group})

@login_required
def update_group(request, group_id):
    group = get_object_or_404(Group, id=group_id, created_by=request.user)

    if request.method == 'POST':
        form = GroupForm(request.POST, request.FILES, instance=group)
        if form.is_valid():
            form.save()
            return redirect('communities')
    else:
        form = GroupForm(instance=group)

    return render(request, 'chat/update_group.html', {'form': form, 'group': group})

@login_required
def delete_group(request, group_id):
    group = get_object_or_404(Group, id=group_id, created_by=request.user)

    if request.method == 'POST':
        group.delete()
        return redirect('communities')

    return render(request, 'chat/delete_group.html', {'group': group})

@login_required
def messages(request):
    # Get all unique profiles of users who have communicated with the requesting user
    sender_profiles = Profile.objects.filter(user__sent_messages__recipient=request.user).distinct()
    recipient_profiles = Profile.objects.filter(user__received_messages__sender=request.user).distinct()

    # Combine the two sets of profiles and remove the current user's profile
    users = (sender_profiles | recipient_profiles).exclude(user=request.user)

    return render(request, 'chat/messages.html', {'users': users})


@login_required
def unchatted_users(request):
    # Get all users excluding the current user
    all_users = User.objects.exclude(pk=request.user.pk)

    # Get users who have not communicated with the requesting user
    unchatted_users = all_users.exclude(
        Q(sent_messages__recipient=request.user) | Q(received_messages__sender=request.user)
    )

    return render(request, 'chat/unchatted_users.html', {'unchatted_users': unchatted_users})
                                                 