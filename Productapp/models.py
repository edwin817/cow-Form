from django.db import models

# Create your models here.
class cartdb(models.Model):
    productname = models.CharField(max_length=30, null=True, blank=True)
    productqut = models.IntegerField(null=True, blank=True)
    totalprice = models.IntegerField(null=True, blank=True)
    productprice = models.IntegerField(null=True, blank=True)
    user = models.CharField(max_length=30, null=True, blank=True)
    image = models.ImageField(null=True)

class paymentdetaildb(models.Model):
    fullname = models.CharField(max_length=30, null=True, blank=True)
    emaill = models.CharField(max_length=30, null=True, blank=True)
    phonenumber = models.IntegerField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    address =models.TextField(max_length=30, null=True, blank=True)
    name =  models.CharField(max_length=30, null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)
    Month = models.CharField(max_length=100, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    cvv = models.IntegerField(null=True, blank=True)
    productname = models.CharField(max_length=30, null=True, blank=True)
    productprice = models.IntegerField(null=True, blank=True)
    total = models.CharField(max_length=100, null=True, blank=True)

class userdb(models.Model):
    username = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(max_length=30, null=True, blank=True)
    password = models.IntegerField( null=True, blank=True)
    confirmpassword = models.IntegerField(null=True, blank=True)

