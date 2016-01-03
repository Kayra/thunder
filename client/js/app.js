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
                templateUrl: '/partials/list.html',
                controller: 'RoutineListController as vm',
            })
            .state('create_routine', {
                url: '/create_routine',
                templateUrl: '/partials/add_routine.html',
                controller: 'RoutineAddRoutineController as vm',
            })
            .state('create_exercises', {
                url: '/create_exercises',
                templateUrl: '/partials/add_exercises.html',
                controller: 'RoutineAddExercisesController as vm',
            })
            .state('edit_routine', {
                url: '/edit/:routineName',
                templateUrl: '/partials/edit.html',
                controller: 'RoutineEditController as vm',
            })
            .state('use_routine', {
                url: '/use/:routineName',
                templateUrl: '/partials/use.html',
                controller: 'RoutineUseController as vm',
            });

        $urlRouterProvider.otherwise('/');

    });

})();

