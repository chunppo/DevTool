from django.conf.urls import url

import views

urlpatterns = [
    url(r'^main/$', views.main, name='main'),
    url(r'^coupon/$', views.qrcode_coupon, name='qrcode_coupon'),
]
