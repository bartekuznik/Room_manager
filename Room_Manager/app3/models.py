from django.db import models

class Server(models.Model):
    ip = models.CharField(max_length=250)
    occupation = models.IntegerField(default=0)
    