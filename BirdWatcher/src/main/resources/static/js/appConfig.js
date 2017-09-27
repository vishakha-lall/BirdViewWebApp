app.config(function($stateProvider, $urlRouterProvider) {
    $stateProvider
    .state('login', {
    	controller: '/views/login/loginController',
    	url: '/login',
        views: {
        	'': { templateUrl: '/views/login.html' },
        }
    })
    .state('signup', {
    	controller: '/views/userManagement/userManagementController.js',
    	url: '/signup',
        views: {
        	'': { templateUrl: '/views/userManagement.html' },
        }
    })
    .state('home', {
    	controller: '/views/home/homeController.js',
        url: '/home',
        views: {
        	'': { templateUrl: '/views/home.html' },
        }
    })
    .state('nouser', {
    	controller: '/views/nouser/nouserController.js',
        url: '/nouser',
        views: {
        	'': { templateUrl: '/views/nouser.html' },
        }
    })
    .state('uploadImage', {
    	controller: '/views/controllers/uploadImageController.js',
        url: '/uploadImage',
        views: {
        	'': { templateUrl: '/views/uploadImage.html' },
        }
    });
    $urlRouterProvider.otherwise('/login');
}); 