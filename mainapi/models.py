from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=255, unique=True)
    customer_name = models.CharField(max_length=255)
    date = models.DateField()


class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='details')
    description = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=5,decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    line_total = models.DecimalField(max_digits=10,decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
