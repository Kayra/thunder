(function(){
    var app = angular.module('routineApp', [
        'ui.router',
        'ngResource',
        'routineApp.services',
        'routineApp.controllers',
    ])

    .congfig(function($interpolateProvider, $httpProvider, $resourceProvider, $stateProvider, $urlRouterProvider){

    // Force angular to use square brackets for template tag
    $interpolateProvider.startSymbol('[[').endSymbol(']]');

    // CSRF Support
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

    // This only works in angular 3!
    // It makes dealing with Django slashes at the end of everything easier.
    $resourceProvider.defaults.stripTrailingSlashes = false;

    });




    //Test data
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

    var routines = [routine1, routine2, routine3]

    app.controller('RoutineListController', function(){
        this.routines = routines;
    });

})();

