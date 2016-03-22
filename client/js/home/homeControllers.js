(function() {

    var homeControllers = angular.module('routineApp.homeControllers', []);

    homeControllers.controller('HomeController', function() {

        var vm = this;

    });

    homeControllers.controller('NavController', ['UserService', '$state', function(UserService, $state){

        var vm = this;

        vm.logout = function() {

            localStorage.removeItem('token');
            localStorage.removeItem('user');
            $state.go('user_authenticate');

        };

        vm.userIsLoggedIn = function() {
            return UserService.isLoggedIn();
        };

        vm.isHomePage = function() {
            console.log($state.current.name);
            return $state.current.name == 'home';
        };

    }]);

})();
