from django.db import models

# Create your models here.
class BankDetail(models.Model):
    ifsc = models.CharField(max_length=11)
    bank_id = models.PositiveSmallIntegerField()
    branch = models.CharField(max_length=150)
    address = models.TextField()
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    bank_name =  models.CharField(max_length=150)
