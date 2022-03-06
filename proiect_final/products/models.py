# from datetime import timezone
from django.db import models
from datetime import datetime
# from datetime import date
# from users.models import AuthUser

# Create your models here.


class Products(models.Model):

    tip_produs = models.CharField(max_length=100)
    cantitate = models.IntegerField(default=0)
    um = models.CharField(max_length=10)
    expiration_date = models.DateField(default=datetime.now)
    recur = models.BooleanField(default=True)
    minqty = models.IntegerField(default=0)
    active = models.BooleanField(default=1)
    necesar = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.tip_produs} - {self.cantitate} - {self.um} - {self.expiration_date}"


    def expired(self):
        # print(type(self.expiration_date),datetime.now())
        # print(self.expiration_date < datetime.now())
        return self.expiration_date <= datetime.now().date()
        # return False


