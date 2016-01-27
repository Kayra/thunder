from django.conf.urls import url

from routines import views

urlpatterns = [

    url(r'^get-full-routine', views.getFullRoutine, name='get_full_routine'),

    url(r'^create-exercises', views.createExercises, name='create_exercises'),

    url(r'^create-exercise', views.createExercise, name='create_exercise'),

    url(r'^edit-exercise', views.editExercise, name='edit_exercise'),

    url(r'^delete-exercise', views.deleteExercise, name='delete_exercise'),

    url(r'^routines/$', views.RoutineList.as_view()),

    url(r'^routines/(?P<pk>[0-9]+)/$', views.RoutineDetail.as_view()),

    url(r'^exercises/$', views.ExerciseList.as_view()),

    url(r'^exercises/(?P<pk>[0-9]+)/$', views.ExerciseDetail.as_view()),

]
