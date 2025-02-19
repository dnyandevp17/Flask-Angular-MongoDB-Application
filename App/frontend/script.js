const app = angular.module('todoapp', [])
app.controller('MainController', function($scope, $http) {
    $scope.isModalVisible = false;

    // Retrieve Data by Name
    $scope.retrieveData = function() {
        if ($scope.name) {
            $http.get(`http://localhost:5000/${$scope.name}`)
            .then(function(response) {
                const data = response.data;
                $scope.output = `Name: ${data.Name} | Company: ${data.Company} | Domain: ${data.Domain}`;
            })
        }
        $scope.name = ""
    };
 
    // Post Data
    $scope.postData = function() {
        const postData = {
            Name: $scope.postName,
            Company: $scope.postCompanyname,
            Domain: $scope.postDomain
        };
 
        $http.post("http://localhost:5000/postData", postData, {
            headers: { 'Content-Type': 'application/json' }
        })

        .then(function(response){
            $scope.isModalVisible = true;
            $scope.message = "Data Saved"

        })
        $scope.postName = "";
        $scope.postCompanyname = "";
        $scope.postDomain = "";
    };

    $scope.closeAlert = function(){
        $scope.isModalVisible = false;  
    }
 
});