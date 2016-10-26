import xmltodict
import urllib
import dicttoxml
import collections
import Star

class Systems():

    def __init__(self, url):
    	data = urllib.request.urlopen(url).read().decode('utf-8')

    	self.system_dict = xmltodict.parse(data, dict_constructor=dict)

    	initialize_system_xml_values()

    	self.stars = []
    	for star in self.system_dict['system']['star']:
    		temp_star = Star(star)
    		self.stars.append(temp_star)


    def initialize_system_xml_values():
    	self.name = self.system_dict['system']['name']
    	self.right_ascension = self.system_dict['system']['rightascension']
    	self.declination = self.system_dict['system']['declination']
    	self.distance_error_minus = self.system_dict['system']['distance']['@errorminus']
    	self.distance_error_plus = self.system_dict['system']['distance']['@errorplus']