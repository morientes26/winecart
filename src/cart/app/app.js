var app = angular.module("app", ['ngRoute', 'ngCookies'])
.run(function($rootScope, $cookies, shoppingcart) {

    $rootScope.API_URL = "http://127.0.0.1:8000/api/";
    shoppingcart.init('testovac_1');
	
})

// configure our routes
app.config(function($routeProvider) {
    
    $routeProvider

        // route for the product list in basic cart
        .when('/', {
            templateUrl : 'pages/list.html',
            controller  : 'list'
        })

        // route for the product list in event cart
        .when('/event', {
            templateUrl : 'pages/event.html',
            controller  : 'event'
        })

        // route for the detail of product 
        // if id then url is 'detail/?id='
        // if detailId then url is 'detail/id'
        .when('/detail/:detailId', {
            templateUrl : 'pages/detail.html',
            controller  : 'detail'
        })

        // route for the order
        .when('/order', {
            templateUrl : 'pages/order.html',
            controller  : 'order'
        });

});

// get customer shopping cart
app.service('shoppingcart', function($cookies) {

	this.init = function (customerName) {
		// Setting a cookie
		if ($cookies.getObject('customer')==null){		
			var customer = {
								name: customerName,
								items: []
							}
			$cookies.putObject('customer', customer);
			console.log('init cookies');
		}
	}
    this.getCustomer = function () {
    	return $cookies.getObject('customer');
    }

    this.add = function(id){
    	var customer = this.getCustomer();
    	if (customer.items[id] == undefined)
    		customer.items[id] = 0;
    	customer.items[id] += 1;
    	$cookies.putObject('customer', customer);
    }
    this.remove = function(id){
    	var customer = this.getCustomer();
    	if (customer.items[id] == undefined)
    		customer.items[id] = 1;
    	if (customer.items[id]>0)
    		customer.items[id] = customer.items[id] - 1;
    	$cookies.putObject('customer', customer);
    }
    this.clear = function(){
    	var customer = this.getCustomer();
    	customer.items = [];
    	$cookies.putObject('customer', customer);
    }
});

// default value of angular bind element. Example: {{ count | default:0 }}
app.filter('default', [function(){
  return function(value, def) {
    return value || def;
  };
}]);