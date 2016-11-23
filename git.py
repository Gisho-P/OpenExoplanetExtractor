import subprocess


def pull():
	p = subprocess.Popen(args=['./gitCommands.sh pull' ], shell=True)
	p.wait()

def commit(message):
	p = subprocess.Popen(args=['./gitCommands.sh commit ' + message], shell=True)
	p.wait()

def addFile(files):
	p = subprocess.Popen(args=['./gitCommands.sh add ' + files], shell=True)
	#p.wait()

def clone():
	p = subprocess.Popen(args=['./gitCommands.sh clone'],shell=True)
	p.wait()

def push():
	p = subprocess.Popen(args=['./gitCommands.sh push'], shell=True)
	p.wait()



clone();
addFile(".")
commit("added file")
push()
