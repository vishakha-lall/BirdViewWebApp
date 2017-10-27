app.controller('nouserController', function($scope,$location,$http){	
	$scope.login=function(){
		$location.path('/login');
	}
	$scope.signup=function(){
		$location.path('/signup');
	};
});
