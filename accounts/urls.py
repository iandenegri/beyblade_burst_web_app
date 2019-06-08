from django.urls import path

from . import views


urlpatterns = [
    # path('', someview, name='some-name'),
    path('signup/', views.SignUp.as_view(), name='signup'),
]