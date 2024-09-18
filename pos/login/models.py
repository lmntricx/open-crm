from django.db import models


# Create your models here.
class Users(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.TextField(max_length=255)
    level = models.IntegerField(null=True)

