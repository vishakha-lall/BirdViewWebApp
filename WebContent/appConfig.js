app.config(function($stateProvider, $urlRouterProvider) {
	$urlRouterProvider.otherwise('/login');
    $stateProvider

    .state('login', {
    	controller: '/login/loginController',
    	url: '/login',
        views: {
        	'': { templateUrl: 'login.html' },
        }
    })
    .state('home', {
        url: '/home',
        views: {
        	'': { templateUrl: 'home.html' },
        }
    });
}); 