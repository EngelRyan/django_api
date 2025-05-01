from django.db import models
from django.utils.timezone import now

from .validators import validate_min_data

# Create your models here.
class Person(models.Model):
    age = models.IntegerField()
    name = models.CharField(max_length=100)
    birth_date = models.DateField(default=now, validators=[validate_min_data])

    def __str__(self):
        return self.name