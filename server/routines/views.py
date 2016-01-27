from rest_framework import generics

from routines.models import Routine, Exercise

from routines.serializers import RoutineSerializer, ExerciseSerializer

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

    def get_queryset(self):
        routineId = self.request.query_params['routineId']
        return Exercise.objects.filter(routine__id=routineId)


class ExerciseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
