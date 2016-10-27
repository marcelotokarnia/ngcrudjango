(function(){
    var table_mod = angular.module('table', ['fast_ajax']);
    table_mod.directive('showTable', function(){
        return {
            restrict: 'E',
            replace: true,
            scope: {
            },
            templateUrl: '/static/show-table.html',
            controller: function($scope, FAjax){
                $scope.table = [];
                $scope.loading = true;
                FAjax.get('/core/get_table').success(function(response){
                    $scope.table = response.table.entries;
                }).finally(function(){
                    $scope.loading = false;
                });
            }
        }
    });
})();