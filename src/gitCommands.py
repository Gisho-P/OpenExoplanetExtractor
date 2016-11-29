import subprocess


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

