from django.db import models
from django.db.models import F


# Create your models here.
class Galaxy(models.Model):
    name = models.CharField(max_length=100)
    size_x = models.IntegerField(null=True)
    size_y = models.IntegerField(null=True)

    class Meta:
        verbose_name_plural = "Galaxies"


class StarSystem(models.Model):
    name = models.CharField(max_length=100)
    position_x = models.IntegerField(null=True)
    position_y = models.IntegerField(null=True)
    galaxy = models.ForeignKey("Galaxy", on_delete=models.SET_NULL, null=True)


class Star(models.Model):
    name = models.CharField(max_length=100)
    diameter = models.IntegerField(null=True)
    color = models.CharField(max_length=100)
    star_system = models.ForeignKey("StarSystem", on_delete=models.SET_NULL, null=True)

    @property
    def square(self):
        return self.diameter*self.diameter*3.14


class Planet(models.Model):
    name = models.CharField(max_length=100)
    diameter = models.IntegerField(null=True)
    color = models.CharField(max_length=100)
    star_system = models.ForeignKey("StarSystem", on_delete=models.SET_NULL, null=True)
    live = models.BooleanField(null=True)

    @property
    def square(self):
        return self.diameter*self.diameter*3.14
