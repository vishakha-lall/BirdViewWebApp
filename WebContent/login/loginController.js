app.controller('loginController', function($scope,$location){	
	$scope.login=function(){
		if ($scope.username=="vishakha" && $scope.password=="awesome"){/*encrypt*/
			 alert("Login Successful!");
			 $location.path('/home');
		}
		else{
			 $scope.error="Invalid Credentials";
		}
	};
});
