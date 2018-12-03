from beyblade_burst_web_app.models import EnergyLayer, ForgeDisk, PerformanceTip
from rest_framework import serializers


class EnergyLayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EnergyLayer
        fields = ('name', 'japanese_name', 'abbreviation', 'aliases', 'product_code', 'initial_release',
                  'weight', 'part_image', 'spin_direction', 'system',)


class ForgeDiskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ForgeDisk
        fields = ('name', 'abbreviation', 'product_code', 'weight')


class PerformanceTipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PerformanceTip
        fields = ('name', 'abbreviation', 'product_code', 'weight')
