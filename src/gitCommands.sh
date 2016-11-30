#!/bin/bash
if [ $1 = "clone" ]
then
	if [ -d "./systems" ] ;
	then
		cd ./systems/open_exoplanet_catalogue
		git pull https://a02f89cd8bca565ae600e30b1388bc57954e0a1a@github.com/T01test/open_exoplanet_catalogue.git
		exit
	else
		mkdir ./systems
		cd systems
		git clone https://a02f89cd8bca565ae600e30b1388bc57954e0a1a@github.com/T01test/open_exoplanet_catalogue.git
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
		git clone https://a02f89cd8bca565ae600e30b1388bc57954e0a1a@github.com/T01test/open_exoplanet_catalogue.git
	fi
	exit
fi



if [ $1 = "push" ]
then
	cd systems/open_exoplanet_catalogue/systems
	git push https://a02f89cd8bca565ae600e30b1388bc57954e0a1a@github.com/T01test/open_exoplanet_catalogue.git
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
	git add "$2.xml" 2> /dev/null
fi


if [ $1 = "branch" ]
then
	cd systems/open_exoplanet_catalogue
	git branch "$2"
	git checkout "$2"
	git push --set-upstream https://a02f89cd8bca565ae600e30b1388bc57954e0a1a@github.com/T01test/open_exoplanet_catalogue.git "$2"
fi


if [ $1 = "checkout" ]
then
	cd systems/open_exoplanet_catalogue
	git checkout "$2"
fi
