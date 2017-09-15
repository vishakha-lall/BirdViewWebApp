app.controller('loginController', function($scope,$location,$http){	
	$scope.login=function(){
		if ($scope.user.username=="vishakha" && $scope.user.password=="awesome"){/*encrypt*/
			 alert("Login Successful!");
			 $http.POST('/login',$scope.user)
			 .success(function(response){
				 console.log("success");
			 })
			 .error(function(response){
				 console.log("fail");
			 });
			 $location.path('/home')
			 
		}
		else{
			 $scope.error="Invalid Credentials";
		}
	};
});
