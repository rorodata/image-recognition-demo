/*
 * Javascript library to interact with the rorodata platform.
 */

var roro = (function() {
    var VERSION = "0.1.0";

    function Client(base_url) {
        this.base_url = base_url;

        // Add a trailing / if not already present
        if (this.base_url[this.base_url.length-1] != "/")
            this.base_url += "/";
    }
    Client.prototype.invoke = function(function_name, args, success, error) {
        if (typeof jQuery === 'undefined') {
            console.log("jQuery is required to run the invoke function. Please include it as well.");
            return;
        }
        var url = this.base_url + function_name;
        $.ajax({
            type: 'POST',
            url: url,
            data: JSON.stringify(args),
            success: success,
            error: error,
            contentType: "application/json",
            dataType: 'json'
        });
    }
    
    return {
        client: function(url) {
            return new Client(url);
        },
        VERSION: VERSION
    };
}());

