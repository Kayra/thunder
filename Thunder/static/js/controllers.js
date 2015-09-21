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


    routineAppControllers.controller('RoutineEditController', function() {

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

        // Format the completion time to fit in the form
        angular.forEach(exercises, function(exercise, index){

            var completion_time = exercise.completion_time.split(":");

            if (parseInt(completion_time[0]) < 10) {
                exercise.minutes = '0' + completion_time[0];
            } else {
                exercise.minutes = completion_time[0];
            }

            if (parseInt(completion_time[1]) < 10) {
                exercise.seconds = completion_time[1] + 0;
            } else {
                exercise.seconds = completion_time[1];
            }

        });

        this.routine = routine;
        this.exercises = exercises;

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
                exerciseObj.routine = routine.name;

                var exerciseJson = angular.toJson(exerciseObj);
                console.log(exerciseJson);

            });
        };

    });


    routineAppControllers.controller('RoutineUseController', ['$interval', function($interval){

        var ctrl = this;

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
            completion_time:'0:15',
            position:'4',
            routine:'insanity'
        }
        ];


        ctrl.routine = routine;
        ctrl.exercises = exercises;
        ctrl.total_exercises = exercises.length;

        ctrl.current_position = 1;

        ctrl.current_exercise = setCurrentExercise(ctrl.exercises, ctrl.current_position);

        var count_down;
        var reset = false;
        ctrl.timerStartStop = function(){

            // If the timer has run through completely, reset it
            if (reset) {
                exerciseReset();
            }

            // If already running, stop the timer
            if (angular.isDefined(count_down)) {
                $interval.cancel(count_down);
                count_down = undefined;
            } else {

                count_down = $interval(function(){

                    if (exerciseHasEnded(ctrl.current_exercise.count_down_time)) {

                        ctrl.current_position == ctrl.current_position++;

                        // If the last exercise has finished, stop the timer
                        // Otherwise move on to the next exercise
                        if (ctrl.current_position > ctrl.total_exercises) {
                            $interval.cancel(count_down);
                            count_down = undefined;
                            ctrl.current_position == ctrl.current_position--;
                            reset = true;
                        } else {
                            ctrl.current_exercise = setCurrentExercise(ctrl.exercises, ctrl.current_position);
                        }

                    } else {
                        countDown(ctrl.current_exercise.count_down_time);
                    }

                }, 1000);
            }

        };

        ctrl.timerReset = function(){

            if (angular.isDefined(count_down)) {
                $interval.cancel(count_down);
                count_down = undefined;
            }

            exerciseReset();

        };

        function exerciseReset(){

            ctrl.current_position = 1;
            ctrl.current_exercise = setCurrentExercise(ctrl.exercises, ctrl.current_position);

            reset = false;

        }

        function exerciseHasEnded(time){

            return time.seconds == 0 && time.minutes == 00;
        }

        function setCurrentExercise(exercises, position){

            var indexPosition = position - 1;
            var current_exercise = exercises[indexPosition];

            current_exercise.count_down_time = completionTimeToObj(current_exercise.completion_time);

            return current_exercise;
        }

        function countDown(time){

            if (time.seconds > 0 && time.minutes > -1){
                time.seconds == time.seconds--;
                return time;
            } else if (time.minutes > 0) {
                time.minutes == time.minutes--;
                time.seconds = 60;
                return time;
            }

        };

        function completionTimeToObj(completion_time){

            var completionSplit = completion_time.split(":");
            var minutes = parseInt(completionSplit[0]);
            var seconds = parseInt(completionSplit[1]);

            return {
                minutes: minutes,
                seconds: seconds
            }

        };


    }]);


})();
