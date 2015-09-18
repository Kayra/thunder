from __future__ import absolute_import

from django.conf.urls import url

from . import views

urlpatterns = [

    # url(r'^$', views.routineView, name='routine'),

    url(r'^.*$', views.routineView, name='routine'),

    # APIs

    url(r'^api/routine_create$', views.routineCreate, name='routine_create'),

    url(r'^api/exercise_create$', views.exerciseCreate, name='exercise_create'),

]
