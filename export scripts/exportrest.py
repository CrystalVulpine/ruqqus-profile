import json
import sys
import subprocess

extra_posts = []

with open("myposts.json", "r") as f:
	for jsonline in f:
		comment = json.loads(jsonline)
		post_id = post["id"]
		with open("post_" + post_id + ".json", "a+") as af:
			write(jsonline + "\n")

# get commented-on posts as well
with open("mycomments.json", "r") as f:
	for jsonline in f:
		comment = json.loads(jsonline)
		post_id = comment["post_id"]
		if comment["post"].get("author_name", "[deleted]") != 'CrystalVulpine' and not post_id in extra_posts:
			extra_posts.append(post_id)

with open("comments.fx.2021-10-30.txt.sort", "r") as f:
	for jsonline in f:
		comment = json.loads(jsonline)
		
		post_id = comment["post_id"]
		
		# grep already got any comments on posts I'm the author of as well as any of mine on others' posts
		if comment["post"].get("author_name", "[deleted]") != 'CrystalVulpine' and not post_id in posts:
			commentcommand += ' -hFe \'"post_id":"' + post_id + '"\''
			postcommand += ' -hFe \'"item_id_alias":"' + post_id + '"\''
			posts.append(post_id)

subprocess.call(commentcommand + ' comments.fx.2021-10-30.txt.sort | grep -hFv \'"author_name":"CrystalVulpine"\' >> comments.json', shell=True)
subprocess.call(postcommand + " ruqqus.submf.2021-10-14.json >> posts.json", shell=True)
