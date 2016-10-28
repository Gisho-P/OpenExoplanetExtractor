
class Planet():

    def __init__(self, planet_dict):

        self.planet_dict = planet_dict

        initialize_planet_dict_values()


    def initialize_planet_dict_values():
        self.name = self.planet_dict['name']
        self.planet_list = self.planet_dict['list']

        self.mass = self.planet_dict['mass']
        self.mass_error_minus = self.planet_dict['mass']['@errorminus']
        self.mass_error_plus = self.planet_dict['mass']['@errorplus']

        self.radius = self.planet_dict['radius']
        self.radius_error_minus = self.planet_dict['radius']['@errorminus']
        self.radius_error_plus = self.planet_dict['radius']['@errorplus']

        self.temperature = self.planet_dict['temperature']
        self.temperature_error_minus = self.planet_dict['temperature']
        ['@errorminus']
        self.temperature_error_plus = self.planet_dict['temperature']
        ['@errorplus']

        self.period = self.planet_dict['period']
        self.period_error_minus = self.planet_dict['period']['@errorminus']
        self.period_error_plus = self.planet_dict['period']['@errorplus']

        self.eccentricity = self.planet_dict['eccentricity']

        self.semi_major_axis = self.planet_dict['semimajoraxis']
        self.semi_major_axis_error_minus = self.planet_dict['semimajoraxis']
        ['@errorminus']
        self.semi_major_axis_error_plus = self.planet_dict['semimajoraxis']
        ['@errorplus']

        self.inclination = self.planet_dict['inclination']
        self.inclination_error_minus = self.planet_dict['inclination']
        ['@errorminus']
        self.inclination_error_plus = self.planet_dict['inclination']
        ['@errorplus']

        self.description = self.planet_dict['description']

        self.transit_time = self.planet_dict['transittime']
        self.transit_time_error_minus = self.planet_dict['transittime']
        ['@errorminus']
        self.transit_time_error_plus = self.planet_dict['transittime']
        ['@errorplus']

        self.is_transiting = self.planet_dict['istransiting']
        self.discovery_year = self.planet_dict['discoveryyear']