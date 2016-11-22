import subprocess


def pull():
	subprocess.Popen(args=['./gitCommands.sh pull' ], shell=True)

def commit(message):
	subprocess.Popen(args=['./gitCommands.sh commit ' + message], shell=True)

def add(files):
	subprocess.Popen(args=['./gitCommands.sh add' + files], shell=True)

def clone():
	subprocess.Popen(args=['./gitCommands.sh clone'],shell=True)

def push():
	subprocess.Popen(args=['./gitCommands.sh push'], shell=True)

