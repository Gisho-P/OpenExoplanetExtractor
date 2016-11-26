#!/bin/bash
if [ $1 = "clone" ]
then
	if [ -d ./systems ]
	then
		cd ./systems
		git pull
		exit
	else
		mkdir ./systems
		cd systems
		git clone https://T01test:passorfail1@github.com/T01test/open_exoplanet_catalogue.git
		exit
	fi
	exit
fi

if [ $1 = "pull" ]
then
	if [ -d ./systems ]
	then
 		cd systems
		git pull
	else
		mkdir ./systems
		cd systems
		git clone https://T01test:passorfail1@github.com/T01test/open_exoplanet_catalogue.git
	fi
	exit
fi



if [ $1 = "push" ]
then
	cd ./systems
	git push https://T01test:passorfail1@github.com/T01test/open_exoplanet_catalogue.git
	exit
fi





if [ $1 = "commit" ]
then
	cd systems
	message=""
	shift
	for i in $*
	do
		message=$message" "$i
	done
	git commit -m "$message"
	exit
fi






if [ $1 = "add" ]
then
	if [ $2 = '.' ]
	then
		cd systems
		git add $2
	else
		shift
		cd systems
		for i in $*
		do
			git add $i
		done
	fi
fi

if [ $1 = "branch" ]
then
	cd systems
	git branch $2
	git checkout $2
	git push https://T01test:passorfail1@github.com/T01test/open_exoplanet_catalogue.git $2
fi

if [ $1 = "checkout" ]
then
	cd systems
	git checkout $2
fi
