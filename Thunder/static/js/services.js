(function(){

    var routineAppServices = angular.module('routineApp.services', []);

    routineAppServices.factory("RoutineService", ['$http', 'AuthUser', function($http, AuthUser){

        var routine = {};

        routine.getRoutines = function() {
            return $http.get('api/get/routines', {
                params: {
                    user: AuthUser['id']
                }
            });
        };

        routine.getRoutine = function(routineName) {
            return $http.get('api/get/routine', {
                params: {
                    user: AuthUser['id'],
                    routine: routineName
                }
            });
        };

        routine.postRoutine = function(routineJson) {
            return $http.post('api/post/routine', routineJson);
        };

        routine.postRoutineDelete = function(routineJson) {
            return $http.post('api/post/routine-delete', routineJson)
        };

        routine.postExercises = function(exercisesJson) {
            return $http.post('api/post/exercises', exercisesJson);
        };

        routine.postExercise = function(exerciseJson) {
            return $http.post('api/post/exercise', exerciseJson)
        };

        routine.postExerciseDelete = function(exerciseJson) {
            return $http.post('api/post/exercise-delete', exerciseJson)
        };

        return routine;

    }]);

})();
