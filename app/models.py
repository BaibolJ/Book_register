from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=123)
    author = models.CharField(max_length=70)
    date = models.DateField()

    def __str__(self):
        return self.title
