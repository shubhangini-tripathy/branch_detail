from django.conf.urls import url
from django.contrib import admin

# from .views import bank_detail
from .views import bank_list

urlpatterns = [
    # url(r'^(?P<ifsc>[-\w]+)/$', bank_detail, name='detail'),
    # url(r'^(?P<bank_name>[-\w]+)/$', bank_list, name='branch'),
    url(r'/*', bank_list, name='branch'),

]
