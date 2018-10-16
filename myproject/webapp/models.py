from django.db import models
# Create your models here.
class Employee(models.Model):
    firstname=models.CharField(max_length=10)
    lastname=models.CharField(max_length=10)
    emp_id=models.IntegerField()

    def __str__(self):
        return self.firstname

class Category(models.Model):
    cat_name=models.CharField(max_length=50)
    cat_des=models.CharField(max_length=50)
    cat_id=models.IntegerField()

    def __str__(self):
        # return '%s %s' % (self.cat_name,self.cat_des)
        return '{} - {}'.format(self.cat_name,self.cat_des)
    