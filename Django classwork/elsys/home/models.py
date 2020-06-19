# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models

class Author(models.Model):
    name = models.CharField(max_length = 25)
    dataJoined = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    title = models.CharField(max_length = 25)
    text = models.TextField()
    image = models.ImageField(null = True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    enctype="multipart/form-data"
