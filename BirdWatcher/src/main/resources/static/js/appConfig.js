app.config(function($stateProvider, $urlRouterProvider) {
    $stateProvider
    .state('login', {
    	controller: '/js/loginController',
    	url: '/login',
        views: {
        	'': { templateUrl: '/views/login.html' },
        }
    })
    .state('home', {
    	controller: '/js/homeController.js',
        url: '/home',
        views: {
        	'': { templateUrl: '/views/home.html' },
        }
    })
    .state('nouser', {
    	controller: '/js/nouserController.js',
        url: '/nouser',
        views: {
        	'': { templateUrl: '/views/nouser.html' },
        }
    })
    .state('signup', {
    	controller: '/js/signupController.js',
    	url: '/signup',
        views: {
        	'': { templateUrl: '/views/signup.html' },
        }
    })
    .state('upload', {
    	/*controller: '/js/uploadImageController.js',*/
        url: '/upload',
        views: {
        	'': { templateUrl: '/views/upload.html' },
        }
    })
    .state('techstack', {
        url: '/techstack',
        views: {
        	'': { templateUrl: '/views/techstack.html' },
        }
    });
    $urlRouterProvider.otherwise('/login');
}); 