
class Planet():

    def __init__(self, planet_dict):

        self.planet_dict = planet_dict

        self.initialize_planet_dict_values()


    def initialize_planet_dict_values(self):
        self.name = self.planet_dict['name']
        self.planet_list = self.planet_dict['list']

        self.mass = self.planet_dict['mass']
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

    def update(self, other, system_name, star_name):
        updates = []

        if not self.name == other.name:
            updates.append([system_name, star_name, self.planet_dict['name']])
        if not self.planet_list == self.planet_list:
            updates.append([system_name, star_name, self.planet_dict[
                'name'], 'list'])

        if not self.mass == self.planet_dict['mass']:
            updates.append([system_name, star_name, self.planet_dict[
                'name'], 'mass'])
        try:
            if not self.mass_error_minus == self.planet_dict[
                'mass']['@errorminus']:
                updates.append([system_name, star_name, self.planet_dict[
                    'name'], 'mass', '@errorminus'])
        except Exception:
            pass

        try:
            if not self.mass_error_minus == self.planet_dict[
                'mass']['@errorplus']:
                updates.append([system_name, star_name, self.planet_dict[
                    'name'], 'mass', '@errorplus'])
        except Exception:
            pass

        if not self.radius == other.radius:
            updates.append([system_name, star_name, self.planet_dict[
                'name'], 'radius'])

        if not self.radius_error_minus == other.radius_error_minus:
            updates.append([system_name, star_name, self.planet_dict[
                'name'], 'radius', '@errorminus'])

        if not self.radius_error_plus == other.radius_error_plus:
            updates.append([system_name, star_name, self.planet_dict[
                'name'], 'radius', '@errorplus'])

        if not self.temperature == other.temperature:
            updates.append([system_name, star_name, self.planet_dict[
                'name'], 'temperature'])

        if not self.temperature_error_minus == other.temperature_error_minus:
            updates.append([system_name, star_name, self.planet_dict[
                'name'], 'temperature', '@errorminus'])

        if not self.temperature_error_plus == self.temperature_error_plus:
            updates.append([system_name, star_name, self.planet_dict[
                'name'], 'temperature', '@errorplus'])

        if not self.period == self.period:
            updates.append([system_name, star_name, self.planet_dict[
                'name'], 'period'])

        if not self.period_error_minus == other.period_error_minus:
            updates.append([system_name, star_name, self.planet_dict[
                'name'], 'period', '@errorminus'])

        if not self.period_error_plus == self.period_error_plus:
            updates.append([system_name, star_name, self.planet_dict[
                'name'], 'period', '@errorplus'])

        if not self.eccentricity == other.eccentricity:
            updates.append([system_name, star_name, self.planet_dict[
                'name'], 'eccentricity'])

        if not self.semi_major_axis == other.semi_major_axis:
            updates.append([system_name, star_name, self.planet_dict[
                'name'], 'semimajoraxis'])

        if not self.semi_major_axis_error_minus == other.semi_major_axis_error_minus:
            updates.append([system_name, star_name, self.planet_dict[
                'name'], 'semimajoraxis', '@errorminus'])

        if not self.semi_major_axis_error_plus == other.semi_major_axis_error_plus:
            updates.append([system_name, star_name, self.planet_dict[
                'name'], 'semimajoraxis', '@errorplus'])

        if not self.inclination == other.inclination:
            updates.append([system_name, star_name, self.planet_dict[
                'name'], 'inclination'])

        if not self.inclination_error_minus == other.inclination_error_minus:
            updates.append([system_name, star_name, self.planet_dict[
                'name'], 'inclination', '@errorminus'])

        if not self.inclination_error_plus == other.inclination_error_plus:
            updates.append([system_name, star_name, self.planet_dict[
                'name'], 'inclination', '@errorplus'])

        if not self.description == other.description:
            updates.append([system_name, star_name, self.planet_dict[
                'name'], 'description'])

        if not self.transit_time == other.transit_time:
            updates.append([system_name, star_name, self.planet_dict[
                'name'], 'transittime'])

        if not self.transit_time_error_minus == other.transit_time_error_minus:
            updates.append([system_name, star_name, self.planet_dict[
                'name'], 'transittime', '@errorminus'])

        if not self.transit_time_error_plus == other.transit_time_error_plus:
            updates.append([system_name, star_name, self.planet_dict[
                'name'], 'transittime', '@errorplus'])

        if not self.is_transiting == other.is_transiting:
            updates.append([system_name, star_name, self.planet_dict[
                'name'], 'istransiting'])

        if not self.discovery_year == other.discovery_year:
            updates.append([system_name, star_name, self.planet_dict[
                'name'], 'discoveryyear'])
        return updates
