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
        self.mag_R = self.star_dict['magR']['#text']

        self.mag_I_error_minus = self.star_dict['magI']['@errorminus']
        self.mag_I_error_plus = self.star_dict['magI']['@errorplus']
        self.mag_I = self.star_dict['magI']['#text']

        self.mag_H_error_minus = self.star_dict['magH']['@errorminus']
        self.mag_H_error_plus = self.star_dict['magH']['@errorplus']
        self.mag_H = self.star_dict['magH']['#text']

        self.mag_K_error_minus = self.star_dict['magK']['@errorminus']
        self.mag_K_error_plus = self.star_dict['magK']['@errorplus']
        self.mag_K = self.star_dict['magK']['#text']

        self.name = self.star_dict['name']
        self.mass = self.star_dict['mass']['#text']
        self.mass_error_minus = self.star_dict['mass']['@errorminus']
        self.mass_error_plus = self.star_dict['mass']['@errorplus']

        self.radius = self.star_dict['radius']
        self.radius_error_minus = self.star_dict['radius']['@errorminus']
        self.radius_error_plus = self.star_dict['radius']['@errorplus']

        self.temperature = self.star_dict['temperature']['#text']
        self.temperature_error_minus = self.star_dict[
            'temperature']['@errorminus']
        self.temperature_error_plus = self.star_dict[
            'temperature']['@errorplus']

        self.mag_J = self.star_dict['magJ']['#text']
        self.mag_J_error_minus = self.star_dict['magJ']['@errorminus']
        self.mag_J_error_plus = self.star_dict['magJ']['@errorplus']

        self.age = self.star_dict['age']

        self.metallicity = self.star_dict['metallicity']['#text']
        self.metallicity_error_minus = self.star_dict[
            'metallicity']['@errorminus']
        self.metallicity_error_plus = self.star_dict[
            'metallicity']['@errorplus']

        self.spectral_type = self.star_dict['spectraltype']

    '''(Star, Star) -> list(list(string))
    Takes another System and compares the values and updates it to other's
    values.
    Returns a list of all the updated values
    '''
    def update(self, other, system_name):
        updates = []
        updates += self.update_star_values(other, system_name)
        
        for i, planet in enumerate(self.planets):
            updates += planet.update(other.planets[i],
                                     system_name, self.star_dict['name'])
        
        return updates

    def update_star_values(self, other, system_name):
        updates = []
        if not self.mag_R_error_minus == other.mag_R_error_minus:
            updates.append([system_name, self.star_dict[
                'name'], 'magR', '@errorminus'])
        if not self.mag_R_error_plus == other.mag_R_error_plus:
            updates.append([system_name, self.star_dict[
                'name'], 'magR', '@errorplus'])
        if not self.mag_R == other.mag_R:
            updates.append([system_name, self.star_dict['name'], 'magR'])

        if not self.mag_I_error_minus == other.mag_I_error_minus:
            updates.append([system_name, self.star_dict[
                'name'], 'magI', '@errorminus'])
        if not self.mag_I_error_plus == other.mag_I_error_plus:
            updates.append([system_name, self.star_dict[
                'name'], 'magI', '@errorplus'])
        if not self.mag_I == other.mag_I:
            updates.append([system_name, self.star_dict['name'], 'magI'])

        if not self.mag_H_error_minus == other.mag_H_error_minus:
            updates.append([system_name, self.star_dict[
                'name'], 'magH', '@errorminus'])
        if not self.mag_H_error_plus == other.mag_H_error_plus:
            updates.append([system_name, self.star_dict[
                'name'], 'magH', '@errorplus'])
        if not self.mag_H == other.mag_H:
            updates.append([system_name, self.star_dict['name'], 'magH'])

        if not self.mag_K_error_minus == other.mag_K_error_minus:
            updates.append([system_name, self.star_dict[
                'name'], 'magK', '@errorminus'])
        if not self.mag_K_error_plus == other.mag_K_error_plus:
            updates.append([system_name, self.star_dict[
                'name'], 'magK', '@errorplus'])
        if not self.mag_K == other.mag_K:
            updates.append([system_name, self.star_dict['name'], 'magK'])

        if not self.name == other.name:
            updates.append([system_name, self.star_dict['name']])

        if not self.mass == other.mass:
            updates.append([system_name, self.star_dict['name'], 'mass'])
        if not self.mass_error_minus == other.mass_error_minus:
            updates.append([system_name, self.star_dict[
                'name'], 'mass', '@errorminus'])
        if not self.mass_error_plus == other.mass_error_plus:
            updates.append([system_name, self.star_dict[
                'name'], 'mass', '@errorplus'])

        if not self.radius == other.radius:
            updates.append([system_name, self.star_dict['name'], 'radius'])
        if not self.radius_error_minus == other.radius_error_minus:
            updates.append([system_name, self.star_dict[
                'name'], 'radius', '@errorminus'])
        if not self.radius_error_plus == other.radius_error_plus:
            updates.append([system_name, self.star_dict[
                'name'], 'radius', '@errorplus'])

        if not self.temperature == other.temperature:
            updates.append([system_name, self.star_dict[
                'name'], 'temperature'])
        if not self.temperature_error_minus == other.temperature_error_minus:
            updates.append([system_name, self.star_dict[
                'name'], 'temperature', '@errorminus'])
        if not self.temperature_error_plus == other.temperature_error_plus:
            updates.append([system_name, self.star_dict[
                'name'], 'temperature', '@errorplus'])

        if not self.mag_J == other.mag_J:
            updates.append([system_name, self.star_dict['name'], 'magJ'])
        if not self.mag_J_error_minus == other.mag_J_error_minus:
            updates.append([system_name, self.star_dict[
                'name'], 'magJ', '@errorminus'])
        if not self.mag_J_error_plus == other.mag_J_error_plus:
            updates.append([system_name, self.star_dict[
                'name'], 'magJ', '@errorplus'])

        if not self.age == other.age:
            updates.append([system_name, self.star_dict['name'], 'age'])

        if not self.metallicity == other.metallicity:
            updates.append([system_name, self.star_dict[
                'name'], 'metallicity'])
        if not self.metallicity_error_minus == other.metallicity_error_minus:
            updates.append([system_name, self.star_dict[
                'name'], 'metallicity', '@errorminus'])
        if not self.metallicity_error_plus == other.metallicity_error_plus:
            updates.append([system_name, self.star_dict[
                'name'], 'metallicity', '@errorplus'])

        if not self.spectral_type == other.spectral_type:
            updates.append([system_name, self.star_dict[
                'name'], 'spectraltype'])
        return updates
