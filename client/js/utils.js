(function(){

    errorHandler = function(response, headers) {
        if (headers == 0) {
            return "The server seems to be down.";
        } else {
            return response;
        };
    };

})()
