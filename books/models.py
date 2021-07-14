from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    description = models.TextField()
    image_link = models.URLField(blank=True, null=True)
    inserted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
