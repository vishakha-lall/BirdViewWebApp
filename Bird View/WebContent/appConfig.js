routerApp.config(function($stateProvider, $urlRouterProvider) {

    $urlRouterProvider.otherwise('/login');
    $stateProvider

    .state('login', {
        url: '/login',
        views: {
        	'': { templateUrl: 'login.html' },
        }
    });
}); 
