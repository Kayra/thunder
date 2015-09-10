(function(){

    var routineAppFilters = angular.module('routineApp.filters', []);

    routineAppFilters.filter('range', function() {
        return function(input, min, max) {
        min = parseInt(min); //Make string input int
        max = parseInt(max);
        for (var i=min; i<max; i++)
            if (i<10) {
                input.push('0' + i)
            } else {
                input.push(i.toString());
            }
        return input;
        };
    });

})();
