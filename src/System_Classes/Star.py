import Planet

class Star():

    def __init__(self, star_dict):

        self.star_dict = star_dict

        initialize_star_dict_values()

        self.planets = []
        for planet in self.star_dict['planet']:
            temp_planet = Planet(planet)
            self.planets.append(temp_planet)


    def initialize_star_dict_values():
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

    def update(self, other):
        