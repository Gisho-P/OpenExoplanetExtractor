import urllib.request
import csv
from io import StringIO

# Extracts the list of exoplanets from the exoplanet.eu website and stores each individual system of planets into an individual dictionary,
# then returns a list of all the different systems in a dictionary
def readExoplaneteu():
    url = "http://exoplanet.eu/catalog/csv/"
    data = urllib.request.urlopen(url).read().decode('utf-8')
    reader = csv.DictReader(StringIO(data))
    data_dict = {}
    # Store the data from the csv file into a dict with the name as the key, and each attribute having a dictionary
    # with the respective attributes name as it's key
    for row in reader:
        key = row.pop('# name')
        data_dict[key] = row
    return mapAttributes(data_dict)

# Recursively searches through a dictionary and removes all empty key value pairs
def removeEmptyAttributes(catalog_dict):
    empty_attributes = set()
    # loop through all attributes
    for attr in catalog_dict:
        # If it's a value (i.e a string) then check that it's not empty
        if((type(catalog_dict[attr]) is str) and not catalog_dict[attr]):
            empty_attributes.add(attr)
        # If it's a dict, this indicates that we should recursively check this dict for empty values
        elif((type(catalog_dict[attr]) is dict)):
            catalog_dict[attr] = removeEmptyAttributes(catalog_dict[attr])
            if(not catalog_dict[attr]):
                empty_attributes.add(attr)
        # if it's a list, then check each element for if it's empty
        elif(type(catalog_dict[attr]) is list and attr != "planet"): # planet is initially empty but will be filled
            for element in catalog_dict[attr]:
                if element == "":
                    catalog_dict[attr].remove(element)
            if(len(catalog_dict[attr]) == 1):
                catalog_dict[attr] = catalog_dict[attr][0]
            if(not catalog_dict[attr]):
                empty_attributes.add(attr)
    # remove all empty attributes
    for attr in empty_attributes:
        catalog_dict.pop(attr)
    return catalog_dict

# Converts from degrees, to hms. Pass true for second arg if converting for right ascension
def dd2hms(dd, ra):
    deg = int(dd)
    if(ra):
        hr = deg * 24. / 360
    else:
        hr = deg
    mindec= (dd-deg) * 60
    min = int(mindec)
    sec = (mindec-min) * 60
    return str("%02d" % (int(hr)),) + " " + str("%02d" % (abs(min),)) + " " + str("%02d" % (abs(int(sec)),))

