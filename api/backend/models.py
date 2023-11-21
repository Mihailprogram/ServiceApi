from django.db import models


class Service(models.Model):
    cadastral_number = models.IntegerField()
    width = models.IntegerField()
    longitude = models.IntegerField()
    status = models.BooleanField()
