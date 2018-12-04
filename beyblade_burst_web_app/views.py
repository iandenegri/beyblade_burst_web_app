from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404

from beyblade_burst_web_app.models import EnergyLayer, ForgeDisk, PerformanceTip, Combination
from beyblade_burst_web_app.serializers import (EnergyLayerSerializer, ForgeDiskSerializer, PerformanceTipSerializer,
                                                CombinationSerializer)

from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


# Create your views here.


@permission_classes([AllowAny])
class EnergyLayerViewSet(viewsets.ModelViewSet):
    """
    API Endpoint that allows energy layers to be viewed or edited.
    Sample URL's to select a part:
    'http://localhost:8000/api/energy_layers/V/'
    'http://localhost:8000/api/energy_layers/A2/'
    'http://localhost:8000/api/energy_layers/kD/'
    """
    queryset = EnergyLayer.objects.all().order_by("abbreviation")
    serializer_class = EnergyLayerSerializer


@permission_classes([AllowAny])
class ForgeDiskViewSet(viewsets.ModelViewSet):
    """
    API Endpoint that allows forge disks to be viewed or edited.
    """
    queryset = ForgeDisk.objects.all().order_by("abbreviation")
    serializer_class = ForgeDiskSerializer


@permission_classes([AllowAny])
class PerformanceTipViewSet(viewsets.ModelViewSet):
    """
    API Endpoint that allows performance tips to be viewed or edited.
    """
    queryset = PerformanceTip.objects.all().order_by("abbreviation")
    serializer_class = PerformanceTipSerializer


@permission_classes([AllowAny])
class CombinationViewSet(viewsets.ModelViewSet):
    """
    API Endpoint that allows combinations to be viewed or edited.
    """
    queryset = Combination.objects.all().order_by("name")
    serializer_class = CombinationSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def api_login(request):
    username = request.data['username']
    password = request.data['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)