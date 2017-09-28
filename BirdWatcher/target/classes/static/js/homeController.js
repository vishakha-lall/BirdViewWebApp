app.controller('homeController', function($scope,$location,$http){	
	$scope.uploadImage=function(){
		$location.path('/upload');
	};
});
