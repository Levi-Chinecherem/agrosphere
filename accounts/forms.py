from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class ProfileForm(UserCreationForm):
    full_name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    occupation = forms.ChoiceField(choices=Profile.OCCUPATION_CHOICES, required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control-file', 'name': 'image'}))
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'full_name', 'email', 'occupation', 'image']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
