from django import forms
from .models import postModel

class postForm(forms.ModelForm):
    class Meta:
        model = postModel
        fields = ['name', 'title']
        