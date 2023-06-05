from django.shortcuts import render
from .models import Post
from django.views.generic import ListView


def home(request):
    return render(request, 'index.html')


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
