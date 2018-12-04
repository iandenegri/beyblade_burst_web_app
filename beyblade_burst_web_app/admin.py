from django.contrib import admin
from beyblade_burst_web_app.models import EnergyLayer, ForgeDisk, PerformanceTip, Combination

# Register your models here.


@admin.register(EnergyLayer)
class EnergyLayerAdmin(admin.ModelAdmin):
    pass


@admin.register(ForgeDisk)
class ForgeDiskAdmin(admin.ModelAdmin):
    pass


@admin.register(PerformanceTip)
class PerformanceTipAdmin(admin.ModelAdmin):
    pass


@admin.register(Combination)
class CombinationAdmin(admin.ModelAdmin):
    pass
