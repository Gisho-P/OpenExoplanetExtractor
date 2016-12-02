#!/bin/bash
if [ $1 = "clone" ]
then
	if [ -d "./systems/open_exoplanet_catalogue" ] ;
	then
		cd ./systems/open_exoplanet_catalogue
		git pull https://T01test:passorfail1@github.com/T01test/open_exoplanet_catalogue.git
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
 		cd systems/open_exoplanet_catalogue
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
	cd systems/open_exoplanet_catalogue/systems
	git push https://T01test:passorfail1@github.com/T01test/open_exoplanet_catalogue.git
	exit
fi





if [ $1 = "commit" ]
then
	cd systems/open_exoplanet_catalogue/
	git commit -m "$2"
	exit
fi



if [ $1 = "add" ]
then
	cd systems/open_exoplanet_catalogue/systems
	git add "$2.xml"
fi


if [ $1 = "branch" ]
then
	cd systems/open_exoplanet_catalogue
	git branch "$2"
	git checkout "$2"
	git push --set-upstream https://T01test:passorfail1@github.com/T01test/open_exoplanet_catalogue.git "$2"
fi


if [ $1 = "checkout" ]
then
	cd systems/open_exoplanet_catalogue
	git checkout "$2"
fi
