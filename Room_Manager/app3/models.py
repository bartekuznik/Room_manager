from django.db import models

# Create your models here.

class Status(models.Model):
    ip = models.CharField(max_length=250)
    occupation = models.CharField(max_length=250)
    status = models.CharField(max_length=250)

    