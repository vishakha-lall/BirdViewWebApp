app.config(function($stateProvider, $urlRouterProvider){
    $urlRouterProvider.otherwise('/login');
    $stateProvider.state('/login', {
            url: '/login',
            templateUrl: '/login/login.html',
            controller: 'loginController'
        });
});
