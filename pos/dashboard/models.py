from django.db import models


# Create your models here.
class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Price = models.IntegerField(null=False)
    DateAdded = models.CharField(max_length=255)
    Distributor = models.CharField(max_length=255)


class Orders(models.Model):
    OrderId = models.AutoField(primary_key=True)
    CustomerId = models.IntegerField(null=False)
    ProductId = models.CharField(max_length=255, null=True, default=0)
    OrderDate = models.CharField(max_length=255)
    Status = models.IntegerField(null=False)
    Qty = models.IntegerField(null=False)


class Customers(models.Model):
    CustomerId = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    Phone = models.IntegerField(null=False)
    Email = models.EmailField(max_length=255, null=True)

    Street = models.CharField(max_length=255, null=True)
    Town = models.CharField(max_length=255, null=True)
    City = models.CharField(max_length=255, null=True)
    PostalCode = models.IntegerField(null=True)
