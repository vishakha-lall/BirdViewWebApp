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
    	controller: '/js/uploadController.js',
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
    })
    .state('about', {
        url: '/about',
        views: {
        	'': { templateUrl: '/views/about.html' },
        }
    })
    .state('result', {
    	controller: '/js/resultController.js',
        url: '/result',
        views: {
        	'': { templateUrl: '/views/result.html' },
        }
    })
    .state('dictionary', {
    	controller: '/js/dictionaryController.js',
        url: '/dictionary',
        views: {
        	'': { templateUrl: '/views/dictionary.html' },
        }
    })
    .state('discover', {
    	controller: '/js/discoverController.js',
        url: '/discover',
        views: {
        	'': { templateUrl: '/views/discover.html' },
        }
    })
    .state('resultdiscover', {
    	controller: '/js/resultDiscoverController.js',
        url: '/resultDiscover',
        views: {
        	'': { templateUrl: '/views/resultDiscover.html' },
        }
    });
    $urlRouterProvider.otherwise('/login');
}); 