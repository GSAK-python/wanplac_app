from django.db import models


class Boats(models.Model):
    type = models.CharField(max_length=20)
    quantity = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.type)
