from django.db import models

# Create your models here.


class EnergyLayer(models.Model):
    name = models.CharField(max_length=30)
    japanese_name = models.CharField(max_length=50, blank=True)
    abbreviation = models.CharField(max_length=8, blank=True, primary_key=True)
    aliases = models.CharField(max_length=50, blank=True)
    product_code = models.CharField(max_length=8, blank=True)
    initial_release = models.DateField(blank=True)
    weight = models.DecimalField(max_digits=10, decimal_places=3)
    part_image = models.ImageField(upload_to='parts/layers/', blank=True)

    LEFT = 'LT'
    RIGHT = 'RT'
    spin_direction_choices = (
        (LEFT, "Left"),
        (RIGHT, 'Right')
    )
    spin_direction = models.CharField(
        max_length=2,
        choices=spin_direction_choices,
        default=RIGHT
    )

    BURST = 'BR'
    DUAL_LAYER = 'DR'
    GOD_SYS = 'GD'
    CHO_Z = 'CZ'
    system_choices = (
        (BURST, 'Burst'),
        (DUAL_LAYER, 'Dual Layer'),
        (GOD_SYS, 'God Layer'),
        (CHO_Z, 'Cho Z')
    )
    system = models.CharField(
        max_length=2,
        choices=system_choices,
        blank=True
    )

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