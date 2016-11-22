function cloneRepo {
	if [ -d ./systems ]
	then
		cd systems
		git pull
		exit
	else
		mkdir ./systems
		cd systems
		git clone https://username:password@github.com/username/repoName.git
		exit
	fi
	exit
}

function pullRepo {

	if [ -d ./systems ]
	then
		git pull
	else
		mkdir ./systems
		cd systems
		git clone https://uername:password@github.com/username/repoName.git
	fi
	exit
}

function addFile {
	if [ $2 = "." ]
	then
		git add .
	else
		shift
		for i in $*
		do
			git add $i
		done
	fi
}

function commitRepo {

	cd systems
	git commit -m "$2"
	exit
}

function pushRepo {

	git push
	exit
}

if [ $1 = "clone" ]
then
	cloneRepo
fi

if [ $1 = "pull" ]
then
	pullRepo
fi

if [ $1 = "push" ]
then
	pushRepo
fi

if [ $1 = "commit" ]
then
	commitRepo
fi

if [ $1 = "add" ]
then
	addFile
fi
