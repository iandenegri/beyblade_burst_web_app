from django.db import models

# Create your models here.


class EnergyLayer(models.Model):
    name = models.CharField(max_length=30)
    abbreviation = models.CharField(max_length=8, blank=True, primary_key=True)
    product_code = models.CharField(max_length=8, blank=True)
    weight = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return self.name


class ForgeDisk(models.Model):
    name = models.CharField(max_length=30)
    abbreviation = models.CharField(max_length=8, blank=True, primary_key=True)
    product_code = models.CharField(max_length=8, blank=True)
    weight = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return self.name


class PerformanceTip(models.Model):
    name = models.CharField(max_length=30)
    abbreviation = models.CharField(max_length=8, blank=True, primary_key=True)
    product_code = models.CharField(max_length=8, blank=True)
    weight = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return self.name
