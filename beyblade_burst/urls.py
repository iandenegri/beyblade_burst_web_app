"""beyblade_burst URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve
from django.conf import settings

from beyblade_burst_web_app.views import Index

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('admin/', admin.site.urls),
    
    path('accounts/', include('accounts.urls')),  # Adding this path manually so that users can register using the same path.
    path('accounts/', include('django.contrib.auth.urls')),  # Using this to handle sign ins using default User model...

    path('beyblade_burst_web_app/', include('beyblade_burst_web_app.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(
        r'media/(?P<path>.*)$', 
        serve, 
        {'document_root': settings.MEDIA_ROOT,}
        ),
]
