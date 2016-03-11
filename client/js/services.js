(function(){

    var googleMapsAppServices = angular.module('routineApp.services', []);

    var domain = 'http://127.0.0.1:8000/';

    googleMapsAppServices.factory("MapService", ['$http', function($http, AuthUser){

        var map = {};

        map.getAddresses = function() {
            return $http.get(domain + 'maps/');
        };

        return routine;

    }]);


})();
