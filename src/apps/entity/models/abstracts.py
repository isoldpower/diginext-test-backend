from django.db import models

from .label import Label


class AbstractEntity(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    name = models.CharField(max_length=31, blank=False, null=False)
    labels = models.ManyToManyField(Label, blank=True)

    class Meta:
        abstract = True
