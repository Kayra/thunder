from rest_framework import serializers

from .models import Routine, Exercise


class RoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routine


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise


class FullRoutineSerializer(serializers.ModelSerializer):

    routine = RoutineSerializer()

    class Meta:
        model = Exercise
        fields = ('name', 'completion_time', 'position', 'routine')
