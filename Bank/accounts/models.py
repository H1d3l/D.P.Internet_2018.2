from django.db import models
from django.utils import timezone

# Create your models here.

class Account(models.Model):
    owner = models.CharField(max_length=200,null=False)
    balance = models.FloatField(null=False)
    create_date = models.DateTimeField()