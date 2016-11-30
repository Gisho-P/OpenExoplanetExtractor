import subprocess
import urllib.request
import urllib.parse
import http.client
token = "a02f89cd8bca565ae600e30b1388bc57954e0a1a"
def gitPull():
	p = subprocess.Popen(args=['./gitCommands.sh pull' ], shell=True)
	p.wait()

def gitCommit(message):
	p = subprocess.Popen(args=["./gitCommands.sh commit '%s'" %(message)], shell=True)
	p.wait()

def gitAdd(file):
	p = subprocess.Popen(args=["./gitCommands.sh add '%s'" %(file)], shell=True)
	p.wait()

def gitClone():
	p = subprocess.Popen(args=['./gitCommands.sh clone'],shell=True)
	p.wait()

def gitPush():
	p = subprocess.Popen(args=['./gitCommands.sh push'], shell=True)
	p.wait()

def gitBranch(branch_name):
	p = subprocess.Popen(args=["./gitCommands.sh branch '%s'" %(branch_name)], shell=True)
	p.wait()

def gitCheckout(branch_name):
	p = subprocess.Popen(args=["./gitCommands.sh checkout '%s'" %(branch_name)], shell=True)
	p.wait()

def gitPullRequest(branch_name):
	url = "https://api.github.com/repos/T01test/open_exoplanet_catalogue/pulls/"
	data = {
	        'title': 'Merge %s with master'%(branch_name),
	        'head': 'T01test:%s'%(branch_name),
	        'base': 'master'
	      }
	#conn = http.client.HTTPSConnection("api.github.com")
	#conn.putheader('Authorization', 'token a02f89cd8bca565ae600e30b1388bc57954e0a1a')
	#conn.endheader()
	#conn.putrequest("POST", "/repos/T01test/open_exoplanet_catalogue/pulls/", urllib.urlencode(data).encode())
	#conn.send()
	#response = conn.getresponse()
	#print(response.status, response.reason)
	#request = urllib.request.Request(url, urllib.parse.urlencode(data).encode())
	#print(urllib.request.urlopen(request).read().decode())

	request = urllib.request.Request(url, urllib.parse.urlencode(data).encode())
	request.add_header('Authorization', 'token %s' % token)
	response = urllib.request.urlopen(request)
	print(response.read())

gitPullRequest("11-29-15-38")


#a02f89cd8bca565ae600e30b1388bc57954e0a1a