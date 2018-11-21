from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=40, null = False)
    closed = models.BooleanField(False)
    pub_date = models.DateField(null = False)

    def __str__(self):
        self.question_text
        self.pub_date
        self.closed

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE,null=True)
    choice_text = models.CharField(max_length=20)
    votes = models.IntegerField(default=0)

    def __str__(self):
        self.question
        self.choice_text
        self.votes

