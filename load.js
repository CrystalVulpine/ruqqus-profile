function getUser( index )
{
        if ( index >= usernames.length ) {
                loadPage();
                return;
        }

	let username = usernames[ index ];
	$.ajax( { url: "users/" + username + ".json",
		  dataType: "json",
		  success: function( response ) {
		 	           response.permalink = "index.html?user=" + username;
		 	           users[ username ] = response;
		 	           getUser( index + 1 );
		           },
		  error: function() {
		        console.log("error: " + username);
		  } } );
}

function start()
{
	(window.onpopstate = function () {
		var match, pl = /\+/g, search = /([^&=]+)=?([^&]*)/g, decode = function (s) { return decodeURIComponent(s.replace(pl, " ")); }, query  = window.location.search.substring(1);
		urlParams = {};
		while (match = search.exec(query))
			urlParams[decode(match[1])] = decode(match[2]);
	})();

	env = new nunjucks.Environment(new nunjucks.WebLoader('views'));

	env.addFilter('full_link', function(link) {
		return link;
	});

	page = parseInt(urlParams["page"]) || 1;
	profilename = urlParams["user"] || usernames[ 0 ];
	
	getUser( 0 );
}

start();

