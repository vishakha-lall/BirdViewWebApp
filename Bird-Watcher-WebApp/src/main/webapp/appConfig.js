app.config(function($stateProvider, $urlRouterProvider) {
    $stateProvider
    .state('login', {
    	controller: '/login/loginController',
    	url: '/login',
        views: {
        	'': { templateUrl: 'login.html' },
        }
    })
    .state('signup', {
    	controller: '/userManagement/userManagementController.js',
    	url: '/signup',
        views: {
        	'': { templateUrl: 'userManagement.html' },
        }
    })
    .state('home', {
        url: '/home',
        views: {
        	'': { templateUrl: 'home.html' },
        }
    });
    $urlRouterProvider.otherwise('/login');
}); 