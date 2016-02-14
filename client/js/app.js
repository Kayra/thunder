(function(){

    var app = angular.module('routineApp', [
        'ui.router',
        'ngResource',
        'ngMessages',
        'ngCookies',
        'routineApp.services',
        'routineApp.controllers',
        'routineApp.directives'
    ])

    .config(function($interpolateProvider, $httpProvider, $resourceProvider, $stateProvider, $locationProvider, $urlRouterProvider){

        // CSRF Support
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

        // Routing
        $locationProvider.html5Mode({
          enabled: true,
          requireBase: false
        });

        $stateProvider
            .state('list_routines', {
                url: '/',
                templateUrl: '/partials/list_routines.html',
                controller: 'RoutineListController as list',
            })
            .state('create_routine', {
                url: '/create_routine',
                templateUrl: '/partials/create_routine.html',
                controller: 'RoutineCreateRoutineController as create',
            })
            .state('create_exercises', {
                url: '/create_exercises',
                templateUrl: '/partials/create_exercises.html',
                controller: 'RoutineCreateExercisesController as create',
            })
            .state('edit_routine', {
                url: '/edit/:routineName',
                templateUrl: '/partials/edit_routine.html',
                controller: 'RoutineEditController as edit',
            })
            .state('use_routine', {
                url: '/use/:routineName',
                templateUrl: '/partials/use_routine.html',
                controller: 'RoutineUseController as use',
            })
            .state('login_user', {
                url: '/login',
                templateUrl: '/partials/login_user.html',
                controller: 'UserLoginController as login',
            });;

        $urlRouterProvider.otherwise('/');

    });

})();

