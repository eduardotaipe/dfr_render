from django.db import models

class PetModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()

