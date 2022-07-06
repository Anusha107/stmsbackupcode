from django.db import models

# Create your models here.


class companyreg(models.Model):
    userid = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class Add_company(models.Model):
    name = models.CharField(max_length=20)
    symbol = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    address = models.CharField(max_length=30)
    phonenumber = models.IntegerField()
    select = models.CharField(max_length=10)
    image = models.ImageField(upload_to='product_image/')

class Add_Agent(models.Model):
    id = models.AutoField(primary_key=True,max_length=1000)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    address = models.CharField(max_length=20)
    phonenumber = models.IntegerField()



