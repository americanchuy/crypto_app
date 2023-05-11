from django.db import models

# Create your models here.

class currency(models.Model):
    name = models.CharField(max_length=20)
    rank = models.IntegerField()
    volume24 = models.FloatField(max_length=20)
    price = models.FloatField(max_length=20)
    ticker = models.CharField(max_length=8, default = '')
    

