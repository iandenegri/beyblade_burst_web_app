from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, TemplateView, DetailView, CreateView
from django.urls import reverse

from beyblade_burst_web_app.models import BeybladePart, Combination
from beyblade_burst_web_app.serializers import (BeybladePartSerializer, CombinationSerializer)
from beyblade_burst_web_app.forms import BeybladePartCreateForm, CombinationCreateForm

from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


# Create your views here.
class Index(TemplateView):
    template_name="beyblade_burst_web_app/html/index.html"

    def get_context_data(self, *args, **kwargs):
        context = super(Index, self).get_context_data(*args, **kwargs)
        all_parts = list(BeybladePart.objects.all())
        latest_parts = all_parts[-3:] # This can fail in an instance where there's less than 3 parts. Soon this will fail if there are less than 3 parts that qualify as "latest"

        last_combo = Combination.objects.all().latest('id')

        context['latest_parts'] = latest_parts
        context['last_combo'] = last_combo

        return context


class BeybladePartListView(ListView):
    model = BeybladePart
    queryset = BeybladePart.objects.all().order_by('initial_release')
    template_name="beyblade_burst_web_app/html/part_list.html"

    def get_context_data(self, **kwargs):
        context = super(BeybladePartListView, self).get_context_data(**kwargs)
        return context

    def head(self, *args, **kwargs):
        last_part = self.get_queryset().latest('id')
        response = HttpResponse('')
        # RFC 1123 date format
        response['name'] = last_part['name']
        return response

class BeybladePartDetailView(DetailView):
    model = BeybladePart
    template_name="beyblade_burst_web_app/html/part_detail.html"

class BeybladePartCreateView(CreateView):
    model = BeybladePart
    form_class = BeybladePartCreateForm
    template_name = "beyblade_burst_web_app/html/part_create.html"

    def get_success_url(self, *args, **kwargs):
        return reverse('beyblade_part_detail', kwargs={'pk':self.object.id})

class CombinationCreateView(CreateView):
    model = Combination
    form_class = CombinationCreateForm
    template_name = "beyblade_burst_web_app/html/combo_create.html"

    def get_success_url(self, *args, **kwargs):
        return reverse('index')

# API VIEWS

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

@permission_classes([AllowAny])
class BeybladePartViewSet(viewsets.ModelViewSet):
    """
    API Endpoint that allows beyblade parts to be viewed or edited.
    """
    queryset = BeybladePart.objects.all().order_by("product_code")
    serializer_class = BeybladePartSerializer


@permission_classes([AllowAny])
class CombinationViewSet(viewsets.ModelViewSet):
    """
    API Endpoint that allows combinations to be viewed or edited.
    """
    queryset = Combination.objects.all().order_by("name")
    serializer_class = CombinationSerializer