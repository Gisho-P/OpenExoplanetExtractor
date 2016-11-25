import subprocess


def gitPull():
	p = subprocess.Popen(args=['./gitCommands.sh pull' ], shell=True)
	p.wait()

def gitCommit(message):
	p = subprocess.Popen(args=['./gitCommands.sh commit ' + message], shell=True)
	p.wait()

def gitAdd(files):
	p = subprocess.Popen(args=['./gitCommands.sh add ' + files], shell=True)
	p.wait()

def gitClone():
	p = subprocess.Popen(args=['./gitCommands.sh clone'],shell=True)
	p.wait()

def gitPush():
	p = subprocess.Popen(args=['./gitCommands.sh push'], shell=True)
	p.wait()

def gitBranch(branch_name):
	p = subprocess.Popen(args=['./gitCommands.sh branch ' + branch_name], shell=True)
	p.wait()

def gitCheckout(branch_name):
	p = subprocess.Popen(args=['./gitCommands.sh checkout ' + branch_name], shell=True)
	p.wait()

