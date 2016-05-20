(function(){

    var app = angular.module('routineApp', [
        'ui.router',
        'ngResource',
        'ngMessages',
        'angular-jwt',
        'routineApp.homeControllers',
        'routineApp.routineControllers',
        'routineApp.routineServices',
        'routineApp.userControllers',
        'routineApp.userServices',
        'routineApp.directives',
        'routineApp.filters'
    ])

    .config(function($interpolateProvider, $httpProvider, $resourceProvider, $stateProvider, $locationProvider, $urlRouterProvider, jwtInterceptorProvider){

        jwtInterceptorProvider.authPrefix = '';

        jwtInterceptorProvider.tokenGetter = function(jwtHelper, UserService) {

            var token = localStorage.getItem('token');

            if (token && !jwtHelper.isTokenExpired(token)) {

                var tokenJson = (angular.toJson({'token': token}));

                UserService.refreshToken(tokenJson)
                .success(function(response){
                    localStorage.setItem('token', response['token']);
                })
                .error(function(){

                });
            }

            return "JWT " + localStorage.getItem('token');
        }

        $httpProvider.interceptors.push('jwtInterceptor');

        // Routing
        $locationProvider.html5Mode({
          enabled: true,
          requireBase: false
        });

        $stateProvider
            .state('home', {
                url: '/home',
                templateUrl: '/partials/home/home.html',
                controller: 'HomeController as home'
            })
            .state('routines', {
                url: '/',
                templateUrl: '/partials/routines/routines.html',
                controller: 'RoutineListController as list'
            })
            .state('routine_create_routine', {
                url: '/create-routine',
                templateUrl: '/partials/routines/routine_create_routine.html',
                controller: 'RoutineCreateRoutineController as create'
            })
            .state('routine_create_exercises', {
                url: '/create-exercises',
                templateUrl: '/partials/routines/routine_create_exercises.html',
                controller: 'RoutineCreateExercisesController as create'
            })
            .state('routine_edit', {
                url: '/edit/:id',
                templateUrl: '/partials/routines/routine_edit.html',
                controller: 'RoutineEditController as edit'
            })
            .state('routine_use', {
                url: '/use/:id',
                templateUrl: '/partials/routines/routine_use.html',
                controller: 'RoutineUseController as use'
            })
            .state('user_authenticate', {
                url: '/login',
                templateUrl: '/partials/users/user_authenticate.html',
                controller: 'UserLoginController as login'
            })
            .state('user_create', {
                url: '/signup',
                templateUrl: '/partials/users/user_create.html',
                controller: 'UserCreateController as create'
            });

        $urlRouterProvider.otherwise('/');

    })

    .run(function($rootScope, $location, UserService, $state) {

        $rootScope.$on('$stateChangeStart', function (event, toState, toParams, fromState) {

            if (!UserService.isLoggedIn() && toState.name!="user_authenticate" && toState.name!="user_create" ) {

                $rootScope.returnTo = new Object();

                if (toState.url.indexOf(":") != -1) {
                    $rootScope.returnTo.State = toState.url.split(":")[0];
                } else {
                    $rootScope.returnTo.State = toState.url;
                }
                $rootScope.returnTo.StateParams = toParams.Id;

                $state.go('user_authenticate');
                event.preventDefault();
            }

        });
    });


})();

