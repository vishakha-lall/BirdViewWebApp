app.config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: '/login/login.html',
        controller: 'loginController'
      });
});