from django.db import models

# My Book model with 3 fields
class Book(models.Model):
    title = models.CharField(max_length=50)
    author_name = models.CharField(max_length=50)
    author_surname = models.CharField(max_length=50)
    
