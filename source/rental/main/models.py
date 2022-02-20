from django.db import models
import uuid

class Rental(models.Model):

    type_choises = (('IN_PROGRESS', 'IN_PROGRESS'), ('FINISHED', 'FINISHED'), ('CANCELED', 'CANCELED'))

    rentalUid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    username = models.CharField(max_length=80)

    paymentUid = models.UUIDField(default=uuid.uuid4)
    carUid = models.UUIDField(default=uuid.uuid4)

    dateFrom = models.DateField()
    dateTo = models.DateField()

    status = models.CharField(max_length=20, choices=type_choises)




