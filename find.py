import json
import sys
import os.path

username = sys.argv[1] if len( sys.argv ) > 1 else "CrystalVulpine"

posts = []
threads = []

def export_post( id, data, user ):
	print("Post " + id)
	if user:
		with open(username + "_posts.json", "a+") as af:
			json.dump(data, af)
			af.write("\n")
	if not os.path.isfile("posts/post_" + id + ".json"):
		with open("posts/post_" + id + ".json", "a+") as af:
			json.dump(data, af)
			af.write("\n")
		threads.append( id )
	posts.append( id )

with open("submissions.f1.2021-10-30.txt.sort", "r") as f:
	for jsonline in f:
		post = json.loads(jsonline)
		if not post["id"] in posts and post.get("author_name", "[unknown]") == username:
			export_post( post["id"], post, True )

with open("comments.fx.2021-10-30.txt.sort", "r") as f:
	for jsonline in f:
		comment = json.loads(jsonline)
		post = comment["post"]
		if not post["id"] in posts and post.get("author_name", "[unknown]") == username:
			export_post( post["id"], post, True )
		if comment.get("author_name", "[unknown]") == username:
			print("Comment " + comment["id"])
			with open(username + "_comments.json", "a+") as af:
				json.dump(comment, af)
				af.write("\n")
			if not post["id"] in posts:
				export_post( post["id"], post, False )

with open("comments.fx.2021-10-30.txt.sort", "r") as f:
	for jsonline in f:
		comment = json.loads(jsonline)
		if comment["post_id"] in threads:
				print("Thread Comment " + comment["id"])
				with open("posts/post_" + comment["post_id"] + ".json", "a+") as af:
					json.dump(comment, af)
					af.write("\n")

with open("ruqqus.submf.2021-10-14.json", "r") as f:
	for jsonline in f:
		post = json.loads(jsonline.replace("\\\\", "\\"))
		if post.get("author", "[unknown]") == '@' + username and not post["item_id_alias"] in posts:
			with open(username + "_missing_posts.json", "a+") as af:
				json.dump(post, af)
				af.write("\n")

