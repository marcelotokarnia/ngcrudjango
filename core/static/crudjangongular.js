(function(){
    var crudjangongular_module = angular.module('crudjangongular_app', ['crud', 'table']);
    crudjangongular_app_module.config(function($controllerProvider, $interpolateProvider, $httpProvider) {
        $controllerProvider.allowGlobals();
        $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
        $httpProvider.defaults.headers.common['X-CSRFToken'] = window.CSRF_TOKEN;
        $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
        $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';
        $httpProvider.useApplyAsync(true);
    });
})();
