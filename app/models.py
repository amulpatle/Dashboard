from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_customer = models.BooleanField('Is customer', default=False)
    is_employee = models.BooleanField('Is employee', default=False)
    # address_line1 = models.CharField(max_length=100,null=True,blank=True)
    # city = models.CharField(max_length=50,null=True)
    # state = models.CharField(max_length=50,null=True)
    # pincode = models.CharField(max_length=10,null=True)
    # profile_picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True)
