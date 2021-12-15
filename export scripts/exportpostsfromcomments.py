import json
import sys

post_ids = []
output = ""

with open("comments.fx.2021-10-30.txt.sort", "r") as f:
	for jsonline in f:
		comment = json.loads(jsonline)
		post_id = comment["post"]["id"]
		if comment["post"].get("author_name", "[unknown]") == 'CrystalVulpine' and not post_id in post_ids:
			print(post_id + "\n")
			post_ids.append(post_id)
			output += json.dumps(comment["post"]) + "\n"

with open("postsfromcomments.json", "w+") as af:
	af.write(output)
