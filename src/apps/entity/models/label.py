from django.db import models


class Label(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    title = models.CharField(max_length=31)

    def __str__(self):
        return self.title
