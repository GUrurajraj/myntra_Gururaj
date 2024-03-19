from django.db import models
from django.contrib.auth.models import User


class CustomManager(models.Manager):
    def mobile_list(self):
        return self.filter(category__exact="Mobile")  # orm query

    def cloths_list(self):
        return self.filter(category__exact="Cloths")  # orm query

    def shoes_list(self):
        return self.filter(category__exact="Shoes")  # orm query

    def electronics_list(self):
        return self.filter(category__exact="Electronics")  # orm query

    def pricerange(self, r1, r2):
        return self.filter(price__range=(r1, r2))


# Create your models here.
class Product(models.Model):
    userid = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    productid = models.IntegerField(primary_key=True)
    productname = models.CharField(max_length=50)
    type = (
        ("Mobile", "Mobile"),
        ("Cloths", "Cloths"),
        ("Shoes", "Shoes"),
        ("Electronics", "Electronics"),
    )
    category = models.CharField(max_length=50, choices=type, default="")
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to="photos")
    objects = models.Manager()
    productmanager = CustomManager()


class Cart(models.Model):
    userid = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    productid = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    qty = models.PositiveIntegerField(default=0)


class Order(models.Model):
    orderid = models.IntegerField(primary_key=True)
    userid = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    productid = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    qty = models.PositiveIntegerField(default=0)
