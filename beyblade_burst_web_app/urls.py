from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers
from .views import api_login, BeybladePartListView, BeybladePartViewSet, CombinationViewSet, BeybladePartDetailView


router = routers.DefaultRouter()
router.register('beyblade_parts', BeybladePartViewSet, 'beyblade_parts')
router.register('combinations', CombinationViewSet, 'combinations')


urlpatterns = [
    path('login/', api_login),

    path('', BeybladePartListView.as_view(), name="beyblade_part_list"),
    path('<int:pk>/', BeybladePartDetailView.as_view(), name='beyblade_part_detail'),
] + router.urls
