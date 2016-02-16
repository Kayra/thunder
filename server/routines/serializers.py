from rest_framework import serializers

from .models import Routine, Exercise


class RoutineSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Routine


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
