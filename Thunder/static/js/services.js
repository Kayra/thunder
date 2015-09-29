(function(){

    var routineAppServices = angular.module('routineApp.services', []);

    routineAppServices.factory("RoutineListService", ['$http', 'AuthUser', function($http, AuthUser){


        var routineList = {};

        routineList.getRoutines = function() {
            return $http.get('routines/api/get/routines', {
                params: {
                    user: AuthUser['id']
                }
            });
        };

        return routineList;



        // var routines = $http.get('routines/api/get/routines', {params:{user:AuthUser['id']}}).success(function(data){

        //     user = {user:AuthUser['id']};
        //     routines = data;

        // });
        //     console.log(routines.$$state.data);

        // return routines;

    }]);

})();
