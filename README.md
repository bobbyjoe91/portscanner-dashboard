#### Requirement
Python3<br>
Django 2.2.3<br>
Pip, pip3, or pip3.7<br>

pymongo -> pip install pymongo<br>
dnspython -> pip install dnspython<br>
djongo -> pip install djongo<br>

you can use pip3 or pip3.7 to install all dependencies. Just replace 'pip' with 'pip3' or 'pip3.7'<br><br>

### Database
The host of the database is set into localhost as default setting.<br>
You can change it in portscanner_dashboard/settings.py
```
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'asli_ri_services_2',
        'HOST': '127.0.0.1', # 10.8.30.69
        'PORT': 27017
    }
}
```

### Models
Models can be accessed in dashboard/models.py. The attributes of the models are specified below:<br>
```
from django.db import models

class Status(models.Model):
    host = models.CharField(max_length=15)
    port = models.CharField(max_length=5)
    status = models.CharField(max_length=3)
    agent = models.CharField(max_length=15)
    timestamp = models.DateTimeField()
```
<br>
The database should contain attributes named 'id', 'host', 'port', 'status', 'agent', and 'timestamp'.
