(function() {

    var homeControllers = angular.module('routineApp.homeControllers', []);

    homeControllers.controller('HomeController', function() {

        var vm = this;

    });

    homeControllers.controller('NavController', ['UserService', '$state', function(UserService, $state){

        var vm = this;

        vm.userName = localStorage.getItem('userName');

        vm.logout = function() {
            localStorage.removeItem('token');
            localStorage.removeItem('user');
            localStorage.removeItem('userName');
            $state.go('user_authenticate');
        };

        vm.userIsLoggedIn = function() {
            return UserService.isLoggedIn();
        };

        vm.isHomePage = function() {
            return $state.current.name == 'home';
        };

    }]);

})();
