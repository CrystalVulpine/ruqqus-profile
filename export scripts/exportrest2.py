import json
import sys
import subprocess

post_list = []

# get commented-on posts as well
with open("comments.fx.2021-10-30.txt.sort", "r") as f:
	for jsonline in f:
		comment = json.loads(jsonline)
		post_id = comment["post_id"]
		if comment.get("author_name", "[deleted]") == 'CrystalVulpine' or comment["post"].get("author_name", "[deleted]") == 'CrystalVulpine':
			with open("posts/" + post_id + ".json", "a+") as af:
				write(jsonline + "\n")
			if not post_id in post_list:
				post_list.append(post_id)



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
