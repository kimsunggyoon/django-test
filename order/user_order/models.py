from django.db import models

# Create your models here.

class Shop(models.Model):
    shop_name = models.CharField(max_length=20)
    shop_address = models.CharField(max_length=40)


class Order(models.Model):
    shop = models.ForeignKey(Shop,on_delete=models.CASCADE)
    adddress = models.CharField(max_length=40)