function loadPage()
{
	$.ajax({
		url: "listing/posts/" + profilename + "_" + (page - 1) + ".json",
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
				if (post.url && (post.url.endsWith('.png') || post.url.endsWith('.jpg') || post.url.endsWith('.jpeg') || post.url.endsWith('.gif') || post.url.endsWith('.webm') || post.url.endsWith('.webp') || post.url.endsWith('.bmp'))) {
					post.is_image = true;
					post.thumb_url = post.url;
				}
				listing.push(post);
			}
			$.ajax({
				url: "listing/posts/" + profilename + "_" + (page) + ".json",
				dataType: "text",
				success: function(response) {
					document.documentElement.innerHTML = env.render('userpage.html', { u: users[profilename], darkMode: darkMode, sidebarCollapsed: sidebarCollapsed, listing: listing, request_path: window.location.pathname, userpage: true, page: page, next_exists: true } );
				},
				error: function (jqXHR, exception) {
					document.documentElement.innerHTML = env.render('userpage.html', { u: users[profilename], darkMode: darkMode, sidebarCollapsed: sidebarCollapsed, listing: listing, request_path: window.location.pathname, userpage: true, page: page, next_exists: false } );
				}
			});
		}
	});
}

