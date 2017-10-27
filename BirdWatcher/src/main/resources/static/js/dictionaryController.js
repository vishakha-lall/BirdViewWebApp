app.controller('dictionaryController', function($scope,$location,$http){	
    uploadUrl = "http://192.168.1.128/birdDictGenerator.py"; 
    $http.get(uploadUrl)
    .then(function(response) {
        var content = response.data;
        var i;
        $scope.split=[];
        for(i=0; i<200; i++){
        	$scope.split[i]=content.data[i];
        }
    	
    }, function(response) {
        alert("Something went wrong");
        $scope.content="OOPS! Please try again"
    });
});
