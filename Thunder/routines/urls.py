from __future__ import absolute_import

from django.conf.urls import url

from . import views

urlpatterns = [

    # url(r'^$', views.routineView, name='routine'),

    url(r'^$', views.routineView, name='routine'),

    # APIs

    url(r'^api/routine_create$', views.routineCreate, name='routine_create'),

    url(r'^api/exercise_create$', views.exerciseCreate, name='exercise_create'),

    url(r'^api/get/routines$', views.getRoutines, name='get_routines'),

    url(r'^api/get/routine$', views.getRoutine, name='get_routine'),

    url(r'^api/post/routine$', views.postRoutine, name='post_routine'),

    url(r'^api/post/routine-delete$', views.postRoutineDelete, name='post_routine_delete'),

    url(r'^api/post/exercises$', views.postExercises, name='post_exercises'),

    url(r'^api/post/exercise$', views.postExercise, name='post_exercise'),

    url(r'^api/post/exercise-delete$', views.postExerciseDelete, name='post_exercise_delete'),

]
