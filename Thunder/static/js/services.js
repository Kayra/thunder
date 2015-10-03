(function(){

    var routineAppServices = angular.module('routineApp.services', []);

    routineAppServices.factory("RoutineService", ['$http', 'AuthUser', function($http, AuthUser){

        var routine = {};

        routine.getRoutines = function() {
            return $http.get('routines/api/get/routines', {
                params: {
                    user: AuthUser['id']
                }
            });
        };

        routine.getRoutine = function(routineName) {
            return $http.get('routines/api/get/routine', {
                params: {
                    user: AuthUser['id'],
                    routine: routineName
                }
            });
        };

        routine.postRoutine = function(routineJson) {
            return $http.post('routines/api/post/routine', routineJson);
        };

        routine.postRoutineDelete = function(routineJson) {
            return $http.post('routines/api/post/routine-delete', routineJson)
        };

        routine.postExercises = function(exercisesJson) {
            return $http.post('routines/api/post/exercises', exercisesJson);
        };

        routine.postExercise = function(exerciseJson) {
            return $http.post('routines/api/post/exercise', exerciseJson)
        };

        routine.postExerciseDelete = function(exerciseJson) {
            return $http.post('routines/api/post/exercise-delete', exerciseJson)
        };

        return routine;

    }]);

})();
