from django.utils.datastructures import MultiValueDictKeyError

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Routine, Exercise

from .serializers import RoutineSerializer, ExerciseSerializer, FullRoutineSerializer

from .utilities import updateTotalTime


@api_view(['GET'])
def getRoutines(request):

    try:
        routines = Routine.objects.all()
    except Routine.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    serializer = RoutineSerializer(routines, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getFullRoutine(request):

    try:
        identifier = request.query_params['id']
    except MultiValueDictKeyError:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    exercises = Exercise.objects.filter(routine__id=identifier).order_by('position')
    fullSerializer = FullRoutineSerializer(exercises, many=True)
    return Response(fullSerializer.data)


@api_view(['POST'])
def createRoutine(request):

    routineSerializer = RoutineSerializer(data=request.data)

    if routineSerializer.is_valid():
        routineSerializer.save()
        return Response(routineSerializer.data)

    else:
        return Response(routineSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteRoutine(request):

    #  Handle both query params and data to satisfy the lack of query params in test client
    try:
        identifier = request.query_params['id']
    except MultiValueDictKeyError:
        identifier = request.data['id']

    try:
        routine = Routine.objects.get(pk=identifier)
    except Routine.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    routine.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def createExercises(request):

    exercisesSerializer = ExerciseSerializer(data=request.data, many=True)

    if exercisesSerializer.is_valid():

        exercisesSerializer.save()

        # Update the total time. This needs to change
        try:
            routine = Routine.objects.get(id=request.data[0]['routine'])
            exercises = Exercise.objects.filter(routine=request.data[0]['routine'])
            totalTime = updateTotalTime(exercises)
            routine.total_time = totalTime
            routine.save()
        except MultiValueDictKeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(exercisesSerializer.data)

    else:
        return Response(exercisesSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


#  NEEDS WORK
@api_view(['POST'])
def createExercise(request):

    try:
        exercise = Exercise.objects.get(name=request.data['name'], position=request.data['position'])
        routineID = Routine.objects.get(name=request.data['routine']).id
        request.data['routine'] = routineID
        exerciseSerializer = ExerciseSerializer(exercise, data=request.data)

    except Exercise.DoesNotExist:
        routineID = Routine.objects.get(name=request.data['routine']).id
        request.data['routine'] = routineID
        exerciseSerializer = ExerciseSerializer(data=request.data)

    except MultiValueDictKeyError:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if exerciseSerializer.is_valid():

        exerciseSerializer.save()

        # Update the total time. This needs to change
        routine = Routine.objects.get(id=request.data['routine'])
        exercises = Exercise.objects.filter(routine=routine)
        totalTime = updateTotalTime(exercises)
        routine.total_time = totalTime
        routine.save()

        return Response(exerciseSerializer.data)

    else:
        return Response(exerciseSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteExercise(request):

    try:
        exercise = Exercise.objects.get(pk=request.data['id'])
        exercise.delete()

        # Update the total time. This needs to change
        routine = Routine.objects.get(name=request.data['routine'])
        exercises = Exercise.objects.filter(routine=routine)
        totalTime = updateTotalTime(exercises)
        routine.total_time = totalTime
        routine.save()

        return Response(status=status.HTTP_202_ACCEPTED)

    except Exercise.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
