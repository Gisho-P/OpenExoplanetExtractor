import collections
from star import *
import sys
sys.path.insert(0, '..')
from Conflict import *

class System():

    '''(System, Dictionary) -> NoneType
    Initialises the System object, which also initialises the Star
    and Planet objects.
    Requires the dictionary representation of a System
    '''
    def __init__(self, system_dict):

        self.system_dict = system_dict

    '''(System, System) -> list(list(string))
    Takes another System and compares the values and updates it to other's
    values.
    Returns a list of all the updated values
    '''
    def update(self, other):

        updates = []

        system_A = self.system_dict['system']
        system_B = other.system_dict['system']
        for prop, value in self.system_dict['system'].items():
            if prop != 'star':
                if system_A[prop] != system_B[prop]:
                    system_A[prop] = system_B[prop]# Conflict.resolve(system_A[
                        # 'name'], prop, system_A[prop], system_B[prop])
                    updates.append([other.system_dict['system']['name'], prop])
            # dealing with stars
            else:
                if isinstance(self.system_dict['system']['star'], list):
                    for i, star in enumerate(self.system_dict['system']['star']):
                        star_A = Star(star)
                        star_B = Star(other.system_dict['system']['star'][i])
                        star_updates = star_A.update(star_B, self.system_dict[
                                                         'system']['name'])
                        updates += star_updates
                else:
                    star_A = Star(self.system_dict['system']['star'])
                    star_B = Star(other.system_dict['system']['star'])
                    updates += star_A.update(star_B, self.system_dict[
                                                         'system']['name'])
        return updates
