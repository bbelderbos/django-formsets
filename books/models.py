from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    inserted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
