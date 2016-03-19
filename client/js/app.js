(function(){

    var app = angular.module('routineApp', [
        'ui.router',
        'ngResource',
        'ngMessages',
        'ngCookies',
        'angular-jwt',
        'routineApp.userControllers',
        'routineApp.routineControllers',
        'routineApp.services',
        'routineApp.directives'
    ])

    .config(function($interpolateProvider, $httpProvider, $resourceProvider, $stateProvider, $locationProvider, $urlRouterProvider, jwtInterceptorProvider){

        // CSRF Support
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

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
            .state('routines', {
                url: '/',
                templateUrl: '/partials/list_routines.html',
                controller: 'RoutineListController as list'
            })
            .state('routine_create_routine', {
                url: '/create_routine',
                templateUrl: '/partials/create_routine.html',
                controller: 'RoutineCreateRoutineController as create'
            })
            .state('routine_create_exercises', {
                url: '/create_exercises',
                templateUrl: '/partials/create_exercises.html',
                controller: 'RoutineCreateExercisesController as create'
            })
            .state('routine_edit', {
                url: '/edit/:routineName',
                templateUrl: '/partials/edit_routine.html',
                controller: 'RoutineEditController as edit'
            })
            .state('routine_use', {
                url: '/use/:routineName',
                templateUrl: '/partials/use_routine.html',
                controller: 'RoutineUseController as use'
            })
            .state('user_authenticate', {
                url: '/login',
                templateUrl: '/partials/login_user.html',
                controller: 'UserLoginController as login'
            })
            .state('user_create', {
                url: '/signup',
                templateUrl: '/partials/create_user.html',
                controller: 'UserCreateController as create'
            });

        $urlRouterProvider.otherwise('/');

    })

    .run(function($rootScope, $location, UserService, $state) {

        $rootScope.$on('$stateChangeStart', function (event, toState, toParams, fromState) {

            if (!UserService.isLoggedIn() && toState.name!="login_user" && toState.name!="create_user" ) {

                $rootScope.returnTo = new Object();

                if (toState.url.indexOf(":") != -1) {
                    $rootScope.returnTo.State = toState.url.split(":")[0];
                } else {
                    $rootScope.returnTo.State = toState.url;
                }
                $rootScope.returnTo.StateParams = toParams.Id;

                $state.go('login_user');
                event.preventDefault();
            }

        });
    });


})();

