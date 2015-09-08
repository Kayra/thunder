(function(){

    var routineAppControllers = angular.module('routineApp.controllers', []);

    // Test data
    var routines = [
    {
        name: 'Insanity',
        total_time: '00:40:00'
    },
    {
        name: 'Rest day',
        total_time: '00:20:30'
    },
    {
        name: 'Dance choreography',
        total_time: '00:10:25'
    }
    ];

    routineAppControllers.controller('RoutineListController', function() {
        this.routines = routines;
    });

    routineAppControllers.controller('RoutineAddController', function($filter) {

        this.exercises = [{position: '1'}, {position: '2'}, {position: '3'}, {position: '4'}, {position: '5'}];

        this.routine = {};

        this.addNewExercise = function() {
            var newExercisePosition = this.exercises.length + 1;
            this.exercises.push({'position': newExercisePosition});
        };

        this.removeExercise = function() {
            var lastExercise = this.exercises.length - 1;
            this.exercises.splice(lastExercise);
        };

        this.saveExercises = function() {

        };

        this.submit = function($event) {
            $event.preventDefault();
            // console.log(this.routine.name);
            var routine = this.routine.name;
            console.log(this.exercises);
            angular.forEach(this.exercises, function(exercise, index){

                console.log(exercise.position);
                console.log(exercise.name);
                var completion_time = $filter('date')(exercise.completion_time, "HH:mm")
                console.log(completion_time);
                console.log(routine);

            });
        };

    });

})();
