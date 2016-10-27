(function() {
    var fast_ajax_module = angular.module('fast_ajax', []);

    fast_ajax_module.factory('FAjax', function ($http) {

        return {
            get: http_get,
            post: http_post,
            delete: http_delete,
            update: http_put
        };

        function http_put(url, params){
            if (!params){
                return;
            }
            var promise = $http({
                method: 'PUT',
                url: url,
                data: angular.toJson(params),
                headers: {
                    "Content-Type": "application/json"
                }
            });
            return promise;
        }

        function http_delete(url){
            var promise = $http({
                method: 'DELETE',
                url: url
            });
            return promise;
        }

        function http_get(url, params) {
            if (!params) {
                params = {};
            }
            var promise = $http({
                method: 'GET',
                url: url,
                params: params
            });
            return promise;
        }

        function http_post(url, params) {
            if (!params) {
                params = {};
            }
            var promise = $http({
                method: 'POST',
                url: url,
                data: angular.toJson(params),
                headers: {
                    "Content-Type": "application/json"
                }
            });
            return promise;
        }
    });
}());