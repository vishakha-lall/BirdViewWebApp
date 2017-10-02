app.controller('resultController', function($scope,$http) {
	$http({
		method:"GET",
		url:"/result",
	}).then(function success(response){
		alert(JSON.stringify(response.data));
	}, function error(response){
	});
});