from django.db import models

# Create your models here.
class User(models.Model):
    Name = models.CharField(max_length=200,blank=False,null=False)
    UserID = models.CharField(max_length=100,blank=False,null=False)
    Password = models.CharField(max_length=100,blank=False,null=False)
    DOB = models.DateField(blank=False,null=False)
    email = models.EmailField(default='Example@gmail.com',blank=False,null=False)
    Phone = models.CharField(default=' ',max_length=10,blank=False,null=False)
    PlaceofBirth = models.TextField(default='',blank=True,null=True)
class Login(models.Model):
    UserID = models.CharField(max_length=200)
    Password = models.CharField(max_length=200)