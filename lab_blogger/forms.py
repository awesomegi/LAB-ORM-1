from django import forms
from blog_db.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'poster']
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
