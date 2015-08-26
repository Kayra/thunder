from __future__ import absolute_import

from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.routineListView, name='list'),

    url(r'^add_edit/$', views.routineAddEditView, name='add_edit'),

    url(r'^use/$', views.routineUseView, name='use'),

]
