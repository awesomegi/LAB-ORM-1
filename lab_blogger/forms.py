from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter your post title...',
                'class': 'form-input',
            }),
            'content': forms.Textarea(attrs={
                'placeholder': 'Write your post content here...',
                'class': 'form-textarea',
                'rows': 10,
            }),
        }
