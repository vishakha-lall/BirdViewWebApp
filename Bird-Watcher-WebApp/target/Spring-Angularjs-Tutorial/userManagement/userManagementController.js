app.controller('userManagementController', function($scope, $http) {
		$scope.users = []
		$scope.userform = {
			name : "",
			password : ""
		};

		getUserDetails();

		function getUserDetails() {
			$http({
				method : 'GET',
				url : 'userdetails'
			}).then(function successCallback(response) {
				$scope.users = response.data;
			}, function errorCallback(response) {
				console.log(response.statusText);
			});
		}

		$scope.processUser = function() {
			$http({
				method : 'POST',
				url : 'user',
				data : angular.toJson($scope.userform),
				headers : {
					'Content-Type' : 'application/json'
				}
			}).then(getUserDetails(), clearForm())
			  .success(function(data){
				$scope.users= data
		    });
		}
		$scope.editUser = function(user) {
			$scope.userform.name = user.name;
			$scope.userform.password = user.password;
			disableName();
		}
		$scope.deleteUser = function(user) {
			$http({
				method : 'DELETE',
				url : 'deleteuser',
				data : angular.toJson(user),
				headers : {
					'Content-Type' : 'application/json'
				}
			}).then(getUserDetails());
		}

		function clearForm() {
			$scope.userform.name = "";
			$scope.userform.password = "";
			document.getElementById("name").disabled = false;
		}
		;
		function disableName() {
			document.getElementById("name").disabled = true;
		}
	});