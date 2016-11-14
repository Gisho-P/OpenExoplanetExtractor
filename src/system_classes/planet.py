
class Planet():

    def __init__(self, planet_dict):

        self.planet_dict = planet_dict

        self.initialize_planet_dict_values()


    def initialize_planet_dict_values(self):
        self.name = self.planet_dict['name']
        self.planet_list = self.planet_dict['list']

        # not sure if we need this one, since mass never has any text in it
        # self.mass = self.planet_dict['mass']
        # not every planet has all the properties, hence the try/excepts
        try:
            self.mass_upper_limit = self.planet_dict['mass']['@upperlimit']
        except Exception:
            self.mass_upper_limit = ''
        try:
            self.mass_error_minus = self.planet_dict['mass']['@errorminus']
        except Exception:
            self.mass_error_minus = ''
        try:
            self.mass_error_plus = self.planet_dict['mass']['@errorplus']
        except Exception:
            self.mass_error_plus = ''

        self.radius = self.planet_dict['radius']['#text']
        self.radius_error_minus = self.planet_dict['radius']['@errorminus']
        self.radius_error_plus = self.planet_dict['radius']['@errorplus']

        self.temperature = self.planet_dict['temperature']['#text']
        self.temperature_error_minus = self.planet_dict['temperature']
        ['@errorminus']
        self.temperature_error_plus = self.planet_dict['temperature']
        ['@errorplus']

        self.period = self.planet_dict['period']['#text']
        self.period_error_minus = self.planet_dict['period']['@errorminus']
        self.period_error_plus = self.planet_dict['period']['@errorplus']

        self.eccentricity = self.planet_dict['eccentricity']

        self.semi_major_axis = self.planet_dict['semimajoraxis']['#text']
        self.semi_major_axis_error_minus = self.planet_dict[
            'semimajoraxis']['@errorminus']
        self.semi_major_axis_error_plus = self.planet_dict[
            'semimajoraxis']['@errorplus']

        self.inclination = self.planet_dict['inclination']['#text']
        self.inclination_error_minus = self.planet_dict[
            'inclination']['@errorminus']
        self.inclination_error_plus = self.planet_dict[
            'inclination']['@errorplus']

        self.description = self.planet_dict['description']

        self.transit_time = self.planet_dict['transittime']['#text']
        self.transit_time_error_minus = self.planet_dict[
            'transittime']['@errorminus']
        self.transit_time_error_plus = self.planet_dict[
            'transittime']['@errorplus']

        self.is_transiting = self.planet_dict['istransiting']
        self.discovery_year = self.planet_dict['discoveryyear']

    def update(self, other, system_name, star_name):
        updates = []

        for prop, value in star_dict.items():
            if self.star_dict[prop] != other.star_dict[prop]:
                self.star_dict[prop] = Conflict.resolve(system_name + "/" + str(self.star_dict[
                    'name']), prop, self.star_dict[prop], other.star_dict[prop])
                updates.append([system_name, other.star_dict['name'], prop])

        return updates