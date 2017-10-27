app.controller('waitController', ['$scope', 'shareResponseData', function($scope, shareResponseData){
    var result={};
    while(shareResponseData.getShared()==0){
    };
    shareResponseData.getData(result);
    alert(JSON.stringify(result));
}]);
