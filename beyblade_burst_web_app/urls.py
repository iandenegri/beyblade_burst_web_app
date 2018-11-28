from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('energy_layers', views.EnergyLayerViewSet, 'energy_layers')
router.register('forge_disks', views.ForgeDiskViewSet, 'forge_disks')
router.register('performance_tips', views.PerformanceTipViewSet, 'performance_tips')


urlpatterns = [
    # path('admin/', admin.site.urls),
    # re_path(r'^', include(router.urls)),
    # re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^login/$', views.api_login),
] + router.urls
