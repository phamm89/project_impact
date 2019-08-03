from django.urls import path, re_path
from core import views

urlpatterns = [
    path(r'^$', views.app, name='twilio'),
    re_path(r'^token', views.token, name='token'),
]


