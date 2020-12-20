from django.db import models

class Customers (models.Model):
    tracking_code = models.CharField(max_length=20,null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    national_code = models.CharField(max_length=10)
    created_date = models.DateTimeField(null=True)
    update_date = models.DateTimeField(null=True)
    STATUS = (
        (1,'در حال بررسی'),
        (2,'رد درخواست'),
        (3,'تایید')
    )
    status = models.CharField(max_length=20, choices=STATUS)
    