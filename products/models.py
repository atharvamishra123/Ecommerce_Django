from django.db import models
from loginsignup.models import CustomUsers


# Create your models here.
class Products(models.Model):
    CATEGORY = (
                ("male", "male"),
                ("female", "female"),
                )

    name = models.CharField(max_length=25)
    gender = models.CharField(max_length=10, null=True, choices=CATEGORY)
    pic = models.ImageField(upload_to="myimages")
    
    def __str__(self):
        return self.name


class Sub_Products(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    pic = models.ImageField(upload_to="sub_products")
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ManyToManyField(CustomUsers, blank=True)

    def __str__(self):
        return self.name
