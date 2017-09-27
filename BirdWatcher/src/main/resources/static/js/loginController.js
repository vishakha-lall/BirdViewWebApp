app.controller('loginController', function($scope,$location,$http){	
	$scope.login=function(){
		$http({
			method:"POST",
			url:"LoginController",
			headers: {'Content-Type': "text/plain"},
			data:{
				username:$scope.username,
				password:$scope.password
			}
		}).then(function success(response){
			console.log("Login data sent");
			$location.path(response.data);
		}, function error(response){
			console.log("Login data not sent");
			$location.path("/nouser");
		});
	}
	$scope.signup=function(){
		$location.path('/signup');
	};
});
