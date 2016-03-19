(function(){

    var userServices = angular.module('routineApp.userServices', []);

    var domain = 'http://127.0.0.1:8000/';

    userServices.factory("UserService", ['$http', 'jwtHelper', function($http, jwtHelper) {

        var user = {};

        user.createUser = function(userJson) {
            return $http.post(domain + 'users/users/', userJson, {
                skipAuthorization: true
            });
        };

        user.authenticateUser = function(userJson) {
            return $http.post(domain + 'users/user-auth/', userJson, {
                skipAuthorization: true
            });
        };

        user.refreshToken = function(token) {
            return $http.post(domain + 'users/token-refresh/', token, {
                skipAuthorization: true
            });
        };

        user.isLoggedIn = function() {
            var token = localStorage.getItem('token');

            if (token && !jwtHelper.isTokenExpired(token)) {
                return true;
            } else {
                return false;
            }
        }

        return user;

    }]);

    userServices.factory("SharedProperties", function() {

        var property = {};

        var value;

        property.getProperty = function() {
            return value;
        };

        property.setProperty = function(newValue) {
            value = newValue;
        };

        return property;

    });

})();
