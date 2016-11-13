import xmltodict
import json
import urllib.request
import csv
import dicttoxml
import collections


def readNASAExoplanetArchive():
    
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

def mapAttributes(data_dict):
    found_stars = set()
    final_catalog = []
    systems = {}
    catalog = {}
    # Organize by system 
    # Add to system if planet orbits the star 
    for planet_name in data_dict:
        # pl_hostname is interchangable with the systen/star name
        if ((data_dict[planet_name]['pl_hostname'] not in found_stars)):
            found_stars.add(data_dict[planet_name]['pl_hostname'])
            catalog = {
                'name': data_dict[planet_name]['pl_hostname'],
                'rightascension': data_dict[planet_name]['ra'],
                'star':{
                    'temperature':{
                        '@errorplus': data_dict[planet_name]['st_tefferr1'],
                        '@errorminus': data_dict[planet_name]['st_tefferr2'],
                        '#text': data_dict[planet_name]['st_teff']
                    },
                    'name':[
                        data_dict[planet_name]['pl_hostname']
                    ],
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
                'declination':data_dict[planet_name]['dec']
            }
            
            catalog["star"]["planet"] = []
            systems.update({data_dict[planet_name]['pl_hostname'] : catalog})
            
            planet = {
                'lastupdate': data_dict[planet_name]['rowupdate'],
                'period':{
                    '@errorplus': data_dict[planet_name]['pl_orbpererr1'],
                    '@errorminus': data_dict[planet_name]['pl_orbpererr2'],
                    '#text': data_dict[planet_name]['pl_orbper']
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
                'discoverymethod':data_dict[planet_name]['pl_discmethod'],
                'inclination':{
                    '@errorplus': data_dict[planet_name]['pl_orbinclerr1'],
                    '@errorminus': data_dict[planet_name]['pl_orbinclerr2'],
                    '#text': data_dict[planet_name]['pl_orbincl']
                    }
            }
            
            systems[data_dict[planet_name]['pl_hostname']]["star"]["planet"].append(planet)
            
    # Add all system to a list for duplicates
    for system_key in systems:
        final_catalog.append({"system" : systems[system_key]})
    return final_catalog
