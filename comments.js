function loadPage()
{
	$.ajax({
		url: "listing/comments/" + profilename + "_" + (page - 1) + ".json",
		dataType: "text",
		success: function(response) {
			var listing = [];
			var posts = response.split("\n");
			for (poststr of posts) {
				if (poststr == '') {
					break;
				}
				let post = JSON.parse(poststr);
				if (usernames.includes(post.author_name)) {
					post.author = users[post.author_name];
				}
				listing.push(post);
			}
			$.ajax({
				url: "listing/comments/" + profilename + "_" + (page) + ".json",
				dataType: "text",
				success: function(response) {
					document.documentElement.innerHTML = env.render('userpage_comments.html', { u: users[profilename], darkMode: darkMode, sidebarCollapsed: sidebarCollapsed, listing: listing, request_path: window.location.pathname, userpage: true, page: page, next_exists: true } );
				},
				error: function (jqXHR, exception) {
					document.documentElement.innerHTML = env.render('userpage_comments.html', { u: users[profilename], darkMode: darkMode, sidebarCollapsed: sidebarCollapsed, listing: listing, request_path: window.location.pathname, userpage: true, page: page, next_exists: false } );
				}
			});
		}
	});
}

