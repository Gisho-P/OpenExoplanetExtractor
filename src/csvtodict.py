import xmltodict
import json
import urllib.request
import csv
import dicttoxml
import collections

def readExoplaneteu():

    url = "http://exoplanet.eu/catalog/csv/"
    data = urllib.request.urlopen(url).read().decode('utf-8')
    data_dict = {}
    data = data.split("\n")
    attribute_names = data[0].split(",")
    planet_names = []
    for line in data[1:]:
        row_attr = line.split(",")
        attributes = {}
        if(len(row_attr) > 1): # ignore empty lines
            # Store the value of each attribute under the attribute name THIS ISNT WORKING PROPERLY STORING INCORECTLY SOMETIMES
            for index in range(1, len(attribute_names) - 1):
                attributes[attribute_names[index]] = row_attr[index]
            data_dict[row_attr[0]] = attributes
            planet_names.append(row_attr[0])
    
    found_stars = set()
    final_catalog = []
    systems = {}
    catalog = {}    
    # Create a system for each star
    for index in range(0, len(data_dict) - 1):
        if ((data_dict[planet_names[index]]['star_name'] not in found_stars)):
            found_stars.add(data_dict[planet_names[index]]['star_name'])
            if(data_dict[planet_names[index]]['star_name'] == ""):
                print("ss")
            
            catalog = {   
               'name': data_dict[planet_names[index]]['star_name'],
               'rightascension': data_dict[planet_names[index]]['ra'],
               'star':{  
                  'temperature':{  
                     '@errorplus': data_dict[planet_names[index]]['star_teff_error_max'],
                     '@errorminus': data_dict[planet_names[index]]['star_teff_error_min'],
                     '#text': data_dict[planet_names[index]]['star_teff']
                  },
                  'age': data_dict[planet_names[index]]['star_age'],
                  'name':[  
                      data_dict[planet_names[index]]['star_name'],
                      #data_dict[planet_names[index]]["star_alternate_names\\r"] cant find key, probably a problem with slash in strings
                  ],
                  'magK':{  
                     '@errorplus':'',
                     '@errorminus':'',
                     '#text': data_dict[planet_names[index]]['mag_k']
                  },
                  'magI':{  
                     '@errorplus':'',
                     '@errorminus':'',
                     '#text': data_dict[planet_names[index]]['mag_i']
                  },
                  'radius':{  
                     '@errorplus': data_dict[planet_names[index]]['star_radius_error_max'],
                     '@errorminus': data_dict[planet_names[index]]['star_radius_error_min'],
                     '#text': data_dict[planet_names[index]]['star_radius']
                  },
                  'magR':{  
                     '@errorplus':'',
                     '@errorminus':'',
                     '#text': ''
                  },
                  'spectraltype': data_dict[planet_names[index]]['star_sp_type'],
                  'mass':{  
                     '@errorplus': data_dict[planet_names[index]]['star_mass_error_max'],
                     '@errorminus': data_dict[planet_names[index]]['star_mass_error_min'],
                     '#text': data_dict[planet_names[index]]['star_mass']
                  },
                  'metallicity':{  
                     '@errorplus': data_dict[planet_names[index]]['star_metallicity_error_max'],
                     '@errorminus': data_dict[planet_names[index]]['star_metallicity_error_min'],
                     '#text': data_dict[planet_names[index]]['star_metallicity']
                  },
                  'magJ':{  
                     '@errorplus':'',
                     '@errorminus':'',
                     '#text': data_dict[planet_names[index]]['mag_j']
                  },
                  'magH':{  
                     '@errorplus':'',
                     '@errorminus':'',
                     '#text': data_dict[planet_names[index]]['mag_h']
                  }
               },
               'distance':{  
                  '@errorplus': data_dict[planet_names[index]]['star_distance_error_max'],
                  '@errorminus': data_dict[planet_names[index]]['star_distance_error_min'],
                  '#text': data_dict[planet_names[index]]['star_distance']
               },
               'declination':''
            }
            catalog["planet"] = []
            systems.update({data_dict[planet_names[index]]['star_name'] : catalog})
        
        planet = {  
                'transittime':{  
                   '@errorplus': data_dict[planet_names[index]]['tzero_tr_error_max'],
                   '#text': data_dict[planet_names[index]]['tzero_tr'],
                   '@errorminus': data_dict[planet_names[index]]['tzero_tr_error_min'],
                   '@unit':''
                },
                'lastupdate': data_dict[planet_names[index]]['updated'],
                'temperature':{  
                   '@errorplus': '',
                   '@errorminus': '',
                   '#text': data_dict[planet_names[index]]['temp_calculated']
                },
                'discoveryyear': data_dict[planet_names[index]]['discovered'],
                'period':{  
                   '@errorplus': data_dict[planet_names[index]]['orbital_period_error_max'],
                   '@errorminus': data_dict[planet_names[index]]['orbital_period_error_min'],
                   '#text': data_dict[planet_names[index]]['orbital_period']
                },
                'name':[  
                    planet_names[index],
                   ''
                ],
                'semimajoraxis':{  
                   '@errorplus': data_dict[planet_names[index]]['semi_major_axis_error_max'],
                   '@errorminus': data_dict[planet_names[index]]['semi_major_axis_error_min'],
                   '#text': data_dict[planet_names[index]]['semi_major_axis']
                },
                'radius':{  
                   '@errorplus': data_dict[planet_names[index]]['radius_error_max'],
                   '@errorminus': data_dict[planet_names[index]]['radius_error_min'],
                   '#text': data_dict[planet_names[index]]['radius']
                },
                'eccentricity': data_dict[planet_names[index]]['eccentricity'],
                'istransiting':'',
                'discoverymethod':'',
                'description':'',
                'inclination':{  
                   '@errorplus': data_dict[planet_names[index]]['inclination_error_max'],
                   '@errorminus': data_dict[planet_names[index]]['inclination_error_min'],
                   '#text': data_dict[planet_names[index]]['inclination']
                },
                'list':'',
                'mass':{  
                   '@upperlimit': data_dict[planet_names[index]]['mass']
                }
             }
        systems[data_dict[planet_names[index]]['star_name']]["planet"].append(planet)
            
    for system_key in systems:
        final_catalog.append({"system" : systems[system_key]})
    return final_catalog
    
print(readExoplaneteu())        