#!/usr/bin/python3
import sys, getopt
import exoplanetEUreader
import NASAreader
import OECreader
sys.path.append('/system_classes')
import system

def run(argv):
    uflag = rflag = aflag = False
    repo_name = []
    try:
        opts, args = getopt.getopt(argv, "u:r:a:", ["update=", "resolve=", "auto="])
    except getopt.GetoptError:
        print("run.py -u <repo name/all> -r <m/t> -a <#ofHours>")
    # read command line arguments
    for opt, arg in opts:
        if opt in ("-u", "--update"):
            # run merge functionality on give repo url
            repo_name = arg
            uflag = True
        elif opt in ("-r", "--resolve"):
            # set value for auto resolving
            resolve_input = arg
            rflag = True
        elif opt in ("-a", "--auto"):
            # set how often the program will automatically run
            auto_resolve_input = arg
            aflag = True


    # handle configuration command options first
    if(rflag):
        # set resolve value and save to config file
        if resolve_input == "m":
            print("Auto resolve set to my conflict")
            # TODO
        elif resolve_input == "t":
            print("Auto resolve set to their conflict")
            # TODO
        else:
            print("%s is not a recognised option")


    if(aflag):
        # set how often the program will auto run
        print("The merge will run every %s hours" % (auto_resolve_input))
        # TODO


    # run merge after options are set
    if(uflag):
        print(repo_name)
        if repo_name in ("NASA", "Nasa", "nasa", "n"):
            print("Merging Open exoplanet Catalogue with NASA exoplanet Archive")
            ext_repo = NASAreader.readNASA()
        elif repo_name in ("EU", "eu", "exoplanet.eu"):
            print("Merging Open exoplanet Catalogue with The Extrasolar Planets Encyclopaedia")
            ext_repo = exoplanetEUreader.readExoplaneteu()
        elif: repo_name in ("all", "All", "ALL"):
        	print("Merging with all repositories")
        	ext_repo = NASAreader.readNASA()
        	ext_repo.update(exoplanetEUreader.readExoplaneteu())
        	# append other repos here
        # add new exoplanet repos/archives/catalogues here
        else:
            print("%s is not a recognised repository" % (repo_name))

        if(ext_repo is not None):
        	# gitClone()
            # list of system objects from other repository
            ext_repo = []
            update_log = []
            # create system object from each dict
            for ext_system_dict in ext_repo:
            	system_updated = False
                # convert to object
                ext_system = System(ext_system_dict)
                ext_systems.append(ext_system)
                # read oec system into object
                oec_system = readSystem(ext_system.system_dict[name][0])
                if(oec_system is not None):
                	#merge the two
                	system_updated = True
                	update_log.append(oec_system.update(ext_system))

                writeSystem(oec_system)
                # addFile(path)
			#gitPush()



if __name__ == "__main__":
    run(sys.argv[1:])