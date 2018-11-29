from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=40,null=False)
    closed = models.BooleanField(False)
    pub_date = models.DateField(null=False)
