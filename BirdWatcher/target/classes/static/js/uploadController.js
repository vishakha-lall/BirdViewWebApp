app.directive('fileModel', ['$parse', function ($parse) {
    return {
        restrict: 'A',
        link: function(scope, element, attrs) {
            var model = $parse(attrs.fileModel);
            var modelSetter = model.assign;
            
            element.bind('change', function(){
                scope.$apply(function(){
                    modelSetter(scope, element[0].files[0]);
                });
            });
        }
    };
}]);

app.service('shareResponseData', function() {
	var birds=[];
	addBird = function(newBird) {
		birds.push(newBird);
	  };

	getBirds = function(){
	      return birds;
	  };

	  return {
		  addBird: addBird,
		  getBirds: getBirds
	  };
});

app.controller('uploadController', ['$scope','$http','$location','shareResponseData', function($scope,$http,$location,shareResponseData){
	var resultObject;
    $scope.uploadFile = function(){
        var file = $scope.myFile;
        console.log('file is ' );
        console.dir(file);
        var fd = new FormData();
        fd.append('file', file);
        $http.post("/upload", fd, {
            transformRequest: angular.identity,
            headers: {'Content-Type': undefined}
        }).then(function success(response){
				alert("Image uploaded to server");
		}, function error(response){
				alert("Image could not be uploaded to server");
		});
        
        uploadUrl = "http://192.168.1.128/imageOpener.py";
        $http.post(uploadUrl, fd, {
            transformRequest: angular.identity,
            headers: {'Content-Type': undefined}
        }).then(function success(res){
				alert("Image forwarded to script");
				alert(JSON.stringify(res.data));
				resultObject=res.data;
				resultGenerator();		 
			    $location.path('/result');
        }, function error(res){
				alert("Image could not be forwarded to script");
				res.data={"result": true, "tuples": [{"species_name": "blue winged warbler", "extracted_text": "The blue-winged warbler (Vermivora cyanoptera) is a fairly common New World warbler, 11.5 cm (4.5 in) long and weighing 8.5 g (0.30 oz). It breeds in eastern North America in southern Ontario and the eastern United States. Its range is extending northwards, where it is replacing the very closely related golden-winged warbler, Vermivora chrysoptera.", "wikipedia_link": "https://en.wikipedia.org/wiki/Blue-winged_warbler", "location_info": "distribution and habitat blue-winged warblers are migratory new world warblers. they winter in southern central america and breed from east-central nebraska in the west to southern minnesota, wisconsin, michigan and southern ontario in the north to central new york, southern vermont, southern new hampshire and new england to the east, south to western south carolina, northern georgia, northern alabama, eastern tennessee and southern missouri.[1] it is a very rare vagrant to western europe, with one bird wandering to ireland. the breeding habitat is open scrubby areas. ^ cite error: the named reference terres was invoked but never defined (see the help page)."}, {"species_name": "prothonotary warbler", "extracted_text": "The prothonotary warbler (Protonotaria citrea) is a small songbird of the New World warbler family. It is the only member of the genus Protonotaria.", "wikipedia_link": "https://en.wikipedia.org/wiki/Prothonotary_warbler", "location_info": "distribution it breeds in hardwood swamps in extreme southeastern ontario and eastern united states. it winters in the west indies, central america and northern south america.[1] it is a rare vagrant to western states, most notably california. ^ stiles, gary; skutch, alexander (1989). a guide to the birds of costa rica. cornell university press. isbn 0-8014-9600-4. "}, {"species_name": "wilson warbler", "extracted_text": "The Wilson's warbler (Cardellina pusilla) is a small New World warbler. It is greenish above and yellow below, with rounded wings and a long, slim tail. The male has a black crown patch; depending on the subspecies, that mark is reduced or absent in the female. It breeds across Canada and south through the western United States, and winters from Mexico south through much of Central America. It is a very rare vagrant to western Europe.", "wikipedia_link": "https://en.wikipedia.org/wiki/Wilson's_warbler", "location_info": "Not found"}, {"species_name": "yellow throated vireo", "extracted_text": "The yellow-throated vireo (Vireo flavifrons) is a small American songbird.\"Vireo\" is a Latin word referring to a green migratory bird, perhaps the female golden oriole, possibly the European greenfinch. The specific flavifrons is from the Latin words flavus, \"yellow\", and frons, \"forehead\".\n\nAdults are mainly olive on the head and upperparts with a yellow throat and white belly; they have dark eyes with yellow \"spectacles\". The tail and wings are dark with white wing bars. They have thick blue-grey legs and a stout bill.\nTheir breeding habitat is open deciduous woods in southern Canada and the eastern United States.\nThese birds migrate to the deep southern United States, Mexico, and Central America. They are very rare vagrants to western Europe; there is a September 1990 record from Kenidjack Valley in Cornwall, Great Britain, and September 1998 record from Heligoland, a small German archipelago in the German Bight.\nThey forage for insects high in trees. They also eat berries, especially before migration and in winter when they are occasionally seen feeding on gumbo-limbo (Bursera simaruba) fruit. They make a thick cup nest attached to a fork in a tree branch.", "wikipedia_link": "https://en.wikipedia.org/wiki/Yellow-throated_vireo", "location_info": "Not found"}, {"species_name": "pine warbler", "extracted_text": "The pine warbler (Setophaga pinus) is a small songbird of the New World warbler family.", "wikipedia_link": "https://en.wikipedia.org/wiki/Pine_warbler", "location_info": "distribution and habitat female their breeding habitats are open pine woods in eastern north america. these birds are permanent residents in southern florida. some of them, however, migrate to northeastern mexico and islands in the caribbean. the first record for south america was a vagrant wintering female seen at vista nieve, colombia, on 20 november 2002; this bird was foraging as part of a mixed-species feeding flock that also included wintering blackburnian and tennessee warblers.[1] ^ cite error: the named reference strewe2004 was invoked but never defined (see the help page)."}]};
		        alert(JSON.stringify(res));
		        resultObject=res;
				resultGenerator();		 
			    $location.path('/result');
		                
		});
       
    };
    resultGenerator = function(){
    	var birds=[];
    	var bird1={
    			species_name:resultObject.tuples[0].species_name,
    			extracted_text:resultObject.tuples[0].extracted_text,
    			wikipedia_link:resultObject.tuples[0].wikipedia_link,
    			location_info:resultObject.tuples[0].location_info,
    			image_links:resultObject.tuples[0].image_links
    	};
    	shareResponseData.addBird(bird1);
    	
    	var bird2={
    			species_name:resultObject.tuples[1].species_name,
    			extracted_text:resultObject.tuples[1].extracted_text,
    			wikipedia_link:resultObject.tuples[1].wikipedia_link,
    			location_info:resultObject.tuples[1].location_info,
    			image_links:resultObject.tuples[1].image_links
    	};
    	shareResponseData.addBird(bird2);
    	
    	var bird3={
    			species_name:resultObject.tuples[2].species_name,
    			extracted_text:resultObject.tuples[2].extracted_text,
    			wikipedia_link:resultObject.tuples[2].wikipedia_link,
    			location_info:resultObject.tuples[2].location_info,
    			image_links:resultObject.tuples[2].image_links
    	};
    	shareResponseData.addBird(bird3);
    	
    	var bird4={
    			species_name:resultObject.tuples[3].species_name,
    			extracted_text:resultObject.tuples[3].extracted_text,
    			wikipedia_link:resultObject.tuples[3].wikipedia_link,
    			location_info:resultObject.tuples[3].location_info,
    			image_links:resultObject.tuples[3].image_links
    	};
    	shareResponseData.addBird(bird4);
    	
    	var bird5={
    			species_name:resultObject.tuples[4].species_name,
    			extracted_text:resultObject.tuples[4].extracted_text,
    			wikipedia_link:resultObject.tuples[4].wikipedia_link,
    			location_info:resultObject.tuples[4].location_info,
    			image_links:resultObject.tuples[4].image_links
    	};
    	shareResponseData.addBird(bird5);
    }
    
    
}]);
