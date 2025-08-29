from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    """ This saves the blog posts """ # docstrings """ """ # they add extra meaning to the code.

    title = models.CharField(max_length=200, blank=True, null=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    minutes = models.IntegerField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    published = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.title)
    
# models
# views 
# urls
# templates ::: css, html, bootstrap