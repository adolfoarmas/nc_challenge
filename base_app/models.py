from random import choices
from django.db import models
from .choices import (
    PAYMENT_METHOD,
    PAYMENT_STATUS,
    SERVICE_TYPE,
    )


class Payable(models.Model):
    bar_code =  models.CharField(primary_key=True, max_length=12)
    service_type = models.CharField(max_length=3, choices=SERVICE_TYPE)
    service_description = models.CharField(max_length=30)
    due_date = models.DateField()
    service_cost = models.DecimalField(max_digits=8, decimal_places=2)
    #currency = models.CharField(max_length=3, choices=CURRENCY)
    payment_status = models.CharField(max_length=2, choices=PAYMENT_STATUS)


class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    bar_code =  models.OneToOneField(Payable, on_delete=models.DO_NOTHING)
    payment_method = models.CharField(max_length=2, choices=PAYMENT_METHOD)
    # null regarding tu db behavior / blank regarding to forms validations
    card_number = models.DecimalField(max_digits=16, decimal_places=0, null=True, blank=True) 
    payment_ammount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_date = models.DateField()
    
