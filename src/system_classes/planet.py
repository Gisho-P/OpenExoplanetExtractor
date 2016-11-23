import sys
sys.path.insert(0, '..')
from Conflict import *

class Planet():

    def __init__(self, planet_dict):

        self.planet_dict = planet_dict

    def update(self, other, system_name, star_name):
        updates = []

        for prop, value in self.planet_dict.items():
            if self.planet_dict[prop] != other.planet_dict[prop]:
                self.planet[prop] = Conflict.resolve(
                    system_name + "/" + star_name + "/" + str(self.planet_dict[
                        'name']), prop, self.planet_dict[
                            prop],other.planet_dict[prop])
                updates.append([system_name, star_name, other.planet_dict[
                    'name'], prop])

        return updates