import urllib.request
import csv
from io import StringIO


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
               'rightascension': data_dict[planet_name]['ra'],
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
                     '@errorplus':'',
                     '@errorminus':'',
                     '#text': data_dict[planet_name]['mag_k']
                  },
                  'magI':{  
                     '@errorplus':'',
                     '@errorminus':'',
                     '#text': data_dict[planet_name]['mag_i']
                  },
                  'radius':{  
                     '@errorplus': data_dict[planet_name]['star_radius_error_max'],
                     '@errorminus': data_dict[planet_name]['star_radius_error_min'],
                     '#text': data_dict[planet_name]['star_radius']
                  },
                  'magR':{  
                     '@errorplus':'',
                     '@errorminus':'',
                     '#text': ''
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
                     '@errorplus':'',
                     '@errorminus':'',
                     '#text': data_dict[planet_name]['mag_j']
                  },
                  'magH':{  
                     '@errorplus':'',
                     '@errorminus':'',
                     '#text': data_dict[planet_name]['mag_h']
                  }
               },
               'distance':{  
                  '@errorplus': data_dict[planet_name]['star_distance_error_max'],
                  '@errorminus': data_dict[planet_name]['star_distance_error_min'],
                  '#text': data_dict[planet_name]['star_distance']
               },
               'declination':''
            }
            catalog["planet"] = []
            systems.update({data_dict[planet_name]['star_name'] : catalog})
        
        planet = {  
                'transittime':{  
                   '@errorplus': data_dict[planet_name]['tzero_tr_error_max'],
                   '#text': data_dict[planet_name]['tzero_tr'],
                   '@errorminus': data_dict[planet_name]['tzero_tr_error_min'],
                   '@unit':''
                },
                'lastupdate': data_dict[planet_name]['updated'],
                'temperature':{  
                   '@errorplus': '',
                   '@errorminus': '',
                   '#text': data_dict[planet_name]['temp_calculated']
                },
                'discoveryyear': data_dict[planet_name]['discovered'],
                'period':{  
                   '@errorplus': data_dict[planet_name]['orbital_period_error_max'],
                   '@errorminus': data_dict[planet_name]['orbital_period_error_min'],
                   '#text': data_dict[planet_name]['orbital_period']
                },
                'name':[  
                    planet_name,
                   ''
                ],
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
                'istransiting':'',
                'discoverymethod':'',
                'description':'',
                'inclination':{  
                   '@errorplus': data_dict[planet_name]['inclination_error_max'],
                   '@errorminus': data_dict[planet_name]['inclination_error_min'],
                   '#text': data_dict[planet_name]['inclination']
                },
                'list':'',
                'mass':{  
                   '@upperlimit': data_dict[planet_name]['mass']
                }
             }
        systems[data_dict[planet_name]['star_name']]["planet"].append(planet)
    
    # After storing all the information from the planets into the systems adds all systems to a list to return
    for system_key in systems:
        final_catalog.append({"system" : systems[system_key]})
    return final_catalog

readExoplaneteu()