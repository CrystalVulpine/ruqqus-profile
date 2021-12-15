import json
import sys

posts = []
with open("comments.fx.2021-10-30.txt.sort", "r") as f:
	for jsonline in f:
		comment = json.loads(jsonline)
		if comment.get("author_name", "[deleted]") == 'CrystalVulpine':
			print("Exporting comment " + comment["id"])
			with open("mycomments.json", "a+") as af:
				json.dump(comment, af)
				af.write("\n")
			post_id = comment["post_id"]
			if not post_id in posts:
				posts.append(post_id)

with open("ruqqus.submf.2021-10-14.json", "r") as f:
	for jsonline in f:
		post = json.loads(jsonline)
		if post.get("author", "[deleted]") == '@CrystalVulpine' or post["item_id_alias"] in posts:
			print("Exporting post " + post["item_id_alias"])
			with open("myposts.json", "a+") as af:
				json.dump(post, af)
				af.write("\n")
			if not post["item_id_alias"] in posts:
				posts.append(post["item_id_alias"])

with open("comments.fx.2021-10-30.txt.sort", "r") as f:
	for jsonline in f:
		comment = json.loads(jsonline)
		if comment["post_id"] in posts and comment.get("author_name", "[deleted]") != 'CrystalVulpine':
			print("Exporting comment " + comment["id"])
			with open("mycomments.json", "a+") as af:
				json.dump(comment, af)
				af.write("\n")

