import json
import requests

def authURL(url):
	if len(auth.strip()) > 0:
		return url+"?access_token="+auth
	else:
		return url

def printUser(url, fil):
	u = json.loads(requests.get(authURL(url)).text)
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
	return True

repo = raw_input("Repository Name (username/repoName): ")
auth = raw_input("Create a Personal Access Token at https://github.com/settings/tokens/new \nPaste it here: ")

while len(auth.strip()) == 0:
	a = raw_input("Are you sure you want to continue without an API token? \nThis will greatly limit the amount of calls able to be made. \n[Y/n]:").lower()
	if a == "n" or a == "no":
		auth = raw_input("Paste your Personal Access Token here: ")
	if a == "y" or a == "yes":
		break

d = json.loads(requests.get(authURL("https://api.github.com/repos/"+repo+"/contributors")).text)
o = json.loads(requests.get(authURL("https://api.github.com/repos/"+repo)).text)

with open('humans.txt', 'wb') as f:
	print "\nOwner of "+repo+":"
	f.write('/* OWNER */\n')
	printUser(o["owner"]["url"], f)
	print "\nContributors to "+repo+" \n(more info will be written to humans.txt):"
	f.write('\n/* CONTRIBUTORS */\n')
	for i in d:
		printUser(i["url"], f)