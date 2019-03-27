from beyblade_burst_web_app.models import BeybladePart, Combination
from rest_framework import serializers


class BeybladePartSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeybladePart
        fields = ('name', 'japanese_name', 'abbreviation', 'aliases', 'product_code', 'initial_release',
                  'weight', 'part_image', 'spin_direction', 'system', 'part_type')


class CombinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Combination
        fields = ('id', 'name', 'layer', 'disk', 'tip')
        depth = 1
