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
        serializer = RoutineSerializer(routines, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Exception as error:
        print('Couldn\'t get routines because:')
        print(error)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getRoutine(request):

    routineName = request.GET.get("routine", None)

    if routineName:

        exercises = Exercise.objects.filter(routine__name=routineName).order_by('position')

        fullSerializer = FullRoutineSerializer(exercises, many=True)

        return Response(fullSerializer.data, status=status.HTTP_200_OK)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def createRoutine(request):

    try:
        routine = Routine.objects.get(name=request.data['name'])
        routineSerializer = RoutineSerializer(routine, data=request.data)

    except Routine.DoesNotExist:
        routineSerializer = RoutineSerializer(data=request.data)

    except MultiValueDictKeyError:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if routineSerializer.is_valid():
        routineSerializer.save()
        return Response(routineSerializer.data)

    else:
        return Response(routineSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteRoutine(request):

    try:
        routine = Routine.objects.get(name=request.data['old_name'])
        routine.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

    except Routine.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def createExercises(request):

    # Convert routine name to ID
    for exercise in request.data:
        routineID = Routine.objects.get(name=exercise['routine']).id
        exercise['routine'] = routineID

    exercisesSerializer = ExerciseSerializer(data=request.data, many=True)

    if exercisesSerializer.is_valid():

        exercisesSerializer.save()

        # Update the total time. This needs to change
        routine = Routine.objects.get(id=request.data[0]['routine'])
        exercises = Exercise.objects.filter(routine=request.data[0]['routine'])
        totalTime = updateTotalTime(exercises)
        routine.total_time = totalTime
        routine.save()

        return Response(exercisesSerializer.data, status=status.HTTP_202_ACCEPTED)

    else:
        print(exercisesSerializer.errors)
        return Response(exercisesSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

    if exerciseSerializer.is_valid():

        exerciseSerializer.save()

        # Update the total time. This needs to change
        routine = Routine.objects.get(id=request.data['routine'])
        exercises = Exercise.objects.filter(routine=routine)
        totalTime = updateTotalTime(exercises)
        routine.total_time = totalTime
        print(totalTime)
        routine.save()

        return Response(exerciseSerializer.data, status=status.HTTP_202_ACCEPTED)

    else:
        print(exerciseSerializer.errors)
        return Response(exerciseSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteExercise(request):

    try:
        exercise = Exercise.objects.get(name=request.data['name'], position=request.data['position'], routine__name=request.data['routine'])
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
