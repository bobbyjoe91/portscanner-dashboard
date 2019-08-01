from django.db import models

'''
model untuk status host dan port
'''
class Status(models.Model):
    host = models.CharField(max_length=15)
    port = models.CharField(max_length=5)
    status = models.CharField(max_length=3)
    agent = models.CharField(max_length=15)
    timestamp = models.DateTimeField()

'''
    model untuk nama/ jenis/ keterangan service.
    Data pada model ini ditampilkan pada halaman utama,
    kolom "Service"
'''
class Service(models.Model):
    host = models.CharField(max_length=15)
    port = models.CharField(max_length=15)
    service = models.CharField(max_length=20)
