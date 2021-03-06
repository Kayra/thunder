from rest_framework import serializers

from .models import Routine, Exercise


class RoutineSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Routine


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
