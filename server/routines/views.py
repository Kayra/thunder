from rest_framework import generics, status
from rest_framework.response import Response

from routines.models import Routine, Exercise
from routines.serializers import RoutineSerializer, ExerciseSerializer
from routines.utilities import updateTotalTime


class RoutineList(generics.ListCreateAPIView):
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Routine.objects.filter(user=self.request.user)


class RoutineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer


class ExerciseList(generics.ListCreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

    def get_queryset(self):
        routineId = self.request.query_params['routineId']
        return Exercise.objects.filter(routine__id=routineId)

    def perform_create(self, serializer):
        serializer.save()
        updateTotalTime(serializer.data['routine'])


class ExerciseCreateMany(generics.CreateAPIView):
    serializer_class = ExerciseSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()
        updateTotalTime(serializer.data[0]['routine'])


class ExerciseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

    def perform_update(self, serializer):
        serializer.save()
        updateTotalTime(serializer.data['routine'])

    def perform_destroy(self, instance):
        instance.delete()
        updateTotalTime(instance.routine.id)
