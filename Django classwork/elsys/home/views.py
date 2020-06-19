# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm

from home.models import Author, Post

def index(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "index.html", context)

def index_author(request):
    authors = Author.objects.all()
    context = {"authors": authors}
    return render(request, "authors.html", context)

def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)    

def create(request):
    if request.method == "POST":
        print(request.POST)

        name = request.POST.get("author")
        src = request.FILES.get("myfile")
        
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['myfile'])
            form.save()
        
        try:
            author = Author.objects.get(name=name)
        except Author.DoesNotExist:
            author = Author(name=name)
            author.save()

        obj = Post(title=request.POST.get("title"),
                   text=request.POST.get("text"),
                   author=author, image=form)
        obj.save()
        return render(request, "success.html")
    return render(request, "create.html")

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        post.delete()
        context = {"action": "delete"}
        return render(request, "delete.html", context)
    print(post.author)
    context = {"post": post}
    return render(request, "detail.html", context)
