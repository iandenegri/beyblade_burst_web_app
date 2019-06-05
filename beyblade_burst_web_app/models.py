from django.db import models

# Create your models here.

# After thinking about this for a while, I think that having just one part model would be easier. This would make serializing the parts and returning the parts to the user easier. Perhaps it would be possible to do this the original way but I think that this way will allow development to begin again.
class BeybladePart(models.Model):
    abbreviation = models.CharField(max_length=8, blank=True)
    name = models.CharField(max_length=30, unique=True)
    japanese_name = models.CharField(max_length=50, blank=True)
    aliases = models.CharField(max_length=50, blank=True)
    product_code = models.CharField(max_length=8, blank=True)
    initial_release = models.DateField(blank=True)
    weight = models.DecimalField(max_digits=10, decimal_places=3, blank=True)
    part_image = models.ImageField(upload_to='parts/layers/', blank=True)
    
    # FIELDS WITH CHOICES.
    part_types = (
        ("LAYER", 'Energy Layer'),
        ("DISK", 'Forge Disk'),
        ("TIP", 'Performance Tip'),
        ("FRAME", 'Disk Frame'),
        ("CHIP", 'Gatinko Chip'),
        ("WEIGHT", 'Gatinko Weight'),
        ("BASE", 'Gatinko Base')
    )
    part_type = models.CharField(
        max_length=30,
        choices=part_types,
        blank=False
    )

    system_choices = (
        ("BURST", 'Burst'),
        ("DUAL_LAYER", 'Dual Layer'),
        ("GOD_SYS", 'God Layer'),
        ("CHO_Z", 'Cho Zetsu'),
        ("GT", "Gatinko")
    )
    system = models.CharField(
        max_length=30,
        choices=system_choices,
        blank=True
    )

    spin_direction_choices = (
        ("LEFT", "Left"),
        ("RIGHT", "Right"),
        ("DUAL", "Dual"),
    )
    spin_direction = models.CharField(
        max_length=5,
        choices=spin_direction_choices,
        blank=True,
    )

    class Meta:
        verbose_name_plural = 'Parts'
        verbose_name = 'Part'

    def __str__(self):
        return self.name


class Combination(models.Model):
    name = models.CharField(max_length=50, unique=True)
    layer = models.ForeignKey(BeybladePart, on_delete=models.CASCADE, related_name="layers", related_query_name="layer")
    disk = models.ForeignKey(BeybladePart, on_delete=models.CASCADE, related_name="disks", related_query_name="disk")
    tip = models.ForeignKey(BeybladePart, on_delete=models.CASCADE, related_name="tips", related_query_name="tip")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Combinations'
        verbose_name = 'Combination'
