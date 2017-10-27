app.controller('resultDiscoverController', ['$scope', 'shareDiscoverData', function($scope, shareDiscoverData){
	$scope.bird={};
	$scope.bird=shareDiscoverData.getBird();
}]);
