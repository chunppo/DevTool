from django.conf.urls import url

import views

urlpatterns = [
    url(r'^$', views.list, name='index'),
    url(r'^list/$', views.list, name='list'),
    url(r'^servergroup/$', views.server_group, name='server_group'),
    url(r'^servergroup/add/$', views.server_group_add, name='server_group_add'),
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results,
]
