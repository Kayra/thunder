(function(){

    var routineAppControllers = angular.module('routineApp.controllers', [        'routineApp.filters',
                'ngCookies',
                ]);


    routineAppControllers.controller('RoutineListController', function() {

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

        this.routines = routines;
    });


    routineAppControllers.controller('RoutineAddRoutineController', ['$cookies', function($cookies) {

        this.submit = function($event) {

            $event.preventDefault();

            var routineObj = {};

            routineObj.name = this.routine.name;
            routineObj.user = 'nothingatm';

            $cookies.put('routine', routineObj.name);

            var routineJson = angular.toJson(routineObj);
            console.log(routineJson);


        };

    }]);


    routineAppControllers.controller('RoutineAddExercisesController', ['$cookies', function($filter, $cookies) {

        this.exercises = [{position: '1'}, {position: '2'}, {position: '3'}, {position: '4'}, {position: '5'}];

        this.addNewExercise = function() {
            var newExercisePosition = this.exercises.length + 1;
            this.exercises.push({'position': newExercisePosition});
        };

        this.removeExercise = function() {
            var lastExercise = this.exercises.length - 1;
            this.exercises.splice(lastExercise);
        };

        this.submit = function($event) {

            $event.preventDefault();

            angular.forEach(this.exercises, function(exercise, index){

                var exerciseObj = {};

                exerciseObj.position = exercise.position;
                exerciseObj.name = exercise.name;
                exerciseObj.completion_time = exercise.minutes + ":" + exercise.seconds;
                //Need an if else
                // exerciseObj.routine = $cookies.get('routine');

                var exerciseJson = angular.toJson(exerciseObj);
                console.log(exerciseJson);

            });
        };

    }]);


    routineAppControllers.controller('RoutineUseController', function(){

        var routine = {name:'insanity', total_time: '37:15'};

        var exercises = [
        {
            name:'Warm up',
            completion_time:'1:30',
            position:'1',
            routine:'insanity'
        },
        {
            name:'Jumping jacks',
            completion_time:'2:15',
            position:'2',
            routine:'insanity'
        },
        {
            name:'Standing jacks',
            completion_time:'3:45',
            position:'3',
            routine:'insanity'
        },
        {
            name:'Sitting jacks',
            completion_time:'2:15',
            position:'4',
            routine:'insanity'
        }
        ];


        this.routine = routine;
        this.exercises = exercises;
        this.total_exercises = exercises.length;
        var total_time;

        angular.forEach(exercises, function(exercise, index){



        });

    });


})();
