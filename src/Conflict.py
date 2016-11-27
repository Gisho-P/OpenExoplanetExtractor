from configparser import ConfigParser

class Conflict:
    config = ConfigParser()
    config.read('config.ini')
    auto_resolve = config['DEFAULT']['Auto'].getboolean('on')
    resolve_mc = config['DEFAULT']['Conflict'].getboolean('mine')
    def resolve(path, value, my_conflict, their_conflict):
        if Conflict.isConflicting(my_conflict, their_conflict):
            if Conflict.auto_resolve:
                returnval = my_conflict if Conflict.resolve_mc else their_conflict
            else:
                print("Conflict found at: %s" % (path))
                print("My Conflict: %s = %s" % (value, my_conflict))
                print("Their Conflict: %s = %s" % (value, their_conflict))
                print("Please select an option(mc, tc, edit): ", end='')
                conflict_action = input()
                valid_input = False
                while (not valid_input):
                    if conflict_action == "mc":
                        returnval = my_conflict
                        valid_input = True
                    elif conflict_action == "tc":
                        returnval = their_conflict
                        valid_input = True
                    elif conflict_action == "edit":
                        print("Please enter a new value: ", end='')
                        returnval = input()
                        valid_input = True
                    else:
                        print("Please enter a valid option(mc, tc, edit): ", end='')
                        conflict_action = input()
        else:
            returnval = my_conflict
        return returnval


    def isConflicting(conflict1, conflict2):
        # more logic to be added in the future
        return conflict1 != conflict2
