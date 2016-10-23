import xmltodict
import json
import urllib.request
import csv
import dicttoxml
import collections


def readNASAExoplanetArchive():
    
    url = "http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets&format=json"
    data = urllib.request.urlopen(url).read().decode('utf-8')
    a = json.loads(data)
    
    
    planet_name = a[0]['pl_hostname']
    space = ' '
    final_name = planet_name + space + a[0]['pl_letter']
    
    
    star = {'temperature': {'@errorplus': a[0]['st_tefferr1'], '@errorminus': a[0]['st_tefferr2'] }, 'name': planet_name, 'radius': {'@errorplus': a[0]['st_raderr1'], '@errorminus': a[0]['st_raderr2']}}
    planet = {'Period': {'@errorplus': a[0]['pl_orbpererr1'], '@errorminus': a[0]['pl_orbpererr2'] }, 'lastupdate': a[0]['rowupdate'], 'name': final_name, 'semimajoraxis': {'@errorplus': a[0]['pl_orbsmaxerr1'], '@errorminus': a[0]['pl_orbsmaxerr2']}, 'radius': {'@errorplus': a[0]['pl_radjerr1'], '@errorminus': a[0]['pl_radjerr2']}, 'eccentricity': {'@errorplus': a[0]['pl_orbeccenerr1'], '@errorminus': a[0]['pl_orbeccenerr2'] } , 'discoverymethod': a[0]['pl_discmethod'], 'mass': {'@errorplus': a[0]['pl_bmassjerr1'], '@errorminus': a[0]['pl_bmassjerr2']}  }
    
    
    catalog = { 'system' : {'name': planet_name, 'rightascension': a[0]['ra_str'], 'distance': {'@errorplus': a[0]['st_disterr1'], '@errorminus': a[0]['st_disterr2']}, 'star': star, 'planet' : planet} }
    
    print(catalog)
