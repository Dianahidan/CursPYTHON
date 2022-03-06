# from products.models import Products
# from django.db import models

# class Reteta(models.Model):

#     nume_reteta = models.CharField(max_length=100)
#     tip_produs = models.CharField(max_length=100)
#     cantitate = models.ForeignKey(Products, on_delete=models.CASCADE)
#     um = models.CharField(max_length=10)
#     active = models.BooleanField(default=1)

#     def __str__(self):
#         return f"{self.tip_produs} - {self.cantitate} - {self.um}"

