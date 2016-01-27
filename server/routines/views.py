from django.utils.datastructures import MultiValueDictKeyError

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from routines.models import Routine, Exercise

from routines.serializers import RoutineSerializer, ExerciseSerializer, FullRoutineSerializer

from routines.utilities import updateTotalTime


class RoutineList(generics.ListCreateAPIView):
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer


class RoutineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer


class ExerciseList(generics.ListCreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class ExerciseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


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
def createExercises(request):

    exercisesSerializer = ExerciseSerializer(data=request.data, many=True)

    if exercisesSerializer.is_valid():

        exercisesSerializer.save()

        updateTotalTime(id=request.data[0]['routine'])

        return Response(exercisesSerializer.data)

    else:
        return Response(exercisesSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def createExercise(request):

    exerciseSerializer = ExerciseSerializer(data=request.data)

    if exerciseSerializer.is_valid():

        exerciseSerializer.save()

        updateTotalTime(request.data['routine'])

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
        updateTotalTime(exercise.routine.id)
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

    updateTotalTime(exercise.routine.id)

    return Response(status=status.HTTP_202_ACCEPTED)
