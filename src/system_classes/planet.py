
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

    def update(self, other, system_name, star_name):
        updates = []

        if self.name == self.planet_dict['name']:
            updates.append([system_name, star_name, self.planet_dict['name']])
        if self.planet_list == self.planet_dict['list']:
            updates.append([system_name, star_name, self.planet_dict[
                'name'], 'list'])

        if self.mass == self.planet_dict['mass']:
            updates.append([system_name, star_name, self.planet_dict['name'], 'mass'])

        if self.mass_error_minus == self.planet_dict['mass']['@errorminus']:
            updates.append([system_name, star_name, self.planet_dict[
                'name'], 'mass', '@errorminus'])

        if self.mass_error_plus == self.planet_dict['mass']['@errorplus']:
            updates.append([system_name, star_name, self.planet_dict[
                'name'], 'mass', '@errorplus']

        if self.radius == self.planet_dict['radius']:
            updates.append([system_name, star_name, self.planet_dict['name'], 'radius'])

        if self.radius_error_minus == self.planet_dict['radius']['@errorminus']:
            updates.append([system_name, star_name, self.planet_dict[
                'name'], 'radius', '@errorminus']

        if self.radius_error_plus == self.planet_dict['radius']['@errorplus']:
            updates.append([system_name, star_name, self.planet_dict[
                'name'], 'radius', '@errorplus'])

        if self.temperature == self.planet_dict['temperature']:
            updates.append([system_name, star_name, self.planet_dict['name'], 'temperature'])

        if self.temperature_error_minus == self.planet_dict[
            'temperature']['@errorminus']:
            updates.append([system_name, star_name, self.planet_dict[
                'name'], 'temperature', '@errorminus'])

        if self.temperature_error_plus == self.planet_dict[
            'temperature']['@errorplus']:
            updates.append([system_name, star_name, self.planet_dict[
                'name'], 'temperature', '@errorplus'])

        if self.period == self.planet_dict['period']:
            updates.append([system_name, star_name, self.planet_dict['name'], 'period'])

        if self.period_error_minus == self.planet_dict[
            'period']['@errorminus']:
            updates.append([system_name, star_name, self.planet_dict[
                'name'], 'period', '@errorminus'])

        if self.period_error_plus == self.planet_dict['period']['@errorplus']:
            updates.append([system_name, star_name, self.planet_dict[
                'name'], 'period', '@errorplus']

        if self.eccentricity == self.planet_dict['eccentricity']:
            updates.append([system_name, star_name, self.planet_dict['name'], 'eccentricity'])

        if self.semi_major_axis == self.planet_dict['semimajoraxis']:
            updates.append([system_name, star_name, self.planet_dict['name'], 'semimajoraxis'])

        if self.semi_major_axis_error_minus == self.planet_dict[
            'semimajoraxis']['@errorminus']:
            updates.append([system_name, star_name, self.planet_dict[
                'name'], 'semimajoraxis', '@errorminus'])

        if self.semi_major_axis_error_plus == self.planet_dict[
            'semimajoraxis']['@errorplus']:
            updates.append([system_name, star_name, self.planet_dict[
                'name'], 'semimajoraxis', '@errorplus'])

        if self.inclination == self.planet_dict['inclination']:
            updates.append([system_name, star_name, self.planet_dict[
                'name'], 'inclination'])

        if self.inclination_error_minus == self.planet_dict[
            'inclination']['@errorminus']:
            updates.append([system_name, star_name, self.planet_dict[
                'name'], 'inclination', '@errorminus'])

        if self.inclination_error_plus == self.planet_dict[
            'inclination']['@errorplus']:
            updates.append([system_name, star_name, self.planet_dict[
                'name'], 'inclination', '@errorplus'])

        if self.description == self.planet_dict['description']:
            updates.append([system_name, star_name, self.planet_dict[
                'name'], 'description'])

        if self.transit_time == self.planet_dict['transittime']:
            updates.append([system_name, star_name, self.planet_dict[
                'name'], 'transittime'])

        if self.transit_time_error_minus == self.planet_dict[
            'transittime']['@errorminus']:
            updates.append([system_name, star_name, self.planet_dict[
                'name'], 'transittime', '@errorminus'])

        if self.transit_time_error_plus == self.planet_dict[
            'transittime']['@errorplus']:
            updates.append([system_name, star_name, self.planet_dict[
                'name'], 'transittime', '@errorplus'])

        if self.is_transiting == self.planet_dict['istransiting']:
            updates.append([system_name, star_name, self.planet_dict[
                'name'], 'istransiting'])

        if self.discovery_year == self.planet_dict['discoveryyear']:
            updates.append([system_name, star_name, self.planet_dict[
                'name'], 'discoveryyear'])
        return updates