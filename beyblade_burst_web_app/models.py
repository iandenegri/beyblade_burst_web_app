from django.db import models

# Create your models here.


class EnergyLayer(models.Model):
    name = models.CharField(max_length=30)
    abbreviation = models.CharField(max_length=8, blank=True, primary_key=True)
    product_code = models.CharField(max_length=8, blank=True)
    weight = models.DecimalField(max_digits=10, decimal_places=3)

    class Meta:
        verbose_name_plural = 'Energy Layers'
        verbose_name = 'Energy Layer'

    def __str__(self):
        return self.name


class ForgeDisk(models.Model):
    name = models.CharField(max_length=30)
    abbreviation = models.CharField(max_length=8, blank=True, primary_key=True)
    product_code = models.CharField(max_length=8, blank=True)
    weight = models.DecimalField(max_digits=10, decimal_places=3)

    class Meta:
        verbose_name_plural = 'Forge Disks'
        verbose_name = 'Forge Disk'

    def __str__(self):
        return self.name


class PerformanceTip(models.Model):
    name = models.CharField(max_length=30)
    abbreviation = models.CharField(max_length=8, blank=True, primary_key=True)
    product_code = models.CharField(max_length=8, blank=True)
    weight = models.DecimalField(max_digits=10, decimal_places=3)

    class Meta:
        verbose_name_plural = 'Performance Tips'
        verbose_name = 'Performance Tip'

    def __str__(self):
        return self.name


"""
class Combination(models.Model):
    name = models.CharField(max_length=50)
    layer = models.ForeignKey(EnergyLayer, on_delete=models.CASCADE)
    disk = models.ForeignKey(ForgeDisk, on_delete=models.CASCADE)
    tip = models.ForeignKey(PerformanceTip, on_delete=models.CASCADE)

"""