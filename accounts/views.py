from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import Profile
from django.contrib.auth import authenticate, login


def registration(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            # Create a new User instance
            user = form.save(commit=False)
            # Set the password separately to ensure it's hashed
            user.set_password(form.cleaned_data['password1'])
            user.save()

            # Create a new Profile instance and link it to the User
            profile = Profile(user=user)
            profile.full_name = form.cleaned_data['full_name']
            profile.email = form.cleaned_data['email']
            profile.occupation = form.cleaned_data['occupation']
            # Check if an image is provided before saving it
            if 'image' in form.cleaned_data:
                profile.image = form.cleaned_data['image']

            profile.save()

            # Log in the user
            authenticated_user = authenticate(username=user.username, password=form.cleaned_data['password1'])
            login(request, authenticated_user)

            return redirect('profile')
    else:
        form = ProfileForm()

    return render(request, 'accounts/registration_form.html', {'form': form})

@login_required
def profile(request):
    # Retrieve the user's profile
    user_profile = Profile.objects.get(user=request.user)

    return render(request, 'accounts/profile.html', {'user_profile': user_profile})
