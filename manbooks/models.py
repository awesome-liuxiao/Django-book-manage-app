import datetime
from django.db import models
from django.utils import timezone

class Book(models.Model):
    book_name = models.CharField(max_length=200)
    author_name = models.CharField(max_length=200)
    link_addr = models.CharField(max_length=200)
    pub_year = models.IntegerField()
    def __str__(self):
        return self.book_name