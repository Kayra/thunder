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
def getRoutine(request):

    try:
        identifier = request.query_params['id']
    except MultiValueDictKeyError:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    try:
        routine = Routine.objects.get(pk=identifier)
    except Routine.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except TypeError:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializedRoutine = RoutineSerializer(routine)
    return Response(serializedRoutine.data)


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


@api_view(['PUT'])
def editRoutine(request):

    try:
        routine = Routine.objects.get(pk=request.data['id'])
        serializedRoutine = RoutineSerializer(routine, data=request.data)
    except MultiValueDictKeyError:
        serializedRoutine = RoutineSerializer(data=request.data)
    except Routine.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if serializedRoutine.is_valid():
        serializedRoutine.save()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(serializedRoutine.errors, status=status.HTTP_400_BAD_REQUEST)


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


@api_view(['POST'])
def createExercise(request):

    exerciseSerializer = ExerciseSerializer(data=request.data)

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


@api_view(['PUT'])
def editExercise(request):

    try:
        exercise = Exercise.objects.get(pk=request.data['id'])
        serializedExercise = ExerciseSerializer(exercise, data=request.data)
    except MultiValueDictKeyError:
        serializedExercise = ExerciseSerializer(data=request.data)
    except Exercise.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if serializedExercise.is_valid():
        serializedExercise.save()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(serializedExercise.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteExercise(request):

    #  Handle both query params and data to satisfy the lack of query params in test client
    try:
        exercise = Exercise.objects.get(pk=request.query_params['id'])
    except MultiValueDictKeyError:
        try:
            exercise = Exercise.objects.get(pk=request.data['id'])
        except MultiValueDictKeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    except Exercise.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    exercise.delete()

    # Update the total time. This needs to change
    routine = Routine.objects.get(pk=request.data['routine'])
    exercises = Exercise.objects.filter(routine=routine)
    totalTime = updateTotalTime(exercises)
    routine.total_time = totalTime
    routine.save()

    return Response(status=status.HTTP_202_ACCEPTED)
