from django import forms
from .models import Product

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('name', 'description', 'price', 'image')
