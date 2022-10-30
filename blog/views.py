from django.shortcuts import render, get_object_or_404
from .models import Blog

def allblogs(request):
    return render(request, 'blog/allblogs.html', {
        'blogs': Blog.objects
    })

def detail(request, blog_id):
    get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {
        'blog': get_object_or_404(Blog, pk=blog_id)
    })