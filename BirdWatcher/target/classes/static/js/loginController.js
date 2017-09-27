app.controller('loginController', function($scope,$location,$http){	
	$scope.login=function(){
		var userData={
				username:$scope.username,
				password:$scope.password
		};
		$http({
			method:"POST",
			url:"/login/authenticate",
			data:userData
		}).then(function success(response){
			console.log("Login data sent successfully");
			alert(response.data);
			if(response.data=="success"){
				console.log("Successful Login");
				$location.path('/home');
			}else{
				console.log("Login Unsuccessful");
				$location.path('/nouser');
			}
		}, function error(response){
			console.log("Login data not sent");
			$location.path('/nouser');
		});
	}
	$scope.signup=function(){
		$location.path('/signup');
	};
});
