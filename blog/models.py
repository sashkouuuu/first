from froala_editor.fields import FroalaField
from django.db import models
from MyBlog.settings import TYPE_OF_CATALOGUE

class Article(models.Model):
    title = models.CharField(max_length=200)
    type= models.IntegerField(choices=TYPE_OF_CATALOGUE, default=0)
    content = FroalaField(default='')
    cover = models.ImageField(upload_to='blog/media/', null=True, blank=True)


    def __str__(self):
        return self.title