from django.contrib.auth.models import User

from rest_framework import serializers

from routines.models import Routine


class UserSerializer(serializers.ModelSerializer):
    routines = serializers.PrimaryKeyRelatedField(many=True, queryset=Routine.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'routines')
