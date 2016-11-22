from planet import *
import sys
sys.path.insert(0, '..')
from Conflict import *

class Star():

    def __init__(self, star_dict):

        self.star_dict = star_dict

    '''(Star, Star) -> list(list(string))
    Takes another System and compares the values and updates it to other's
    values.
    Returns a list of all the updated values
    '''
    def update(self, other, system_name):
        updates = []
        for prop, value in self.star_dict.items():
            if prop != 'planet':
                if self.star_dict[prop] != other.star_dict[prop]:
                    self.star_dict[prop] = other.star_dict[prop]# Conflict.resolve(
                        # system_name + "/" + str(self.star_dict[
                        #   'name']), prop, self.star_dict[
                        #        prop], other.star_dict[prop])
                    updates.append([system_name, other.star_dict['name'], prop])
            # dealing with planets
            else:
                if isinstance(self.star_dict['planet'], list):
                    for i, planet in enumerate(self.star_dict['planet']):
                        planet_A = Planet(planet)
                        planet_B = Planet(other.star_dict['planet'][i])
                        planet_updates = planet_A.update(
                            planet_B, system_name, other.star_dict['name'])
                        updates += planet_updates
                else:
                    planet_A = Planet(self.system_dict['system']['star'])
                    planet_B = Planet(other.system_dict['system']['star'])
                    updates += planet_A.update(planet_B,
                                               system_name, other.star_dict[
                                                   'name'])
        
        return updates
