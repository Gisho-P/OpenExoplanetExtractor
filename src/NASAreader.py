import xmltodict
import json
import urllib.request
import csv
import dicttoxml
import collections


def readNASA():

    url = "http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets&format=json"
    data = urllib.request.urlopen(url).read().decode('utf-8')
    reader = json.loads(data)
    data_dict = {}

    # Set the planet_name as key
    # All other attributes are stored as a value
    for index in range(0, len(reader) - 1):
        pl_name = reader[index]['pl_hostname']
        plname_with_letter = "%s %s" % (pl_name, reader[index]['pl_letter'])
        del reader[index]['pl_letter']
        data_dict[plname_with_letter] = reader[index]

    return mapAttributes(data_dict)

# Recursively searches through a dictionary and removes all empty key value pairs
def removeEmptyAttributes(catalog_dict):
    empty_attributes = set()
    # loop through all attributes
    for attr in catalog_dict:
        # If it's a value (i.e a string) then check that it's not empty
        if(catalog_dict[attr] is None):
            empty_attributes.add(attr)
        # If it's a dict, this indicates that we should recursively check this dict for empty values
        elif((type(catalog_dict[attr]) is dict)):
            catalog_dict[attr] = removeEmptyAttributes(catalog_dict[attr])
            if((catalog_dict[attr] is None)):
                empty_attributes.add(attr)
        # if it's a list, then check each element for if it's empty
        elif(type(catalog_dict[attr]) is list and attr != "planet"): # planet is initially empty but will be filled
            for element in catalog_dict[attr]:
                if element is None:
                    catalog_dict[attr].remove(element)
            if(len(catalog_dict[attr]) == 1):
                catalog_dict[attr] = catalog_dict[attr][0]
            if((catalog_dict[attr] is None)):
                empty_attributes.add(attr)
    # remove all empty attributes
    for attr in empty_attributes:
        catalog_dict.pop(attr)
    return catalog_dict

# Format Right Ascension and Declination for OEC
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

# Format discovery method for OEC
def disc_method(st):
    if st == "Radial Velocity":
        return 'RV'
    else:
        return st[0].lower() + st[1:]

def round_one(num):
    if num != None:
        return round(num, 1)

def mapAttributes(data_dict):
    found_stars = set()
    final_catalog = []
    systems = {}
    catalog = {}
    # Organize by system
    # Add to system if planet orbits the star
    for planet_name in data_dict:
        # pl_hostname is interchangable with the system/star name
        if ((data_dict[planet_name]['pl_hostname'] not in found_stars)):
            found_stars.add(data_dict[planet_name]['pl_hostname'])
            catalog = {
                'name': data_dict[planet_name]['pl_hostname'],
                'rightascension': dd2hms(float(data_dict[planet_name]['ra']), True),
                'star':{
                    'temperature':{
                        '@errorplus': data_dict[planet_name]['st_tefferr1'],
                        '@errorminus': data_dict[planet_name]['st_tefferr2'],
                        '#text': data_dict[planet_name]['st_teff']
                    },
                    'name': data_dict[planet_name]['pl_hostname'],
                    'radius':{
                        '@errorplus': data_dict[planet_name]['st_raderr1'],
                        '@errorminus': data_dict[planet_name]['st_raderr2'],
                        '#text': data_dict[planet_name]['st_rad']
                    },
                    'mass':{
                        '@errorplus': data_dict[planet_name]['st_masserr1'],
                        '@errorminus': data_dict[planet_name]['st_masserr2'],
                        '#text': data_dict[planet_name]['st_mass']
                    }
                },

                'distance':{
                    '@errorplus': data_dict[planet_name]['st_disterr1'],
                    '@errorminus': data_dict[planet_name]['st_disterr2'],
                    '#text': data_dict[planet_name]['st_dist']
                    },
                'declination': dd2hms(float(data_dict[planet_name]['dec']), False)
            }

            catalog["star"]["planet"] = []
            systems.update({data_dict[planet_name]['pl_hostname'] : removeEmptyAttributes(catalog)})

        planet = {
            'lastupdate': data_dict[planet_name]['rowupdate'],
            'period':{
                '@errorplus': round_one(data_dict[planet_name]['pl_orbpererr1']),
                '@errorminus': round_one(data_dict[planet_name]['pl_orbpererr2']),
                '#text': round_one(data_dict[planet_name]['pl_orbper'])
                },
            'name': planet_name,
            'semimajoraxis':{
                '@errorplus': data_dict[planet_name]['pl_orbsmaxerr1'],
                '@errorminus': data_dict[planet_name]['pl_orbsmaxerr2'],
                '#text': data_dict[planet_name]['pl_orbsmax']
                },
            'radius':{
                '@errorplus': data_dict[planet_name]['st_raderr1'],
                '@errorminus': data_dict[planet_name]['st_raderr2'],
                '#text': data_dict[planet_name]['st_rad']
                },
            'eccentricity': data_dict[planet_name]['pl_orbeccen'],
            'discoverymethod': disc_method(data_dict[planet_name]['pl_discmethod']),
            'inclination':{
                '@errorplus': data_dict[planet_name]['pl_orbinclerr1'],
                '@errorminus': data_dict[planet_name]['pl_orbinclerr2'],
                '#text': data_dict[planet_name]['pl_orbincl']
            }
        }

        systems[data_dict[planet_name]['pl_hostname']]["star"]["planet"].append(removeEmptyAttributes(planet))

    # Add all system to a list for duplicates
    for system_key in systems:
        final_catalog.append({"system" : systems[system_key]})
    return final_catalog
