/* Angular settings */

$interpolateProvider.startSymbol('[[').endSymbol(']]');

$httpProvider.default.xsrfCookieName = 'csrftoken';
$httpProvider.default.xsrfHeaderName = 'X-CSRFToken';

$resourceProvider.defaults.stripTrailingSlashes = false;
