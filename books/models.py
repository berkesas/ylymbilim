from django.db import models
from categories.models import Category
import os
# Create your models here.


class Book(models.Model):
    class Status(models.IntegerChoices):
        Published = 1
        Draft = 0

    title = models.CharField(max_length=255)
    author = models.CharField(null=True, max_length=255)
    tags = models.CharField(null=True, max_length=255)
    description = models.TextField(null=True)
    category = models.ForeignKey(
        Category, null=True, on_delete=models.SET_NULL)
    picture = models.ImageField(upload_to="books", null=True)
    file = models.FileField(upload_to="books", null=True)
    view_count = models.IntegerField(default=0)
    download_count = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=Status.choices, default=0)

    def __str__(self):
        return self.title
    
    def filename(self):
        return os.path.basename(self.file.name)
