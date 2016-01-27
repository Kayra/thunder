from django.conf.urls import url

from routines import views

urlpatterns = [

    url(r'^routines/$', views.RoutineList.as_view()),

    url(r'^routines/(?P<pk>[0-9]+)/$', views.RoutineDetail.as_view()),

    url(r'^exercises/$', views.ExerciseList.as_view()),

    url(r'^exercises/create-many/$', views.ExerciseCreateMany.as_view()),

    url(r'^exercises/(?P<pk>[0-9]+)/$', views.ExerciseDetail.as_view()),

]
