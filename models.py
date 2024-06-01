from django.db import models
class employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    address=models.TextField(max_length=200)
    job=models.CharField(max_length=100)
    salary=models.IntegerField()

# Create your models here.
