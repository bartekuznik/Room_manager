from django.db import models

# Create your models here.

class Status(models.Model):
    ip = models.CharField(max_length=250)
    occupation = models.IntegerField(default=0)
    status = models.CharField(max_length=250)

    