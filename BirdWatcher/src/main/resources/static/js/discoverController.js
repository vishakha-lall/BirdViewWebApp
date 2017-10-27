app.service('shareDiscoverData', function() {
	var bird={};
	addBird = function(newBird) {
		bird=newBird
	  };

	getBird = function(){
	      return bird;
	  };

	  return {
		  addBird: addBird,
		  getBird: getBird
	  };
});

app.controller('discoverController', function($scope,$location,$http,shareDiscoverData){	
	var content={};
	$scope.search=function(){
		$http({
			  method: 'GET',
			  url: 'http://192.168.1.128/birdDiscoverer.py',
			  params: {name:$scope.birdName}
			}).then(function successCallback(response) {
			    alert(JSON.stringify(response.data));
			    content=response.data;
			    shareDiscoverData.addBird(content);
			    $location.path("/resultDiscover");
			  }, function errorCallback(response) {
			   alert("OOPS")
		});

	}
});
