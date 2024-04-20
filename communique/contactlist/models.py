from django.db import models

# Create your models here.

class CustomTable(models.Model):
    table_name = models.CharField(max_length=200)

    def __str__(self):
        return self.table_name

class DbConTab():
    name = models.CharField(max_length=100)