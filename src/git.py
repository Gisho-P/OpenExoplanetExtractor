import subprocess


def pull():
	'''Nothing->Nothing
	It calls the bash file with the git pull arguement
	'''
	p = subprocess.Popen(args=['./gitCommands.sh pull' ], shell=True)
	p.wait()

def commit(message):
	'''Nothing->Nothing
	It calls the bash file that does commit with a message arguement
	'''	
	p = subprocess.Popen(args=['./gitCommands.sh commit ' + message], shell=True)
	p.wait()

def addFile(files):
	'''Nothing->Nothing
	It calls the bash file that does git add with either a . or file name(s) 
	arguement
	'''	
	p = subprocess.Popen(args=['./gitCommands.sh add ' + files], shell=True)
	p.wait()

def clone():
	'''Nothing->Nothing
	It calls the bash file with the git clone arguement
	'''	
	p = subprocess.Popen(args=['./gitCommands.sh clone'],shell=True)
	p.wait()

def push():
	'''Nothing->Nothing
	It calls the bash file with the git push arguement
	'''
	p = subprocess.Popen(args=['./gitCommands.sh push'], shell=True)
	p.wait()


