from django.db import models


class Route(models.Model):
    route = models.CharField(max_length=50)
    distance = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.route)
