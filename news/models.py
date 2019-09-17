from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    Heading = models.CharField(max_length=100)
    News = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    tags = models.CharField(max_length = 250)
    author = models.CharField(max_length=32)
    excerpt = models.TextField()
    

    def __str__(self):
        return '%s'%(self.tags+' : '+self.Heading)
