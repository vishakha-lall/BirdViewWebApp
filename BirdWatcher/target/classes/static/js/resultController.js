app.controller('resultController', ['$scope', 'shareResponseData', function($scope, shareResponseData){
    $scope.birds=[];
	$scope.birds=shareResponseData.getBirds();
    alert($scope.birds);
}]);
