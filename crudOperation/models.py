from django.db import models

# Create your models here.
class Employee(models.Model):
    empId = models.CharField(max_length=20)
    empName = models.CharField(max_length=100)
    empEmail = models.EmailField()
    empContact = models.CharField(max_length=10)
    class Meta:
        db_table = 'employee'