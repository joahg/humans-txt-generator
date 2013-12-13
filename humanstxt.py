import json
import requests

def printUser(url, fil):
	u = json.loads(requests.get(url).text)
	fil.write('\n  ')
	try:
		if len(u["name"].strip()) == 0:
			raise Exception("Name cannot be empty") 
		fil.write(u["name"].encode('ascii', 'ignore'))
		n = u["name"]
	except:
		fil.write(u["login"].encode('ascii', 'ignore'))
		n = u["login"]
	fil.write("\n  GitHub Profile: "+u["html_url"].encode('ascii', 'ignore'))
	try:
		if len(u["location"].strip()) == 0:
			raise Exception("Location cannot be empty") 
		fil.write("\n  Location: "+u["location"].encode('ascii', 'ignore'))
	except:
		pass
	try:
		if len(u["blog"].strip()) == 0:
			raise Exception("Blog cannot be empty") 
		fil.write("\n  Website: "+u["blog"].encode('ascii', 'ignore'))
	except:
		pass
	fil.write("\n")		
	print n

repo = raw_input("Repository Name (username/repoName): ")
auth = raw_input("Create a Personal Access Token at https://github.com/settings/tokens/new \nPaste it here: ")

d = json.loads(requests.get("https://api.github.com/repos/"+repo+"/contributors?access_token="+auth).text)
o = json.loads(requests.get("https://api.github.com/repos/"+repo+"?access_token="+auth).text)

with open('humans.txt', 'wb') as f:
	print "\nOwner of "+repo+":"
	f.write('/* OWNER */\n')
	printUser(o["owner"]["url"]+"?access_token="+auth, f)
	print "\nContributors to "+repo+" \n(more info will be written to output.txt):"
	f.write('\n/* CONTRIBUTORS */\n')
	for i in d:
		printUser(i["url"]+"?access_token="+auth, f)