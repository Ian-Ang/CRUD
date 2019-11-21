import datetime
from django.db import models

# Create your models here.
class Book(models.Model):
    book_choices = (
        ('one of novel','One of Novel'),
        ('documentation','Documentation'),
        ('other','Other'),
    )

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date_published = models.DateField(default=datetime.datetime.today, blank=True, null=True)
    number_of_page = models.IntegerField(blank=True, null=True)
    type_of_book = models.CharField(blank=True, max_length=100, choices=book_choices)

    def __str__(self):
        return self.title
