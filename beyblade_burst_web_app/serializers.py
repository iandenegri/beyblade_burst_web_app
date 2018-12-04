from beyblade_burst_web_app.models import EnergyLayer, ForgeDisk, PerformanceTip, Combination
from rest_framework import serializers


class EnergyLayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnergyLayer
        fields = ('name', 'japanese_name', 'abbreviation', 'aliases', 'product_code', 'initial_release',
                  'weight', 'part_image', 'spin_direction', 'system',)


class ForgeDiskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForgeDisk
        fields = ('name', 'abbreviation', 'product_code', 'weight')


class PerformanceTipSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerformanceTip
        fields = ('name', 'abbreviation', 'product_code', 'weight')


class CombinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Combination
        fields = ('id', 'name', 'layer', 'disk', 'tip')
