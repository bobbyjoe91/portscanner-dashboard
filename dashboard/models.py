from django.db import models

class Status(models.Model):
    host = models.CharField(max_length=15)
    port = models.CharField(max_length=5)
    status = models.CharField(max_length=3)
    agent = models.CharField(max_length=15)
    timestamp = models.DateTimeField()
