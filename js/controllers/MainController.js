app.controller('MainController', ['$scope', '$http', function($scope, $http) { 
	$scope.details = {};
	$scope.busses = [];
	$scope.send = function() {
	};

	// var web_url = "https://api.octranspo1.com/v1.2/Gtfs?appID=3a647e7d&apiKey=d51425ec5540622e71c764e84430f751&table=routes&format=json"

	$http.get("Gtfs/routes.txt")
	.success(function(response){
		// $scope.busses = response.Gtfs;
		for (var i = 0; i < response.Gtfs.length; i += 2) {
			$scope.busses.push(response.Gtfs[i].route_short_name);
			console.log(response.Gtfs[i]);
			console.log(response.Gtfs[i].route_short_name);
		}
		// console.log($scope.busses)
	});
}]);