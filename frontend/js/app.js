(function(){

    var app = angular.module('routineApp', [
        'ui.router',
        'ngResource',
        'routineApp.services',
        'routineApp.controllers',
        'ngCookies'
    ])

    .config(function($interpolateProvider, $httpProvider, $resourceProvider, $stateProvider, $locationProvider, $urlRouterProvider){

    // Force angular to use square brackets for template tag
    $interpolateProvider.startSymbol('[[').endSymbol(']]');

    // CSRF Support
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

    // This only works in angular 3!
    // It makes dealing with Django slashes at the end of everything easier.
    // $resourceProvider.defaults.stripTrailingSlashes = false;

    // Routing
    $locationProvider.html5Mode({
      enabled: true,
      requireBase: false
    });

    $stateProvider
        .state('list', {
            url: '/',
            templateUrl: 'partials/list.html',
            controller: 'RoutineListController',
        })
        .state('add_routine', {
            url: '/add_routine',
            templateUrl: 'partials/add_routine.html',
            controller: 'RoutineAddRoutineController',
        })
        .state('add_exercises', {
            url: '/add_exercises',
            templateUrl: 'partials/add_exercises.html',
            controller: 'RoutineAddExercisesController',
        })
        .state('edit', {
            url: '/edit',
            templateUrl: 'partials/edit.html',
            controller: 'RoutineEditController',
        })
        .state('use', {
            url: '/use',
            templateUrl: 'partials/use.html',
            controller: 'RoutineUseController',
        });

    $urlRouterProvider.otherwise('/');

    });

})();