# Maps the values extracted from the EU sites exoplanets to the corresponding names in the OEC format to a dictionary
def mapAttributes(data_dict):
    found_stars = set()
    final_catalog = []
    systems = {}
    catalog = {}
    # For each unique star a system will be created
    # Then each planet will be added to the system of which star it corresponds to
    for planet_name in data_dict:
        if ((data_dict[planet_name]['star_name'] not in found_stars)):
            found_stars.add(data_dict[planet_name]['star_name'])
            catalog = {
               'name': data_dict[planet_name]['star_name'],
               'rightascension': dd2hms(float(data_dict[planet_name]['ra']), True),
               'declination': dd2hms(float(data_dict[planet_name]['dec']), False),
               'star':{
                  'temperature':{
                     '@errorplus': data_dict[planet_name]['star_teff_error_max'],
                     '@errorminus': data_dict[planet_name]['star_teff_error_min'],
                     '#text': data_dict[planet_name]['star_teff']
                  },
                  'age': data_dict[planet_name]['star_age'],
                  'name':[
                      data_dict[planet_name]['star_name'],
                      data_dict[planet_name]["star_alternate_names"]
                  ],
                  'magK':{
                     '#text': data_dict[planet_name]['mag_k']
                  },
                  'magI':{
                     '#text': data_dict[planet_name]['mag_i']
                  },
                  'radius':{
                     '@errorplus': data_dict[planet_name]['star_radius_error_max'],
                     '@errorminus': data_dict[planet_name]['star_radius_error_min'],
                     '#text': data_dict[planet_name]['star_radius']
                  },
                  'spectraltype': data_dict[planet_name]['star_sp_type'],
                  'mass':{
                     '@errorplus': data_dict[planet_name]['star_mass_error_max'],
                     '@errorminus': data_dict[planet_name]['star_mass_error_min'],
                     '#text': data_dict[planet_name]['star_mass']
                  },
                  'metallicity':{
                     '@errorplus': data_dict[planet_name]['star_metallicity_error_max'],
                     '@errorminus': data_dict[planet_name]['star_metallicity_error_min'],
                     '#text': data_dict[planet_name]['star_metallicity']
                  },
                  'magJ':{
                     '#text': data_dict[planet_name]['mag_j']
                  },
                  'magH':{
                     '#text': data_dict[planet_name]['mag_h']
                  },
                  'magV':{
                     '#text': data_dict[planet_name]['mag_v']
                  }
               },
               'distance':{
                  '@errorplus': data_dict[planet_name]['star_distance_error_max'],
                  '@errorminus': data_dict[planet_name]['star_distance_error_min'],
                  '#text': data_dict[planet_name]['star_distance']
               }
            }
            catalog["star"]["planet"] = []
            systems.update({data_dict[planet_name]['star_name'] : removeEmptyAttributes(catalog)})

        planet = {
                'transittime':{
                   '@errorplus': data_dict[planet_name]['tzero_tr_error_max'],
                   '#text': data_dict[planet_name]['tzero_tr'],
                   '@errorminus': data_dict[planet_name]['tzero_tr_error_min'],
                   '@unit':''
                },
                'lastupdate': data_dict[planet_name]['updated'],
                'temperature':{
                   '#text': data_dict[planet_name]['temp_calculated']
                },
                'discoveryyear': data_dict[planet_name]['discovered'],
                'period':{
                   '@errorplus': data_dict[planet_name]['orbital_period_error_max'],
                   '@errorminus': data_dict[planet_name]['orbital_period_error_min'],
                   '#text': data_dict[planet_name]['orbital_period']
                },
                'name':
                    planet_name
                ,
                'semimajoraxis':{
                   '@errorplus': data_dict[planet_name]['semi_major_axis_error_max'],
                   '@errorminus': data_dict[planet_name]['semi_major_axis_error_min'],
                   '#text': data_dict[planet_name]['semi_major_axis']
                },
                'radius':{
                   '@errorplus': data_dict[planet_name]['radius_error_max'],
                   '@errorminus': data_dict[planet_name]['radius_error_min'],
                   '#text': data_dict[planet_name]['radius']
                },
                'eccentricity': data_dict[planet_name]['eccentricity'],
                'inclination':{
                   '@errorplus': data_dict[planet_name]['inclination_error_max'],
                   '@errorminus': data_dict[planet_name]['inclination_error_min'],
                   '#text': data_dict[planet_name]['inclination']
                },
                'mass':{
                   '@upperlimit': data_dict[planet_name]['mass']
                },
                'periastron':{
                   '@errorplus': data_dict[planet_name]['omega_error_max'],
                   '@errorminus': data_dict[planet_name]['omega_error_min'],
                   '#text': data_dict[planet_name]['omega']
                },
                'periastrontime':{
                   '@errorplus': data_dict[planet_name]['tperi_error_max'],
                   '@errorminus': data_dict[planet_name]['tperi_error_min'],
                   '#text': data_dict[planet_name]['tperi']
                },
                'impactparameter':{
                   '@errorplus': data_dict[planet_name]['impact_parameter_error_max'],
                   '@errorminus': data_dict[planet_name]['impact_parameter_error_min'],
                   '#text': data_dict[planet_name]['impact_parameter']
                }
             }
        systems[data_dict[planet_name]['star_name']]["star"]["planet"].append(removeEmptyAttributes(planet))

    # After storing all the information from the planets into the systems adds all systems to a list to return
    for system_key in systems:
        final_catalog.append({"system" : systems[system_key]})
    return final_catalog

print(readExoplaneteu())
        
