from django.db import models
import uuid


class Payment(models.Model):
    type_choises = (('PAID', 'paid'), ('CANCELED', 'canceled'))
    #id = models.AutoField(primary_key=True)
    paymentUid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    status = models.CharField(max_length=20,choices=type_choises)
    price = models.IntegerField()
