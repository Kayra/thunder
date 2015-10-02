(function(){

    var routineAppControllers = angular.module('routineApp.controllers', [        'routineApp.filters',
                'ngCookies',
                ]);


    routineAppControllers.controller('RoutineListController', ['RoutineService', function(RoutineService) {

        var ctrl = this;

        ctrl.getRoutines = function() {
            RoutineService.getRoutines().then(function(response){
                ctrl.routines = response.data;
            })
        }

        ctrl.getRoutines();

    }]);


    routineAppControllers.controller('RoutineAddRoutineController', ['$cookies', 'AuthUser', 'RoutineService', function($cookies, AuthUser, RoutineService) {

        this.postRoutine = function(routineJson){
            RoutineService.postRoutine(routineJson).then(function(response){
                console.log(response);
            });
        };

        this.submit = function($event) {

            $event.preventDefault();

            var routineObj = {};

            routineObj.name = this.routine.name;
            routineObj.user = AuthUser['id'];

            $cookies.put('routine', routineObj.name);

            var routineJson = angular.toJson(routineObj);

            console.log(routineJson);
            this.postRoutine(routineJson);


        };

    }]);


    routineAppControllers.controller('RoutineAddExercisesController', ['$cookies', 'RoutineService', function($cookies, RoutineService) {

        var ctrl = this;

        ctrl.exercises = [{position: '1'}, {position: '2'}, {position: '3'}, {position: '4'}, {position: '5'}];

        ctrl.addNewExercise = function() {
            var newExercisePosition = this.exercises.length + 1;
            this.exercises.push({'position': newExercisePosition});
        };

        ctrl.removeExercise = function() {
            var lastExercise = this.exercises.length - 1;
            this.exercises.splice(lastExercise);
        };

        ctrl.postExercises = function(exercisesJson){
            RoutineService.postExercises(exercisesJson).then(function(response){
                console.log(response);
            });
        };

        ctrl.submit = function($event) {

            $event.preventDefault();

            var exerciseObjs = [];

            angular.forEach(this.exercises, function(exercise, index){
                if (exercise.name) {

                    var exerciseObj = {};
                    exerciseObj.position = exercise.position;
                    exerciseObj.name = exercise.name;
                    exerciseObj.completion_time = exercise.minutes + ":" + exercise.seconds;
                    exerciseObj.routine = 'hit';
                    //Need an if else
                    // exerciseObj.routine = $cookies.get('routine');

                    exerciseObjs.push(exerciseObj);

                }
            });

            var exercisesJson = angular.toJson(exerciseObjs);
            ctrl.postExercises(exercisesJson);

        };

    }]);


    routineAppControllers.controller('RoutineEditController', ['RoutineService', function(RoutineService) {

        var ctrl = this;

        ctrl.routine = {name:'insanity', total_time: '37:15'};

        ctrl.exercises = [];

        this.getRoutine = function() {
            RoutineService.getRoutine(ctrl.routine.name).then(function(response){
                ctrl.exercises = response.data;
                ctrl.formatCompletionTimes(ctrl.exercises);

        console.log(ctrl.exercises);
            });
        };

        this.getRoutine()

        // Format the completion time to fit in the form
        ctrl.formatCompletionTimes = function(exercises){
            angular.forEach(exercises, function(exercise, index){

                var completion_time = exercise.completion_time.split(":");

                exercise.minutes = completion_time[1];
                exercise.seconds = completion_time[2];

            });
        }


        ctrl.addNewExercise = function() {
            var newExercisePosition = ctrl.exercises.length + 1;
            ctrl.exercises.push({'position': newExercisePosition});
        };

        ctrl.removeExercise = function() {
            var lastExercise = ctrl.exercises.length - 1;
            ctrl.exercises.splice(lastExercise);
        };

        ctrl.submit = function($event) {

            $event.preventDefault();

            angular.forEach(ctrl.exercises, function(exercise, index){

                var exerciseObj = {};

                exerciseObj.position = exercise.position;
                exerciseObj.name = exercise.name;
                exerciseObj.completion_time = exercise.minutes + ":" + exercise.seconds;
                exerciseObj.routine = routine.name;

                var exerciseJson = angular.toJson(exerciseObj);
                console.log(exerciseJson);

            });
        };

    }]);


    routineAppControllers.controller('RoutineUseController', ['$interval', 'RoutineService', function($interval, RoutineService){

        var ctrl = this;

        var routine = {name:'insanity', total_time: '37:15'};

        ctrl.getRoutine = function() {
            RoutineService.getRoutine(routine.name).then(function(response){

                ctrl.routine = response.data[0].routine;
                ctrl.exercises = response.data;
                ctrl.total_exercises = ctrl.exercises.length;
                ctrl.current_exercise = setCurrentExercise(ctrl.exercises, ctrl.current_position);

            })
        }

        ctrl.getRoutine();

        ctrl.current_position = 1;


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
                // return time;
            } else if (time.minutes > 0) {
                time.minutes == time.minutes--;
                time.seconds = 60;
                // return time;
            }

        };

        function completionTimeToObj(completion_time){

            // Not starting at index of 0 because django stores times as 00:00:00
            var completionSplit = completion_time.split(":");
            var minutes = parseInt(completionSplit[1]);
            var seconds = parseInt(completionSplit[2]);

            return {
                minutes: minutes,
                seconds: seconds
            }

        };


    }]);


})();
