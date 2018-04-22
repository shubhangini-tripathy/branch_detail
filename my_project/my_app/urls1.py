from django.conf.urls import url
from django.contrib import admin

from .views import bank_detail

urlpatterns = [
    url(r'^(?P<ifsc>\d+)/$', bank_detail, name='detail'),
]
