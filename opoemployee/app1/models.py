from django.db import models

# Create your models here.

class Employee(models.Model):
	name=models.CharField(max_length=30)
	phone_number=models.IntegerField(default='123456789')
	password=models.CharField(max_length=500)
	email=models.CharField(max_length=100,unique=True)