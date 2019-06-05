from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers
from .views import api_login, BeybladePartList, BeybladePartViewSet, CombinationViewSet


router = routers.DefaultRouter()
router.register('beyblade_parts', BeybladePartViewSet, 'beyblade_parts')
router.register('combinations', CombinationViewSet, 'combinations')


urlpatterns = [
    # path('admin/', admin.site.urls),
    # re_path(r'^', include(router.urls)),
    # re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login/', api_login),
    path('', BeybladePartList.as_view(), name="beyblade_part_list")
] + router.urls
