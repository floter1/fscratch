from django.db import models

# Create your models here.

class Members(models.Model):
	user_name = models.CharField(max_length=250)
	age = models.CharField(max_length=250)
	phone = models.CharField(max_length=250)
	