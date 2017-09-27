app.controller('signupController', function($scope,$location,$http){	
	$scope.signup=function(){
		var userData={
				username:$scope.username,
				email:$scope.email,
				password:$scope.password
		};
		$http({
			method:"POST",
			url:"/signup",
			data:userData
		}).then(function success(response){
			console.log("Signup data sent successfully");
			if(response.data=="success"){
				console.log("User Added");
				alert("User added successfully");
				$location.path('/home');
			}else{
				console.log("User not added");
				$location.path('/signup');
			}
		}, function error(response){
			console.log("Signup data not sent");
			$location.path('/signup');
		});
	}
});
