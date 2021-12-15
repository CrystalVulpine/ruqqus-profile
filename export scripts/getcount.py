import json
import sys

count = 0
with open("myposts-html.json", "r") as f:
	for jsonline in f:
		if '{"item_id_alias":"cd76"' in jsonline:
			count += 1

print(str(count))
