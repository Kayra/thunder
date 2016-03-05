(function(){

    var routineAppControllers = angular.module('routineApp.controllers', ['routineApp.filters',
                'ngCookies',
                ]);


    routineAppControllers.controller('RoutineListController', ['RoutineService', 'SharedProperties', function(RoutineService, SharedProperties) {

        var vm = this;

        vm.setId = function(id) {
            SharedProperties.setProperty(id);
        };

        vm.getRoutines = function() {
            RoutineService.getRoutines()
            .success(function(response){
                vm.routines = response;
            })
            .error(function() {
                // Need error handling
            });
        }

        vm.getRoutines();

    }]);


    routineAppControllers.controller('RoutineCreateRoutineController', ['RoutineService', 'SharedProperties', '$state', function(RoutineService, SharedProperties, $state) {

        var vm = this;

        vm.createRoutine = function(routineJson) {
            RoutineService.createRoutine(routineJson)
            .success(function(response) {
                SharedProperties.setProperty(response.id);
            })
            .error(function(){
                // Need error handling
            });
        };

        vm.submit = function() {

            var routineObj = {};

            routineObj.name = vm.routine.name;

            var routineJson = angular.toJson(routineObj);

            vm.createRoutine(routineJson);

            $state.go('create_exercises');

        };

    }]);


    routineAppControllers.controller('RoutineCreateExercisesController', ['RoutineService', 'SharedProperties', '$state', function(RoutineService, SharedProperties, $state) {

        var vm = this;

        vm.exercises = [{position: '1'}, {position: '2'}, {position: '3'}, {position: '4'}, {position: '5'}];

        vm.addNewExercise = function() {
            var newExercisePosition = vm.exercises.length + 1;
            vm.exercises.push({'position': newExercisePosition});
        };

        vm.removeExercise = function() {
            var lastExercise = vm.exercises.length - 1;
            vm.exercises.splice(lastExercise);
        };

        vm.createExercises = function(exercisesJson){
            RoutineService.createExercises(exercisesJson)
            .success(function(response) {
                $state.go('list_routines');
            })
            .error(function() {
                // Need error handling
            });
        };

        vm.submit = function() {

            var routineId = SharedProperties.getProperty();

            var exerciseObjs = [];

            angular.forEach(vm.exercises, function(exercise, index){
                if (exercise.name) {

                    var exerciseObj = {};
                    exerciseObj.position = exercise.position;
                    exerciseObj.name = exercise.name;
                    exerciseObj.completion_time = "00:" + exercise.minutes + ":" + exercise.seconds;
                    exerciseObj.routine = routineId;

                    exerciseObjs.push(exerciseObj);

                }
            });

            var exercisesJson = angular.toJson(exerciseObjs);
            vm.createExercises(exercisesJson);

        };

    }]);


    routineAppControllers.controller('RoutineEditController', ['RoutineService', 'SharedProperties', '$location', '$state', function(RoutineService, SharedProperties, $location, $state) {

        var vm = this;

        var routineId = SharedProperties.getProperty();

        vm.getRoutine = function(routineId) {
            RoutineService.getRoutine(routineId)
            .success(function(response){
                vm.routine = response;
            })
            .error(function(){

            });
        };

        vm.getExercises = function(routineId) {
            RoutineService.getExercises(routineId)
            .success(function(response){
                vm.exercises = response;
                vm.formatCompletionTimes(vm.exercises);
            })
            .error(function(){

            });
        }

        // Format the completion time to fit in the form
        vm.formatCompletionTimes = function(exercises){
            exercises.forEach(function(exercise){

                var completion_time = exercise.completion_time.split(":");

                exercise.minutes = completion_time[1];
                exercise.seconds = completion_time[2];

            });
        };

        vm.addNewExercise = function() {
            var newExercisePosition = vm.exercises.length + 1;
            vm.exercises.push({'position': newExercisePosition, 'minutes': '00', 'seconds': '00'});
        };

        vm.createExercise = function(exerciseJson) {
            RoutineService.createExercise(exerciseJson)
            .success(function(response){

            })
            .error(function(){

            });
        };

        vm.deleteExerciseClick = function() {
            var lastExercise = vm.exercises.length - 1;

            // delete exercise from the database
            vm.deleteExercise(vm.exercises[lastExercise].id);

            vm.exercises.splice(lastExercise);
        };

        vm.editExercise = function(exerciseJson, exerciseId) {
            RoutineService.editExercise(exerciseJson, exerciseId)
            .success(function(response){

            })
            .error(function(){

            });
        };

        vm.editRoutine = function(routineJson, routineId) {
            RoutineService.editRoutine(routineJson, routineId)
            .success(function(response){

            })
            .error(function(){

            });
        };

        vm.deleteExercise = function(exerciseId) {
            RoutineService.deleteExercise(exerciseId)
            .success(function(response){

            })
            .error(function(){

            });
        };

        vm.deleteRoutine = function(routineId) {
            RoutineService.deleteRoutine(routineId)
            .success(function(response){
                $state.go('list_routines');
            })
            .error(function(){

            });
        }

        vm.findNewExercises = function(exercises) {

            newExercises = [];

            exercises.forEach(function(exercise){
                if (typeof exercise.id == 'undefined') {
                    newExercises.push(exercise);
                }
            });

            return newExercises;
        };

        vm.submit = function() {

            var routineJson = angular.toJson(vm.routine);
            vm.editRoutine(routineJson, vm.routine.id);

            var exerciseObjs = [];

            angular.forEach(vm.exercises, function(exercise, index){

                if (typeof exercise.id !== 'undefined') {

                    var exerciseObj = {};

                    exerciseObj.id = exercise.id;
                    exerciseObj.position = exercise.position;
                    exerciseObj.name = exercise.name;
                    exerciseObj.completion_time = "00:" + exercise.minutes + ":" + exercise.seconds;
                    exerciseObj.routine = vm.routine.id;

                    var exerciseJson = angular.toJson(exerciseObj);

                    vm.editExercise(exerciseJson, exercise.id);

                } else if (typeof exercise.id == 'undefined') {

                    var exerciseObj = {};

                    exerciseObj.position = exercise.position;
                    exerciseObj.name = exercise.name;
                    exerciseObj.completion_time = "00:" + exercise.minutes + ":" + exercise.seconds;
                    exerciseObj.routine = vm.routine.id;

                    var exerciseJson = angular.toJson(exerciseObj);

                    vm.createExercise(exerciseJson);

                };

            });

        };

        vm.getRoutine(routineId);
        vm.getExercises(routineId);

    }]);


    routineAppControllers.controller('RoutineUseController', ['RoutineService', 'SharedProperties', '$interval', '$location', function( RoutineService, SharedProperties, $interval, $location){

        var vm = this;

        var routineId = SharedProperties.getProperty();

        vm.getRoutine = function(routineId) {
            RoutineService.getRoutine(routineId)
            .success(function(response){
                vm.routine = response;
            })
            .error(function(){

            });
        };

        vm.getExercises = function(routineId) {
            RoutineService.getExercises(routineId)
            .success(function(response){
                vm.exercises = response;
                vm.total_exercises = vm.exercises.length;
                vm.current_position = 1;
                vm.current_exercise = setCurrentExercise(vm.exercises, vm.current_position);
            })
            .error(function(){

            });
        };

        vm.getRoutine(routineId);
        vm.getExercises(routineId);

        var count_down;
        var reset = false;
        vm.timerStartStop = function(){

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

                    if (exerciseHasEnded(vm.current_exercise.count_down_time)) {

                        vm.current_position == vm.current_position++;

                        // If the last exercise has finished, stop the timer
                        // Otherwise move on to the next exercise
                        if (vm.current_position > vm.total_exercises) {
                            $interval.cancel(count_down);
                            count_down = undefined;
                            vm.current_position == vm.current_position--;
                            reset = true;
                        } else {
                            vm.current_exercise = setCurrentExercise(vm.exercises, vm.current_position);
                        }

                    } else {
                        countDown(vm.current_exercise.count_down_time);
                    }

                }, 1000);
            }

        };

        vm.timerReset = function(){

            if (angular.isDefined(count_down)) {
                $interval.cancel(count_down);
                count_down = undefined;
            }

            exerciseReset();

        };

        vm.previousExercise = function() {
            console.log(vm.current_position);
            if (vm.current_position - 1 >= 1) {
                vm.current_position = vm.current_position - 1;
                vm.current_exercise = setCurrentExercise(vm.exercises, vm.current_position);

                if (angular.isDefined(count_down)) {
                    $interval.cancel(count_down);
                    count_down = undefined;
                }
            }
        };

        vm.nextExercise = function() {
            if (vm.current_position + 1 <= vm.exercises.length) {
                vm.current_position = vm.current_position + 1;
                vm.current_exercise = setCurrentExercise(vm.exercises, vm.current_position);
                if (angular.isDefined(count_down)) {
                    $interval.cancel(count_down);
                    count_down = undefined;
                }
            }
        };

        function exerciseReset(){

            vm.current_position = 1;
            vm.current_exercise = setCurrentExercise(vm.exercises, vm.current_position);

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


    routineAppControllers.controller('UserLoginController', ['UserService', 'jwtHelper', '$state', '$rootScope', '$location', function(UserService, jwtHelper, $state, $rootScope, $location){

        var vm = this;

        vm.submit = function() {

            var userJson = angular.toJson(vm.user);

            UserService.authenticateUser(userJson)
            .success(function(response){

                var tokenPayload = jwtHelper.decodeToken(response['token']);
                localStorage.setItem('token', response['token']);
                localStorage.setItem('user', tokenPayload['user_id']);

                if ($rootScope.returnTo && $rootScope.returnTo.StateParams && $rootScope.returnTo.State != '/login') {
                    $location.path($rootScope.returnTo.State + $rootScope.returnTo.StateParams);
                } else if ($rootScope.returnTo && $rootScope.returnTo.State != '/login') {
                    $location.path($rootScope.returnTo.State);
                } else {
                    $state.go('list_routines');
                }
            })
            .error(function(response){
                console.log(response);
            });
        };

    }]);

    routineAppControllers.controller('UserCreateController', ['UserService', '$state', function(UserService, $state){

        var vm = this;

        vm.submit = function() {

            var userJson = angular.toJson(vm.user);

            UserService.createUser(userJson)
            .success(function(response){
                $state.go('login_user');
            })
            .error(function(response){

                var errorString = "";

                for(var error in response) {
                    errorString += error + ': ' + response[error] + ' ';
                }

                alert(errorString);

            });
        };

    }]);

    routineAppControllers.controller('NavController', ['UserService', '$state', function(UserService, $state){

        var vm = this;

        vm.logout = function() {

            localStorage.removeItem('token');
            localStorage.removeItem('user');
            $state.go('login_user');

        };

        vm.userIsLoggedIn = function() {
            return UserService.isLoggedIn();
        };

    }]);

})();
