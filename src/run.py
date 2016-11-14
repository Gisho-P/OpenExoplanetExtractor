#!/usr/bin/python3
import sys, getopt
import exoplanetEUreader
import NASAreader
import OECreader
sys.path.append('/system_classes')
import system

def run(argv):
    uflag = False
    rflag = False
    aflag = False
    eflag = False
    try:
        opts, args = getopt.getopt(argv, "u:r:a:e:", ["update=", "resolve=", "auto=", "email="])
    except getopt.GetoptError:
        print "run.py -u <repo name> -r <m/t> -a <#ofHours> -e <email Address>"
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
        elif opt in ("-e", "--email"):
            # add/ remove an email from the emailing list
            email_input = arg
            eflag = True

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
    if(eflag):
        # if email is already in mailing list remove it
        # otherwise add it
        # email list used to send report email after successful merge and
        # report if conflict emerged
        print("email : %s added/removed from mailing list" % (email_input))
        #TODO


    # run merge after options are set
    if(uflag):
        if repo_name in ("NASA", "Nasa", "nasa", "n"):
            print("Merging Open exoplanet Catalogue with NASA exoplanet Archive")
            other_repo = NASAreader.readNASA()
        elif repo_name in ("EU", "eu", "exoplanet.eu"):
            print("Merging Open exoplanet Catalogue with The Extrasolar Planets Encyclopaedia")
            other_repo = exoplanetEUreader.readExoplaneteu()
        # add new exoplanet repos/archives/catalogues here
        else:
            print("%s is not a recognised repository")

        if(other_repo is not None):
            # list of system objects from other repository
            other_systems = []
            # create system object from each dict
            for other_system_dict in other_repo:
                # convert to object
                other_system = System(other_system_dict)
                other_systems.push(other_system)
                # read oec system into object
                oec_system = searchForSys(other_system.mainName)
                # merge the two systems
                oec_system.update(other_system)
                updated_systems.push(oec_system)
            print(updated_systems)



if __name__ == "__main__":
    run(sys.argv[1:])