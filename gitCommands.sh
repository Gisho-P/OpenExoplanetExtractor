#!/bin/bash
if [ $1 = "clone" ]
then
	if [ -d ./systems ]
	then
		cd systems/Test
		git pull
		exit
	else
		mkdir ./systems
		cd systems
		git clone https://HarshilPatel12:harshilpatel1@github.com/HarshilPatel12/Test.git
		exit
	fi
	exit
fi

if [ $1 = "pull" ]
then
	if [ -d ./systems ]
	then
		git pull
	else
		mkdir ./systems
		cd systems
		git clone https://HarshilPatel12:harshilpatel1@github.com/HarshilPatel12/Test.git
	fi
	exit
fi



if [ $1 = "push" ]
then
	git push https://HarshilPatel12:harshilpatel1@github.com/HarshilPatel12/Test.git
	exit
fi





if [ $1 = "commit" ]
then
	cd systems/Test
	git commit -m "'"$2"'"
	exit
fi






if [ $1 = "add" ]
then
	if [ $2 = '.' ]
	then
		cd systems/Test
		git add $2
	else
		shift
		cd systems/Test
		for i in $*
		do
			git add $i
		done
	fi
fi
