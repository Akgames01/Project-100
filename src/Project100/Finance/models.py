from django.db import models

# Create your models here.
class Stock(models.Model):
    Name = models.TextField(max_length=200,null=False,blank=False)