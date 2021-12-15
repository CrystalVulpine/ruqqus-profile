import json
import sys

posts = []
with open("comments.fx.2021-10-30.txt.sort", "r") as f:
	current_line = 1
	for jsonline in f:
		#if current_line != 1636417:
		#	jsonline += ','
		comment = json.loads(jsonline)
		if comment["author"] == '@CrystalVulpine':
			with open("mycomments.json", "a+") as af:
				print("Exporting comment " + comment["fullname"])
				json.dump(comment, af)
			post_fullname = comment["post"]["fullname"]
			if not post_fullname in posts:
				posts.append(post_fullname)
		current_line += 1

with open("ruqqus.submf.2021-10-14.json", "r") as f:
	current_line = 1
	for jsonline in f:
		#if current_line != 550271:
		#	jsonline += ','
		post = json.loads(jsonline)
		if post["author"] == '@CrystalVulpine' or post["item_id_alias"] in posts:
			with open("myposts.json", "a+") as af:
				print("Exporting post " + post["item_id_alias"])
				json.dump(post, af)
			if not post["item_id_alias"] in posts:
				posts.append(post["item_id_alias"])
		current_line += 1

with open("comments.fx.2021-10-30.txt.sort", "r") as f:
	current_line = 1
	for jsonline in f:
		#if current_line != 1636417:
		#	jsonline += ','
		comment = json.loads(jsonline)
		if comment["post"]["fullname"] in posts and comment["author"] != '@CrystalVulpine':
			with open("mycomments.json", "a+") as af:
				print("Exporting comment " + comment["fullname"])
				json.dump(comment, af)
		current_line += 1

