(function(){

    var routineAppControllers = angular.module('routineApp.userControllers', []);

    routineAppControllers.controller('UserLoginController', ['UserService', 'jwtHelper', '$state', '$rootScope', '$location', function(UserService, jwtHelper, $state, $rootScope, $location) {

        var vm = this;

        vm.submit = function() {

            var userJson = angular.toJson(vm.user);

            UserService.authenticateUser(userJson)
            .success(function(response){

                var tokenPayload = jwtHelper.decodeToken(response['token']);
                localStorage.setItem('token', response['token']);
                localStorage.setItem('user', tokenPayload['user_id']);
                localStorage.setItem('userName', tokenPayload['username']);

                if ($rootScope.returnTo && $rootScope.returnTo.StateParams && $rootScope.returnTo.State != '/login') {
                    $location.path($rootScope.returnTo.State + $rootScope.returnTo.StateParams);
                } else if ($rootScope.returnTo && $rootScope.returnTo.State != '/login') {
                    $location.path($rootScope.returnTo.State);
                } else {
                    $state.go('routines');
                }
            })
            .error(function(response, headers) {
                vm.error = errorHandler(response, headers);
            });
        };

    }]);

    routineAppControllers.controller('UserCreateController', ['UserService', '$state', function(UserService, $state) {

        var vm = this;

        vm.submit = function() {

            var userJson = angular.toJson(vm.user);

            UserService.createUser(userJson)
            .success(function(response) {
                $state.go('user_authenticate');
            })
            .error(function(response, headers) {
                vm.error = errorHandler(response, headers);
            });
        };

    }]);


})();
