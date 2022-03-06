from django.db import models

class ShoppingList(models.Model):

    tip_produs = models.CharField(max_length=100)
    cantitate = models.IntegerField()
    um = models.CharField(max_length=10)
    active = models.BooleanField(default=1)

    def __str__(self):
        return f"{self.tip_produs} - {self.cantitate} -{self.um}"