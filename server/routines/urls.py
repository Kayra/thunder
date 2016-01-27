from django.conf.urls import url

from routines import views

urlpatterns = [

    url(r'^get-routines', views.getRoutines, name='get_routines'),

    url(r'^get-routine', views.getRoutine, name='get_routine'),

    url(r'^get-full-routine', views.getFullRoutine, name='get_full_routine'),

    url(r'^create-routine', views.createRoutine, name='create_routine'),

    url(r'^edit-routine', views.editRoutine, name='edit_routine'),

    url(r'^delete-routine', views.deleteRoutine, name='delete_routine'),

    url(r'^create-exercises', views.createExercises, name='create_exercises'),

    url(r'^create-exercise', views.createExercise, name='create_exercise'),

    url(r'^edit-exercise', views.editExercise, name='edit_exercise'),

    url(r'^delete-exercise', views.deleteExercise, name='delete_exercise'),

    url(r'^routines/$', views.RoutineList.as_view()),

    url(r'^routines/(?P<pk>[0-9]+)/$', views.RoutineDetail.as_view()),

]
