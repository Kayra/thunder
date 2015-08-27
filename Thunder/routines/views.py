from __future__ import absolute_import

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Routine, Exercise

from .serializers import RoutineSerializer, ExerciseSerializer


@login_required
def routineListView(request):
    return render(request, 'routines/routine_list.html')


@login_required
def routineAddEditView(request):
    return render(request, 'routines/routine_add_edit.html')


@login_required
def routineUseView(request):
    return render(request, 'routines/routine_use.html')


# API #########################################################################

@api_view(['POST'])
def routineCreate(request):

    serializer = RoutineSerializer(data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def exerciseCreate(request):

    serializer = ExerciseSerializer(data=request.data)
    serializer.initial_data['routine'] = Routine.objects.filter(name=serializer.initial_data['routine'])[:1]

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def routineGet(request):

    exercises = Exercise.objects.get(routine=request.data['routine'], routine__user=request.user)
    serializer = ExerciseSerializer(exercises, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def routinesGet(request):

    routines = Routine.objects.get(user=request.user)
    serializer = RoutineSerializer(routines, many=True)

    return Response(serializer.data)
