

function cloneRepo {
	mkdir systems
	cd systems
	git clone http://github.com/HarshilPatel12/Test.git
}

function pullRepo {

	git pull origin $2
}

function commitRepo {

	git commit -m "$2"
}

function pushRepo {

	git push origin $2
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
