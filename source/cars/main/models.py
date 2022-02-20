from django.db import models
import uuid


# Create your models here.
class Car(models.Model):
    type_choises = (('SEDAN','sedan'),('SUV','suv'),('MINIVAN','minivan'),('ROADSTER','roadster'))

    carUid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    brand = models.CharField(max_length=80)
    model = models.CharField(max_length=80)
    registrationNumber = models.CharField(max_length=80)
    power = models.IntegerField()
    price = models.IntegerField()
    carType = models.CharField(max_length=20,choices=type_choises)
    availability = models.BooleanField()


