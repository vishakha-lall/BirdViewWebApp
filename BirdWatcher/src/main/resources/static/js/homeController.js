app.controller('homeController', function($scope,$location,$http){	
	$scope.uploadImage=function(){
		$location.path('/upload');
	};
	$scope.techstack=function(){
		$location.path('/techstack');
	};
	$scope.about=function(){
		$location.path('/about');
	};
	$scope.dictionary=function(){
		$location.path('/dictionary');
	};
	$scope.discover=function(){
		$location.path('/discover');
	};
});
