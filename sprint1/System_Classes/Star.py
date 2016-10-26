import Planet

class Star():

	def __init__(self, xml_dict):
        self.star_dict = xml_dict

        self.mag_R_error_minus = self.star_dict['magR']['@errorminus']
        self.mag_R_error_plus = self.star_dict['magR']['@errorplus']
