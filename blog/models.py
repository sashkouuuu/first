from ckeditor.fields import RichTextField
from django.db import models
from MyBlog.settings import TYPE_OF_CATALOGUE

class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    type= models.IntegerField(choices=TYPE_OF_CATALOGUE, default=0)
    content = RichTextField(default='')


    def __str__(self):
        return self.title