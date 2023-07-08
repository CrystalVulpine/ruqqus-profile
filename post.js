function loadPage()
{
	var pid = urlParams["id"];
	var cid = urlParams["cid"];
	var linked_comment;
	$.ajax({
		url: "posts/post_" + urlParams["id"] + ".json",
		dataType: "text",
		success: function(response) {
			var objects = response.split("\n");
			var comments = [];
			var post = JSON.parse(objects[0]);
			if (usernames.includes(post.author_name)) {
				post.author = users[post.author_name];
			}
			if (post.url && (post.url.endsWith('.png') || post.url.endsWith('.jpg') || post.url.endsWith('.jpeg') || post.url.endsWith('.gif') || post.url.endsWith('.webm') || post.url.endsWith('.webp') || post.url.endsWith('.bmp'))) {
				post.is_image = true;
				post.thumb_url = post.url;
			}
			for (let i = 1; i < objects.length; ++i) {
				if (objects[i] == '') {
					continue;
				}
				let comment = JSON.parse(objects[i]);
				if (comment.parent_comment_id == null) {
					comment.is_top_level = true;
				}
				if (comment.id == cid) {
					linked_comment = comment;
				}
				comment.permalink = "/post.html?id=" + pid + "&cid=" + comment.id;
				comments.push(comment);
				if (post.guild == null) {
					post.guild = comment.guild;	
				}
			}
			for (comment of comments) {
				if (usernames.includes(comment.author_name)) {
				        comment.author = users[comment.author_name];
			        }
				if (comment.parent_comment_id != null) {
					let found = false;
					for (comment2 of comments) {
						if (comment2.id == comment.parent_comment_id[0]) {
							if (!comment2.replies) {
								comment2.replies = [];
							}
							comment2.replies.push(comment);
							found = true;
							break;
						}
					}
					if (!found) {
						let missingcomment = {};
						missingcomment.missing = true;
						missingcomment.body = "[deleted, or removed by admins, or missing]";
						missingcomment.body_html = "<p style=\"color:red!important\">[deleted, or removed by admins, or missing]</p>";
						missingcomment.id = comment.parent_comment_id[0];
						missingcomment.replies = [];
						missingcomment.replies.push(comment);
						comments.push(missingcomment);
					}
				}
			}
			for (let i = 0; i < comments.length; ++i) {
				if ((cid == null && !comments[i].is_top_level) || (cid != null && comments[i].id != cid)) {
					comments.splice(i, 1);
					--i;
				}
			}
			document.documentElement.innerHTML = env.render('submission.html', { darkMode: darkMode, sidebarCollapsed: sidebarCollapsed, p: post, b: post.guild, comments: comments, linked_comment: linked_comment, request_path: window.location.pathname } );
		}
	});
}

