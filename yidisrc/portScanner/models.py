from django.db import models

# Create your models here.

class PortScanner(models.Model):
    id = models.AutoField(primary_key=True)
    ip_address = models.CharField(max_length=64)
    port_num = models.IntegerField()
    port_status = models.CharField(max_length=64)