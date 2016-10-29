import collections
import Star

class System():

    '''(System, Dictionary) -> NoneType
    Initialises the System object, which also initialises the Star
    and Planet objects.
    Requires the dictionary representation of a System
    '''
    def __init__(self, system_dict):
	
	self.system_dict = system_dict

    	initialize_system_dict_values()

    	self.stars = []
    	for star in self.system_dict['system']['star']:
	    temp_star = Star(star)
	    self.stars.append(temp_star)


    def initialize_system_dict_values():
    	self.name = self.system_dict['system']['name']
    	self.right_ascension = self.system_dict['system']['rightascension']
    	self.declination = self.system_dict['system']['declination']
    	self.distance_error_minus = self.system_dict['system'][
	    'distance']['@errorminus']
    	self.distance_error_plus = self.system_dict['system'][
	    'distance']['@errorplus']

	'''(System, System) -> list(list(string))
	Takes another System and compares the values and updates it to other's
	values.
	Returns a list of all the updated values
	'''
	def update(self, other):

	    updates = update_system_values(other)
    
	    for star in self.star():
		star_updates = self.star.update()
		updates += star_updates

	    return updates


	def update_system_values(other):
	    updates = []
	    if not self.name == other.name:
		updates.add(['system', 'name'])

	    if not self.right_ascension == other.right_ascension:
		updates.add(['system', 'rightascension'])

	    if not self.declination == other.declination:
		updates.add['system', 'declination']

	    if not self.distance_error_minus == other.distance_error_minus:
		updates.add(['system', 'distance', '@errorminus'])

	    if not self.distance_error_plus == other.distance_error_plus:
		updates.add(['system', 'distance', '@errorplus'])
