from django.shortcuts import render
from beyblade_burst_web_app.models import EnergyLayer, ForgeDisk, PerformanceTip
from rest_framework import viewsets
from beyblade_burst_web_app.serializers import EnergyLayerSerializer, ForgeDiskSerializer, PerformanceTipSerializer

# Create your views here.


class EnergyLayerViewSet(viewsets.ModelViewSet):
    """
    API Endpoint that allows energy layers to be viewed or edited.
    """
    queryset = EnergyLayer.objects.all().order_by("abbreviation")
    serializer_class = EnergyLayerSerializer


class ForgeDiskViewSet(viewsets.ModelViewSet):
    """
    API Endpoint that allows forge disks to be viewed or edited.
    """
    queryset = ForgeDisk.objects.all().order_by("abbreviation")
    serializer_class = ForgeDiskSerializer


class PerformanceTipViewSet(viewsets.ModelViewSet):
    """
    API Endpoint that allows performance tips to be viewed or edited.
    """
    queryset = PerformanceTip.objects.all().order_by("abbreviation")
    serializer_class = PerformanceTipSerializer
