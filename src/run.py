#!/usr/bin/python3

import sys, getopt
import datetime
from gitCommands import *
from exoplanetEUreader import *
from  NASAreader import *
from OECreader import *
sys.path.append('/system_classes')
from system import *
from configparser import ConfigParser

def run(argv):
    config = ConfigParser()
    config.read('config.ini')

    uflag = aflag = rflag = fflag = False
    try :
        (opts, args) = getopt.getopt(argv, "u:a:r:f:", ["update=", "auto=", "resolve=", "freq="])
    except getopt.GetoptError:
        print("run.py -u <repo name/all> -a <on/off> -r <m/t> -f <#ofHours>")
    # read command line arguments
    for opt, arg in opts:
        if opt in ("-u", "--update"):
            # run merge functionality on give repo name
            repo_name = arg
            uflag = True
        elif opt in ("-a", "--auto"):
            # set how often the program will automatically run
            auto_resolve_input = arg
            aflag = True
        elif opt in ("-r", "--resolve"):
            # set value for auto resolving
            resolve_input = arg
            rflag = True
        elif opt in ("-f", "--freq"):
            # set how often the program will automatically run
            run_frequency_input = arg
            fflag = True

    if(aflag):
        # set how often the program will auto run
        print("Auto resolve is %s" % (auto_resolve_input))
        config["DEFAULT"]["Auto"] = str(auto_resolve_input)

    if(rflag):
        # set resolve value and save to config file
        if resolve_input == "m":
            print("Auto resolve set to my conflict")
            config["DEFAULT"]["Conflict"] = "mine"
        elif resolve_input == "t":
            print("Auto resolve set to their conflict")
            config["DEFAULT"]["Conflict"] = "theirs"
        else:
            print("%s is not a recognised option" % (resolve_input))

    if(fflag):
        # set how often the program will auto run
        print("The merge will run every %s hours" % (run_frequency_input))
        config["DEFAULT"]["Frequency"] = str(run_frequency_input)

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

    # run merge after options are set
    if(uflag):
        ext_repo = []
        if repo_name in ("NASA", "Nasa", "nasa", "n"):
            print("Merging Open Exoplanet Catalogue with NASA exoplanet Archive")
            ext_repo = readNASA()
        elif repo_name in ("EU", "eu", "exoplanet.eu"):
            print("Merging Open Exoplanet Catalogue with The Extrasolar Planets Encyclopaedia")
            ext_repo = readExoplaneteu()
        elif repo_name in ("all", "All", "ALL"):
            print("Merging with all repositories")
            ext_repo = readNASA()
            ext_repo.update(readExoplaneteu())
            # append other repos here
        # add new exoplanet repos/archives/catalogues here
        else:
            print("%s is not a recognised repository" % (repo_name))

        if(ext_repo is not None):
            numChanged = 0
            update_log = []
            gitClone()
            branch_name = '{:%Y-%b-%d_%H.%M.%S}'.format(datetime.datetime.now())

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
                    oec_system_updates = oec_system.update(ext_system)
                    update_log.extend(oec_system_updates)
                    if len(oec_system_updates) != 0:
                        system_updated = True
                        numChanged += 1
                else:
                    # otherwise the system is added
                    oec_system = ext_system
                    oec_name = ext_system.getName()
                    numChanged += 1
                    system_updated = True

                writeSystem(oec_name, oec_system)

                # if file created or changed then git add the changes
                if system_updated:
                    gitAdd(oec_name)

            commit_message = "%s: update, Updated/Added %d systems" % (
                '{:%Y-%b-%d~%H:%M:%S}'.format(datetime.datetime.now()),
                numChanged)
        gitCommit(commit_message)
        gitPush()
        gitPullRequest(branch_name)
        print("Merge complete: %s"%commit_message)



if __name__ == "__main__":
    run(sys.argv[1:])
