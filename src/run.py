#!/usr/bin/python3
import sys, getopt
import datetime
from gitCommands import *
import exoplanetEUreader
import NASAreader
import OECreader
sys.path.append('/system_classes')
from system import *

def run(argv):
    uflag = rflag = aflag = False
    try :
        (opts, args) = getopt.getopt(argv, "u:r:a:", ["update=", "resolve=", "auto="])
    except getopt.GetoptError:
        print("run.py -u <repo name/all> -r <m/t> -a <#ofHours>")
    # read command line arguments
    for opt, arg in opts:
        if opt in ("-u", "--update"):
            # run merge functionality on give repo name
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


    if(rflag):
        # set resolve value and save to config file
        if resolve_input == "m":
            print("Auto resolve set to my conflict")
            # TODO
        elif resolve_input == "t":
            print("Auto resolve set to their conflict")
            # TODO
        else:
            print("%s is not a recognised option" % (resolve_input))


    if(aflag):
        # set how often the program will auto run
        print("The merge will run every %s hours" % (auto_resolve_input))
        # TODO


    # run merge after options are set
    if(uflag):
        ext_repo = []
        if repo_name in ("NASA", "Nasa", "nasa", "n"):
            print("Merging Open exoplanet Catalogue with NASA exoplanet Archive")
            ext_repo = NASAreader.readNASA()
        elif repo_name in ("EU", "eu", "exoplanet.eu"):
            print("Merging Open exoplanet Catalogue with The Extrasolar Planets Encyclopaedia")
            ext_repo = exoplanetEUreader.readExoplaneteu()
        elif repo_name in ("all", "All", "ALL"):
            print("Merging with all repositories")
            ext_repo = NASAreader.readNASA()
            ext_repo.update(exoplanetEUreader.readExoplaneteu())
            # append other repos here
        # add new exoplanet repos/archives/catalogues here
        else:
            print("%s is not a recognised repository" % (repo_name))

        if(ext_repo is not None):
            numUpdated = numAdded = 0
            update_log = []
            gitClone()
            branch_name = '{:%Y-%b-%d %H}'.format(datetime.datetime.now())
            gitBranch(branch_name)


            # create system object from each dict
            for ext_system_dict in ext_repo:
                system_updated = False
                oec_system_updates = []
                # convert to object
                ext_system = System(ext_system_dict)
                # read oec system into object
                (oec_name, oec_system) = readSystem(ext_system.getName())



                if(oec_system is not None):
                    # if it exists updated it
                    system_updated = True
                    oec_system_updates = oec_system.update(ext_system)
                    update_log.extend(oec_system_updates)
                    if len(oec_system_updates) != 0:
                        numUpdated += 1
                else:
                    # otherwise the system is added
                    oec_system = ext_system
                    oec_name = ext_system.getName()[0]
                    numAdded += 1

                writeSystem(oec_name, oec_system)

                # if file created or changed
                if((oec_system is None) or len(oec_system_updates) != 0):
                    gitAdd(oec_name)

            commit_message = "%s: update| Updated %d systems | Added %d systems" % (
                '{:%Y-%b-%d}'.format(datetime.datetime.now()),
                numUpdated, numAdded)
            gitCommit(commit_message)
            gitPush()



if __name__ == "__main__":
    run(sys.argv[1:])
