from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('beyblade_parts', views.BeybladePartViewSet, 'beyblade_parts')
router.register('combinations', views.CombinationViewSet, 'combinations')
# router.register('part_list', views.PartListViewSet, 'part_list')


urlpatterns = [
    # path('admin/', admin.site.urls),
    # re_path(r'^', include(router.urls)),
    # re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^login/$', views.api_login),
] + router.urls
