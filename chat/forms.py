from django import forms
from .models import Group

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'description', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
