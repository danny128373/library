from django.db import models
from .library import Library
from .librarian import Librarian


class Book(models.Model):
    # Book instance
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    isbn = models.CharField(max_length=50)
    year_published = models.IntegerField()
    # assigning location and library as foreignkey
    location = models.ForeignKey(Library, on_delete=models.CASCADE)
    librarian = models.ForeignKey(Librarian, on_delete=models.CASCADE)
