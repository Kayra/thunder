(function(){

    var routineAppServices = angular.module('routineApp.services', []);

    var domain = 'http://127.0.0.1:8000/';

    routineAppServices.factory("RoutineService", ['$http', function($http, AuthUser){

        var routine = {};

        routine.getRoutines = function() {
            return $http.get(domain + 'routines/get-routines');
        };

        routine.getRoutine = function(routineId) {
            return $http.get(domain + 'routines/get-routine', {
                params: {
                    id: routineId
                }
            });
        };

        routine.getFullRoutine = function(routineId) {
            return $http.get(domain + 'routines/get-full-routine', {
                params: {
                    id: routineId
                }
            });
        };

        routine.createRoutine = function(routineJson) {
            return $http.post(domain + 'routines/create-routine', routineJson);
        };

        routine.editRoutine = function(routineJson) {
            return $http.put(domain + 'routines/edit-routine', routineJson)
        };

        routine.deleteRoutine = function(routineId) {
            return $http.post(domain + 'routines/delete-routine', {
                params: {
                    id: routineId
                }
            });
        };

        routine.createExercises = function(exercisesJson) {
            return $http.post(domain + 'routines/create-exercises', exercisesJson);
        };

        routine.createExercise = function(exerciseJson) {
            return $http.post(domain + 'routines/create-exercise', exerciseJson)
        };

        routine.editExercise = function(exerciseJson) {
            return $http.put(domain + 'routines/edit-exercise', exerciseJson)
        };

        routine.deleteExercise = function(exerciseId) {
            return $http.delete(domain + 'routines/delete-exercise', {
                params: {
                    id: exerciseId
                }
            });
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
