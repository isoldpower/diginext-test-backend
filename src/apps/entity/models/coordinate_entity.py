from django.db import models
from .abstracts import AbstractEntity


class CoordinateEntity(AbstractEntity):
    x = models.FloatField(blank=False, null=False, default=0.0)
    y = models.FloatField(blank=False, null=False, default=0.0)

    class Meta:
        db_table = 'coordinate_entity'

    def __str__(self):
        return self.name
