myApp = angular.module('steele', ['ui.router', 'ngResource']); //Module and resources


/*Configurations*/
myApp.config(function ($stateProvider, $urlRouterProvider, $locationProvider, $httpProvider) {
    $stateProvider
        .state('film', {
            url: '/',
            templateUrl: 'assets/partials/film.html',
            controller: 'FilmController'
        });

    $urlRouterProvider.otherwise('/'); //Default page set to root

    $locationProvider.html5Mode({
        enabled: true,
        requireBase: false
    });

    $httpProvider.defaults.headers.common = {};
    $httpProvider.defaults.headers.post = {};
    $httpProvider.defaults.headers.put = {};
    $httpProvider.defaults.headers.patch = {};
});


/*Film page controller*/
myApp.controller("FilmController", function ($scope, api, $http) {

    $scope.data_input = function(){ //On search makes a call to API with input of postcode and film title
        $http.get('http://127.0.0.1:5000/' + $scope.postcode_input + '/' + $scope.film_input).success(function(data) {
            $scope.cinedata = data; //Stores data in scope
        });
    };
});



/*Factory API function*/
myApp.factory('api', function ($resource, $http) {});
