from django.db import models

# Create your models here.

class Articles(models.Model):
	title = models.CharField(max_length=250)
	content = models.TextField(max_length=250)
	writer = models.CharField(max_length=250)

class Category(models.Model):
    title = models.CharField(max_length=250)
    year = models.CharField(max_length=250)
    month = models.CharField(max_length=250)
    day = models.CharField(max_length=250)    