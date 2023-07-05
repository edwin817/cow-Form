from django.db import models

# Create your models here.
class fadb(models.Model):
    name=models.CharField(max_length=30,null=True,blank=True)
    description=models.CharField(max_length=100,null=True,blank=True)
    image=models.ImageField(upload_to="profile",null=True,blank=True)

class apdb(models.Model):
    Name = models.CharField(max_length=30, null=True, blank=True)
    Category = models.CharField(max_length=30, null=True, blank=True)
    Price = models.IntegerField( null=True, blank=True)
    Qnty = models.IntegerField(null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to="profile", null=True, blank=True)

