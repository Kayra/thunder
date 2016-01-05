(function(){

    var routineAppServices = angular.module('routineApp.services', []);

    var domain = 'http://127.0.0.1:8000/';

    routineAppServices.factory("RoutineService", ['$http', function($http, AuthUser){

        var routine = {};

        routine.getRoutines = function() {
            return $http.get(domain + 'routines/get-routines');
        };

        routine.getRoutine = function(routineName) {
            return $http.get(domain + 'api/get/routine', {
                params: {
                    routine: routineName
                }
            });
        };

        routine.createRoutine = function(routineJson) {
            return $http.post(domain + 'routines/create-routine', routineJson);
        };

        routine.postRoutineDelete = function(routineJson) {
            return $http.post(domain + 'api/post/routine-delete', routineJson)
        };

        routine.createExercises = function(exercisesJson) {
            return $http.post(domain + 'routines/create-exercises', exercisesJson);
        };

        routine.postExercise = function(exerciseJson) {
            return $http.post(domain + 'api/post/exercise', exerciseJson)
        };

        routine.postExerciseDelete = function(exerciseJson) {
            return $http.post(domain + 'api/post/exercise-delete', exerciseJson)
        };

        return routine;

    }]);

    routineAppServices.factory("SharedProperties", function() {

        var property = {};

        var value;

        property.getProperty = function() {
            return value;
        };

        property.setProperty = function(newValue) {
            value = newValue;
        };

        return property;

    });

})();
