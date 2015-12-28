from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^get-routines', views.getRoutines, name='get_routines'),

    url(r'^get-routine', views.getRoutine, name='get_routine'),

    url(r'^create-routine', views.postRoutine, name='create_routine'),

    url(r'^delete-routine', views.postRoutineDelete, name='delete_routine'),

    url(r'^create-exercises', views.postExercises, name='create_exercises'),

    url(r'^create-exercise', views.postExercise, name='create_exercise'),

    url(r'^delete-exercise', views.postExerciseDelete, name='delete_exercise'),

]
