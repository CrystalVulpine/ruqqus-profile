import my_json as json
import sys

posts = []
with open("comments.fx.2021-10-30.txt.sort", "r") as f:
	for jsonline in f:
		comment = json.loads(jsonline)
		if comment.author == '@CrystalVulpine':
			with open("mycomments.json", "a") as af:
				print("Exporting comment " + comment.fullname)
				json.dump(comment, af)
			if not comment.post.fullname in posts:
				posts.append(comment.post.fullname)

with open("ruqqus.submf.2021-10-14.json", "r") as f:
	for jsonline in f:
		post = json.loads(jsonline)
		if post.author == '@CrystalVulpine' or post.fullname in posts:
			with open("myposts.json", "a") as af:
				json.dump(post, af)

