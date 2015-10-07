from __future__ import absolute_import

from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^get/routines$', views.getRoutines, name='get_routines'),

    url(r'^get/routine$', views.getRoutine, name='get_routine'),

    url(r'^post/routine$', views.postRoutine, name='post_routine'),

    url(r'^post/routine-delete$', views.postRoutineDelete, name='post_routine_delete'),

    url(r'^post/exercises$', views.postExercises, name='post_exercises'),

    url(r'^post/exercise$', views.postExercise, name='post_exercise'),

    url(r'^post/exercise-delete$', views.postExerciseDelete, name='post_exercise_delete'),

]
