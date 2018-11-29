from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    data_published = models.DateTimeField(null=False)
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)

    def __str__(self):
        self.title
