from planet import *

class Star():

    def __init__(self, star_dict):

        self.star_dict = star_dict

        self.initialize_star_dict_values()

        # case if there are multiple planets
        if isinstance(self.star_dict['planet'], list):
            self.planets = []
            for planet in self.star_dict['planet']:
                temp_planet = Planet(planet)
                self.planets.append(temp_planet)
        else:
            self.planets = Planet(self.star_dict['planet'])

    def initialize_star_dict_values(self):
        self.mag_R_error_minus = self.star_dict['magR']['@errorminus']
        self.mag_R_error_plus = self.star_dict['magR']['@errorplus']
        self.mag_R = self.star_dict['magR']

        self.mag_I_error_minus = self.star_dict['magI']['@errorminus']
        self.mag_I_error_plus = self.star_dict['magI']['@errorplus']
        self.mag_I = self.star_dict['magI']

        self.mag_H_error_minus = self.star_dict['magH']['@errorminus']
        self.mag_H_error_plus = self.star_dict['magH']['@errorplus']
        self.mag_H = self.star_dict['magH']

        self.mag_K_error_minus = self.star_dict['magK']['@errorminus']
        self.mag_K_error_plus = self.star_dict['magK']['@errorplus']
        self.mag_K = self.star_dict['magK']

        self.name = self.star_dict['name']
        self.mass = self.star_dict['mass']
        self.mass_error_minus = self.star_dict['mass']['@errorminus']
        self.mass_error_plus = self.star_dict['mass']['@errorplus']

        self.radius = self.star_dict['radius']
        self.radius_error_minus = self.star_dict['radius']['@errorminus']
        self.radius_error_plus = self.star_dict['radius']['@errorplus']

        self.temperature = self.star_dict['temperature']
        self.temperature_error_minus = self.star_dict['temperature']
        ['@errorminus']
        self.temperature_error_plus = self.star_dict['temperature']
        ['@errorplus']

        self.mag_J = self.star_dict['magJ']
        self.mag_J_error_minus = self.star_dict['magJ']['@errorminus']
        self.mag_J_error_plus = self.star_dict['magJ']['@errorplus']

        self.age = self.star_dict['age']

        self.metallicity = self.star_dict['metallicity']
        self.metallicity_error_minus = self.star_dict['metallicity']
        ['@errorminus']
        self.metallicity_error_plus = self.star_dict['metallicity']
        ['@errorplus']

        self.spectral_type = self.star_dict['spectraltype']

    '''(Star, Star) -> list(list(string))
    Takes another System and compares the values and updates it to other's
    values.
    Returns a list of all the updated values
    '''
    def update(self, other, system_name):

        updates = update_star_values(other)
        
        for i, planet in enumerate(self.planets):
            updates.update(planet.update(planet[i]), system_name, self.star_dict['name'])
        
        return updates

    def update_star_values(other):
        updates = []
        if not self.mag_R_error_minus == self.star_dict['magR']['@errorminus']:
            updates.append([system_name, self.star_dict['name'], 'magR', '@errorminus'])
        if not self.mag_R_error_plus == self.star_dict['magR']['@errorplus']:
            updates.append([system_name, self.star_dict['name'], 'magR', '@errorplus'])
        if not self.mag_R == self.star_dict['magR']:
            updates.append([system_name, self.star_dict['name'], 'magR'])

        if not self.mag_I_error_minus == self.star_dict['magI']['@errorminus']:
            updates.append([system_name, self.star_dict['name'], 'magI', '@errorminus'])
        if not self.mag_I_error_plus == self.star_dict['magI']['@errorplus']:
            updates.append([system_name, self.star_dict['name'], 'magI', '@errorplus'])
        if not self.mag_I == self.star_dict['magI']:
            updates.append([system_name, self.star_dict['name'], 'magI'])

        if not self.mag_H_error_minus == self.star_dict['magH']['@errorminus']:
            updates.append([system_name, self.star_dict['name'], 'magH', '@errorminus'])
        if not self.mag_H_error_plus == self.star_dict['magH']['@errorplus']:
            updates.append([system_name, self.star_dict['name'], 'magH', '@errorplus'])
        if not self.mag_H == self.star_dict['magH']:
            updates.append([system_name, self.star_dict['name'], 'magH'])

        if not self.mag_K_error_minus == self.star_dict['magK']['@errorminus']:
            updates.append([system_name, self.star_dict['name'], 'magK', '@errorminus'])
        if not self.mag_K_error_plus == self.star_dict['magK']['@errorplus']:
            updates.append([system_name, self.star_dict['name'], 'magK', '@errorplus'])
        if not self.mag_K == self.star_dict['magK']:
            updates.append([system_name, self.star_dict['name'], 'magK'])

        if not self.name == self.star_dict['name']:
            updates.append([system_name, self.star_dict['name']])

        if not self.mass == self.star_dict['mass']:
            updates.append([system_name, self.star_dict['name'], 'mass'])
        if not self.mass_error_minus == self.star_dict['mass']['@errorminus']:
            updates.append([system_name, self.star_dict['name'], 'mass', '@errorminus'])
        if not self.mass_error_plus == self.star_dict['mass']['@errorplus']:
            updates.append([system_name, self.star_dict['name'], 'mass', '@errorplus'])

        if not self.radius == self.star_dict['radius']:
            updates.append([system_name, self.star_dict['name'], 'radius'])
        if not self.radius_error_minus == self.star_dict['radius'][
            '@errorminus']:
            updates.append([system_name, self.star_dict['name'], 'radius', '@errorminus'])
        if not self.radius_error_plus == self.star_dict[
            'radius']['@errorplus']:
            updates.append([system_name, self.star_dict['name'], 'radius', '@errorplus'])

        if not self.temperature == self.star_dict['temperature']:
            updates.append([system_name, self.star_dict['name'], 'temperature'])
        if not self.temperature_error_minus == self.star_dict[
            'temperature']['@errorminus']:
            updates.append([system_name, self.star_dict['name'], 'temperature', '@errorminus'])
        if not self.temperature_error_plus == self.star_dict[
            'temperature']['@errorplus']:
            updates.append([system_name, self.star_dict['name'], 'temperature', '@errorplus'])

        if not self.mag_J == self.star_dict['magJ']:
            updates.append([system_name, self.star_dict['name'], 'magJ'])
        if not self.mag_J_error_minus == self.star_dict['magJ']['@errorminus']:
            updates.append([system_name, self.star_dict['name'], 'magJ', '@errorminus'])
        if not self.mag_J_error_plus == self.star_dict['magJ']['@errorplus']:
            updates.append([system_name, self.star_dict['name'], 'magJ', '@errorplus'])

        if not self.age == self.star_dict['age']:
            updates.append([system_name, self.star_dict['name'], 'age'])

        if not self.metallicity == self.star_dict['metallicity']:
            updates.append([system_name, self.star_dict['name'], 'metallicity'])
        if not self.metallicity_error_minus == self.star_dict[
            'metallicity']['@errorminus']:
            updates.append([system_name, self.star_dict['name'], 'metallicity', '@errorminus'])
        if not self.metallicity_error_plus == self.star_dict[
            'metallicity']['@errorplus']:
            updates.append([system_name, self.star_dict['name'], 'metallicity', '@errorplus'])

        if not self.spectral_type == self.star_dict['spectraltype']:
            updates.append([system_name, self.star_dict['name'], 'spectraltype'])