from django.conf.urls import url

from routines import views

urlpatterns = [

    url(r'^routines/$', views.RoutineListCreate.as_view(), name='routine_list_create'),

    url(r'^routines/(?P<pk>[0-9]+)/$', views.RoutineDetail.as_view(), name='routine_detail'),

    url(r'^exercises/$', views.ExerciseList.as_view(), name='exercise_list_create'),

    url(r'^exercises/create-many/$', views.ExerciseCreateMany.as_view(), name='exercise_create_many'),

    url(r'^exercises/(?P<pk>[0-9]+)/$', views.ExerciseDetail.as_view(), name='exercise_detail'),

]
