from django.contrib import admin
from beyblade_burst_web_app.models import BeybladePart, Combination

# Register your models here.


@admin.register(BeybladePart)
class BeybladePartAdmin(admin.ModelAdmin):
    list_display = ['name', 'product_code', 'abbreviation', ]
    ordering = ['product_code', 'name']

@admin.register(Combination)
class CombinationAdmin(admin.ModelAdmin):
    pass
