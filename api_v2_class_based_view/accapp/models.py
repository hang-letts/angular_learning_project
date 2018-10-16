from django.db import models

# Create your models here.
class LoginModel(models.Model):
    email=models.EmailField(max_length=100)
    psswrd=models.CharField(max_length=100)

    def __str__(self):
        return "{}-{}".format(self.email,self.psswrd)

class ProfileModel(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone_no=models.CharField(max_length=10)

    def __str__(self):
        return "{}-{}-{}-{}".format(self.first_name,self.last_name,self.email,self.phone_no)