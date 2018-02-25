from django.shortcuts import render
from .models import Post

def post_list(request):
	posts = Post.Objects.all();
	return render(request, 'blog/post_list.html', {'posts':posts})