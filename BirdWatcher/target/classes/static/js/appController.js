app.controller('appController',function($scope,$http){
	$http({
		method:"GET",
		url:"/"	
	});
})