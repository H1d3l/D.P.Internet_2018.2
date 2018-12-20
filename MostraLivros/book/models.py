from django.db import models

# Create your models here.

TITLE_CHOICE = (
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.')
)

class Author(models.Model):

    name = models.CharField(max_length=60,null=False)
    title = models.CharField(max_length=3,null=False, choices=TITLE_CHOICE)
    birth_date = models.DateField(blank=True,null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        self.name


class Book(models.Model):
    name = models.CharField(max_length=100,null=False)
    authors = models.ManyToManyField(Author,null=False)


    def __str__(self):
        self.name