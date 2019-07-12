from django.db import models

# Create your models here.
class status(models.Model):
    ip = models.CharField(max_length=15)
    port = models.CharField(max_length=6)
    status = models.CharField(max_length=4)
    timestamp = models.DateField()
