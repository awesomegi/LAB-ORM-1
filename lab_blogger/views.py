from django.shortcuts import render, redirect
from blog_db.models import Post
from .forms import PostForm


# Homepage: shows all published posts, newest first
def home(request):
    posts = Post.objects.filter(is_published=True).order_by('-published_at')
    return render(request, 'home.html', {'posts': posts})


# Add Post page: handles the form to create a new post
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lab_blogger:home')  # go back to homepage after saving
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form': form})
