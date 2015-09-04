(function(){

    var routineAppControllers = angular.module('routineApp.controllers', []);

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

    routineAppControllers.controller('RoutineListController', function(){
        this.routines = routines;
    })

})();
