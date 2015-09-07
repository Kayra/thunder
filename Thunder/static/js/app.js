(function(){

    var app = angular.module('routineApp', [
        'ui.router',
        'ngResource',
        'routineApp.services',
        'routineApp.controllers',
    ])

    .config(function($interpolateProvider, $httpProvider, $resourceProvider, $stateProvider, $locationProvider, $urlRouterProvider){

    // Force angular to use square brackets for template tag
    $interpolateProvider.startSymbol('[[').endSymbol(']]');

    // CSRF Support
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

    // This only works in angular 3!
    // It makes dealing with Django slashes at the end of everything easier.
    $resourceProvider.defaults.stripTrailingSlashes = false;

    // Routing
    $locationProvider.html5Mode({
      enabled: true,
      requireBase: false
    });
    $urlRouterProvider.otherwise('/');

    $stateProvider
        .state('list', {
            url: '/',
            templateUrl: 'static/partials/routine/routine_list.html',
            controller: 'RoutineListController',
        });

    });

})();

