import os
from django.utils import timezone
from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class TailingsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().using('tailings')


class TailingsBaseModel(models.Model):
    objects = TailingsManager()

    class Meta:
        abstract = True


class MonitoringTypes(models.TextChoices):
    SENTINEL = 'sentinel', _('Sentinel')
    TSX = 'tsx', _('TerrasarX')


class SortOrder(models.TextChoices):
    ASC = 'asc', _('Ascending')
    DESC = 'desc', _('Descending')


class Client(TailingsBaseModel):
    name = models.CharField(max_length=100, blank=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class MonitoringFrequency(TailingsBaseModel):
    sort_order = models.CharField(
        max_length=10,
        choices=SortOrder.choices,
        blank=False,
        null=True,
        default=SortOrder.ASC
    )
    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name


class Site(TailingsBaseModel):
    name = models.CharField(max_length=100, blank=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    geometry = models.PolygonField(srid=4326)
    monitoring_type = models.CharField(max_length=30, choices=MonitoringTypes.choices, default=MonitoringTypes.SENTINEL)
    monitoring_frequency = models.ForeignKey(MonitoringFrequency, on_delete=models.CASCADE)
    relative_orbit = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.client.name}"


class ModelRun(TailingsBaseModel):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)


class MonitoringPoint(TailingsBaseModel):
    code = models.CharField(null=True, blank=True, max_length=10)
    geometry = models.PointField(srid=4326, null=True)
    height = models.FloatField(blank=True, null=True)
    h_stdev = models.FloatField(blank=True, null=True)
    vel = models.FloatField(blank=True, null=True)
    v_stdev = models.FloatField(blank=True, null=True)
    coherence = models.FloatField(blank=True, null=True)
    eff_area = models.FloatField(blank=True, null=True)
    model_run = models.ForeignKey(ModelRun, null=True, on_delete=models.CASCADE)


class MonitoringSample(TailingsBaseModel):
    monitoring_point = models.ForeignKey(MonitoringPoint, on_delete=models.CASCADE)
    date = models.DateField()
    value = models.FloatField(blank=True, null=True)
