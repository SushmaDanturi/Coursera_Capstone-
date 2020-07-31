<h3 id="version">1. Dowloading the Data to Explore</h3>


```python
import numpy as np 
import pandas as pd 
import json

#!conda install -c conda-forge geopy --yes 
#from geopy.geocoders import Nominatim 

#!conda install -c conda-forge folium=0.5.0 --yes 
#import folium 

print('Libraries imported.')
```

    Libraries imported.



```python
!wget -q -O 'newyork_data.json' https://cocl.us/new_york_dataset
print('Data downloaded!')
```

    Data downloaded!



```python
with open('newyork_data.json') as json_data:
    newyork_data = json.load(json_data)
```


```python
newyork_data
```




    {'type': 'FeatureCollection',
     'totalFeatures': 306,
     'features': [{'type': 'Feature',
       'id': 'nyu_2451_34572.1',
       'geometry': {'type': 'Point',
        'coordinates': [-73.84720052054902, 40.89470517661]},
       'geometry_name': 'geom',
       'properties': {'name': 'Wakefield',
        'stacked': 1,
        'annoline1': 'Wakefield',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.84720052054902,
         40.89470517661,
         -73.84720052054902,
         40.89470517661]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.2',
       'geometry': {'type': 'Point',
        'coordinates': [-73.82993910812398, 40.87429419303012]},
       'geometry_name': 'geom',
       'properties': {'name': 'Co-op City',
        'stacked': 2,
        'annoline1': 'Co-op',
        'annoline2': 'City',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.82993910812398,
         40.87429419303012,
         -73.82993910812398,
         40.87429419303012]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.3',
       'geometry': {'type': 'Point',
        'coordinates': [-73.82780644716412, 40.887555677350775]},
       'geometry_name': 'geom',
       'properties': {'name': 'Eastchester',
        'stacked': 1,
        'annoline1': 'Eastchester',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.82780644716412,
         40.887555677350775,
         -73.82780644716412,
         40.887555677350775]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.4',
       'geometry': {'type': 'Point',
        'coordinates': [-73.90564259591682, 40.89543742690383]},
       'geometry_name': 'geom',
       'properties': {'name': 'Fieldston',
        'stacked': 1,
        'annoline1': 'Fieldston',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.90564259591682,
         40.89543742690383,
         -73.90564259591682,
         40.89543742690383]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.5',
       'geometry': {'type': 'Point',
        'coordinates': [-73.9125854610857, 40.890834493891305]},
       'geometry_name': 'geom',
       'properties': {'name': 'Riverdale',
        'stacked': 1,
        'annoline1': 'Riverdale',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.9125854610857,
         40.890834493891305,
         -73.9125854610857,
         40.890834493891305]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.6',
       'geometry': {'type': 'Point',
        'coordinates': [-73.90281798724604, 40.88168737120521]},
       'geometry_name': 'geom',
       'properties': {'name': 'Kingsbridge',
        'stacked': 1,
        'annoline1': 'Kingsbridge',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.90281798724604,
         40.88168737120521,
         -73.90281798724604,
         40.88168737120521]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.7',
       'geometry': {'type': 'Point',
        'coordinates': [-73.91065965862981, 40.87655077879964]},
       'geometry_name': 'geom',
       'properties': {'name': 'Marble Hill',
        'stacked': 2,
        'annoline1': 'Marble',
        'annoline2': 'Hill',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.91065965862981,
         40.87655077879964,
         -73.91065965862981,
         40.87655077879964]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.8',
       'geometry': {'type': 'Point',
        'coordinates': [-73.86731496814176, 40.89827261213805]},
       'geometry_name': 'geom',
       'properties': {'name': 'Woodlawn',
        'stacked': 1,
        'annoline1': 'Woodlawn',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.86731496814176,
         40.89827261213805,
         -73.86731496814176,
         40.89827261213805]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.9',
       'geometry': {'type': 'Point',
        'coordinates': [-73.8793907395681, 40.87722415599446]},
       'geometry_name': 'geom',
       'properties': {'name': 'Norwood',
        'stacked': 1,
        'annoline1': 'Norwood',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.8793907395681,
         40.87722415599446,
         -73.8793907395681,
         40.87722415599446]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.10',
       'geometry': {'type': 'Point',
        'coordinates': [-73.85744642974207, 40.88103887819211]},
       'geometry_name': 'geom',
       'properties': {'name': 'Williamsbridge',
        'stacked': 1,
        'annoline1': 'Williamsbridge',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.85744642974207,
         40.88103887819211,
         -73.85744642974207,
         40.88103887819211]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.11',
       'geometry': {'type': 'Point',
        'coordinates': [-73.83579759808117, 40.866858107252696]},
       'geometry_name': 'geom',
       'properties': {'name': 'Baychester',
        'stacked': 1,
        'annoline1': 'Baychester',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.83579759808117,
         40.866858107252696,
         -73.83579759808117,
         40.866858107252696]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.12',
       'geometry': {'type': 'Point',
        'coordinates': [-73.85475564017999, 40.85741349808865]},
       'geometry_name': 'geom',
       'properties': {'name': 'Pelham Parkway',
        'stacked': 1,
        'annoline1': 'Pelham Parkway',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.85475564017999,
         40.85741349808865,
         -73.85475564017999,
         40.85741349808865]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.13',
       'geometry': {'type': 'Point',
        'coordinates': [-73.78648845267413, 40.84724670491813]},
       'geometry_name': 'geom',
       'properties': {'name': 'City Island',
        'stacked': 2,
        'annoline1': 'City',
        'annoline2': 'Island',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.78648845267413,
         40.84724670491813,
         -73.78648845267413,
         40.84724670491813]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.14',
       'geometry': {'type': 'Point',
        'coordinates': [-73.8855121841913, 40.870185164975325]},
       'geometry_name': 'geom',
       'properties': {'name': 'Bedford Park',
        'stacked': 2,
        'annoline1': 'Bedford',
        'annoline2': 'Park',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.8855121841913,
         40.870185164975325,
         -73.8855121841913,
         40.870185164975325]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.15',
       'geometry': {'type': 'Point',
        'coordinates': [-73.9104159619131, 40.85572707719664]},
       'geometry_name': 'geom',
       'properties': {'name': 'University Heights',
        'stacked': 2,
        'annoline1': 'University',
        'annoline2': 'Heights',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.9104159619131,
         40.85572707719664,
         -73.9104159619131,
         40.85572707719664]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.16',
       'geometry': {'type': 'Point',
        'coordinates': [-73.91967159119565, 40.84789792606271]},
       'geometry_name': 'geom',
       'properties': {'name': 'Morris Heights',
        'stacked': 2,
        'annoline1': 'Morris',
        'annoline2': 'Heights',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.91967159119565,
         40.84789792606271,
         -73.91967159119565,
         40.84789792606271]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.17',
       'geometry': {'type': 'Point',
        'coordinates': [-73.89642655981623, 40.86099679638654]},
       'geometry_name': 'geom',
       'properties': {'name': 'Fordham',
        'stacked': 1,
        'annoline1': 'Fordham',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.89642655981623,
         40.86099679638654,
         -73.89642655981623,
         40.86099679638654]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.18',
       'geometry': {'type': 'Point',
        'coordinates': [-73.88735617532338, 40.84269615786053]},
       'geometry_name': 'geom',
       'properties': {'name': 'East Tremont',
        'stacked': 2,
        'annoline1': 'East',
        'annoline2': 'Tremont',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.88735617532338,
         40.84269615786053,
         -73.88735617532338,
         40.84269615786053]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.19',
       'geometry': {'type': 'Point',
        'coordinates': [-73.87774474910545, 40.83947505672653]},
       'geometry_name': 'geom',
       'properties': {'name': 'West Farms',
        'stacked': 2,
        'annoline1': 'West',
        'annoline2': 'Farms',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.87774474910545,
         40.83947505672653,
         -73.87774474910545,
         40.83947505672653]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.20',
       'geometry': {'type': 'Point',
        'coordinates': [-73.9261020935813, 40.836623010706056]},
       'geometry_name': 'geom',
       'properties': {'name': 'High  Bridge',
        'stacked': 1,
        'annoline1': 'Highbridge',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.9261020935813,
         40.836623010706056,
         -73.9261020935813,
         40.836623010706056]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.21',
       'geometry': {'type': 'Point',
        'coordinates': [-73.90942160757436, 40.819754370594936]},
       'geometry_name': 'geom',
       'properties': {'name': 'Melrose',
        'stacked': 1,
        'annoline1': 'Melrose',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.90942160757436,
         40.819754370594936,
         -73.90942160757436,
         40.819754370594936]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.22',
       'geometry': {'type': 'Point',
        'coordinates': [-73.91609987487575, 40.80623874935177]},
       'geometry_name': 'geom',
       'properties': {'name': 'Mott Haven',
        'stacked': 1,
        'annoline1': 'Mott Haven',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.91609987487575,
         40.80623874935177,
         -73.91609987487575,
         40.80623874935177]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.23',
       'geometry': {'type': 'Point',
        'coordinates': [-73.91322139386135, 40.801663627756206]},
       'geometry_name': 'geom',
       'properties': {'name': 'Port Morris',
        'stacked': 2,
        'annoline1': 'Port',
        'annoline2': 'Morris',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.91322139386135,
         40.801663627756206,
         -73.91322139386135,
         40.801663627756206]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.24',
       'geometry': {'type': 'Point',
        'coordinates': [-73.8957882009446, 40.81509904545822]},
       'geometry_name': 'geom',
       'properties': {'name': 'Longwood',
        'stacked': 1,
        'annoline1': 'Longwood',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.8957882009446,
         40.81509904545822,
         -73.8957882009446,
         40.81509904545822]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.25',
       'geometry': {'type': 'Point',
        'coordinates': [-73.88331505955291, 40.80972987938709]},
       'geometry_name': 'geom',
       'properties': {'name': 'Hunts Point',
        'stacked': 2,
        'annoline1': 'Hunts',
        'annoline2': 'Point',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.88331505955291,
         40.80972987938709,
         -73.88331505955291,
         40.80972987938709]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.26',
       'geometry': {'type': 'Point',
        'coordinates': [-73.90150648943059, 40.82359198585534]},
       'geometry_name': 'geom',
       'properties': {'name': 'Morrisania',
        'stacked': 1,
        'annoline1': 'Morrisania',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.90150648943059,
         40.82359198585534,
         -73.90150648943059,
         40.82359198585534]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.27',
       'geometry': {'type': 'Point',
        'coordinates': [-73.86574609554924, 40.821012197914015]},
       'geometry_name': 'geom',
       'properties': {'name': 'Soundview',
        'stacked': 1,
        'annoline1': 'Soundview',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.86574609554924,
         40.821012197914015,
         -73.86574609554924,
         40.821012197914015]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.28',
       'geometry': {'type': 'Point',
        'coordinates': [-73.85414416189266, 40.80655112003589]},
       'geometry_name': 'geom',
       'properties': {'name': 'Clason Point',
        'stacked': 2,
        'annoline1': 'Clason',
        'annoline2': 'Point',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.85414416189266,
         40.80655112003589,
         -73.85414416189266,
         40.80655112003589]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.29',
       'geometry': {'type': 'Point',
        'coordinates': [-73.81635002158441, 40.81510925804005]},
       'geometry_name': 'geom',
       'properties': {'name': 'Throgs Neck',
        'stacked': 1,
        'annoline1': 'Throgs Neck',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.81635002158441,
         40.81510925804005,
         -73.81635002158441,
         40.81510925804005]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.30',
       'geometry': {'type': 'Point',
        'coordinates': [-73.8240992675385, 40.844245936947374]},
       'geometry_name': 'geom',
       'properties': {'name': 'Country Club',
        'stacked': 2,
        'annoline1': 'Country',
        'annoline2': 'Club',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.8240992675385,
         40.844245936947374,
         -73.8240992675385,
         40.844245936947374]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.31',
       'geometry': {'type': 'Point',
        'coordinates': [-73.85600310535783, 40.837937822267286]},
       'geometry_name': 'geom',
       'properties': {'name': 'Parkchester',
        'stacked': 1,
        'annoline1': 'Parkchester',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.85600310535783,
         40.837937822267286,
         -73.85600310535783,
         40.837937822267286]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.32',
       'geometry': {'type': 'Point',
        'coordinates': [-73.84219407604444, 40.8406194964327]},
       'geometry_name': 'geom',
       'properties': {'name': 'Westchester Square',
        'stacked': 2,
        'annoline1': 'Westchester',
        'annoline2': 'Square',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.84219407604444,
         40.8406194964327,
         -73.84219407604444,
         40.8406194964327]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.33',
       'geometry': {'type': 'Point',
        'coordinates': [-73.8662991807561, 40.84360847124718]},
       'geometry_name': 'geom',
       'properties': {'name': 'Van Nest',
        'stacked': 2,
        'annoline1': 'Van',
        'annoline2': 'Nest',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.8662991807561,
         40.84360847124718,
         -73.8662991807561,
         40.84360847124718]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.34',
       'geometry': {'type': 'Point',
        'coordinates': [-73.85040178030421, 40.847549063536334]},
       'geometry_name': 'geom',
       'properties': {'name': 'Morris Park',
        'stacked': 1,
        'annoline1': 'Morris Park',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.85040178030421,
         40.847549063536334,
         -73.85040178030421,
         40.847549063536334]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.35',
       'geometry': {'type': 'Point',
        'coordinates': [-73.88845196134804, 40.85727710073895]},
       'geometry_name': 'geom',
       'properties': {'name': 'Belmont',
        'stacked': 1,
        'annoline1': 'Belmont',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.88845196134804,
         40.85727710073895,
         -73.88845196134804,
         40.85727710073895]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.36',
       'geometry': {'type': 'Point',
        'coordinates': [-73.91719048210393, 40.88139497727086]},
       'geometry_name': 'geom',
       'properties': {'name': 'Spuyten Duyvil',
        'stacked': 2,
        'annoline1': 'Spuyten',
        'annoline2': 'Duyvil',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.91719048210393,
         40.88139497727086,
         -73.91719048210393,
         40.88139497727086]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.37',
       'geometry': {'type': 'Point',
        'coordinates': [-73.90453054908927, 40.90854282950666]},
       'geometry_name': 'geom',
       'properties': {'name': 'North Riverdale',
        'stacked': 2,
        'annoline1': 'North',
        'annoline2': 'Riverdale',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.90453054908927,
         40.90854282950666,
         -73.90453054908927,
         40.90854282950666]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.38',
       'geometry': {'type': 'Point',
        'coordinates': [-73.8320737824047, 40.85064140940335]},
       'geometry_name': 'geom',
       'properties': {'name': 'Pelham Bay',
        'stacked': 2,
        'annoline1': 'Pelham',
        'annoline2': 'Bay',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.8320737824047,
         40.85064140940335,
         -73.8320737824047,
         40.85064140940335]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.39',
       'geometry': {'type': 'Point',
        'coordinates': [-73.82620275994073, 40.82657951686922]},
       'geometry_name': 'geom',
       'properties': {'name': 'Schuylerville',
        'stacked': 1,
        'annoline1': 'Schuylerville',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.82620275994073,
         40.82657951686922,
         -73.82620275994073,
         40.82657951686922]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.40',
       'geometry': {'type': 'Point',
        'coordinates': [-73.81388514428619, 40.821986118163494]},
       'geometry_name': 'geom',
       'properties': {'name': 'Edgewater Park',
        'stacked': 2,
        'annoline1': 'Edgewater',
        'annoline2': 'Park',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.81388514428619,
         40.821986118163494,
         -73.81388514428619,
         40.821986118163494]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.41',
       'geometry': {'type': 'Point',
        'coordinates': [-73.84802729582735, 40.819014376988314]},
       'geometry_name': 'geom',
       'properties': {'name': 'Castle Hill',
        'stacked': 2,
        'annoline1': 'Castle',
        'annoline2': 'Hill',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.84802729582735,
         40.819014376988314,
         -73.84802729582735,
         40.819014376988314]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.42',
       'geometry': {'type': 'Point',
        'coordinates': [-73.86332361652777, 40.87137078192371]},
       'geometry_name': 'geom',
       'properties': {'name': 'Olinville',
        'stacked': 1,
        'annoline1': 'Olinville',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.86332361652777,
         40.87137078192371,
         -73.86332361652777,
         40.87137078192371]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.43',
       'geometry': {'type': 'Point',
        'coordinates': [-73.84161194831223, 40.86296562477998]},
       'geometry_name': 'geom',
       'properties': {'name': 'Pelham Gardens',
        'stacked': 2,
        'annoline1': 'Pelham',
        'annoline2': 'Gardens',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.84161194831223,
         40.86296562477998,
         -73.84161194831223,
         40.86296562477998]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.44',
       'geometry': {'type': 'Point',
        'coordinates': [-73.91558941773444, 40.83428380733851]},
       'geometry_name': 'geom',
       'properties': {'name': 'Concourse',
        'stacked': 1,
        'annoline1': 'Concourse',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.91558941773444,
         40.83428380733851,
         -73.91558941773444,
         40.83428380733851]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.45',
       'geometry': {'type': 'Point',
        'coordinates': [-73.85053524451935, 40.82977429787161]},
       'geometry_name': 'geom',
       'properties': {'name': 'Unionport',
        'stacked': 1,
        'annoline1': 'Unionport',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.85053524451935,
         40.82977429787161,
         -73.85053524451935,
         40.82977429787161]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.46',
       'geometry': {'type': 'Point',
        'coordinates': [-73.84808271877168, 40.88456130303732]},
       'geometry_name': 'geom',
       'properties': {'name': 'Edenwald',
        'stacked': 1,
        'annoline1': 'Edenwald',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.84808271877168,
         40.88456130303732,
         -73.84808271877168,
         40.88456130303732]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.47',
       'geometry': {'type': 'Point',
        'coordinates': [-74.03062069353813, 40.625801065010656]},
       'geometry_name': 'geom',
       'properties': {'name': 'Bay Ridge',
        'stacked': 1,
        'annoline1': 'Bay Ridge',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-74.03062069353813,
         40.625801065010656,
         -74.03062069353813,
         40.625801065010656]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.48',
       'geometry': {'type': 'Point',
        'coordinates': [-73.99517998380729, 40.61100890202044]},
       'geometry_name': 'geom',
       'properties': {'name': 'Bensonhurst',
        'stacked': 1,
        'annoline1': 'Bensonhurst',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.99517998380729,
         40.61100890202044,
         -73.99517998380729,
         40.61100890202044]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.49',
       'geometry': {'type': 'Point',
        'coordinates': [-74.01031618527784, 40.64510294925429]},
       'geometry_name': 'geom',
       'properties': {'name': 'Sunset Park',
        'stacked': 2,
        'annoline1': 'Sunset',
        'annoline2': 'Park',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-74.01031618527784,
         40.64510294925429,
         -74.01031618527784,
         40.64510294925429]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.50',
       'geometry': {'type': 'Point',
        'coordinates': [-73.95424093127393, 40.7302009848647]},
       'geometry_name': 'geom',
       'properties': {'name': 'Greenpoint',
        'stacked': 1,
        'annoline1': 'Greenpoint',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.95424093127393,
         40.7302009848647,
         -73.95424093127393,
         40.7302009848647]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.51',
       'geometry': {'type': 'Point',
        'coordinates': [-73.97347087708445, 40.59526001306593]},
       'geometry_name': 'geom',
       'properties': {'name': 'Gravesend',
        'stacked': 1,
        'annoline1': 'Gravesend',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.97347087708445,
         40.59526001306593,
         -73.97347087708445,
         40.59526001306593]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.52',
       'geometry': {'type': 'Point',
        'coordinates': [-73.96509448785336, 40.57682506566604]},
       'geometry_name': 'geom',
       'properties': {'name': 'Brighton Beach',
        'stacked': 2,
        'annoline1': 'Brighton',
        'annoline2': 'Beach',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.96509448785336,
         40.57682506566604,
         -73.96509448785336,
         40.57682506566604]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.53',
       'geometry': {'type': 'Point',
        'coordinates': [-73.94318640482979, 40.58689012678384]},
       'geometry_name': 'geom',
       'properties': {'name': 'Sheepshead Bay',
        'stacked': 2,
        'annoline1': 'Sheepshead',
        'annoline2': 'Bay',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.94318640482979,
         40.58689012678384,
         -73.94318640482979,
         40.58689012678384]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.54',
       'geometry': {'type': 'Point',
        'coordinates': [-73.95743840559939, 40.61443251335098]},
       'geometry_name': 'geom',
       'properties': {'name': 'Manhattan Terrace',
        'stacked': 2,
        'annoline1': 'Manhattan',
        'annoline2': 'Terrace',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.95743840559939,
         40.61443251335098,
         -73.95743840559939,
         40.61443251335098]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.55',
       'geometry': {'type': 'Point',
        'coordinates': [-73.95840106533903, 40.63632589026677]},
       'geometry_name': 'geom',
       'properties': {'name': 'Flatbush',
        'stacked': 1,
        'annoline1': 'Flatbush',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.95840106533903,
         40.63632589026677,
         -73.95840106533903,
         40.63632589026677]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.56',
       'geometry': {'type': 'Point',
        'coordinates': [-73.94329119073582, 40.67082917695294]},
       'geometry_name': 'geom',
       'properties': {'name': 'Crown Heights',
        'stacked': 2,
        'annoline1': 'Crown',
        'annoline2': 'Heights',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.94329119073582,
         40.67082917695294,
         -73.94329119073582,
         40.67082917695294]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.57',
       'geometry': {'type': 'Point',
        'coordinates': [-73.93610256185836, 40.64171776668961]},
       'geometry_name': 'geom',
       'properties': {'name': 'East Flatbush',
        'stacked': 1,
        'annoline1': 'East Flatbush',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.93610256185836,
         40.64171776668961,
         -73.93610256185836,
         40.64171776668961]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.58',
       'geometry': {'type': 'Point',
        'coordinates': [-73.98042110559474, 40.642381958003526]},
       'geometry_name': 'geom',
       'properties': {'name': 'Kensington',
        'stacked': 1,
        'annoline1': 'Kensington',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.98042110559474,
         40.642381958003526,
         -73.98042110559474,
         40.642381958003526]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.59',
       'geometry': {'type': 'Point',
        'coordinates': [-73.98007340430172, 40.65694583575104]},
       'geometry_name': 'geom',
       'properties': {'name': 'Windsor Terrace',
        'stacked': 2,
        'annoline1': 'Windsor',
        'annoline2': 'Terrace',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.98007340430172,
         40.65694583575104,
         -73.98007340430172,
         40.65694583575104]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.60',
       'geometry': {'type': 'Point',
        'coordinates': [-73.9648592426269, 40.676822262254724]},
       'geometry_name': 'geom',
       'properties': {'name': 'Prospect Heights',
        'stacked': 2,
        'annoline1': 'Prospect',
        'annoline2': 'Heights',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.9648592426269,
         40.676822262254724,
         -73.9648592426269,
         40.676822262254724]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.61',
       'geometry': {'type': 'Point',
        'coordinates': [-73.91023536176607, 40.66394994339755]},
       'geometry_name': 'geom',
       'properties': {'name': 'Brownsville',
        'stacked': 1,
        'annoline1': 'Brownsville',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.91023536176607,
         40.66394994339755,
         -73.91023536176607,
         40.66394994339755]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.62',
       'geometry': {'type': 'Point',
        'coordinates': [-73.95811529220927, 40.70714439344251]},
       'geometry_name': 'geom',
       'properties': {'name': 'Williamsburg',
        'stacked': 1,
        'annoline1': 'Williamsburg',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.95811529220927,
         40.70714439344251,
         -73.95811529220927,
         40.70714439344251]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.63',
       'geometry': {'type': 'Point',
        'coordinates': [-73.92525797487045, 40.69811611017901]},
       'geometry_name': 'geom',
       'properties': {'name': 'Bushwick',
        'stacked': 1,
        'annoline1': 'Bushwick',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.92525797487045,
         40.69811611017901,
         -73.92525797487045,
         40.69811611017901]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.64',
       'geometry': {'type': 'Point',
        'coordinates': [-73.94178488690297, 40.687231607720456]},
       'geometry_name': 'geom',
       'properties': {'name': 'Bedford Stuyvesant',
        'stacked': 1,
        'annoline1': 'Bedford Stuyvesant',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.94178488690297,
         40.687231607720456,
         -73.94178488690297,
         40.687231607720456]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.65',
       'geometry': {'type': 'Point',
        'coordinates': [-73.99378225496424, 40.695863722724084]},
       'geometry_name': 'geom',
       'properties': {'name': 'Brooklyn Heights',
        'stacked': 2,
        'annoline1': 'Brooklyn',
        'annoline2': 'Heights',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.99378225496424,
         40.695863722724084,
         -73.99378225496424,
         40.695863722724084]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.66',
       'geometry': {'type': 'Point',
        'coordinates': [-73.99856139218463, 40.687919722485574]},
       'geometry_name': 'geom',
       'properties': {'name': 'Cobble Hill',
        'stacked': 2,
        'annoline1': 'Cobble',
        'annoline2': 'Hill',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.99856139218463,
         40.687919722485574,
         -73.99856139218463,
         40.687919722485574]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.67',
       'geometry': {'type': 'Point',
        'coordinates': [-73.99465372828006, 40.680540231076485]},
       'geometry_name': 'geom',
       'properties': {'name': 'Carroll Gardens',
        'stacked': 2,
        'annoline1': 'Carroll',
        'annoline2': 'Gardens',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.99465372828006,
         40.680540231076485,
         -73.99465372828006,
         40.680540231076485]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.68',
       'geometry': {'type': 'Point',
        'coordinates': [-74.0127589747356, 40.676253230250886]},
       'geometry_name': 'geom',
       'properties': {'name': 'Red Hook',
        'stacked': 2,
        'annoline1': 'Red',
        'annoline2': 'Hook',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-74.0127589747356,
         40.676253230250886,
         -74.0127589747356,
         40.676253230250886]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.69',
       'geometry': {'type': 'Point',
        'coordinates': [-73.99444087145339, 40.673931143187154]},
       'geometry_name': 'geom',
       'properties': {'name': 'Gowanus',
        'stacked': 1,
        'annoline1': 'Gowanus',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.99444087145339,
         40.673931143187154,
         -73.99444087145339,
         40.673931143187154]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.70',
       'geometry': {'type': 'Point',
        'coordinates': [-73.97290574369092, 40.68852726018977]},
       'geometry_name': 'geom',
       'properties': {'name': 'Fort Greene',
        'stacked': 2,
        'annoline1': 'Fort',
        'annoline2': 'Greene',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.97290574369092,
         40.68852726018977,
         -73.97290574369092,
         40.68852726018977]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.71',
       'geometry': {'type': 'Point',
        'coordinates': [-73.97705030183924, 40.67232052268197]},
       'geometry_name': 'geom',
       'properties': {'name': 'Park Slope',
        'stacked': 2,
        'annoline1': 'Park',
        'annoline2': 'Slope',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.97705030183924,
         40.67232052268197,
         -73.97705030183924,
         40.67232052268197]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.72',
       'geometry': {'type': 'Point',
        'coordinates': [-73.87661596457296, 40.68239101144211]},
       'geometry_name': 'geom',
       'properties': {'name': 'Cypress Hills',
        'stacked': 2,
        'annoline1': 'Cypress',
        'annoline2': 'Hills',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.87661596457296,
         40.68239101144211,
         -73.87661596457296,
         40.68239101144211]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.73',
       'geometry': {'type': 'Point',
        'coordinates': [-73.88069863917366, 40.669925700847045]},
       'geometry_name': 'geom',
       'properties': {'name': 'East New York',
        'stacked': 1,
        'annoline1': 'East New York',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.88069863917366,
         40.669925700847045,
         -73.88069863917366,
         40.669925700847045]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.74',
       'geometry': {'type': 'Point',
        'coordinates': [-73.87936970045875, 40.64758905230874]},
       'geometry_name': 'geom',
       'properties': {'name': 'Starrett City',
        'stacked': 2,
        'annoline1': 'Starrett',
        'annoline2': 'City',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.87936970045875,
         40.64758905230874,
         -73.87936970045875,
         40.64758905230874]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.75',
       'geometry': {'type': 'Point',
        'coordinates': [-73.90209269778966, 40.63556432797428]},
       'geometry_name': 'geom',
       'properties': {'name': 'Canarsie',
        'stacked': 1,
        'annoline1': 'Canarsie',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.90209269778966,
         40.63556432797428,
         -73.90209269778966,
         40.63556432797428]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.76',
       'geometry': {'type': 'Point',
        'coordinates': [-73.92911302644674, 40.630446043757466]},
       'geometry_name': 'geom',
       'properties': {'name': 'Flatlands',
        'stacked': 1,
        'annoline1': 'Flatlands',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.92911302644674,
         40.630446043757466,
         -73.92911302644674,
         40.630446043757466]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.77',
       'geometry': {'type': 'Point',
        'coordinates': [-73.90818571777423, 40.606336421685626]},
       'geometry_name': 'geom',
       'properties': {'name': 'Mill Island',
        'stacked': 2,
        'annoline1': 'Mill',
        'annoline2': 'Island',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.90818571777423,
         40.606336421685626,
         -73.90818571777423,
         40.606336421685626]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.78',
       'geometry': {'type': 'Point',
        'coordinates': [-73.94353722891886, 40.57791350308657]},
       'geometry_name': 'geom',
       'properties': {'name': 'Manhattan Beach',
        'stacked': 2,
        'annoline1': 'Manhattan',
        'annoline2': 'Beach',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.94353722891886,
         40.57791350308657,
         -73.94353722891886,
         40.57791350308657]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.79',
       'geometry': {'type': 'Point',
        'coordinates': [-73.98868295821637, 40.57429256471601]},
       'geometry_name': 'geom',
       'properties': {'name': 'Coney Island',
        'stacked': 1,
        'annoline1': 'Coney Island',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.98868295821637,
         40.57429256471601,
         -73.98868295821637,
         40.57429256471601]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.80',
       'geometry': {'type': 'Point',
        'coordinates': [-73.99875221443519, 40.59951870282238]},
       'geometry_name': 'geom',
       'properties': {'name': 'Bath Beach',
        'stacked': 2,
        'annoline1': 'Bath',
        'annoline2': 'Beach',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.99875221443519,
         40.59951870282238,
         -73.99875221443519,
         40.59951870282238]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.81',
       'geometry': {'type': 'Point',
        'coordinates': [-73.99049823044811, 40.633130512758015]},
       'geometry_name': 'geom',
       'properties': {'name': 'Borough Park',
        'stacked': 2,
        'annoline1': 'Borough',
        'annoline2': 'Park',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.99049823044811,
         40.633130512758015,
         -73.99049823044811,
         40.633130512758015]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.82',
       'geometry': {'type': 'Point',
        'coordinates': [-74.01931375636022, 40.619219457722636]},
       'geometry_name': 'geom',
       'properties': {'name': 'Dyker Heights',
        'stacked': 2,
        'annoline1': 'Dyker',
        'annoline2': 'Heights',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-74.01931375636022,
         40.619219457722636,
         -74.01931375636022,
         40.619219457722636]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.83',
       'geometry': {'type': 'Point',
        'coordinates': [-73.93010170691196, 40.590848433902046]},
       'geometry_name': 'geom',
       'properties': {'name': 'Gerritsen Beach',
        'stacked': 2,
        'annoline1': 'Gerritsen',
        'annoline2': 'Beach',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.93010170691196,
         40.590848433902046,
         -73.93010170691196,
         40.590848433902046]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.84',
       'geometry': {'type': 'Point',
        'coordinates': [-73.93134404108497, 40.609747779894604]},
       'geometry_name': 'geom',
       'properties': {'name': 'Marine Park',
        'stacked': 1,
        'annoline1': 'Marine Park',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.93134404108497,
         40.609747779894604,
         -73.93134404108497,
         40.609747779894604]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.85',
       'geometry': {'type': 'Point',
        'coordinates': [-73.96784306216367, 40.693229421881504]},
       'geometry_name': 'geom',
       'properties': {'name': 'Clinton Hill',
        'stacked': 2,
        'annoline1': 'Clinton',
        'annoline2': 'Hill',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.96784306216367,
         40.693229421881504,
         -73.96784306216367,
         40.693229421881504]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.86',
       'geometry': {'type': 'Point',
        'coordinates': [-74.0078731120024, 40.57637537890224]},
       'geometry_name': 'geom',
       'properties': {'name': 'Sea Gate',
        'stacked': 2,
        'annoline1': 'Sea',
        'annoline2': 'Gate',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-74.0078731120024,
         40.57637537890224,
         -74.0078731120024,
         40.57637537890224]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.87',
       'geometry': {'type': 'Point',
        'coordinates': [-73.98346337431099, 40.69084402109802]},
       'geometry_name': 'geom',
       'properties': {'name': 'Downtown',
        'stacked': 1,
        'annoline1': 'Downtown',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.98346337431099,
         40.69084402109802,
         -73.98346337431099,
         40.69084402109802]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.88',
       'geometry': {'type': 'Point',
        'coordinates': [-73.98374824115798, 40.685682912091444]},
       'geometry_name': 'geom',
       'properties': {'name': 'Boerum Hill',
        'stacked': 2,
        'annoline1': 'Boerum',
        'annoline2': 'Hill',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.98374824115798,
         40.685682912091444,
         -73.98374824115798,
         40.685682912091444]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.89',
       'geometry': {'type': 'Point',
        'coordinates': [-73.95489867077713, 40.658420017469815]},
       'geometry_name': 'geom',
       'properties': {'name': 'Prospect Lefferts Gardens',
        'stacked': 3,
        'annoline1': 'Prospect',
        'annoline2': 'Lefferts',
        'annoline3': 'Gardens',
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.95489867077713,
         40.658420017469815,
         -73.95489867077713,
         40.658420017469815]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.90',
       'geometry': {'type': 'Point',
        'coordinates': [-73.91306831787395, 40.678402554795355]},
       'geometry_name': 'geom',
       'properties': {'name': 'Ocean Hill',
        'stacked': 2,
        'annoline1': 'Ocean',
        'annoline2': 'Hill',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.91306831787395,
         40.678402554795355,
         -73.91306831787395,
         40.678402554795355]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.91',
       'geometry': {'type': 'Point',
        'coordinates': [-73.86797598081334, 40.67856995727479]},
       'geometry_name': 'geom',
       'properties': {'name': 'City Line',
        'stacked': 2,
        'annoline1': 'City',
        'annoline2': 'Line',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.86797598081334,
         40.67856995727479,
         -73.86797598081334,
         40.67856995727479]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.92',
       'geometry': {'type': 'Point',
        'coordinates': [-73.89855633630317, 40.61514955045308]},
       'geometry_name': 'geom',
       'properties': {'name': 'Bergen Beach',
        'stacked': 2,
        'annoline1': 'Bergen',
        'annoline2': 'Beach',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.89855633630317,
         40.61514955045308,
         -73.89855633630317,
         40.61514955045308]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.93',
       'geometry': {'type': 'Point',
        'coordinates': [-73.95759523489838, 40.62559589869843]},
       'geometry_name': 'geom',
       'properties': {'name': 'Midwood',
        'stacked': 1,
        'annoline1': 'Midwood',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.95759523489838,
         40.62559589869843,
         -73.95759523489838,
         40.62559589869843]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.94',
       'geometry': {'type': 'Point',
        'coordinates': [-73.96261316716048, 40.647008603185185]},
       'geometry_name': 'geom',
       'properties': {'name': 'Prospect Park South',
        'stacked': 2,
        'annoline1': 'Prospect',
        'annoline2': 'Park South',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.96261316716048,
         40.647008603185185,
         -73.96261316716048,
         40.647008603185185]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.95',
       'geometry': {'type': 'Point',
        'coordinates': [-73.91607483951324, 40.62384524478419]},
       'geometry_name': 'geom',
       'properties': {'name': 'Georgetown',
        'stacked': 1,
        'annoline1': 'Georgetown',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.91607483951324,
         40.62384524478419,
         -73.91607483951324,
         40.62384524478419]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.96',
       'geometry': {'type': 'Point',
        'coordinates': [-73.93885815269195, 40.70849241041548]},
       'geometry_name': 'geom',
       'properties': {'name': 'East Williamsburg',
        'stacked': 2,
        'annoline1': 'East',
        'annoline2': 'Williamsburg',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.93885815269195,
         40.70849241041548,
         -73.93885815269195,
         40.70849241041548]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.97',
       'geometry': {'type': 'Point',
        'coordinates': [-73.95880857587582, 40.714822906532014]},
       'geometry_name': 'geom',
       'properties': {'name': 'North Side',
        'stacked': 1,
        'annoline1': 'North Side',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.95880857587582,
         40.714822906532014,
         -73.95880857587582,
         40.714822906532014]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.98',
       'geometry': {'type': 'Point',
        'coordinates': [-73.95800095153331, 40.71086147265064]},
       'geometry_name': 'geom',
       'properties': {'name': 'South Side',
        'stacked': 1,
        'annoline1': 'South Side',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.95800095153331,
         40.71086147265064,
         -73.95800095153331,
         40.71086147265064]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.99',
       'geometry': {'type': 'Point',
        'coordinates': [-73.96836678035541, 40.61305976667942]},
       'geometry_name': 'geom',
       'properties': {'name': 'Ocean Parkway',
        'stacked': 2,
        'annoline1': 'Ocean',
        'annoline2': 'Parkway',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.96836678035541,
         40.61305976667942,
         -73.96836678035541,
         40.61305976667942]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.100',
       'geometry': {'type': 'Point',
        'coordinates': [-74.03197914537984, 40.61476812694226]},
       'geometry_name': 'geom',
       'properties': {'name': 'Fort Hamilton',
        'stacked': 2,
        'annoline1': 'Fort',
        'annoline2': 'Hamilton',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-74.03197914537984,
         40.61476812694226,
         -74.03197914537984,
         40.61476812694226]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.101',
       'geometry': {'type': 'Point',
        'coordinates': [-73.99427936255978, 40.71561842231432]},
       'geometry_name': 'geom',
       'properties': {'name': 'Chinatown',
        'stacked': 1,
        'annoline1': 'Chinatown',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.99427936255978,
         40.71561842231432,
         -73.99427936255978,
         40.71561842231432]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.102',
       'geometry': {'type': 'Point',
        'coordinates': [-73.93690027985234, 40.85190252555305]},
       'geometry_name': 'geom',
       'properties': {'name': 'Washington Heights',
        'stacked': 2,
        'annoline1': 'Washington',
        'annoline2': 'Heights',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.93690027985234,
         40.85190252555305,
         -73.93690027985234,
         40.85190252555305]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.103',
       'geometry': {'type': 'Point',
        'coordinates': [-73.92121042203897, 40.86768396449915]},
       'geometry_name': 'geom',
       'properties': {'name': 'Inwood',
        'stacked': 1,
        'annoline1': 'Inwood',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.92121042203897,
         40.86768396449915,
         -73.92121042203897,
         40.86768396449915]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.104',
       'geometry': {'type': 'Point',
        'coordinates': [-73.94968791883366, 40.823604284811935]},
       'geometry_name': 'geom',
       'properties': {'name': 'Hamilton Heights',
        'stacked': 2,
        'annoline1': 'Hamilton',
        'annoline2': 'Heights',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.94968791883366,
         40.823604284811935,
         -73.94968791883366,
         40.823604284811935]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.105',
       'geometry': {'type': 'Point',
        'coordinates': [-73.9573853935188, 40.8169344294978]},
       'geometry_name': 'geom',
       'properties': {'name': 'Manhattanville',
        'stacked': 2,
        'annoline1': 'Manhattanville',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.9573853935188,
         40.8169344294978,
         -73.9573853935188,
         40.8169344294978]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.106',
       'geometry': {'type': 'Point',
        'coordinates': [-73.94321112603905, 40.81597606742414]},
       'geometry_name': 'geom',
       'properties': {'name': 'Central Harlem',
        'stacked': 2,
        'annoline1': 'Central',
        'annoline2': 'Harlem',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.94321112603905,
         40.81597606742414,
         -73.94321112603905,
         40.81597606742414]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.107',
       'geometry': {'type': 'Point',
        'coordinates': [-73.94418223148524, 40.79224946663033]},
       'geometry_name': 'geom',
       'properties': {'name': 'East Harlem',
        'stacked': 2,
        'annoline1': 'East',
        'annoline2': 'Harlem',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.94418223148524,
         40.79224946663033,
         -73.94418223148524,
         40.79224946663033]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.108',
       'geometry': {'type': 'Point',
        'coordinates': [-73.96050763135, 40.775638573301805]},
       'geometry_name': 'geom',
       'properties': {'name': 'Upper East Side',
        'stacked': 3,
        'annoline1': 'Upper',
        'annoline2': 'East',
        'annoline3': 'Side',
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.96050763135,
         40.775638573301805,
         -73.96050763135,
         40.775638573301805]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.109',
       'geometry': {'type': 'Point',
        'coordinates': [-73.94711784471826, 40.775929849884875]},
       'geometry_name': 'geom',
       'properties': {'name': 'Yorkville',
        'stacked': 1,
        'annoline1': 'Yorkville',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.94711784471826,
         40.775929849884875,
         -73.94711784471826,
         40.775929849884875]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.110',
       'geometry': {'type': 'Point',
        'coordinates': [-73.9588596881376, 40.76811265828733]},
       'geometry_name': 'geom',
       'properties': {'name': 'Lenox Hill',
        'stacked': 2,
        'annoline1': 'Lenox',
        'annoline2': 'Hill',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.9588596881376,
         40.76811265828733,
         -73.9588596881376,
         40.76811265828733]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.111',
       'geometry': {'type': 'Point',
        'coordinates': [-73.94916769227953, 40.76215960576283]},
       'geometry_name': 'geom',
       'properties': {'name': 'Roosevelt Island',
        'stacked': 1,
        'annoline1': 'Roosevelt Island',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 56,
        'borough': 'Manhattan',
        'bbox': [-73.94916769227953,
         40.76215960576283,
         -73.94916769227953,
         40.76215960576283]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.112',
       'geometry': {'type': 'Point',
        'coordinates': [-73.97705923630603, 40.787657998534854]},
       'geometry_name': 'geom',
       'properties': {'name': 'Upper West Side',
        'stacked': 3,
        'annoline1': 'Upper',
        'annoline2': 'West',
        'annoline3': 'Side',
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.97705923630603,
         40.787657998534854,
         -73.97705923630603,
         40.787657998534854]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.113',
       'geometry': {'type': 'Point',
        'coordinates': [-73.98533777001262, 40.77352888942166]},
       'geometry_name': 'geom',
       'properties': {'name': 'Lincoln Square',
        'stacked': 2,
        'annoline1': 'Lincoln',
        'annoline2': 'Square',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.98533777001262,
         40.77352888942166,
         -73.98533777001262,
         40.77352888942166]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.114',
       'geometry': {'type': 'Point',
        'coordinates': [-73.99611936309479, 40.75910089146212]},
       'geometry_name': 'geom',
       'properties': {'name': 'Clinton',
        'stacked': 1,
        'annoline1': 'Clinton',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.99611936309479,
         40.75910089146212,
         -73.99611936309479,
         40.75910089146212]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.115',
       'geometry': {'type': 'Point',
        'coordinates': [-73.98166882730304, 40.75469110270623]},
       'geometry_name': 'geom',
       'properties': {'name': 'Midtown',
        'stacked': 1,
        'annoline1': 'Midtown',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.98166882730304,
         40.75469110270623,
         -73.98166882730304,
         40.75469110270623]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.116',
       'geometry': {'type': 'Point',
        'coordinates': [-73.97833207924127, 40.748303077252174]},
       'geometry_name': 'geom',
       'properties': {'name': 'Murray Hill',
        'stacked': 2,
        'annoline1': 'Murray',
        'annoline2': 'Hill',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.97833207924127,
         40.748303077252174,
         -73.97833207924127,
         40.748303077252174]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.117',
       'geometry': {'type': 'Point',
        'coordinates': [-74.00311633472813, 40.744034706747975]},
       'geometry_name': 'geom',
       'properties': {'name': 'Chelsea',
        'stacked': 1,
        'annoline1': 'Chelsea',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-74.00311633472813,
         40.744034706747975,
         -74.00311633472813,
         40.744034706747975]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.118',
       'geometry': {'type': 'Point',
        'coordinates': [-73.99991402945902, 40.72693288536128]},
       'geometry_name': 'geom',
       'properties': {'name': 'Greenwich Village',
        'stacked': 2,
        'annoline1': 'Greenwich',
        'annoline2': 'Village',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.99991402945902,
         40.72693288536128,
         -73.99991402945902,
         40.72693288536128]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.119',
       'geometry': {'type': 'Point',
        'coordinates': [-73.98222616506416, 40.727846777270244]},
       'geometry_name': 'geom',
       'properties': {'name': 'East Village',
        'stacked': 2,
        'annoline1': 'East',
        'annoline2': 'Village',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.98222616506416,
         40.727846777270244,
         -73.98222616506416,
         40.727846777270244]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.120',
       'geometry': {'type': 'Point',
        'coordinates': [-73.98089031999291, 40.71780674892765]},
       'geometry_name': 'geom',
       'properties': {'name': 'Lower East Side',
        'stacked': 3,
        'annoline1': 'Lower',
        'annoline2': 'East',
        'annoline3': 'Side',
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.98089031999291,
         40.71780674892765,
         -73.98089031999291,
         40.71780674892765]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.121',
       'geometry': {'type': 'Point',
        'coordinates': [-74.01068328559087, 40.721521967443216]},
       'geometry_name': 'geom',
       'properties': {'name': 'Tribeca',
        'stacked': 1,
        'annoline1': 'Tribeca',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-74.01068328559087,
         40.721521967443216,
         -74.01068328559087,
         40.721521967443216]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.122',
       'geometry': {'type': 'Point',
        'coordinates': [-73.99730467208073, 40.71932379395907]},
       'geometry_name': 'geom',
       'properties': {'name': 'Little Italy',
        'stacked': 2,
        'annoline1': 'Little',
        'annoline2': 'Italy',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.99730467208073,
         40.71932379395907,
         -73.99730467208073,
         40.71932379395907]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.123',
       'geometry': {'type': 'Point',
        'coordinates': [-74.00065666959759, 40.72218384131794]},
       'geometry_name': 'geom',
       'properties': {'name': 'Soho',
        'stacked': 1,
        'annoline1': 'Soho',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-74.00065666959759,
         40.72218384131794,
         -74.00065666959759,
         40.72218384131794]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.124',
       'geometry': {'type': 'Point',
        'coordinates': [-74.00617998126812, 40.73443393572434]},
       'geometry_name': 'geom',
       'properties': {'name': 'West Village',
        'stacked': 2,
        'annoline1': 'West',
        'annoline2': 'Village',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-74.00617998126812,
         40.73443393572434,
         -74.00617998126812,
         40.73443393572434]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.125',
       'geometry': {'type': 'Point',
        'coordinates': [-73.96428617740655, 40.797307041702865]},
       'geometry_name': 'geom',
       'properties': {'name': 'Manhattan Valley',
        'stacked': 2,
        'annoline1': 'Manhattan',
        'annoline2': 'Valley',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.96428617740655,
         40.797307041702865,
         -73.96428617740655,
         40.797307041702865]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.126',
       'geometry': {'type': 'Point',
        'coordinates': [-73.96389627905332, 40.807999738165826]},
       'geometry_name': 'geom',
       'properties': {'name': 'Morningside Heights',
        'stacked': 2,
        'annoline1': 'Morningside',
        'annoline2': 'Heights',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.96389627905332,
         40.807999738165826,
         -73.96389627905332,
         40.807999738165826]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.127',
       'geometry': {'type': 'Point',
        'coordinates': [-73.98137594833541, 40.737209832715]},
       'geometry_name': 'geom',
       'properties': {'name': 'Gramercy',
        'stacked': 1,
        'annoline1': 'Gramercy',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.98137594833541,
         40.737209832715,
         -73.98137594833541,
         40.737209832715]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.128',
       'geometry': {'type': 'Point',
        'coordinates': [-74.01686930508617, 40.71193198394565]},
       'geometry_name': 'geom',
       'properties': {'name': 'Battery Park City',
        'stacked': 3,
        'annoline1': 'Battery',
        'annoline2': 'Park',
        'annoline3': 'City',
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-74.01686930508617,
         40.71193198394565,
         -74.01686930508617,
         40.71193198394565]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.129',
       'geometry': {'type': 'Point',
        'coordinates': [-74.0106654452127, 40.70710710727048]},
       'geometry_name': 'geom',
       'properties': {'name': 'Financial District',
        'stacked': 2,
        'annoline1': 'Financial',
        'annoline2': 'District',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-74.0106654452127,
         40.70710710727048,
         -74.0106654452127,
         40.70710710727048]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.130',
       'geometry': {'type': 'Point',
        'coordinates': [-73.91565374304234, 40.76850859335492]},
       'geometry_name': 'geom',
       'properties': {'name': 'Astoria',
        'stacked': 1,
        'annoline1': 'Astoria',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.91565374304234,
         40.76850859335492,
         -73.91565374304234,
         40.76850859335492]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.131',
       'geometry': {'type': 'Point',
        'coordinates': [-73.90184166838284, 40.74634908860222]},
       'geometry_name': 'geom',
       'properties': {'name': 'Woodside',
        'stacked': 1,
        'annoline1': 'Woodside',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.90184166838284,
         40.74634908860222,
         -73.90184166838284,
         40.74634908860222]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.132',
       'geometry': {'type': 'Point',
        'coordinates': [-73.88282109164365, 40.75198138007367]},
       'geometry_name': 'geom',
       'properties': {'name': 'Jackson Heights',
        'stacked': 2,
        'annoline1': 'Jackson',
        'annoline2': 'Heights',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.88282109164365,
         40.75198138007367,
         -73.88282109164365,
         40.75198138007367]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.133',
       'geometry': {'type': 'Point',
        'coordinates': [-73.88165622288388, 40.744048505122024]},
       'geometry_name': 'geom',
       'properties': {'name': 'Elmhurst',
        'stacked': 1,
        'annoline1': 'Elmhurst',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.88165622288388,
         40.744048505122024,
         -73.88165622288388,
         40.744048505122024]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.134',
       'geometry': {'type': 'Point',
        'coordinates': [-73.8381376460028, 40.65422527738487]},
       'geometry_name': 'geom',
       'properties': {'name': 'Howard Beach',
        'stacked': 2,
        'annoline1': 'Howard',
        'annoline2': 'Beach',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.8381376460028,
         40.65422527738487,
         -73.8381376460028,
         40.65422527738487]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.135',
       'geometry': {'type': 'Point',
        'coordinates': [-73.85682497345258, 40.74238175015667]},
       'geometry_name': 'geom',
       'properties': {'name': 'Corona',
        'stacked': 1,
        'annoline1': 'Corona',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.85682497345258,
         40.74238175015667,
         -73.85682497345258,
         40.74238175015667]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.136',
       'geometry': {'type': 'Point',
        'coordinates': [-73.84447500788983, 40.72526378216503]},
       'geometry_name': 'geom',
       'properties': {'name': 'Forest Hills',
        'stacked': 2,
        'annoline1': 'Forest',
        'annoline2': 'Hills',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.84447500788983,
         40.72526378216503,
         -73.84447500788983,
         40.72526378216503]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.137',
       'geometry': {'type': 'Point',
        'coordinates': [-73.82981905825703, 40.7051790354148]},
       'geometry_name': 'geom',
       'properties': {'name': 'Kew Gardens',
        'stacked': 2,
        'annoline1': 'Kew',
        'annoline2': 'Gardens',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.82981905825703,
         40.7051790354148,
         -73.82981905825703,
         40.7051790354148]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.138',
       'geometry': {'type': 'Point',
        'coordinates': [-73.83183321446887, 40.69794731471763]},
       'geometry_name': 'geom',
       'properties': {'name': 'Richmond Hill',
        'stacked': 2,
        'annoline1': 'Richmond',
        'annoline2': 'Hill',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.83183321446887,
         40.69794731471763,
         -73.83183321446887,
         40.69794731471763]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.139',
       'geometry': {'type': 'Point',
        'coordinates': [-73.83177300329582, 40.76445419697846]},
       'geometry_name': 'geom',
       'properties': {'name': 'Flushing',
        'stacked': 1,
        'annoline1': 'Flushing',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.83177300329582,
         40.76445419697846,
         -73.83177300329582,
         40.76445419697846]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.140',
       'geometry': {'type': 'Point',
        'coordinates': [-73.93920223915505, 40.75021734610528]},
       'geometry_name': 'geom',
       'properties': {'name': 'Long Island City',
        'stacked': 3,
        'annoline1': 'Long',
        'annoline2': 'Island',
        'annoline3': 'City',
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.93920223915505,
         40.75021734610528,
         -73.93920223915505,
         40.75021734610528]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.141',
       'geometry': {'type': 'Point',
        'coordinates': [-73.92691617561577, 40.74017628351924]},
       'geometry_name': 'geom',
       'properties': {'name': 'Sunnyside',
        'stacked': 1,
        'annoline1': 'Sunnyside',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.92691617561577,
         40.74017628351924,
         -73.92691617561577,
         40.74017628351924]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.142',
       'geometry': {'type': 'Point',
        'coordinates': [-73.86704147658772, 40.76407323883091]},
       'geometry_name': 'geom',
       'properties': {'name': 'East Elmhurst',
        'stacked': 2,
        'annoline1': 'East',
        'annoline2': 'Elmhurst',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.86704147658772,
         40.76407323883091,
         -73.86704147658772,
         40.76407323883091]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.143',
       'geometry': {'type': 'Point',
        'coordinates': [-73.89621713626859, 40.725427374093606]},
       'geometry_name': 'geom',
       'properties': {'name': 'Maspeth',
        'stacked': 1,
        'annoline1': 'Maspeth',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.89621713626859,
         40.725427374093606,
         -73.89621713626859,
         40.725427374093606]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.144',
       'geometry': {'type': 'Point',
        'coordinates': [-73.90143517559589, 40.70832315613858]},
       'geometry_name': 'geom',
       'properties': {'name': 'Ridgewood',
        'stacked': 1,
        'annoline1': 'Ridgewood',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.90143517559589,
         40.70832315613858,
         -73.90143517559589,
         40.70832315613858]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.145',
       'geometry': {'type': 'Point',
        'coordinates': [-73.87074167435605, 40.70276242967838]},
       'geometry_name': 'geom',
       'properties': {'name': 'Glendale',
        'stacked': 1,
        'annoline1': 'Glendale',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.87074167435605,
         40.70276242967838,
         -73.87074167435605,
         40.70276242967838]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.146',
       'geometry': {'type': 'Point',
        'coordinates': [-73.8578268690537, 40.72897409480735]},
       'geometry_name': 'geom',
       'properties': {'name': 'Rego Park',
        'stacked': 1,
        'annoline1': 'Rego Park',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.8578268690537,
         40.72897409480735,
         -73.8578268690537,
         40.72897409480735]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.147',
       'geometry': {'type': 'Point',
        'coordinates': [-73.8581104655432, 40.68988687915789]},
       'geometry_name': 'geom',
       'properties': {'name': 'Woodhaven',
        'stacked': 1,
        'annoline1': 'Woodhaven',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.8581104655432,
         40.68988687915789,
         -73.8581104655432,
         40.68988687915789]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.148',
       'geometry': {'type': 'Point',
        'coordinates': [-73.84320266173447, 40.680708468265415]},
       'geometry_name': 'geom',
       'properties': {'name': 'Ozone Park',
        'stacked': 1,
        'annoline1': 'Ozone Park',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.84320266173447,
         40.680708468265415,
         -73.84320266173447,
         40.680708468265415]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.149',
       'geometry': {'type': 'Point',
        'coordinates': [-73.80986478649041, 40.66854957767195]},
       'geometry_name': 'geom',
       'properties': {'name': 'South Ozone Park',
        'stacked': 2,
        'annoline1': 'South',
        'annoline2': 'Ozone Park',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.80986478649041,
         40.66854957767195,
         -73.80986478649041,
         40.66854957767195]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.150',
       'geometry': {'type': 'Point',
        'coordinates': [-73.84304528896125, 40.784902749260205]},
       'geometry_name': 'geom',
       'properties': {'name': 'College Point',
        'stacked': 2,
        'annoline1': 'College',
        'annoline2': 'Point',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.84304528896125,
         40.784902749260205,
         -73.84304528896125,
         40.784902749260205]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.151',
       'geometry': {'type': 'Point',
        'coordinates': [-73.81420216610863, 40.78129076602694]},
       'geometry_name': 'geom',
       'properties': {'name': 'Whitestone',
        'stacked': 1,
        'annoline1': 'Whitestone',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.81420216610863,
         40.78129076602694,
         -73.81420216610863,
         40.78129076602694]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.152',
       'geometry': {'type': 'Point',
        'coordinates': [-73.7742736306867, 40.76604063281064]},
       'geometry_name': 'geom',
       'properties': {'name': 'Bayside',
        'stacked': 1,
        'annoline1': 'Bayside',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.7742736306867,
         40.76604063281064,
         -73.7742736306867,
         40.76604063281064]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.153',
       'geometry': {'type': 'Point',
        'coordinates': [-73.79176243728061, 40.76172954903262]},
       'geometry_name': 'geom',
       'properties': {'name': 'Auburndale',
        'stacked': 1,
        'annoline1': 'Auburndale',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.79176243728061,
         40.76172954903262,
         -73.79176243728061,
         40.76172954903262]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.154',
       'geometry': {'type': 'Point',
        'coordinates': [-73.7388977558074, 40.7708261928267]},
       'geometry_name': 'geom',
       'properties': {'name': 'Little Neck',
        'stacked': 2,
        'annoline1': 'Little',
        'annoline2': 'Neck',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.7388977558074,
         40.7708261928267,
         -73.7388977558074,
         40.7708261928267]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.155',
       'geometry': {'type': 'Point',
        'coordinates': [-73.7424982072733, 40.76684609790763]},
       'geometry_name': 'geom',
       'properties': {'name': 'Douglaston',
        'stacked': 1,
        'annoline1': 'Douglaston',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.7424982072733,
         40.76684609790763,
         -73.7424982072733,
         40.76684609790763]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.156',
       'geometry': {'type': 'Point',
        'coordinates': [-73.71548118999145, 40.74944079974332]},
       'geometry_name': 'geom',
       'properties': {'name': 'Glen Oaks',
        'stacked': 2,
        'annoline1': 'Glen',
        'annoline2': 'Oaks',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.71548118999145,
         40.74944079974332,
         -73.71548118999145,
         40.74944079974332]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.157',
       'geometry': {'type': 'Point',
        'coordinates': [-73.72012814826903, 40.72857318176675]},
       'geometry_name': 'geom',
       'properties': {'name': 'Bellerose',
        'stacked': 1,
        'annoline1': 'Bellerose',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.72012814826903,
         40.72857318176675,
         -73.72012814826903,
         40.72857318176675]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.158',
       'geometry': {'type': 'Point',
        'coordinates': [-73.82087764933566, 40.722578244228046]},
       'geometry_name': 'geom',
       'properties': {'name': 'Kew Gardens Hills',
        'stacked': 3,
        'annoline1': 'Kew',
        'annoline2': 'Gardens',
        'annoline3': 'Hills',
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.82087764933566,
         40.722578244228046,
         -73.82087764933566,
         40.722578244228046]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.159',
       'geometry': {'type': 'Point',
        'coordinates': [-73.78271337003264, 40.7343944653313]},
       'geometry_name': 'geom',
       'properties': {'name': 'Fresh Meadows',
        'stacked': 2,
        'annoline1': 'Fresh',
        'annoline2': 'Meadows',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.78271337003264,
         40.7343944653313,
         -73.78271337003264,
         40.7343944653313]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.160',
       'geometry': {'type': 'Point',
        'coordinates': [-73.81174822458634, 40.71093547252271]},
       'geometry_name': 'geom',
       'properties': {'name': 'Briarwood',
        'stacked': 1,
        'annoline1': 'Briarwood',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.81174822458634,
         40.71093547252271,
         -73.81174822458634,
         40.71093547252271]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.161',
       'geometry': {'type': 'Point',
        'coordinates': [-73.79690165888289, 40.70465736068717]},
       'geometry_name': 'geom',
       'properties': {'name': 'Jamaica Center',
        'stacked': 2,
        'annoline1': 'Jamaica',
        'annoline2': 'Center',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.79690165888289,
         40.70465736068717,
         -73.79690165888289,
         40.70465736068717]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.162',
       'geometry': {'type': 'Point',
        'coordinates': [-73.75494976234332, 40.74561857141855]},
       'geometry_name': 'geom',
       'properties': {'name': 'Oakland Gardens',
        'stacked': 2,
        'annoline1': 'Oakland',
        'annoline2': 'Gardens',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.75494976234332,
         40.74561857141855,
         -73.75494976234332,
         40.74561857141855]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.163',
       'geometry': {'type': 'Point',
        'coordinates': [-73.73871484578424, 40.718893092167356]},
       'geometry_name': 'geom',
       'properties': {'name': 'Queens Village',
        'stacked': 2,
        'annoline1': 'Queens',
        'annoline2': 'Village',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.73871484578424,
         40.718893092167356,
         -73.73871484578424,
         40.718893092167356]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.164',
       'geometry': {'type': 'Point',
        'coordinates': [-73.75925009335594, 40.71124344191904]},
       'geometry_name': 'geom',
       'properties': {'name': 'Hollis',
        'stacked': 1,
        'annoline1': 'Hollis',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.75925009335594,
         40.71124344191904,
         -73.75925009335594,
         40.71124344191904]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.165',
       'geometry': {'type': 'Point',
        'coordinates': [-73.7904261313554, 40.696911253789885]},
       'geometry_name': 'geom',
       'properties': {'name': 'South Jamaica',
        'stacked': 1,
        'annoline1': 'South Jamaica',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.7904261313554,
         40.696911253789885,
         -73.7904261313554,
         40.696911253789885]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.166',
       'geometry': {'type': 'Point',
        'coordinates': [-73.75867603727717, 40.69444538522359]},
       'geometry_name': 'geom',
       'properties': {'name': 'St. Albans',
        'stacked': 1,
        'annoline1': 'St. Albans',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.75867603727717,
         40.69444538522359,
         -73.75867603727717,
         40.69444538522359]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.167',
       'geometry': {'type': 'Point',
        'coordinates': [-73.77258787620906, 40.67521139591733]},
       'geometry_name': 'geom',
       'properties': {'name': 'Rochdale',
        'stacked': 1,
        'annoline1': 'Rochdale',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.77258787620906,
         40.67521139591733,
         -73.77258787620906,
         40.67521139591733]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.168',
       'geometry': {'type': 'Point',
        'coordinates': [-73.76042092682287, 40.666230490368584]},
       'geometry_name': 'geom',
       'properties': {'name': 'Springfield Gardens',
        'stacked': 2,
        'annoline1': 'Springfield',
        'annoline2': 'Gardens',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.76042092682287,
         40.666230490368584,
         -73.76042092682287,
         40.666230490368584]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.169',
       'geometry': {'type': 'Point',
        'coordinates': [-73.73526873708026, 40.692774639160845]},
       'geometry_name': 'geom',
       'properties': {'name': 'Cambria Heights',
        'stacked': 2,
        'annoline1': 'Cambria',
        'annoline2': 'Heights',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.73526873708026,
         40.692774639160845,
         -73.73526873708026,
         40.692774639160845]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.170',
       'geometry': {'type': 'Point',
        'coordinates': [-73.73526079428278, 40.659816433428084]},
       'geometry_name': 'geom',
       'properties': {'name': 'Rosedale',
        'stacked': 1,
        'annoline1': 'Rosedale',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.73526079428278,
         40.659816433428084,
         -73.73526079428278,
         40.659816433428084]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.171',
       'geometry': {'type': 'Point',
        'coordinates': [-73.75497968043872, 40.603134432500894]},
       'geometry_name': 'geom',
       'properties': {'name': 'Far Rockaway',
        'stacked': 2,
        'annoline1': 'Far Rockaway',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.75497968043872,
         40.603134432500894,
         -73.75497968043872,
         40.603134432500894]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.172',
       'geometry': {'type': 'Point',
        'coordinates': [-73.8200548911032, 40.60302658351238]},
       'geometry_name': 'geom',
       'properties': {'name': 'Broad Channel',
        'stacked': 2,
        'annoline1': 'Broad',
        'annoline2': 'Channel',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.8200548911032,
         40.60302658351238,
         -73.8200548911032,
         40.60302658351238]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.173',
       'geometry': {'type': 'Point',
        'coordinates': [-73.92551196994168, 40.55740128845452]},
       'geometry_name': 'geom',
       'properties': {'name': 'Breezy Point',
        'stacked': 2,
        'annoline1': 'Breezy',
        'annoline2': 'Point',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.92551196994168,
         40.55740128845452,
         -73.92551196994168,
         40.55740128845452]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.174',
       'geometry': {'type': 'Point',
        'coordinates': [-73.90228960391673, 40.775923015642896]},
       'geometry_name': 'geom',
       'properties': {'name': 'Steinway',
        'stacked': 1,
        'annoline1': 'Steinway',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.90228960391673,
         40.775923015642896,
         -73.90228960391673,
         40.775923015642896]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.175',
       'geometry': {'type': 'Point',
        'coordinates': [-73.80436451720988, 40.79278140360048]},
       'geometry_name': 'geom',
       'properties': {'name': 'Beechhurst',
        'stacked': 1,
        'annoline1': 'Beechhurst',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.80436451720988,
         40.79278140360048,
         -73.80436451720988,
         40.79278140360048]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.176',
       'geometry': {'type': 'Point',
        'coordinates': [-73.7768022262158, 40.782842806245554]},
       'geometry_name': 'geom',
       'properties': {'name': 'Bay Terrace',
        'stacked': 2,
        'annoline1': 'Bay',
        'annoline2': 'Terrace',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.7768022262158,
         40.782842806245554,
         -73.7768022262158,
         40.782842806245554]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.177',
       'geometry': {'type': 'Point',
        'coordinates': [-73.77613282391705, 40.595641807368494]},
       'geometry_name': 'geom',
       'properties': {'name': 'Edgemere',
        'stacked': 1,
        'annoline1': 'Edgemere',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.77613282391705,
         40.595641807368494,
         -73.77613282391705,
         40.595641807368494]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.178',
       'geometry': {'type': 'Point',
        'coordinates': [-73.79199233136943, 40.58914394372971]},
       'geometry_name': 'geom',
       'properties': {'name': 'Arverne',
        'stacked': 1,
        'annoline1': 'Arverne',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.79199233136943,
         40.58914394372971,
         -73.79199233136943,
         40.58914394372971]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.179',
       'geometry': {'type': 'Point',
        'coordinates': [-73.82236121088751, 40.582801696845586]},
       'geometry_name': 'geom',
       'properties': {'name': 'Rockaway Beach',
        'stacked': 2,
        'annoline1': 'Rockaway',
        'annoline2': 'Beach',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.82236121088751,
         40.582801696845586,
         -73.82236121088751,
         40.582801696845586]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.180',
       'geometry': {'type': 'Point',
        'coordinates': [-73.85754672410827, 40.572036730217015]},
       'geometry_name': 'geom',
       'properties': {'name': 'Neponsit',
        'stacked': 1,
        'annoline1': 'Neponsit',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.85754672410827,
         40.572036730217015,
         -73.85754672410827,
         40.572036730217015]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.181',
       'geometry': {'type': 'Point',
        'coordinates': [-73.81276269135866, 40.764126122614066]},
       'geometry_name': 'geom',
       'properties': {'name': 'Murray Hill',
        'stacked': 2,
        'annoline1': 'Murray',
        'annoline2': 'Hill',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.81276269135866,
         40.764126122614066,
         -73.81276269135866,
         40.764126122614066]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.182',
       'geometry': {'type': 'Point',
        'coordinates': [-73.70884705889246, 40.741378421945434]},
       'geometry_name': 'geom',
       'properties': {'name': 'Floral Park',
        'stacked': 1,
        'annoline1': 'Floral Park',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.70884705889246,
         40.741378421945434,
         -73.70884705889246,
         40.741378421945434]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.183',
       'geometry': {'type': 'Point',
        'coordinates': [-73.76714166714729, 40.7209572076444]},
       'geometry_name': 'geom',
       'properties': {'name': 'Holliswood',
        'stacked': 1,
        'annoline1': 'Holliswood',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.76714166714729,
         40.7209572076444,
         -73.76714166714729,
         40.7209572076444]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.184',
       'geometry': {'type': 'Point',
        'coordinates': [-73.7872269693666, 40.71680483014613]},
       'geometry_name': 'geom',
       'properties': {'name': 'Jamaica Estates',
        'stacked': 2,
        'annoline1': 'Jamaica',
        'annoline2': 'Estates',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.7872269693666,
         40.71680483014613,
         -73.7872269693666,
         40.71680483014613]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.185',
       'geometry': {'type': 'Point',
        'coordinates': [-73.82580915110559, 40.7445723092867]},
       'geometry_name': 'geom',
       'properties': {'name': 'Queensboro Hill',
        'stacked': 2,
        'annoline1': 'Queensboro',
        'annoline2': 'Hill',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.82580915110559,
         40.7445723092867,
         -73.82580915110559,
         40.7445723092867]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.186',
       'geometry': {'type': 'Point',
        'coordinates': [-73.79760300912672, 40.723824901829204]},
       'geometry_name': 'geom',
       'properties': {'name': 'Hillcrest',
        'stacked': 1,
        'annoline1': 'Hillcrest',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.79760300912672,
         40.723824901829204,
         -73.79760300912672,
         40.723824901829204]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.187',
       'geometry': {'type': 'Point',
        'coordinates': [-73.93157506072878, 40.761704526054146]},
       'geometry_name': 'geom',
       'properties': {'name': 'Ravenswood',
        'stacked': 1,
        'annoline1': 'Ravenswood',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.93157506072878,
         40.761704526054146,
         -73.93157506072878,
         40.761704526054146]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.188',
       'geometry': {'type': 'Point',
        'coordinates': [-73.84963782402441, 40.66391841925139]},
       'geometry_name': 'geom',
       'properties': {'name': 'Lindenwood',
        'stacked': 1,
        'annoline1': 'Lindenwood',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.84963782402441,
         40.66391841925139,
         -73.84963782402441,
         40.66391841925139]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.189',
       'geometry': {'type': 'Point',
        'coordinates': [-73.74025607989822, 40.66788389660247]},
       'geometry_name': 'geom',
       'properties': {'name': 'Laurelton',
        'stacked': 1,
        'annoline1': 'Laurelton',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.74025607989822,
         40.66788389660247,
         -73.74025607989822,
         40.66788389660247]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.190',
       'geometry': {'type': 'Point',
        'coordinates': [-73.8625247141374, 40.736074570830795]},
       'geometry_name': 'geom',
       'properties': {'name': 'Lefrak City',
        'stacked': 2,
        'annoline1': 'Lefrak',
        'annoline2': 'City',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.8625247141374,
         40.736074570830795,
         -73.8625247141374,
         40.736074570830795]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.191',
       'geometry': {'type': 'Point',
        'coordinates': [-73.8540175039252, 40.57615556543109]},
       'geometry_name': 'geom',
       'properties': {'name': 'Belle Harbor',
        'stacked': 1,
        'annoline1': 'Belle Harbor',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.8540175039252,
         40.57615556543109,
         -73.8540175039252,
         40.57615556543109]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.192',
       'geometry': {'type': 'Point',
        'coordinates': [-73.84153370226186, 40.58034295646131]},
       'geometry_name': 'geom',
       'properties': {'name': 'Rockaway Park',
        'stacked': 1,
        'annoline1': 'Rockaway Park',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.84153370226186,
         40.58034295646131,
         -73.84153370226186,
         40.58034295646131]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.193',
       'geometry': {'type': 'Point',
        'coordinates': [-73.79664750844047, 40.59771061565768]},
       'geometry_name': 'geom',
       'properties': {'name': 'Somerville',
        'stacked': 1,
        'annoline1': 'Somerville',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.79664750844047,
         40.59771061565768,
         -73.79664750844047,
         40.59771061565768]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.194',
       'geometry': {'type': 'Point',
        'coordinates': [-73.75175310731153, 40.66000322733613]},
       'geometry_name': 'geom',
       'properties': {'name': 'Brookville',
        'stacked': 1,
        'annoline1': 'Brookville',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.75175310731153,
         40.66000322733613,
         -73.75175310731153,
         40.66000322733613]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.195',
       'geometry': {'type': 'Point',
        'coordinates': [-73.73889198912481, 40.73301404027834]},
       'geometry_name': 'geom',
       'properties': {'name': 'Bellaire',
        'stacked': 1,
        'annoline1': 'Bellaire',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.73889198912481,
         40.73301404027834,
         -73.73889198912481,
         40.73301404027834]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.196',
       'geometry': {'type': 'Point',
        'coordinates': [-73.85751790676447, 40.7540709990489]},
       'geometry_name': 'geom',
       'properties': {'name': 'North Corona',
        'stacked': 2,
        'annoline1': 'North',
        'annoline2': 'Corona',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.85751790676447,
         40.7540709990489,
         -73.85751790676447,
         40.7540709990489]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.197',
       'geometry': {'type': 'Point',
        'coordinates': [-73.8410221123401, 40.7146110815117]},
       'geometry_name': 'geom',
       'properties': {'name': 'Forest Hills Gardens',
        'stacked': 3,
        'annoline1': 'Forest',
        'annoline2': 'Hills',
        'annoline3': 'Gardens',
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.8410221123401,
         40.7146110815117,
         -73.8410221123401,
         40.7146110815117]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.198',
       'geometry': {'type': 'Point',
        'coordinates': [-74.07935312512797, 40.6449815710044]},
       'geometry_name': 'geom',
       'properties': {'name': 'St. George',
        'stacked': 2,
        'annoline1': 'St.',
        'annoline2': 'George',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.07935312512797,
         40.6449815710044,
         -74.07935312512797,
         40.6449815710044]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.199',
       'geometry': {'type': 'Point',
        'coordinates': [-74.08701650516625, 40.64061455913511]},
       'geometry_name': 'geom',
       'properties': {'name': 'New Brighton',
        'stacked': 2,
        'annoline1': 'New',
        'annoline2': 'Brighton',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.08701650516625,
         40.64061455913511,
         -74.08701650516625,
         40.64061455913511]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.200',
       'geometry': {'type': 'Point',
        'coordinates': [-74.07790192660066, 40.62692762538176]},
       'geometry_name': 'geom',
       'properties': {'name': 'Stapleton',
        'stacked': 1,
        'annoline1': 'Stapleton',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.07790192660066,
         40.62692762538176,
         -74.07790192660066,
         40.62692762538176]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.201',
       'geometry': {'type': 'Point',
        'coordinates': [-74.06980526716141, 40.61530494652761]},
       'geometry_name': 'geom',
       'properties': {'name': 'Rosebank',
        'stacked': 1,
        'annoline1': 'Rosebank',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.06980526716141,
         40.61530494652761,
         -74.06980526716141,
         40.61530494652761]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.202',
       'geometry': {'type': 'Point',
        'coordinates': [-74.1071817826561, 40.63187892654607]},
       'geometry_name': 'geom',
       'properties': {'name': 'West Brighton',
        'stacked': 2,
        'annoline1': 'West',
        'annoline2': 'Brighton',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.1071817826561,
         40.63187892654607,
         -74.1071817826561,
         40.63187892654607]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.203',
       'geometry': {'type': 'Point',
        'coordinates': [-74.08724819983729, 40.624184791313006]},
       'geometry_name': 'geom',
       'properties': {'name': 'Grymes Hill',
        'stacked': 2,
        'annoline1': 'Grymes',
        'annoline2': 'Hill',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.08724819983729,
         40.624184791313006,
         -74.08724819983729,
         40.624184791313006]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.204',
       'geometry': {'type': 'Point',
        'coordinates': [-74.1113288180088, 40.59706851814673]},
       'geometry_name': 'geom',
       'properties': {'name': 'Todt Hill',
        'stacked': 2,
        'annoline1': 'Todt',
        'annoline2': 'Hill',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.1113288180088,
         40.59706851814673,
         -74.1113288180088,
         40.59706851814673]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.205',
       'geometry': {'type': 'Point',
        'coordinates': [-74.0795529253982, 40.58024741350956]},
       'geometry_name': 'geom',
       'properties': {'name': 'South Beach',
        'stacked': 2,
        'annoline1': 'South',
        'annoline2': 'Beach',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.0795529253982,
         40.58024741350956,
         -74.0795529253982,
         40.58024741350956]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.206',
       'geometry': {'type': 'Point',
        'coordinates': [-74.12943426797008, 40.63366930554365]},
       'geometry_name': 'geom',
       'properties': {'name': 'Port Richmond',
        'stacked': 2,
        'annoline1': 'Port',
        'annoline2': 'Richmond',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.12943426797008,
         40.63366930554365,
         -74.12943426797008,
         40.63366930554365]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.207',
       'geometry': {'type': 'Point',
        'coordinates': [-74.15008537046981, 40.632546390481124]},
       'geometry_name': 'geom',
       'properties': {'name': "Mariner's Harbor",
        'stacked': 2,
        'annoline1': "Mariner's",
        'annoline2': 'Harbor',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.15008537046981,
         40.632546390481124,
         -74.15008537046981,
         40.632546390481124]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.208',
       'geometry': {'type': 'Point',
        'coordinates': [-74.17464532993542, 40.63968297845542]},
       'geometry_name': 'geom',
       'properties': {'name': 'Port Ivory',
        'stacked': 2,
        'annoline1': 'Port',
        'annoline2': 'Ivory',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.17464532993542,
         40.63968297845542,
         -74.17464532993542,
         40.63968297845542]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.209',
       'geometry': {'type': 'Point',
        'coordinates': [-74.11918058534842, 40.61333593766742]},
       'geometry_name': 'geom',
       'properties': {'name': 'Castleton Corners',
        'stacked': 2,
        'annoline1': 'Castleton',
        'annoline2': 'Corners',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.11918058534842,
         40.61333593766742,
         -74.11918058534842,
         40.61333593766742]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.210',
       'geometry': {'type': 'Point',
        'coordinates': [-74.16496031329827, 40.594252379161695]},
       'geometry_name': 'geom',
       'properties': {'name': 'New Springville',
        'stacked': 2,
        'annoline1': 'New',
        'annoline2': 'Springville',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.16496031329827,
         40.594252379161695,
         -74.16496031329827,
         40.594252379161695]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.211',
       'geometry': {'type': 'Point',
        'coordinates': [-74.19073717538116, 40.58631375103281]},
       'geometry_name': 'geom',
       'properties': {'name': 'Travis',
        'stacked': 1,
        'annoline1': 'Travis',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.19073717538116,
         40.58631375103281,
         -74.19073717538116,
         40.58631375103281]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.212',
       'geometry': {'type': 'Point',
        'coordinates': [-74.1164794360638, 40.57257231820632]},
       'geometry_name': 'geom',
       'properties': {'name': 'New Dorp',
        'stacked': 2,
        'annoline1': 'New',
        'annoline2': 'Dorp',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.1164794360638,
         40.57257231820632,
         -74.1164794360638,
         40.57257231820632]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.213',
       'geometry': {'type': 'Point',
        'coordinates': [-74.12156593771896, 40.5584622432888]},
       'geometry_name': 'geom',
       'properties': {'name': 'Oakwood',
        'stacked': 1,
        'annoline1': 'Oakwood',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.12156593771896,
         40.5584622432888,
         -74.12156593771896,
         40.5584622432888]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.214',
       'geometry': {'type': 'Point',
        'coordinates': [-74.14932381490992, 40.549480228713605]},
       'geometry_name': 'geom',
       'properties': {'name': 'Great Kills',
        'stacked': 2,
        'annoline1': 'Great',
        'annoline2': 'Kills',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.14932381490992,
         40.549480228713605,
         -74.14932381490992,
         40.549480228713605]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.215',
       'geometry': {'type': 'Point',
        'coordinates': [-74.1643308041936, 40.542230747450745]},
       'geometry_name': 'geom',
       'properties': {'name': 'Eltingville',
        'stacked': 1,
        'annoline1': 'Eltingville',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.1643308041936,
         40.542230747450745,
         -74.1643308041936,
         40.542230747450745]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.216',
       'geometry': {'type': 'Point',
        'coordinates': [-74.17854866165878, 40.53811417474507]},
       'geometry_name': 'geom',
       'properties': {'name': 'Annadale',
        'stacked': 1,
        'annoline1': 'Annadale',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.17854866165878,
         40.53811417474507,
         -74.17854866165878,
         40.53811417474507]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.217',
       'geometry': {'type': 'Point',
        'coordinates': [-74.20524582480326, 40.541967622888755]},
       'geometry_name': 'geom',
       'properties': {'name': 'Woodrow',
        'stacked': 1,
        'annoline1': 'Woodrow',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.20524582480326,
         40.541967622888755,
         -74.20524582480326,
         40.541967622888755]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.218',
       'geometry': {'type': 'Point',
        'coordinates': [-74.24656934235283, 40.50533376115642]},
       'geometry_name': 'geom',
       'properties': {'name': 'Tottenville',
        'stacked': 1,
        'annoline1': 'Tottenville',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.24656934235283,
         40.50533376115642,
         -74.24656934235283,
         40.50533376115642]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.219',
       'geometry': {'type': 'Point',
        'coordinates': [-74.08055351790115, 40.637316067110326]},
       'geometry_name': 'geom',
       'properties': {'name': 'Tompkinsville',
        'stacked': 1,
        'annoline1': 'Tompkinsville',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.08055351790115,
         40.637316067110326,
         -74.08055351790115,
         40.637316067110326]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.220',
       'geometry': {'type': 'Point',
        'coordinates': [-74.09629029235458, 40.61919310792676]},
       'geometry_name': 'geom',
       'properties': {'name': 'Silver Lake',
        'stacked': 2,
        'annoline1': 'Silver',
        'annoline2': 'Lake',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.09629029235458,
         40.61919310792676,
         -74.09629029235458,
         40.61919310792676]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.221',
       'geometry': {'type': 'Point',
        'coordinates': [-74.0971255217853, 40.61276015756489]},
       'geometry_name': 'geom',
       'properties': {'name': 'Sunnyside',
        'stacked': 1,
        'annoline1': 'Sunnyside',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.0971255217853,
         40.61276015756489,
         -74.0971255217853,
         40.61276015756489]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.222',
       'geometry': {'type': 'Point',
        'coordinates': [-73.96101312466779, 40.643675183340974]},
       'geometry_name': 'geom',
       'properties': {'name': 'Ditmas Park',
        'stacked': 2,
        'annoline1': 'Ditmas',
        'annoline2': 'Park',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.96101312466779,
         40.643675183340974,
         -73.96101312466779,
         40.643675183340974]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.223',
       'geometry': {'type': 'Point',
        'coordinates': [-73.93718680559314, 40.66094656188111]},
       'geometry_name': 'geom',
       'properties': {'name': 'Wingate',
        'stacked': 1,
        'annoline1': 'Wingate',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.93718680559314,
         40.66094656188111,
         -73.93718680559314,
         40.66094656188111]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.224',
       'geometry': {'type': 'Point',
        'coordinates': [-73.92688212616955, 40.655572313280764]},
       'geometry_name': 'geom',
       'properties': {'name': 'Rugby',
        'stacked': 1,
        'annoline1': 'Rugby',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.92688212616955,
         40.655572313280764,
         -73.92688212616955,
         40.655572313280764]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.225',
       'geometry': {'type': 'Point',
        'coordinates': [-74.08015734936296, 40.60919044434558]},
       'geometry_name': 'geom',
       'properties': {'name': 'Park Hill',
        'stacked': 2,
        'annoline1': 'Park',
        'annoline2': 'Hill',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.08015734936296,
         40.60919044434558,
         -74.08015734936296,
         40.60919044434558]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.226',
       'geometry': {'type': 'Point',
        'coordinates': [-74.13304143951704, 40.62109047275409]},
       'geometry_name': 'geom',
       'properties': {'name': 'Westerleigh',
        'stacked': 1,
        'annoline1': 'Westerleigh',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.13304143951704,
         40.62109047275409,
         -74.13304143951704,
         40.62109047275409]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.227',
       'geometry': {'type': 'Point',
        'coordinates': [-74.15315246387762, 40.620171512231884]},
       'geometry_name': 'geom',
       'properties': {'name': 'Graniteville',
        'stacked': 1,
        'annoline1': 'Graniteville',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.15315246387762,
         40.620171512231884,
         -74.15315246387762,
         40.620171512231884]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.228',
       'geometry': {'type': 'Point',
        'coordinates': [-74.16510420241124, 40.63532509911492]},
       'geometry_name': 'geom',
       'properties': {'name': 'Arlington',
        'stacked': 1,
        'annoline1': 'Arlington',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.16510420241124,
         40.63532509911492,
         -74.16510420241124,
         40.63532509911492]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.229',
       'geometry': {'type': 'Point',
        'coordinates': [-74.06712363225574, 40.596312571276734]},
       'geometry_name': 'geom',
       'properties': {'name': 'Arrochar',
        'stacked': 1,
        'annoline1': 'Arrochar',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.06712363225574,
         40.596312571276734,
         -74.06712363225574,
         40.596312571276734]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.230',
       'geometry': {'type': 'Point',
        'coordinates': [-74.0766743627905, 40.59826835959991]},
       'geometry_name': 'geom',
       'properties': {'name': 'Grasmere',
        'stacked': 1,
        'annoline1': 'Grasmere',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.0766743627905,
         40.59826835959991,
         -74.0766743627905,
         40.59826835959991]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.231',
       'geometry': {'type': 'Point',
        'coordinates': [-74.08751118005578, 40.59632891379513]},
       'geometry_name': 'geom',
       'properties': {'name': 'Old Town',
        'stacked': 2,
        'annoline1': 'Old',
        'annoline2': 'Town',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.08751118005578,
         40.59632891379513,
         -74.08751118005578,
         40.59632891379513]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.232',
       'geometry': {'type': 'Point',
        'coordinates': [-74.09639905312521, 40.588672948199275]},
       'geometry_name': 'geom',
       'properties': {'name': 'Dongan Hills',
        'stacked': 2,
        'annoline1': 'Dongan',
        'annoline2': 'Hills',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.09639905312521,
         40.588672948199275,
         -74.09639905312521,
         40.588672948199275]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.233',
       'geometry': {'type': 'Point',
        'coordinates': [-74.09348266303591, 40.57352690574283]},
       'geometry_name': 'geom',
       'properties': {'name': 'Midland Beach',
        'stacked': 2,
        'annoline1': 'Midland',
        'annoline2': 'Beach',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.09348266303591,
         40.57352690574283,
         -74.09348266303591,
         40.57352690574283]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.234',
       'geometry': {'type': 'Point',
        'coordinates': [-74.10585598545434, 40.57621558711788]},
       'geometry_name': 'geom',
       'properties': {'name': 'Grant City',
        'stacked': 2,
        'annoline1': 'Grant',
        'annoline2': 'City',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.10585598545434,
         40.57621558711788,
         -74.10585598545434,
         40.57621558711788]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.235',
       'geometry': {'type': 'Point',
        'coordinates': [-74.10432707469124, 40.56425549307335]},
       'geometry_name': 'geom',
       'properties': {'name': 'New Dorp Beach',
        'stacked': 3,
        'annoline1': 'New',
        'annoline2': 'Dorp',
        'annoline3': 'Beach',
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.10432707469124,
         40.56425549307335,
         -74.10432707469124,
         40.56425549307335]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.236',
       'geometry': {'type': 'Point',
        'coordinates': [-74.13916622175768, 40.55398800858462]},
       'geometry_name': 'geom',
       'properties': {'name': 'Bay Terrace',
        'stacked': 2,
        'annoline1': 'Bay',
        'annoline2': 'Terrace',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.13916622175768,
         40.55398800858462,
         -74.13916622175768,
         40.55398800858462]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.237',
       'geometry': {'type': 'Point',
        'coordinates': [-74.19174105747814, 40.531911920489605]},
       'geometry_name': 'geom',
       'properties': {'name': 'Huguenot',
        'stacked': 1,
        'annoline1': 'Huguenot',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.19174105747814,
         40.531911920489605,
         -74.19174105747814,
         40.531911920489605]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.238',
       'geometry': {'type': 'Point',
        'coordinates': [-74.21983106616777, 40.524699376118136]},
       'geometry_name': 'geom',
       'properties': {'name': 'Pleasant Plains',
        'stacked': 2,
        'annoline1': 'Pleasant',
        'annoline2': 'Plains',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.21983106616777,
         40.524699376118136,
         -74.21983106616777,
         40.524699376118136]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.239',
       'geometry': {'type': 'Point',
        'coordinates': [-74.22950350260027, 40.50608165346305]},
       'geometry_name': 'geom',
       'properties': {'name': 'Butler Manor',
        'stacked': 2,
        'annoline1': 'Butler',
        'annoline2': 'Manor',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.22950350260027,
         40.50608165346305,
         -74.22950350260027,
         40.50608165346305]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.240',
       'geometry': {'type': 'Point',
        'coordinates': [-74.23215775896526, 40.53053148283314]},
       'geometry_name': 'geom',
       'properties': {'name': 'Charleston',
        'stacked': 1,
        'annoline1': 'Charleston',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.23215775896526,
         40.53053148283314,
         -74.23215775896526,
         40.53053148283314]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.241',
       'geometry': {'type': 'Point',
        'coordinates': [-74.21572851113952, 40.54940400650072]},
       'geometry_name': 'geom',
       'properties': {'name': 'Rossville',
        'stacked': 1,
        'annoline1': 'Rossville',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.21572851113952,
         40.54940400650072,
         -74.21572851113952,
         40.54940400650072]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.242',
       'geometry': {'type': 'Point',
        'coordinates': [-74.18588674583893, 40.54928582278321]},
       'geometry_name': 'geom',
       'properties': {'name': 'Arden Heights',
        'stacked': 2,
        'annoline1': 'Arden',
        'annoline2': 'Heights',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.18588674583893,
         40.54928582278321,
         -74.18588674583893,
         40.54928582278321]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.243',
       'geometry': {'type': 'Point',
        'coordinates': [-74.17079414786092, 40.555295236173194]},
       'geometry_name': 'geom',
       'properties': {'name': 'Greenridge',
        'stacked': 1,
        'annoline1': 'Greenridge',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.17079414786092,
         40.555295236173194,
         -74.17079414786092,
         40.555295236173194]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.244',
       'geometry': {'type': 'Point',
        'coordinates': [-74.15902208156601, 40.58913894875281]},
       'geometry_name': 'geom',
       'properties': {'name': 'Heartland Village',
        'stacked': 2,
        'annoline1': 'Heartland',
        'annoline2': 'Village',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.15902208156601,
         40.58913894875281,
         -74.15902208156601,
         40.58913894875281]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.245',
       'geometry': {'type': 'Point',
        'coordinates': [-74.1895604551969, 40.59472602746295]},
       'geometry_name': 'geom',
       'properties': {'name': 'Chelsea',
        'stacked': 1,
        'annoline1': 'Chelsea',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.1895604551969,
         40.59472602746295,
         -74.1895604551969,
         40.59472602746295]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.246',
       'geometry': {'type': 'Point',
        'coordinates': [-74.18725638381567, 40.60577868452358]},
       'geometry_name': 'geom',
       'properties': {'name': 'Bloomfield',
        'stacked': 1,
        'annoline1': 'Bloomfield',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.18725638381567,
         40.60577868452358,
         -74.18725638381567,
         40.60577868452358]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.247',
       'geometry': {'type': 'Point',
        'coordinates': [-74.15940948657122, 40.6095918004203]},
       'geometry_name': 'geom',
       'properties': {'name': 'Bulls Head',
        'stacked': 2,
        'annoline1': 'Bulls',
        'annoline2': 'Head',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.15940948657122,
         40.6095918004203,
         -74.15940948657122,
         40.6095918004203]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.248',
       'geometry': {'type': 'Point',
        'coordinates': [-73.95325646837112, 40.7826825671257]},
       'geometry_name': 'geom',
       'properties': {'name': 'Carnegie Hill',
        'stacked': 2,
        'annoline1': 'Carnegie',
        'annoline2': 'Hill',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.95325646837112,
         40.7826825671257,
         -73.95325646837112,
         40.7826825671257]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.249',
       'geometry': {'type': 'Point',
        'coordinates': [-73.98843368023597, 40.72325901885768]},
       'geometry_name': 'geom',
       'properties': {'name': 'Noho',
        'stacked': 1,
        'annoline1': 'Noho',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.98843368023597,
         40.72325901885768,
         -73.98843368023597,
         40.72325901885768]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.250',
       'geometry': {'type': 'Point',
        'coordinates': [-74.00541529873355, 40.71522892046282]},
       'geometry_name': 'geom',
       'properties': {'name': 'Civic Center',
        'stacked': 2,
        'annoline1': 'Civic',
        'annoline2': 'Center',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-74.00541529873355,
         40.71522892046282,
         -74.00541529873355,
         40.71522892046282]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.251',
       'geometry': {'type': 'Point',
        'coordinates': [-73.98871313285247, 40.7485096643122]},
       'geometry_name': 'geom',
       'properties': {'name': 'Midtown South',
        'stacked': 2,
        'annoline1': 'Midtown',
        'annoline2': 'South',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.98871313285247,
         40.7485096643122,
         -73.98871313285247,
         40.7485096643122]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.252',
       'geometry': {'type': 'Point',
        'coordinates': [-74.1340572986257, 40.56960594275505]},
       'geometry_name': 'geom',
       'properties': {'name': 'Richmond Town',
        'stacked': 2,
        'annoline1': 'Richmond',
        'annoline2': 'Town',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.1340572986257,
         40.56960594275505,
         -74.1340572986257,
         40.56960594275505]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.253',
       'geometry': {'type': 'Point',
        'coordinates': [-74.06667766061771, 40.60971934079284]},
       'geometry_name': 'geom',
       'properties': {'name': 'Shore Acres',
        'stacked': 2,
        'annoline1': 'Shore',
        'annoline2': 'Acres',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.06667766061771,
         40.60971934079284,
         -74.06667766061771,
         40.60971934079284]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.254',
       'geometry': {'type': 'Point',
        'coordinates': [-74.072642445484, 40.61917845202843]},
       'geometry_name': 'geom',
       'properties': {'name': 'Clifton',
        'stacked': 1,
        'annoline1': 'Clifton',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.072642445484,
         40.61917845202843,
         -74.072642445484,
         40.61917845202843]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.255',
       'geometry': {'type': 'Point',
        'coordinates': [-74.08402364740358, 40.6044731896879]},
       'geometry_name': 'geom',
       'properties': {'name': 'Concord',
        'stacked': 1,
        'annoline1': 'Concord',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.08402364740358,
         40.6044731896879,
         -74.08402364740358,
         40.6044731896879]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.256',
       'geometry': {'type': 'Point',
        'coordinates': [-74.09776206972522, 40.606794394801]},
       'geometry_name': 'geom',
       'properties': {'name': 'Emerson Hill',
        'stacked': 2,
        'annoline1': 'Emerson',
        'annoline2': 'Hill',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.09776206972522,
         40.606794394801,
         -74.09776206972522,
         40.606794394801]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.257',
       'geometry': {'type': 'Point',
        'coordinates': [-74.09805062373887, 40.63563000681151]},
       'geometry_name': 'geom',
       'properties': {'name': 'Randall Manor',
        'stacked': 2,
        'annoline1': 'Randall',
        'annoline2': 'Manor',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.09805062373887,
         40.63563000681151,
         -74.09805062373887,
         40.63563000681151]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.258',
       'geometry': {'type': 'Point',
        'coordinates': [-74.18622331749823, 40.63843283794795]},
       'geometry_name': 'geom',
       'properties': {'name': 'Howland Hook',
        'stacked': 2,
        'annoline1': 'Howland',
        'annoline2': 'Hook',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.18622331749823,
         40.63843283794795,
         -74.18622331749823,
         40.63843283794795]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.259',
       'geometry': {'type': 'Point',
        'coordinates': [-74.1418167896889, 40.630146741193826]},
       'geometry_name': 'geom',
       'properties': {'name': 'Elm Park',
        'stacked': 2,
        'annoline1': 'Elm',
        'annoline2': 'Park',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.1418167896889,
         40.630146741193826,
         -74.1418167896889,
         40.630146741193826]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.260',
       'geometry': {'type': 'Point',
        'coordinates': [-73.91665331978048, 40.652117451793494]},
       'geometry_name': 'geom',
       'properties': {'name': 'Remsen Village',
        'stacked': 2,
        'annoline1': 'Remsen',
        'annoline2': 'Village',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.91665331978048,
         40.652117451793494,
         -73.91665331978048,
         40.652117451793494]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.261',
       'geometry': {'type': 'Point',
        'coordinates': [-73.88511776379292, 40.6627442796966]},
       'geometry_name': 'geom',
       'properties': {'name': 'New Lots',
        'stacked': 2,
        'annoline1': 'New',
        'annoline2': 'Lots',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.88511776379292,
         40.6627442796966,
         -73.88511776379292,
         40.6627442796966]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.262',
       'geometry': {'type': 'Point',
        'coordinates': [-73.90233474295836, 40.63131755039667]},
       'geometry_name': 'geom',
       'properties': {'name': 'Paerdegat Basin',
        'stacked': 2,
        'annoline1': 'Paerdegat',
        'annoline2': 'Basin',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.90233474295836,
         40.63131755039667,
         -73.90233474295836,
         40.63131755039667]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.263',
       'geometry': {'type': 'Point',
        'coordinates': [-73.91515391550404, 40.61597423962336]},
       'geometry_name': 'geom',
       'properties': {'name': 'Mill Basin',
        'stacked': 2,
        'annoline1': 'Mill',
        'annoline2': 'Basin',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.91515391550404,
         40.61597423962336,
         -73.91515391550404,
         40.61597423962336]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.264',
       'geometry': {'type': 'Point',
        'coordinates': [-73.79646462081593, 40.71145964370482]},
       'geometry_name': 'geom',
       'properties': {'name': 'Jamaica Hills',
        'stacked': 2,
        'annoline1': 'Jamaica',
        'annoline2': 'Hills',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.79646462081593,
         40.71145964370482,
         -73.79646462081593,
         40.71145964370482]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.265',
       'geometry': {'type': 'Point',
        'coordinates': [-73.79671678028349, 40.73350025429757]},
       'geometry_name': 'geom',
       'properties': {'name': 'Utopia',
        'stacked': 1,
        'annoline1': 'Utopia',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.79671678028349,
         40.73350025429757,
         -73.79671678028349,
         40.73350025429757]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.266',
       'geometry': {'type': 'Point',
        'coordinates': [-73.80486120040537, 40.73493618075478]},
       'geometry_name': 'geom',
       'properties': {'name': 'Pomonok',
        'stacked': 1,
        'annoline1': 'Pomonok',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.80486120040537,
         40.73493618075478,
         -73.80486120040537,
         40.73493618075478]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.267',
       'geometry': {'type': 'Point',
        'coordinates': [-73.89467996270574, 40.7703173929982]},
       'geometry_name': 'geom',
       'properties': {'name': 'Astoria Heights',
        'stacked': 2,
        'annoline1': 'Astoria',
        'annoline2': 'Heights',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.89467996270574,
         40.7703173929982,
         -73.89467996270574,
         40.7703173929982]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.268',
       'geometry': {'type': 'Point',
        'coordinates': [-73.90119903387667, 40.83142834161548]},
       'geometry_name': 'geom',
       'properties': {'name': 'Claremont Village',
        'stacked': 2,
        'annoline1': 'Claremont',
        'annoline2': 'Village',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.90119903387667,
         40.83142834161548,
         -73.90119903387667,
         40.83142834161548]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.269',
       'geometry': {'type': 'Point',
        'coordinates': [-73.91584652759009, 40.824780490842905]},
       'geometry_name': 'geom',
       'properties': {'name': 'Concourse Village',
        'stacked': 2,
        'annoline1': 'Concourse',
        'annoline2': 'Village',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.91584652759009,
         40.824780490842905,
         -73.91584652759009,
         40.824780490842905]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.270',
       'geometry': {'type': 'Point',
        'coordinates': [-73.91655551964419, 40.84382617671654]},
       'geometry_name': 'geom',
       'properties': {'name': 'Mount Eden',
        'stacked': 2,
        'annoline1': 'Mount',
        'annoline2': 'Eden',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.91655551964419,
         40.84382617671654,
         -73.91655551964419,
         40.84382617671654]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.271',
       'geometry': {'type': 'Point',
        'coordinates': [-73.90829930881988, 40.84884160724665]},
       'geometry_name': 'geom',
       'properties': {'name': 'Mount Hope',
        'stacked': 2,
        'annoline1': 'Mount',
        'annoline2': 'Hope',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.90829930881988,
         40.84884160724665,
         -73.90829930881988,
         40.84884160724665]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.272',
       'geometry': {'type': 'Point',
        'coordinates': [-73.96355614094303, 40.76028033131374]},
       'geometry_name': 'geom',
       'properties': {'name': 'Sutton Place',
        'stacked': 2,
        'annoline1': 'Sutton',
        'annoline2': 'Place',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.96355614094303,
         40.76028033131374,
         -73.96355614094303,
         40.76028033131374]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.273',
       'geometry': {'type': 'Point',
        'coordinates': [-73.95386782130745, 40.743414090073536]},
       'geometry_name': 'geom',
       'properties': {'name': 'Hunters Point',
        'stacked': 2,
        'annoline1': 'Hunters',
        'annoline2': 'Point',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.95386782130745,
         40.743414090073536,
         -73.95386782130745,
         40.743414090073536]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.274',
       'geometry': {'type': 'Point',
        'coordinates': [-73.96770824581834, 40.75204236950722]},
       'geometry_name': 'geom',
       'properties': {'name': 'Turtle Bay',
        'stacked': 2,
        'annoline1': 'Turtle',
        'annoline2': 'Bay',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.96770824581834,
         40.75204236950722,
         -73.96770824581834,
         40.75204236950722]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.275',
       'geometry': {'type': 'Point',
        'coordinates': [-73.97121928722265, 40.746917410740195]},
       'geometry_name': 'geom',
       'properties': {'name': 'Tudor City',
        'stacked': 2,
        'annoline1': 'Tudor',
        'annoline2': 'City',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.97121928722265,
         40.746917410740195,
         -73.97121928722265,
         40.746917410740195]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.276',
       'geometry': {'type': 'Point',
        'coordinates': [-73.97405170469203, 40.73099955477061]},
       'geometry_name': 'geom',
       'properties': {'name': 'Stuyvesant Town',
        'stacked': 2,
        'annoline1': 'Stuyvesant',
        'annoline2': 'Town',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.97405170469203,
         40.73099955477061,
         -73.97405170469203,
         40.73099955477061]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.277',
       'geometry': {'type': 'Point',
        'coordinates': [-73.9909471052826, 40.739673047638426]},
       'geometry_name': 'geom',
       'properties': {'name': 'Flatiron',
        'stacked': 1,
        'annoline1': 'Flatiron',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.9909471052826,
         40.739673047638426,
         -73.9909471052826,
         40.739673047638426]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.278',
       'geometry': {'type': 'Point',
        'coordinates': [-73.91819286431682, 40.74565180608076]},
       'geometry_name': 'geom',
       'properties': {'name': 'Sunnyside Gardens',
        'stacked': 2,
        'annoline1': 'Sunnyside',
        'annoline2': 'Gardens',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.91819286431682,
         40.74565180608076,
         -73.91819286431682,
         40.74565180608076]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.279',
       'geometry': {'type': 'Point',
        'coordinates': [-73.93244235260178, 40.73725071694497]},
       'geometry_name': 'geom',
       'properties': {'name': 'Blissville',
        'stacked': 1,
        'annoline1': 'Blissville',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.93244235260178,
         40.73725071694497,
         -73.93244235260178,
         40.73725071694497]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.280',
       'geometry': {'type': 'Point',
        'coordinates': [-73.99550751888415, 40.70328109093014]},
       'geometry_name': 'geom',
       'properties': {'name': 'Fulton Ferry',
        'stacked': 2,
        'annoline1': 'Fulton',
        'annoline2': 'Ferry',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.99550751888415,
         40.70328109093014,
         -73.99550751888415,
         40.70328109093014]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.281',
       'geometry': {'type': 'Point',
        'coordinates': [-73.98111603592393, 40.70332149882874]},
       'geometry_name': 'geom',
       'properties': {'name': 'Vinegar Hill',
        'stacked': 2,
        'annoline1': 'Vinegar',
        'annoline2': 'Hill',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.98111603592393,
         40.70332149882874,
         -73.98111603592393,
         40.70332149882874]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.282',
       'geometry': {'type': 'Point',
        'coordinates': [-73.93053108817338, 40.67503986503237]},
       'geometry_name': 'geom',
       'properties': {'name': 'Weeksville',
        'stacked': 1,
        'annoline1': 'Weeksville',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.93053108817338,
         40.67503986503237,
         -73.93053108817338,
         40.67503986503237]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.283',
       'geometry': {'type': 'Point',
        'coordinates': [-73.90331684852599, 40.67786104769531]},
       'geometry_name': 'geom',
       'properties': {'name': 'Broadway Junction',
        'stacked': 2,
        'annoline1': 'Broadway',
        'annoline2': 'Junction',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.90331684852599,
         40.67786104769531,
         -73.90331684852599,
         40.67786104769531]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.284',
       'geometry': {'type': 'Point',
        'coordinates': [-73.9887528074504, 40.70317632822692]},
       'geometry_name': 'geom',
       'properties': {'name': 'Dumbo',
        'stacked': 1,
        'annoline1': 'Dumbo',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.9887528074504,
         40.70317632822692,
         -73.9887528074504,
         40.70317632822692]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.285',
       'geometry': {'type': 'Point',
        'coordinates': [-74.12059399718001, 40.60180957631444]},
       'geometry_name': 'geom',
       'properties': {'name': 'Manor Heights',
        'stacked': 2,
        'annoline1': 'Manor',
        'annoline2': 'Heights',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.12059399718001,
         40.60180957631444,
         -74.12059399718001,
         40.60180957631444]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.286',
       'geometry': {'type': 'Point',
        'coordinates': [-74.13208447484298, 40.60370692627371]},
       'geometry_name': 'geom',
       'properties': {'name': 'Willowbrook',
        'stacked': 1,
        'annoline1': 'Willowbrook',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.13208447484298,
         40.60370692627371,
         -74.13208447484298,
         40.60370692627371]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.287',
       'geometry': {'type': 'Point',
        'coordinates': [-74.21776636068567, 40.541139922091766]},
       'geometry_name': 'geom',
       'properties': {'name': 'Sandy Ground',
        'stacked': 2,
        'annoline1': 'Sandy',
        'annoline2': 'Ground',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.21776636068567,
         40.541139922091766,
         -74.21776636068567,
         40.541139922091766]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.288',
       'geometry': {'type': 'Point',
        'coordinates': [-74.12727240604946, 40.579118742961214]},
       'geometry_name': 'geom',
       'properties': {'name': 'Egbertville',
        'stacked': 1,
        'annoline1': 'Egbertville',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.12727240604946,
         40.579118742961214,
         -74.12727240604946,
         40.579118742961214]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.289',
       'geometry': {'type': 'Point',
        'coordinates': [-73.89213760232822, 40.56737588957032]},
       'geometry_name': 'geom',
       'properties': {'name': 'Roxbury',
        'stacked': 1,
        'annoline1': 'Roxbury',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.89213760232822,
         40.56737588957032,
         -73.89213760232822,
         40.56737588957032]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.290',
       'geometry': {'type': 'Point',
        'coordinates': [-73.95918459428702, 40.598525095137255]},
       'geometry_name': 'geom',
       'properties': {'name': 'Homecrest',
        'stacked': 1,
        'annoline1': 'Homecrest',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.95918459428702,
         40.598525095137255,
         -73.95918459428702,
         40.598525095137255]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.291',
       'geometry': {'type': 'Point',
        'coordinates': [-73.88114319200604, 40.716414511158185]},
       'geometry_name': 'geom',
       'properties': {'name': 'Middle Village',
        'stacked': 2,
        'annoline1': 'Middle',
        'annoline2': 'Village',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.88114319200604,
         40.716414511158185,
         -73.88114319200604,
         40.716414511158185]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.292',
       'geometry': {'type': 'Point',
        'coordinates': [-74.20152556457658, 40.52626406734812]},
       'geometry_name': 'geom',
       'properties': {'name': "Prince's Bay",
        'stacked': 2,
        'annoline1': "Prince's",
        'annoline2': 'Bay',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.20152556457658,
         40.52626406734812,
         -74.20152556457658,
         40.52626406734812]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.293',
       'geometry': {'type': 'Point',
        'coordinates': [-74.13792663771568, 40.57650629379489]},
       'geometry_name': 'geom',
       'properties': {'name': 'Lighthouse Hill',
        'stacked': 2,
        'annoline1': 'Lighthouse',
        'annoline2': 'Hill',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.13792663771568,
         40.57650629379489,
         -74.13792663771568,
         40.57650629379489]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.294',
       'geometry': {'type': 'Point',
        'coordinates': [-74.22957080626941, 40.51954145748909]},
       'geometry_name': 'geom',
       'properties': {'name': 'Richmond Valley',
        'stacked': 2,
        'annoline1': 'Richmond',
        'annoline2': 'Valley',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.22957080626941,
         40.51954145748909,
         -74.22957080626941,
         40.51954145748909]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.295',
       'geometry': {'type': 'Point',
        'coordinates': [-73.82667757138641, 40.79060155670148]},
       'geometry_name': 'geom',
       'properties': {'name': 'Malba',
        'stacked': 1,
        'annoline1': 'Malba',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.82667757138641,
         40.79060155670148,
         -73.82667757138641,
         40.79060155670148]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.296',
       'geometry': {'type': 'Point',
        'coordinates': [-73.890345709872, 40.6819989345173]},
       'geometry_name': 'geom',
       'properties': {'name': 'Highland Park',
        'stacked': 2,
        'annoline1': 'Highland',
        'annoline2': 'Park',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.890345709872,
         40.6819989345173,
         -73.890345709872,
         40.6819989345173]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.297',
       'geometry': {'type': 'Point',
        'coordinates': [-73.94841515328893, 40.60937770113766]},
       'geometry_name': 'geom',
       'properties': {'name': 'Madison',
        'stacked': 1,
        'annoline1': 'Madison',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.94841515328893,
         40.60937770113766,
         -73.94841515328893,
         40.60937770113766]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.298',
       'geometry': {'type': 'Point',
        'coordinates': [-73.86172577555115, 40.85272297633017]},
       'geometry_name': 'geom',
       'properties': {'name': 'Bronxdale',
        'stacked': 1,
        'annoline1': 'Bronxdale',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.86172577555115,
         40.85272297633017,
         -73.86172577555115,
         40.85272297633017]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.299',
       'geometry': {'type': 'Point',
        'coordinates': [-73.85931863221647, 40.86578787802982]},
       'geometry_name': 'geom',
       'properties': {'name': 'Allerton',
        'stacked': 1,
        'annoline1': 'Allerton',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.85931863221647,
         40.86578787802982,
         -73.85931863221647,
         40.86578787802982]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.300',
       'geometry': {'type': 'Point',
        'coordinates': [-73.90152264513144, 40.8703923914147]},
       'geometry_name': 'geom',
       'properties': {'name': 'Kingsbridge Heights',
        'stacked': 2,
        'annoline1': 'Kingsbridge',
        'annoline2': 'Heights',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.90152264513144,
         40.8703923914147,
         -73.90152264513144,
         40.8703923914147]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.301',
       'geometry': {'type': 'Point',
        'coordinates': [-73.94817709920184, 40.64692606658579]},
       'geometry_name': 'geom',
       'properties': {'name': 'Erasmus',
        'stacked': 1,
        'annoline1': 'Erasmus',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.94817709920184,
         40.64692606658579,
         -73.94817709920184,
         40.64692606658579]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.302',
       'geometry': {'type': 'Point',
        'coordinates': [-74.00011136202637, 40.75665808227519]},
       'geometry_name': 'geom',
       'properties': {'name': 'Hudson Yards',
        'stacked': 2,
        'annoline1': 'Hudson',
        'annoline2': 'Yards',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-74.00011136202637,
         40.75665808227519,
         -74.00011136202637,
         40.75665808227519]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.303',
       'geometry': {'type': 'Point',
        'coordinates': [-73.80553002968718, 40.58733774018741]},
       'geometry_name': 'geom',
       'properties': {'name': 'Hammels',
        'stacked': 1,
        'annoline1': 'Hammels',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.80553002968718,
         40.58733774018741,
         -73.80553002968718,
         40.58733774018741]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.304',
       'geometry': {'type': 'Point',
        'coordinates': [-73.76596781445627, 40.611321691283834]},
       'geometry_name': 'geom',
       'properties': {'name': 'Bayswater',
        'stacked': 1,
        'annoline1': 'Bayswater',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.76596781445627,
         40.611321691283834,
         -73.76596781445627,
         40.611321691283834]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.305',
       'geometry': {'type': 'Point',
        'coordinates': [-73.94563070334091, 40.756091297094706]},
       'geometry_name': 'geom',
       'properties': {'name': 'Queensbridge',
        'stacked': 1,
        'annoline1': 'Queensbridge',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.94563070334091,
         40.756091297094706,
         -73.94563070334091,
         40.756091297094706]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.306',
       'geometry': {'type': 'Point',
        'coordinates': [-74.08173992211962, 40.61731079252983]},
       'geometry_name': 'geom',
       'properties': {'name': 'Fox Hills',
        'stacked': 2,
        'annoline1': 'Fox',
        'annoline2': 'Hills',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.08173992211962,
         40.61731079252983,
         -74.08173992211962,
         40.61731079252983]}}],
     'crs': {'type': 'name', 'properties': {'name': 'urn:ogc:def:crs:EPSG::4326'}},
     'bbox': [-74.2492599487305,
      40.5033187866211,
      -73.7061614990234,
      40.9105606079102]}




```python
neighborhoods_data = newyork_data['features']
```


```python
neighborhoods_data[0]
```




    {'type': 'Feature',
     'id': 'nyu_2451_34572.1',
     'geometry': {'type': 'Point',
      'coordinates': [-73.84720052054902, 40.89470517661]},
     'geometry_name': 'geom',
     'properties': {'name': 'Wakefield',
      'stacked': 1,
      'annoline1': 'Wakefield',
      'annoline2': None,
      'annoline3': None,
      'annoangle': 0.0,
      'borough': 'Bronx',
      'bbox': [-73.84720052054902,
       40.89470517661,
       -73.84720052054902,
       40.89470517661]}}




```python
column_names = ['Borough', 'Neighborhood', 'Latitude', 'Longitude'] 

neighborhoods = pd.DataFrame(columns=column_names)
```


```python
neighborhoods
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Borough</th>
      <th>Neighborhood</th>
      <th>Latitude</th>
      <th>Longitude</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
</div>




```python
for data in neighborhoods_data:
    borough = neighborhood_name = data['properties']['borough'] 
    neighborhood_name = data['properties']['name']
        
    neighborhood_latlon = data['geometry']['coordinates']
    neighborhood_lat = neighborhood_latlon[1]
    neighborhood_lon = neighborhood_latlon[0]
    
    neighborhoods = neighborhoods.append({'Borough': borough,
                                          'Neighborhood': neighborhood_name,
                                          'Latitude': neighborhood_lat,
                                          'Longitude': neighborhood_lon}, ignore_index=True)
```


```python
neighborhoods.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Borough</th>
      <th>Neighborhood</th>
      <th>Latitude</th>
      <th>Longitude</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bronx</td>
      <td>Wakefield</td>
      <td>40.894705</td>
      <td>-73.847201</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bronx</td>
      <td>Co-op City</td>
      <td>40.874294</td>
      <td>-73.829939</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Bronx</td>
      <td>Eastchester</td>
      <td>40.887556</td>
      <td>-73.827806</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Bronx</td>
      <td>Fieldston</td>
      <td>40.895437</td>
      <td>-73.905643</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Bronx</td>
      <td>Riverdale</td>
      <td>40.890834</td>
      <td>-73.912585</td>
    </tr>
  </tbody>
</table>
</div>




```python
print('The dataframe has {} boroughs and {} neighborhoods.'.format(
        len(neighborhoods['Borough'].unique()),
        neighborhoods.shape[0]
    )
)
```

    The dataframe has 5 boroughs and 306 neighborhoods.



```python
!conda install -c conda-forge geopy --yes 
from geopy.geocoders import Nominatim 
address = 'New York City, NY'

geolocator = Nominatim(user_agent="ny_explorer")
location = geolocator.geocode(address)
latitude = location.latitude
longitude = location.longitude
print('The geograpical coordinate of New York City are {}, {}.'.format(latitude, longitude))
```

    Collecting package metadata (current_repodata.json): done
    Solving environment: done
    
    # All requested packages already installed.
    
    The geograpical coordinate of New York City are 40.7127281, -74.0060152.



```python
!conda install -c conda-forge folium=0.5.0 --yes 
import folium 

map_newyork = folium.Map(location=[latitude, longitude], zoom_start=10)

# add markers to map
for lat, lng, borough, neighborhood in zip(neighborhoods['Latitude'], neighborhoods['Longitude'], neighborhoods['Borough'], neighborhoods['Neighborhood']):
    label = '{}, {}'.format(neighborhood, borough)
    label = folium.Popup(label, parse_html=True)
    folium.CircleMarker(
        [lat, lng],
        radius=5,
        popup=label,
        color='blue',
        fill=True,
        fill_color='#3186cc',
        fill_opacity=0.7,
        parse_html=False).add_to(map_newyork)  
    
map_newyork
```

    Collecting package metadata (current_repodata.json): done
    Solving environment: done
    
    # All requested packages already installed.
    





<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><span style="color:#565656">Make this Notebook Trusted to load map: File -> Trust Notebook</span><iframe src="about:blank" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" data-html=PCFET0NUWVBFIGh0bWw+CjxoZWFkPiAgICAKICAgIDxtZXRhIGh0dHAtZXF1aXY9ImNvbnRlbnQtdHlwZSIgY29udGVudD0idGV4dC9odG1sOyBjaGFyc2V0PVVURi04IiAvPgogICAgPHNjcmlwdD5MX1BSRUZFUl9DQU5WQVMgPSBmYWxzZTsgTF9OT19UT1VDSCA9IGZhbHNlOyBMX0RJU0FCTEVfM0QgPSBmYWxzZTs8L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2FqYXguZ29vZ2xlYXBpcy5jb20vYWpheC9saWJzL2pxdWVyeS8xLjExLjEvanF1ZXJ5Lm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvanMvYm9vdHN0cmFwLm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9jZG5qcy5jbG91ZGZsYXJlLmNvbS9hamF4L2xpYnMvTGVhZmxldC5hd2Vzb21lLW1hcmtlcnMvMi4wLjIvbGVhZmxldC5hd2Vzb21lLW1hcmtlcnMuanMiPjwvc2NyaXB0PgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9jc3MvYm9vdHN0cmFwLm1pbi5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvY3NzL2Jvb3RzdHJhcC10aGVtZS5taW4uY3NzIi8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vbWF4Y2RuLmJvb3RzdHJhcGNkbi5jb20vZm9udC1hd2Vzb21lLzQuNi4zL2Nzcy9mb250LWF3ZXNvbWUubWluLmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2NkbmpzLmNsb3VkZmxhcmUuY29tL2FqYXgvbGlicy9MZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy8yLjAuMi9sZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9yYXdnaXQuY29tL3B5dGhvbi12aXN1YWxpemF0aW9uL2ZvbGl1bS9tYXN0ZXIvZm9saXVtL3RlbXBsYXRlcy9sZWFmbGV0LmF3ZXNvbWUucm90YXRlLmNzcyIvPgogICAgPHN0eWxlPmh0bWwsIGJvZHkge3dpZHRoOiAxMDAlO2hlaWdodDogMTAwJTttYXJnaW46IDA7cGFkZGluZzogMDt9PC9zdHlsZT4KICAgIDxzdHlsZT4jbWFwIHtwb3NpdGlvbjphYnNvbHV0ZTt0b3A6MDtib3R0b206MDtyaWdodDowO2xlZnQ6MDt9PC9zdHlsZT4KICAgIAogICAgICAgICAgICA8c3R5bGU+ICNtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYgewogICAgICAgICAgICAgICAgcG9zaXRpb24gOiByZWxhdGl2ZTsKICAgICAgICAgICAgICAgIHdpZHRoIDogMTAwLjAlOwogICAgICAgICAgICAgICAgaGVpZ2h0OiAxMDAuMCU7CiAgICAgICAgICAgICAgICBsZWZ0OiAwLjAlOwogICAgICAgICAgICAgICAgdG9wOiAwLjAlOwogICAgICAgICAgICAgICAgfQogICAgICAgICAgICA8L3N0eWxlPgogICAgICAgIAo8L2hlYWQ+Cjxib2R5PiAgICAKICAgIAogICAgICAgICAgICA8ZGl2IGNsYXNzPSJmb2xpdW0tbWFwIiBpZD0ibWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmIiA+PC9kaXY+CiAgICAgICAgCjwvYm9keT4KPHNjcmlwdD4gICAgCiAgICAKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGJvdW5kcyA9IG51bGw7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgdmFyIG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZiA9IEwubWFwKAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJ21hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZicsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB7Y2VudGVyOiBbNDAuNzEyNzI4MSwtNzQuMDA2MDE1Ml0sCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB6b29tOiAxMCwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIG1heEJvdW5kczogYm91bmRzLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbGF5ZXJzOiBbXSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHdvcmxkQ29weUp1bXA6IGZhbHNlLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgY3JzOiBMLkNSUy5FUFNHMzg1NwogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB9KTsKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHRpbGVfbGF5ZXJfMWRlNWRjMjAyMzQ5NDYzZmFmYjdiMDYyNzRjMDg5MzggPSBMLnRpbGVMYXllcigKICAgICAgICAgICAgICAgICdodHRwczovL3tzfS50aWxlLm9wZW5zdHJlZXRtYXAub3JnL3t6fS97eH0ve3l9LnBuZycsCiAgICAgICAgICAgICAgICB7CiAgImF0dHJpYnV0aW9uIjogbnVsbCwKICAiZGV0ZWN0UmV0aW5hIjogZmFsc2UsCiAgIm1heFpvb20iOiAxOCwKICAibWluWm9vbSI6IDEsCiAgIm5vV3JhcCI6IGZhbHNlLAogICJzdWJkb21haW5zIjogImFiYyIKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzEyMjA2ZTJhMzZjYTRjOTU5NjExYjlhMzcyYWE5NGIyID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODk0NzA1MTc2NjEsLTczLjg0NzIwMDUyMDU0OTAyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzJiMTA3YWM2MmNkZDQ4NThiYWQ0ZmI0ZGJmN2UzOTRjID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzI5OTEwYWI1OTNkNDRlZjk4MGE2MTM0YTY4YjU4NzA5ID0gJCgnPGRpdiBpZD0iaHRtbF8yOTkxMGFiNTkzZDQ0ZWY5ODBhNjEzNGE2OGI1ODcwOSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+V2FrZWZpZWxkLCBCcm9ueDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMmIxMDdhYzYyY2RkNDg1OGJhZDRmYjRkYmY3ZTM5NGMuc2V0Q29udGVudChodG1sXzI5OTEwYWI1OTNkNDRlZjk4MGE2MTM0YTY4YjU4NzA5KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzEyMjA2ZTJhMzZjYTRjOTU5NjExYjlhMzcyYWE5NGIyLmJpbmRQb3B1cChwb3B1cF8yYjEwN2FjNjJjZGQ0ODU4YmFkNGZiNGRiZjdlMzk0Yyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl83MmM4MjlkNDU3OTY0Y2NmOWVhYzY2NjY2ZGQ1MWQyOCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjg3NDI5NDE5MzAzMDEyLC03My44Mjk5MzkxMDgxMjM5OF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF80MzYzNzQ5ZTVkMDA0Nzg3OWQ3OWI0OTA2YmViM2Y2YyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF83YWRiZWM3NjcxZGY0ZjBhYTMxYmJlZDEyOWE2YzQ0OSA9ICQoJzxkaXYgaWQ9Imh0bWxfN2FkYmVjNzY3MWRmNGYwYWEzMWJiZWQxMjlhNmM0NDkiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNvLW9wIENpdHksIEJyb254PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF80MzYzNzQ5ZTVkMDA0Nzg3OWQ3OWI0OTA2YmViM2Y2Yy5zZXRDb250ZW50KGh0bWxfN2FkYmVjNzY3MWRmNGYwYWEzMWJiZWQxMjlhNmM0NDkpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNzJjODI5ZDQ1Nzk2NGNjZjllYWM2NjY2NmRkNTFkMjguYmluZFBvcHVwKHBvcHVwXzQzNjM3NDllNWQwMDQ3ODc5ZDc5YjQ5MDZiZWIzZjZjKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzE3OTlmN2M0YjA3ZTQ2NmY4YjRmYTM4MGE0NDZmYjcyID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODg3NTU1Njc3MzUwNzc1LC03My44Mjc4MDY0NDcxNjQxMl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9mYmQ5YTc1MDkxOTk0YTY2YWQ1YjMzMGM0ZDNiZTVmNSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8zMTEyZDUwZjAwYTg0YjcwOGZhM2NiMzVjMDQxNGYyOCA9ICQoJzxkaXYgaWQ9Imh0bWxfMzExMmQ1MGYwMGE4NGI3MDhmYTNjYjM1YzA0MTRmMjgiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkVhc3RjaGVzdGVyLCBCcm9ueDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZmJkOWE3NTA5MTk5NGE2NmFkNWIzMzBjNGQzYmU1ZjUuc2V0Q29udGVudChodG1sXzMxMTJkNTBmMDBhODRiNzA4ZmEzY2IzNWMwNDE0ZjI4KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzE3OTlmN2M0YjA3ZTQ2NmY4YjRmYTM4MGE0NDZmYjcyLmJpbmRQb3B1cChwb3B1cF9mYmQ5YTc1MDkxOTk0YTY2YWQ1YjMzMGM0ZDNiZTVmNSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8yYzU1Yzc5MjgwZWY0NzEwYmZmZDRmZDQxMjU2MmIyNSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjg5NTQzNzQyNjkwMzgzLC03My45MDU2NDI1OTU5MTY4Ml0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9hZTJiZDYxNWRkNDM0MDFhODM5NTVjYmQyOTc3YjY2ZCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF85MjZiY2MyZGM3NzY0NDc3OTJiNWQxOWIwNTM4ODZhOSA9ICQoJzxkaXYgaWQ9Imh0bWxfOTI2YmNjMmRjNzc2NDQ3NzkyYjVkMTliMDUzODg2YTkiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkZpZWxkc3RvbiwgQnJvbng8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2FlMmJkNjE1ZGQ0MzQwMWE4Mzk1NWNiZDI5NzdiNjZkLnNldENvbnRlbnQoaHRtbF85MjZiY2MyZGM3NzY0NDc3OTJiNWQxOWIwNTM4ODZhOSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8yYzU1Yzc5MjgwZWY0NzEwYmZmZDRmZDQxMjU2MmIyNS5iaW5kUG9wdXAocG9wdXBfYWUyYmQ2MTVkZDQzNDAxYTgzOTU1Y2JkMjk3N2I2NmQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMTRiMzM0MTAyYzM0NDg0NmJjOTdlNzM4NDJhYjNlOTcgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44OTA4MzQ0OTM4OTEzMDUsLTczLjkxMjU4NTQ2MTA4NTddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNTlmNzlmZWIwZjEyNDExOGE3YTJiYmMzNDVmODllYWIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNjgyM2E2NjNhNmZmNGUxZDhmNTgxMjJlOTMzMTkxYzQgPSAkKCc8ZGl2IGlkPSJodG1sXzY4MjNhNjYzYTZmZjRlMWQ4ZjU4MTIyZTkzMzE5MWM0IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5SaXZlcmRhbGUsIEJyb254PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF81OWY3OWZlYjBmMTI0MTE4YTdhMmJiYzM0NWY4OWVhYi5zZXRDb250ZW50KGh0bWxfNjgyM2E2NjNhNmZmNGUxZDhmNTgxMjJlOTMzMTkxYzQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMTRiMzM0MTAyYzM0NDg0NmJjOTdlNzM4NDJhYjNlOTcuYmluZFBvcHVwKHBvcHVwXzU5Zjc5ZmViMGYxMjQxMThhN2EyYmJjMzQ1Zjg5ZWFiKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzlhYTM4NDlkYTJkYTRmODA4MjY2NGYwMGY4Y2MxOTMwID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODgxNjg3MzcxMjA1MjEsLTczLjkwMjgxNzk4NzI0NjA0XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzYyNjAzY2I3MWM0NTRiZWY4MDQ3MGFhZDIyOWM0N2RiID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzcwMWVkMTcyMzMxNDQwMzFhMzhiNTc3ZWY4Y2ZkYzBhID0gJCgnPGRpdiBpZD0iaHRtbF83MDFlZDE3MjMzMTQ0MDMxYTM4YjU3N2VmOGNmZGMwYSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+S2luZ3NicmlkZ2UsIEJyb254PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF82MjYwM2NiNzFjNDU0YmVmODA0NzBhYWQyMjljNDdkYi5zZXRDb250ZW50KGh0bWxfNzAxZWQxNzIzMzE0NDAzMWEzOGI1NzdlZjhjZmRjMGEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOWFhMzg0OWRhMmRhNGY4MDgyNjY0ZjAwZjhjYzE5MzAuYmluZFBvcHVwKHBvcHVwXzYyNjAzY2I3MWM0NTRiZWY4MDQ3MGFhZDIyOWM0N2RiKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2ZlNDVjMTMzMmVjZDQ5ODE4NDc4Mjg3NzRjYzVhNTk0ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODc2NTUwNzc4Nzk5NjQsLTczLjkxMDY1OTY1ODYyOTgxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzczMTI2YmQ5ZTdiYzQyNDI5OTY3YzhiZTNiMDI2YWU0ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzFhYWFhMmIzNTNiODQyNDliOTVmY2RlNDlhYzA2MWUyID0gJCgnPGRpdiBpZD0iaHRtbF8xYWFhYTJiMzUzYjg0MjQ5Yjk1ZmNkZTQ5YWMwNjFlMiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+TWFyYmxlIEhpbGwsIE1hbmhhdHRhbjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNzMxMjZiZDllN2JjNDI0Mjk5NjdjOGJlM2IwMjZhZTQuc2V0Q29udGVudChodG1sXzFhYWFhMmIzNTNiODQyNDliOTVmY2RlNDlhYzA2MWUyKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2ZlNDVjMTMzMmVjZDQ5ODE4NDc4Mjg3NzRjYzVhNTk0LmJpbmRQb3B1cChwb3B1cF83MzEyNmJkOWU3YmM0MjQyOTk2N2M4YmUzYjAyNmFlNCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8yNTk5YzdmMTg2Yjk0YTE2YTU4ZTQzYTI5ODE5ZjI0MyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjg5ODI3MjYxMjEzODA1LC03My44NjczMTQ5NjgxNDE3Nl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8xNTVhZjU3NmFhOWM0ZTk3ODJlMDc1ODMxNjUyNzAxYSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9mNDFkZTU2OGZjMjg0YTdiOTc4N2JmYmZlNThjZWYzNSA9ICQoJzxkaXYgaWQ9Imh0bWxfZjQxZGU1NjhmYzI4NGE3Yjk3ODdiZmJmZTU4Y2VmMzUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPldvb2RsYXduLCBCcm9ueDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMTU1YWY1NzZhYTljNGU5NzgyZTA3NTgzMTY1MjcwMWEuc2V0Q29udGVudChodG1sX2Y0MWRlNTY4ZmMyODRhN2I5Nzg3YmZiZmU1OGNlZjM1KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzI1OTljN2YxODZiOTRhMTZhNThlNDNhMjk4MTlmMjQzLmJpbmRQb3B1cChwb3B1cF8xNTVhZjU3NmFhOWM0ZTk3ODJlMDc1ODMxNjUyNzAxYSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9kNzY5YzcyYTk1MWM0MzYyYTBkYWNkNmYwMzA4N2I0MCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjg3NzIyNDE1NTk5NDQ2LC03My44NzkzOTA3Mzk1NjgxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzJhNzdiMDgxM2ViMTQ3YzQ4MDkzNzZiODYwYTMxZDA2ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2JiZDc3ZDRmZWQ4MzRhOGFhN2ZlODgxOTVlOWMwZGVkID0gJCgnPGRpdiBpZD0iaHRtbF9iYmQ3N2Q0ZmVkODM0YThhYTdmZTg4MTk1ZTljMGRlZCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Tm9yd29vZCwgQnJvbng8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzJhNzdiMDgxM2ViMTQ3YzQ4MDkzNzZiODYwYTMxZDA2LnNldENvbnRlbnQoaHRtbF9iYmQ3N2Q0ZmVkODM0YThhYTdmZTg4MTk1ZTljMGRlZCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9kNzY5YzcyYTk1MWM0MzYyYTBkYWNkNmYwMzA4N2I0MC5iaW5kUG9wdXAocG9wdXBfMmE3N2IwODEzZWIxNDdjNDgwOTM3NmI4NjBhMzFkMDYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYzM5N2NkZDYyNjgzNDdlYTljYWMxOWVkYTUzMDI3ODIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44ODEwMzg4NzgxOTIxMSwtNzMuODU3NDQ2NDI5NzQyMDddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfOWNjN2YyODRkZmQ1NDBjOWI2OGI1MWQxZDI5MmQ4NmUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZTJhZjE4MjkxZmNlNDczZmFhNjJlYzhjYzQwY2EyNWUgPSAkKCc8ZGl2IGlkPSJodG1sX2UyYWYxODI5MWZjZTQ3M2ZhYTYyZWM4Y2M0MGNhMjVlIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5XaWxsaWFtc2JyaWRnZSwgQnJvbng8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzljYzdmMjg0ZGZkNTQwYzliNjhiNTFkMWQyOTJkODZlLnNldENvbnRlbnQoaHRtbF9lMmFmMTgyOTFmY2U0NzNmYWE2MmVjOGNjNDBjYTI1ZSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9jMzk3Y2RkNjI2ODM0N2VhOWNhYzE5ZWRhNTMwMjc4Mi5iaW5kUG9wdXAocG9wdXBfOWNjN2YyODRkZmQ1NDBjOWI2OGI1MWQxZDI5MmQ4NmUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZDFiZjcxZThiNzNkNGMyYWFkN2VlZGRkZjc5NjRmMDkgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44NjY4NTgxMDcyNTI2OTYsLTczLjgzNTc5NzU5ODA4MTE3XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzhmNzJjZDIzY2UwMjRkZWQ5YmEwMTFmYzQ4NzE5MTVjID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2U4OGZhYmJjNTYwMDRmZTJiZmY1MzhkNDM4ODZiYmEwID0gJCgnPGRpdiBpZD0iaHRtbF9lODhmYWJiYzU2MDA0ZmUyYmZmNTM4ZDQzODg2YmJhMCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QmF5Y2hlc3RlciwgQnJvbng8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzhmNzJjZDIzY2UwMjRkZWQ5YmEwMTFmYzQ4NzE5MTVjLnNldENvbnRlbnQoaHRtbF9lODhmYWJiYzU2MDA0ZmUyYmZmNTM4ZDQzODg2YmJhMCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9kMWJmNzFlOGI3M2Q0YzJhYWQ3ZWVkZGRmNzk2NGYwOS5iaW5kUG9wdXAocG9wdXBfOGY3MmNkMjNjZTAyNGRlZDliYTAxMWZjNDg3MTkxNWMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOGEyZjhkMGM2ODNkNGJmMWIxN2Q0MTQ2YzhiOTdhYWEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44NTc0MTM0OTgwODg2NSwtNzMuODU0NzU1NjQwMTc5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNGY3MjM2MGQ4MzZkNDEyMzg1NDgxOWI2NjYwZTQ1OTYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfM2NhMDlmNTM4NzU2NDFmM2JiOWQ1OTZhNDRjYjlmYTkgPSAkKCc8ZGl2IGlkPSJodG1sXzNjYTA5ZjUzODc1NjQxZjNiYjlkNTk2YTQ0Y2I5ZmE5IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5QZWxoYW0gUGFya3dheSwgQnJvbng8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzRmNzIzNjBkODM2ZDQxMjM4NTQ4MTliNjY2MGU0NTk2LnNldENvbnRlbnQoaHRtbF8zY2EwOWY1Mzg3NTY0MWYzYmI5ZDU5NmE0NGNiOWZhOSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl84YTJmOGQwYzY4M2Q0YmYxYjE3ZDQxNDZjOGI5N2FhYS5iaW5kUG9wdXAocG9wdXBfNGY3MjM2MGQ4MzZkNDEyMzg1NDgxOWI2NjYwZTQ1OTYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZjVjZTRlNDY5M2E2NDk1MDliNjkzZDE5ZDU5MjI0OTIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44NDcyNDY3MDQ5MTgxMywtNzMuNzg2NDg4NDUyNjc0MTNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMDAzOTY1MzE4NDMxNGQ5YWFjZGY1MzkyYzY5YTQ5YTMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfN2Y0NGIwOTk1N2JkNGJmZmExYzk3NzZhYWZmMzI0YTcgPSAkKCc8ZGl2IGlkPSJodG1sXzdmNDRiMDk5NTdiZDRiZmZhMWM5Nzc2YWFmZjMyNGE3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DaXR5IElzbGFuZCwgQnJvbng8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzAwMzk2NTMxODQzMTRkOWFhY2RmNTM5MmM2OWE0OWEzLnNldENvbnRlbnQoaHRtbF83ZjQ0YjA5OTU3YmQ0YmZmYTFjOTc3NmFhZmYzMjRhNyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9mNWNlNGU0NjkzYTY0OTUwOWI2OTNkMTlkNTkyMjQ5Mi5iaW5kUG9wdXAocG9wdXBfMDAzOTY1MzE4NDMxNGQ5YWFjZGY1MzkyYzY5YTQ5YTMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZjBlZmFjNjVjMjBjNDlkM2E2NjY5YjJiZGE2YzQ2ZGMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44NzAxODUxNjQ5NzUzMjUsLTczLjg4NTUxMjE4NDE5MTNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMTg5NzczYjFmYWE1NGI1ODliMTBiZmVlNDI5ZjVhMTMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMTAzODlmYzk0ZTJiNGRiNWI0ZGNkY2NmN2UzZTNmNmUgPSAkKCc8ZGl2IGlkPSJodG1sXzEwMzg5ZmM5NGUyYjRkYjViNGRjZGNjZjdlM2UzZjZlIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CZWRmb3JkIFBhcmssIEJyb254PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8xODk3NzNiMWZhYTU0YjU4OWIxMGJmZWU0MjlmNWExMy5zZXRDb250ZW50KGh0bWxfMTAzODlmYzk0ZTJiNGRiNWI0ZGNkY2NmN2UzZTNmNmUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZjBlZmFjNjVjMjBjNDlkM2E2NjY5YjJiZGE2YzQ2ZGMuYmluZFBvcHVwKHBvcHVwXzE4OTc3M2IxZmFhNTRiNTg5YjEwYmZlZTQyOWY1YTEzKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2NjZjhkZGM4ZDk2ZjRjZmM4NTUxMmQ5YmI0MTQwN2E1ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODU1NzI3MDc3MTk2NjQsLTczLjkxMDQxNTk2MTkxMzFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMDVmOWU4ZTIzYTMyNGVkOThiODE3N2I5NzdlYTNiNGEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYTI1NGQwY2E3ZDQ5NDNjNzliYWE2YWRlZjNmODQ1NWQgPSAkKCc8ZGl2IGlkPSJodG1sX2EyNTRkMGNhN2Q0OTQzYzc5YmFhNmFkZWYzZjg0NTVkIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Vbml2ZXJzaXR5IEhlaWdodHMsIEJyb254PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8wNWY5ZThlMjNhMzI0ZWQ5OGI4MTc3Yjk3N2VhM2I0YS5zZXRDb250ZW50KGh0bWxfYTI1NGQwY2E3ZDQ5NDNjNzliYWE2YWRlZjNmODQ1NWQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfY2NmOGRkYzhkOTZmNGNmYzg1NTEyZDliYjQxNDA3YTUuYmluZFBvcHVwKHBvcHVwXzA1ZjllOGUyM2EzMjRlZDk4YjgxNzdiOTc3ZWEzYjRhKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzFjZjNhZTExYzE3MjQ5Zjg5MjM5N2FhNzg4ZDQ0NzI2ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODQ3ODk3OTI2MDYyNzEsLTczLjkxOTY3MTU5MTE5NTY1XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2U0Yjg5MjEzMjk3YTQzMjZhMmVkMWIzNTNjZTMyZjA0ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2E1NjA2MWFlNjE5OTRlZjlhMDg2ZTI4ODI4YzBlZDgwID0gJCgnPGRpdiBpZD0iaHRtbF9hNTYwNjFhZTYxOTk0ZWY5YTA4NmUyODgyOGMwZWQ4MCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+TW9ycmlzIEhlaWdodHMsIEJyb254PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9lNGI4OTIxMzI5N2E0MzI2YTJlZDFiMzUzY2UzMmYwNC5zZXRDb250ZW50KGh0bWxfYTU2MDYxYWU2MTk5NGVmOWEwODZlMjg4MjhjMGVkODApOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMWNmM2FlMTFjMTcyNDlmODkyMzk3YWE3ODhkNDQ3MjYuYmluZFBvcHVwKHBvcHVwX2U0Yjg5MjEzMjk3YTQzMjZhMmVkMWIzNTNjZTMyZjA0KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzMyY2M1Zjc5NjBjZTQ5MGY4NjkwMjgxZDZiMjdlZGJhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODYwOTk2Nzk2Mzg2NTQsLTczLjg5NjQyNjU1OTgxNjIzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzIzM2ZmNjA1ZDcyNjRhOThiYjQ0YzAwZmMyNzU4ZjJhID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzRmMmM3NDFmNGQ0MTQ0YTBiNmZkZjZjMWZjYTcxNzZiID0gJCgnPGRpdiBpZD0iaHRtbF80ZjJjNzQxZjRkNDE0NGEwYjZmZGY2YzFmY2E3MTc2YiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Rm9yZGhhbSwgQnJvbng8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzIzM2ZmNjA1ZDcyNjRhOThiYjQ0YzAwZmMyNzU4ZjJhLnNldENvbnRlbnQoaHRtbF80ZjJjNzQxZjRkNDE0NGEwYjZmZGY2YzFmY2E3MTc2Yik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8zMmNjNWY3OTYwY2U0OTBmODY5MDI4MWQ2YjI3ZWRiYS5iaW5kUG9wdXAocG9wdXBfMjMzZmY2MDVkNzI2NGE5OGJiNDRjMDBmYzI3NThmMmEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMzg2MTY5YWMxYWNhNDBkZWIzY2FhZWM1ODcyYmYyZTYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44NDI2OTYxNTc4NjA1MywtNzMuODg3MzU2MTc1MzIzMzhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNjViY2ZiYjZkNmU3NDcyNGFjNzkxNjlmYTA5ZmM1ZmYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMjBiZjY3ZTIzOTZlNDdkN2JhNjM5Nzk1Yjg4MDlkNDEgPSAkKCc8ZGl2IGlkPSJodG1sXzIwYmY2N2UyMzk2ZTQ3ZDdiYTYzOTc5NWI4ODA5ZDQxIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5FYXN0IFRyZW1vbnQsIEJyb254PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF82NWJjZmJiNmQ2ZTc0NzI0YWM3OTE2OWZhMDlmYzVmZi5zZXRDb250ZW50KGh0bWxfMjBiZjY3ZTIzOTZlNDdkN2JhNjM5Nzk1Yjg4MDlkNDEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMzg2MTY5YWMxYWNhNDBkZWIzY2FhZWM1ODcyYmYyZTYuYmluZFBvcHVwKHBvcHVwXzY1YmNmYmI2ZDZlNzQ3MjRhYzc5MTY5ZmEwOWZjNWZmKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzI0NmZhMjg2Y2JmNzQxMGQ4YzFhNTZlODFhZmZhODc0ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODM5NDc1MDU2NzI2NTMsLTczLjg3Nzc0NDc0OTEwNTQ1XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2RlZjYwMzMxNzNlMDRlOWU4N2ZjYTA4MjgxY2E0ZDE1ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzQ4NmEwMjViYTIxYjRlYjViNDZjYmQxZmE2ZDAwMTgwID0gJCgnPGRpdiBpZD0iaHRtbF80ODZhMDI1YmEyMWI0ZWI1YjQ2Y2JkMWZhNmQwMDE4MCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+V2VzdCBGYXJtcywgQnJvbng8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2RlZjYwMzMxNzNlMDRlOWU4N2ZjYTA4MjgxY2E0ZDE1LnNldENvbnRlbnQoaHRtbF80ODZhMDI1YmEyMWI0ZWI1YjQ2Y2JkMWZhNmQwMDE4MCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8yNDZmYTI4NmNiZjc0MTBkOGMxYTU2ZTgxYWZmYTg3NC5iaW5kUG9wdXAocG9wdXBfZGVmNjAzMzE3M2UwNGU5ZTg3ZmNhMDgyODFjYTRkMTUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMWQ0MTBjMWEyMmVlNGJhMDk4ZDJiYThlMWU4NzQ1MDQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44MzY2MjMwMTA3MDYwNTYsLTczLjkyNjEwMjA5MzU4MTNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYjU1NmM2MzIwZTUxNGI1ZGI4MjYyZjUzNDczOTJjMDIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZGFjZDExYjk1ZTIxNDQ3ZWI3NjA1YWEzMTkyMzk0NjUgPSAkKCc8ZGl2IGlkPSJodG1sX2RhY2QxMWI5NWUyMTQ0N2ViNzYwNWFhMzE5MjM5NDY1IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5IaWdoICBCcmlkZ2UsIEJyb254PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9iNTU2YzYzMjBlNTE0YjVkYjgyNjJmNTM0NzM5MmMwMi5zZXRDb250ZW50KGh0bWxfZGFjZDExYjk1ZTIxNDQ3ZWI3NjA1YWEzMTkyMzk0NjUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMWQ0MTBjMWEyMmVlNGJhMDk4ZDJiYThlMWU4NzQ1MDQuYmluZFBvcHVwKHBvcHVwX2I1NTZjNjMyMGU1MTRiNWRiODI2MmY1MzQ3MzkyYzAyKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2E0NTMxODY1MTVjNTRmZTE4ZWY0MWY1OWM5ZmU4OTNkID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODE5NzU0MzcwNTk0OTM2LC03My45MDk0MjE2MDc1NzQzNl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9kM2QzMzUxNjQ5NmM0ZjBmOWM5NzYxZWFmMzNmMDBmYSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9mOGY4MDVkZjBmZWY0OTNhOGI1NDg4MmFkODM2YTYwMyA9ICQoJzxkaXYgaWQ9Imh0bWxfZjhmODA1ZGYwZmVmNDkzYThiNTQ4ODJhZDgzNmE2MDMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk1lbHJvc2UsIEJyb254PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9kM2QzMzUxNjQ5NmM0ZjBmOWM5NzYxZWFmMzNmMDBmYS5zZXRDb250ZW50KGh0bWxfZjhmODA1ZGYwZmVmNDkzYThiNTQ4ODJhZDgzNmE2MDMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYTQ1MzE4NjUxNWM1NGZlMThlZjQxZjU5YzlmZTg5M2QuYmluZFBvcHVwKHBvcHVwX2QzZDMzNTE2NDk2YzRmMGY5Yzk3NjFlYWYzM2YwMGZhKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzk1OGI4MzJmODBiYTQwMWVhODg5N2RiNDc3MDJlZWVmID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODA2MjM4NzQ5MzUxNzcsLTczLjkxNjA5OTg3NDg3NTc1XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzg3NDljNGI2MGNhYTRkZWZiNzY5MTZmYmY1NzU4OGU2ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2NlNTU5ZWFjZjg4YzQ1NTQ5ODIyZTM1MDJkY2I2MDE5ID0gJCgnPGRpdiBpZD0iaHRtbF9jZTU1OWVhY2Y4OGM0NTU0OTgyMmUzNTAyZGNiNjAxOSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+TW90dCBIYXZlbiwgQnJvbng8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzg3NDljNGI2MGNhYTRkZWZiNzY5MTZmYmY1NzU4OGU2LnNldENvbnRlbnQoaHRtbF9jZTU1OWVhY2Y4OGM0NTU0OTgyMmUzNTAyZGNiNjAxOSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl85NThiODMyZjgwYmE0MDFlYTg4OTdkYjQ3NzAyZWVlZi5iaW5kUG9wdXAocG9wdXBfODc0OWM0YjYwY2FhNGRlZmI3NjkxNmZiZjU3NTg4ZTYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYzc1NDdjMjgyNTQxNDBjNmEzYTdiNDE4NzAzMDM4OGUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44MDE2NjM2Mjc3NTYyMDYsLTczLjkxMzIyMTM5Mzg2MTM1XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzJkNGQyNmQzZWY2OTQ4MzdhYWVjMDA3ZWI1YWY0NjJlID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2RlYmI5OGQwZDEyNTQ4NWZiNzNmODJhOTg5ZjIyNjIzID0gJCgnPGRpdiBpZD0iaHRtbF9kZWJiOThkMGQxMjU0ODVmYjczZjgyYTk4OWYyMjYyMyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+UG9ydCBNb3JyaXMsIEJyb254PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8yZDRkMjZkM2VmNjk0ODM3YWFlYzAwN2ViNWFmNDYyZS5zZXRDb250ZW50KGh0bWxfZGViYjk4ZDBkMTI1NDg1ZmI3M2Y4MmE5ODlmMjI2MjMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYzc1NDdjMjgyNTQxNDBjNmEzYTdiNDE4NzAzMDM4OGUuYmluZFBvcHVwKHBvcHVwXzJkNGQyNmQzZWY2OTQ4MzdhYWVjMDA3ZWI1YWY0NjJlKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzFjMjUxYzc0ZmYzZDQ0YzJhM2Q1ZDQ2ZmQ2YjdhOWZjID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODE1MDk5MDQ1NDU4MjIsLTczLjg5NTc4ODIwMDk0NDZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNDQyYjhiZGY2NTRlNGE2NTlmODdjNTMxN2VlN2YzMjYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZjhlNDlmNmNkZDNmNDk5ZDlkOThjMDQ3MTZhYmI5NDggPSAkKCc8ZGl2IGlkPSJodG1sX2Y4ZTQ5ZjZjZGQzZjQ5OWQ5ZDk4YzA0NzE2YWJiOTQ4IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Mb25nd29vZCwgQnJvbng8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzQ0MmI4YmRmNjU0ZTRhNjU5Zjg3YzUzMTdlZTdmMzI2LnNldENvbnRlbnQoaHRtbF9mOGU0OWY2Y2RkM2Y0OTlkOWQ5OGMwNDcxNmFiYjk0OCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8xYzI1MWM3NGZmM2Q0NGMyYTNkNWQ0NmZkNmI3YTlmYy5iaW5kUG9wdXAocG9wdXBfNDQyYjhiZGY2NTRlNGE2NTlmODdjNTMxN2VlN2YzMjYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZDVlMDQ5MzJkZDQ4NGRjNTk1ZDE3MjdkZjY3NTFkMzYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44MDk3Mjk4NzkzODcwOSwtNzMuODgzMzE1MDU5NTUyOTFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMjM0ZWY5YTM1NmQ2NDdjMzk0NTEyNTI5MmM0NTM4NDYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNGRjZDYwMDhmNTllNDViOTkzODYwNDhlY2EyNWJlMmYgPSAkKCc8ZGl2IGlkPSJodG1sXzRkY2Q2MDA4ZjU5ZTQ1Yjk5Mzg2MDQ4ZWNhMjViZTJmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5IdW50cyBQb2ludCwgQnJvbng8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzIzNGVmOWEzNTZkNjQ3YzM5NDUxMjUyOTJjNDUzODQ2LnNldENvbnRlbnQoaHRtbF80ZGNkNjAwOGY1OWU0NWI5OTM4NjA0OGVjYTI1YmUyZik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9kNWUwNDkzMmRkNDg0ZGM1OTVkMTcyN2RmNjc1MWQzNi5iaW5kUG9wdXAocG9wdXBfMjM0ZWY5YTM1NmQ2NDdjMzk0NTEyNTI5MmM0NTM4NDYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNjVkMDI4MTMzNmI5NDlmNzkyMGMzNGVkNTM4NzkxOTYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44MjM1OTE5ODU4NTUzNCwtNzMuOTAxNTA2NDg5NDMwNTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMWYwZTkyOWQ2MDdkNGZkOGE3YmM0YzgwMGMxZTI1MzUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZWJkMTQ2ZmYzNjE0NGRiOWI5ZjE2ZmE1YTc1MTcxYjggPSAkKCc8ZGl2IGlkPSJodG1sX2ViZDE0NmZmMzYxNDRkYjliOWYxNmZhNWE3NTE3MWI4IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Nb3JyaXNhbmlhLCBCcm9ueDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMWYwZTkyOWQ2MDdkNGZkOGE3YmM0YzgwMGMxZTI1MzUuc2V0Q29udGVudChodG1sX2ViZDE0NmZmMzYxNDRkYjliOWYxNmZhNWE3NTE3MWI4KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzY1ZDAyODEzMzZiOTQ5Zjc5MjBjMzRlZDUzODc5MTk2LmJpbmRQb3B1cChwb3B1cF8xZjBlOTI5ZDYwN2Q0ZmQ4YTdiYzRjODAwYzFlMjUzNSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl83ZTViNzU3NGYwZDM0MDhiOTUwNTFjM2E1Zjc0YmI5MiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjgyMTAxMjE5NzkxNDAxNSwtNzMuODY1NzQ2MDk1NTQ5MjRdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfN2UyOTE5ODljNGYyNGI5MWJkNjE1YmY1NjcwMDM0NmQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMTE5MzJlYjBkYzE4NGFkMTkxYWIyZTJlOTdkOWQ4ZDIgPSAkKCc8ZGl2IGlkPSJodG1sXzExOTMyZWIwZGMxODRhZDE5MWFiMmUyZTk3ZDlkOGQyIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Tb3VuZHZpZXcsIEJyb254PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF83ZTI5MTk4OWM0ZjI0YjkxYmQ2MTViZjU2NzAwMzQ2ZC5zZXRDb250ZW50KGh0bWxfMTE5MzJlYjBkYzE4NGFkMTkxYWIyZTJlOTdkOWQ4ZDIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfN2U1Yjc1NzRmMGQzNDA4Yjk1MDUxYzNhNWY3NGJiOTIuYmluZFBvcHVwKHBvcHVwXzdlMjkxOTg5YzRmMjRiOTFiZDYxNWJmNTY3MDAzNDZkKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzRhYTE0YmY0NDY4ZjQxNjBiNGYwYTYxM2ZlYzk3MzdlID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODA2NTUxMTIwMDM1ODksLTczLjg1NDE0NDE2MTg5MjY2XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzljY2U2MTk3YWE4OTRiNTNhMjhjMzYwYWMxYzBjNTc4ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzQxMjE5NGQyMWVhNDQyZmJhYTIyNjZjMjI4YjA0ZjM1ID0gJCgnPGRpdiBpZD0iaHRtbF80MTIxOTRkMjFlYTQ0MmZiYWEyMjY2YzIyOGIwNGYzNSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q2xhc29uIFBvaW50LCBCcm9ueDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOWNjZTYxOTdhYTg5NGI1M2EyOGMzNjBhYzFjMGM1Nzguc2V0Q29udGVudChodG1sXzQxMjE5NGQyMWVhNDQyZmJhYTIyNjZjMjI4YjA0ZjM1KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzRhYTE0YmY0NDY4ZjQxNjBiNGYwYTYxM2ZlYzk3MzdlLmJpbmRQb3B1cChwb3B1cF85Y2NlNjE5N2FhODk0YjUzYTI4YzM2MGFjMWMwYzU3OCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl81MDUxMTZiOWQ0ZTI0YWE2YWY0NjZkMzEyM2U2MjI1NiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjgxNTEwOTI1ODA0MDA1LC03My44MTYzNTAwMjE1ODQ0MV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9iZWZkMDJlYzc2NTQ0NjExYjE4MjdjYzI1NWNjMTA3ZSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8yNWM5OTVjZmFlY2Y0OWU1YTVmOTc3MzkwMDNkYjJmNSA9ICQoJzxkaXYgaWQ9Imh0bWxfMjVjOTk1Y2ZhZWNmNDllNWE1Zjk3NzM5MDAzZGIyZjUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRocm9ncyBOZWNrLCBCcm9ueDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYmVmZDAyZWM3NjU0NDYxMWIxODI3Y2MyNTVjYzEwN2Uuc2V0Q29udGVudChodG1sXzI1Yzk5NWNmYWVjZjQ5ZTVhNWY5NzczOTAwM2RiMmY1KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzUwNTExNmI5ZDRlMjRhYTZhZjQ2NmQzMTIzZTYyMjU2LmJpbmRQb3B1cChwb3B1cF9iZWZkMDJlYzc2NTQ0NjExYjE4MjdjYzI1NWNjMTA3ZSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8yMjZiNmM1MzU1YWM0Y2VkYmM2NTJiMWMxMWI4NmNkNiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjg0NDI0NTkzNjk0NzM3NCwtNzMuODI0MDk5MjY3NTM4NV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9jY2I2OWJiNWNkN2I0ZDYxYThhMzJiODQ0ZjkzNGE2OSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF81ZWYwZjU4NmE1Yjc0YTBkODUyZDAwZTg4NDU2M2M5OCA9ICQoJzxkaXYgaWQ9Imh0bWxfNWVmMGY1ODZhNWI3NGEwZDg1MmQwMGU4ODQ1NjNjOTgiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNvdW50cnkgQ2x1YiwgQnJvbng8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2NjYjY5YmI1Y2Q3YjRkNjFhOGEzMmI4NDRmOTM0YTY5LnNldENvbnRlbnQoaHRtbF81ZWYwZjU4NmE1Yjc0YTBkODUyZDAwZTg4NDU2M2M5OCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8yMjZiNmM1MzU1YWM0Y2VkYmM2NTJiMWMxMWI4NmNkNi5iaW5kUG9wdXAocG9wdXBfY2NiNjliYjVjZDdiNGQ2MWE4YTMyYjg0NGY5MzRhNjkpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNDM3NTc1NzVmZWQwNDZkYTlmZDA4ZDQwMTcwZWE4MTYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44Mzc5Mzc4MjIyNjcyODYsLTczLjg1NjAwMzEwNTM1NzgzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzBjYzFhNDVjOTE5ZDRiMjFiNWRlM2I3MjU3YWIzZDI4ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzdlYjNlY2YzZWFjNjQ0NDhiMDQ4NmIzZDlmZTk3ZjEwID0gJCgnPGRpdiBpZD0iaHRtbF83ZWIzZWNmM2VhYzY0NDQ4YjA0ODZiM2Q5ZmU5N2YxMCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+UGFya2NoZXN0ZXIsIEJyb254PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8wY2MxYTQ1YzkxOWQ0YjIxYjVkZTNiNzI1N2FiM2QyOC5zZXRDb250ZW50KGh0bWxfN2ViM2VjZjNlYWM2NDQ0OGIwNDg2YjNkOWZlOTdmMTApOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNDM3NTc1NzVmZWQwNDZkYTlmZDA4ZDQwMTcwZWE4MTYuYmluZFBvcHVwKHBvcHVwXzBjYzFhNDVjOTE5ZDRiMjFiNWRlM2I3MjU3YWIzZDI4KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzQxY2UzZDk1YmJhNTRiMGE4NDNjNDA0MDgzNzdkYmEzID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODQwNjE5NDk2NDMyNywtNzMuODQyMTk0MDc2MDQ0NDRdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfODMxYzc4NTc0MjNjNGZmMTg5NjE1MzEzMzAwZjFlZTIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNzkzZGE3ZDYyMDFlNGUyYmIzMzdlZTc3NWQ5Y2E1ZDAgPSAkKCc8ZGl2IGlkPSJodG1sXzc5M2RhN2Q2MjAxZTRlMmJiMzM3ZWU3NzVkOWNhNWQwIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5XZXN0Y2hlc3RlciBTcXVhcmUsIEJyb254PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF84MzFjNzg1NzQyM2M0ZmYxODk2MTUzMTMzMDBmMWVlMi5zZXRDb250ZW50KGh0bWxfNzkzZGE3ZDYyMDFlNGUyYmIzMzdlZTc3NWQ5Y2E1ZDApOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNDFjZTNkOTViYmE1NGIwYTg0M2M0MDQwODM3N2RiYTMuYmluZFBvcHVwKHBvcHVwXzgzMWM3ODU3NDIzYzRmZjE4OTYxNTMxMzMwMGYxZWUyKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2Q0YWMxZDhmZGRlNTQ0OWVhYjdiOGY2ODUzN2I1YmZmID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODQzNjA4NDcxMjQ3MTgsLTczLjg2NjI5OTE4MDc1NjFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZjkxMTlkZTI3OWJlNGQ0NzhmODIwYjI0YmRlMDBmODUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNzBkZmFhODY5OTAyNGMxMGJhZGZiNWRiZmE4YzZhNDYgPSAkKCc8ZGl2IGlkPSJodG1sXzcwZGZhYTg2OTkwMjRjMTBiYWRmYjVkYmZhOGM2YTQ2IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5WYW4gTmVzdCwgQnJvbng8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2Y5MTE5ZGUyNzliZTRkNDc4ZjgyMGIyNGJkZTAwZjg1LnNldENvbnRlbnQoaHRtbF83MGRmYWE4Njk5MDI0YzEwYmFkZmI1ZGJmYThjNmE0Nik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9kNGFjMWQ4ZmRkZTU0NDllYWI3YjhmNjg1MzdiNWJmZi5iaW5kUG9wdXAocG9wdXBfZjkxMTlkZTI3OWJlNGQ0NzhmODIwYjI0YmRlMDBmODUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYjkyZTNkMDQ5ZjEwNDk0ZDg1NTNmNGExMzEwMTA1NDEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44NDc1NDkwNjM1MzYzMzQsLTczLjg1MDQwMTc4MDMwNDIxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzZmZTJkYzlkZWVkOTQ4MTNiYzA3ZDE0Yzg1NDJkZGU1ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzE4NmUwY2Q3MmFmMjQxODc4OTc4NGE3MzgwZWFmZTNkID0gJCgnPGRpdiBpZD0iaHRtbF8xODZlMGNkNzJhZjI0MTg3ODk3ODRhNzM4MGVhZmUzZCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+TW9ycmlzIFBhcmssIEJyb254PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF82ZmUyZGM5ZGVlZDk0ODEzYmMwN2QxNGM4NTQyZGRlNS5zZXRDb250ZW50KGh0bWxfMTg2ZTBjZDcyYWYyNDE4Nzg5Nzg0YTczODBlYWZlM2QpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYjkyZTNkMDQ5ZjEwNDk0ZDg1NTNmNGExMzEwMTA1NDEuYmluZFBvcHVwKHBvcHVwXzZmZTJkYzlkZWVkOTQ4MTNiYzA3ZDE0Yzg1NDJkZGU1KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2NhNTBmMjYyYmFhYjQwNDRiNjNmMTRlNWE0MjdiY2FhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODU3Mjc3MTAwNzM4OTUsLTczLjg4ODQ1MTk2MTM0ODA0XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2RiNTcxZTUwMjkzMzQwZDRhYTI3ZTNkOTdiYTZiOTZjID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2M5M2VlODA4YWUxODRiMDU4ZGI4ZjcyODI4NWRkNWFiID0gJCgnPGRpdiBpZD0iaHRtbF9jOTNlZTgwOGFlMTg0YjA1OGRiOGY3MjgyODVkZDVhYiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QmVsbW9udCwgQnJvbng8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2RiNTcxZTUwMjkzMzQwZDRhYTI3ZTNkOTdiYTZiOTZjLnNldENvbnRlbnQoaHRtbF9jOTNlZTgwOGFlMTg0YjA1OGRiOGY3MjgyODVkZDVhYik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9jYTUwZjI2MmJhYWI0MDQ0YjYzZjE0ZTVhNDI3YmNhYS5iaW5kUG9wdXAocG9wdXBfZGI1NzFlNTAyOTMzNDBkNGFhMjdlM2Q5N2JhNmI5NmMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYzJmN2YzMDFkZjc5NDNkM2I3ZTlhYWU1ZmVmZGY3MGIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44ODEzOTQ5NzcyNzA4NiwtNzMuOTE3MTkwNDgyMTAzOTNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYjI2NjIzMzM1OWRkNGFmZDk4NDE5NWM4YjA0YTcyYjcgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfM2JhMDBlNzFiMDZkNDZjY2E4MjUwZWRiYjc0ZmEwOGUgPSAkKCc8ZGl2IGlkPSJodG1sXzNiYTAwZTcxYjA2ZDQ2Y2NhODI1MGVkYmI3NGZhMDhlIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5TcHV5dGVuIER1eXZpbCwgQnJvbng8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2IyNjYyMzMzNTlkZDRhZmQ5ODQxOTVjOGIwNGE3MmI3LnNldENvbnRlbnQoaHRtbF8zYmEwMGU3MWIwNmQ0NmNjYTgyNTBlZGJiNzRmYTA4ZSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9jMmY3ZjMwMWRmNzk0M2QzYjdlOWFhZTVmZWZkZjcwYi5iaW5kUG9wdXAocG9wdXBfYjI2NjIzMzM1OWRkNGFmZDk4NDE5NWM4YjA0YTcyYjcpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYTg2Y2UxYmY4ZWMzNGIwZWIwMzIzYTA0M2I5YjU1OWMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC45MDg1NDI4Mjk1MDY2NiwtNzMuOTA0NTMwNTQ5MDg5MjddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfN2ZmZDkxNDVhMGExNGY1MDhkMjRhY2ZiMDcxZmM4NzkgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYTlmODZmM2YyMWUyNDhlNjgyMGIzYWI1NDYzMGFiYjEgPSAkKCc8ZGl2IGlkPSJodG1sX2E5Zjg2ZjNmMjFlMjQ4ZTY4MjBiM2FiNTQ2MzBhYmIxIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Ob3J0aCBSaXZlcmRhbGUsIEJyb254PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF83ZmZkOTE0NWEwYTE0ZjUwOGQyNGFjZmIwNzFmYzg3OS5zZXRDb250ZW50KGh0bWxfYTlmODZmM2YyMWUyNDhlNjgyMGIzYWI1NDYzMGFiYjEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYTg2Y2UxYmY4ZWMzNGIwZWIwMzIzYTA0M2I5YjU1OWMuYmluZFBvcHVwKHBvcHVwXzdmZmQ5MTQ1YTBhMTRmNTA4ZDI0YWNmYjA3MWZjODc5KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzAxMzJkMzgwNTQ0MDQ5YzJiZTgyNThiN2M2ODM4ZDA2ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODUwNjQxNDA5NDAzMzUsLTczLjgzMjA3Mzc4MjQwNDddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYTA0ZDYxMWQ2NDBhNGVkYThhYjE1MmQ1NjBhY2QzYzQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMjgwMDdlNjk4MDg3NGZiY2E3OWY0MWUwNzQ5YTNhZDcgPSAkKCc8ZGl2IGlkPSJodG1sXzI4MDA3ZTY5ODA4NzRmYmNhNzlmNDFlMDc0OWEzYWQ3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5QZWxoYW0gQmF5LCBCcm9ueDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYTA0ZDYxMWQ2NDBhNGVkYThhYjE1MmQ1NjBhY2QzYzQuc2V0Q29udGVudChodG1sXzI4MDA3ZTY5ODA4NzRmYmNhNzlmNDFlMDc0OWEzYWQ3KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzAxMzJkMzgwNTQ0MDQ5YzJiZTgyNThiN2M2ODM4ZDA2LmJpbmRQb3B1cChwb3B1cF9hMDRkNjExZDY0MGE0ZWRhOGFiMTUyZDU2MGFjZDNjNCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8yOWZmNjI1NWZlZGY0MTNjYmJjNmM3MjBiYWE1ZDU3NiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjgyNjU3OTUxNjg2OTIyLC03My44MjYyMDI3NTk5NDA3M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF80ZDE0MzJiZDYyMGQ0Mzk5OTYwZTJkZjJkYjBhMzQwYiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF81YzMyNTllNTFhYzk0YzdhYmFmMGUzNDg4YTI5ZThlNyA9ICQoJzxkaXYgaWQ9Imh0bWxfNWMzMjU5ZTUxYWM5NGM3YWJhZjBlMzQ4OGEyOWU4ZTciIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlNjaHV5bGVydmlsbGUsIEJyb254PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF80ZDE0MzJiZDYyMGQ0Mzk5OTYwZTJkZjJkYjBhMzQwYi5zZXRDb250ZW50KGh0bWxfNWMzMjU5ZTUxYWM5NGM3YWJhZjBlMzQ4OGEyOWU4ZTcpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMjlmZjYyNTVmZWRmNDEzY2JiYzZjNzIwYmFhNWQ1NzYuYmluZFBvcHVwKHBvcHVwXzRkMTQzMmJkNjIwZDQzOTk5NjBlMmRmMmRiMGEzNDBiKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2I5NjFjN2Q4MzExNDRmMDdiNDJiYTY3NjRhN2I1MTAxID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODIxOTg2MTE4MTYzNDk0LC03My44MTM4ODUxNDQyODYxOV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8yZDcxOTY1YTQwZTE0MWEwYjljZDE4MDllZTg3MTJhMSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9iZTYzNzZlY2EyMDE0ZjAxYWJlYmZkZWU4NGUwMjk0NiA9ICQoJzxkaXYgaWQ9Imh0bWxfYmU2Mzc2ZWNhMjAxNGYwMWFiZWJmZGVlODRlMDI5NDYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkVkZ2V3YXRlciBQYXJrLCBCcm9ueDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMmQ3MTk2NWE0MGUxNDFhMGI5Y2QxODA5ZWU4NzEyYTEuc2V0Q29udGVudChodG1sX2JlNjM3NmVjYTIwMTRmMDFhYmViZmRlZTg0ZTAyOTQ2KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2I5NjFjN2Q4MzExNDRmMDdiNDJiYTY3NjRhN2I1MTAxLmJpbmRQb3B1cChwb3B1cF8yZDcxOTY1YTQwZTE0MWEwYjljZDE4MDllZTg3MTJhMSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl85OTA0YmFkZGYzZjU0YzFlOGVjNmIzMTk0ZWM3MTFkYSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjgxOTAxNDM3Njk4ODMxNCwtNzMuODQ4MDI3Mjk1ODI3MzVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZDI5OTBkYjcxMjM1NGExOWIzNWRiOGJlNzdmZjA3NmQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZTBhNDc2ZTc2ZDYwNDY0YWJhMzQ4ODhjZWIxMzVlZmEgPSAkKCc8ZGl2IGlkPSJodG1sX2UwYTQ3NmU3NmQ2MDQ2NGFiYTM0ODg4Y2ViMTM1ZWZhIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DYXN0bGUgSGlsbCwgQnJvbng8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2QyOTkwZGI3MTIzNTRhMTliMzVkYjhiZTc3ZmYwNzZkLnNldENvbnRlbnQoaHRtbF9lMGE0NzZlNzZkNjA0NjRhYmEzNDg4OGNlYjEzNWVmYSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl85OTA0YmFkZGYzZjU0YzFlOGVjNmIzMTk0ZWM3MTFkYS5iaW5kUG9wdXAocG9wdXBfZDI5OTBkYjcxMjM1NGExOWIzNWRiOGJlNzdmZjA3NmQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNzMyNmI0NDM3NDRlNDZmMzhjNjkyNzBhNDRiY2EyZGUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44NzEzNzA3ODE5MjM3MSwtNzMuODYzMzIzNjE2NTI3NzddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfOGNjNDM1YWE2YzAyNDMxNGJjZmI1ZWZhN2E1Yjk3ZjcgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNjI3ZjBmNzg4NzIxNDU2MzgxNDdhYzMxNDdjMDI5NGYgPSAkKCc8ZGl2IGlkPSJodG1sXzYyN2YwZjc4ODcyMTQ1NjM4MTQ3YWMzMTQ3YzAyOTRmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5PbGludmlsbGUsIEJyb254PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF84Y2M0MzVhYTZjMDI0MzE0YmNmYjVlZmE3YTViOTdmNy5zZXRDb250ZW50KGh0bWxfNjI3ZjBmNzg4NzIxNDU2MzgxNDdhYzMxNDdjMDI5NGYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNzMyNmI0NDM3NDRlNDZmMzhjNjkyNzBhNDRiY2EyZGUuYmluZFBvcHVwKHBvcHVwXzhjYzQzNWFhNmMwMjQzMTRiY2ZiNWVmYTdhNWI5N2Y3KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzc3ZmRiZmRjYmQ4YjQ2MTE4NjVlOTZjOGRjMDM2OTVjID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODYyOTY1NjI0Nzc5OTgsLTczLjg0MTYxMTk0ODMxMjIzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzg4MjE2OWY5ZjU0ZDQ3MDRhMGIzZjVkYmM2ZDhiMTFmID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzlhZTRmM2MzNTQzMDQ1NDRhMzY0N2I0MTY5YmYwMzYyID0gJCgnPGRpdiBpZD0iaHRtbF85YWU0ZjNjMzU0MzA0NTQ0YTM2NDdiNDE2OWJmMDM2MiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+UGVsaGFtIEdhcmRlbnMsIEJyb254PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF84ODIxNjlmOWY1NGQ0NzA0YTBiM2Y1ZGJjNmQ4YjExZi5zZXRDb250ZW50KGh0bWxfOWFlNGYzYzM1NDMwNDU0NGEzNjQ3YjQxNjliZjAzNjIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNzdmZGJmZGNiZDhiNDYxMTg2NWU5NmM4ZGMwMzY5NWMuYmluZFBvcHVwKHBvcHVwXzg4MjE2OWY5ZjU0ZDQ3MDRhMGIzZjVkYmM2ZDhiMTFmKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2Q1MWQ3NGY0YjFkNTQzNGFiODRjZmUwM2E5Mjk0ZjU1ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODM0MjgzODA3MzM4NTEsLTczLjkxNTU4OTQxNzczNDQ0XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzRjZGIyYWIxOTMxNzQwYjM5ZWU4ZDA0ODQ3NGJhNWI2ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzllZGM3ZGQ3ODVmNjQzNmNhN2Q4ODk4NjZkZWJiZDJiID0gJCgnPGRpdiBpZD0iaHRtbF85ZWRjN2RkNzg1ZjY0MzZjYTdkODg5ODY2ZGViYmQyYiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q29uY291cnNlLCBCcm9ueDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNGNkYjJhYjE5MzE3NDBiMzllZThkMDQ4NDc0YmE1YjYuc2V0Q29udGVudChodG1sXzllZGM3ZGQ3ODVmNjQzNmNhN2Q4ODk4NjZkZWJiZDJiKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2Q1MWQ3NGY0YjFkNTQzNGFiODRjZmUwM2E5Mjk0ZjU1LmJpbmRQb3B1cChwb3B1cF80Y2RiMmFiMTkzMTc0MGIzOWVlOGQwNDg0NzRiYTViNik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl84OGJmNGJjY2E5Njk0ZmI4ODk5OTg0YTEyMjJhZWZjNiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjgyOTc3NDI5Nzg3MTYxLC03My44NTA1MzUyNDQ1MTkzNV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8zYzI5NDdjZDliNGU0MTAzYmUzMTYzYmI0YTY2YjZhNCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF81MjliZGI1OGQyZWU0NWU1YTE1MTAwZDA4ZDg3ODFkMSA9ICQoJzxkaXYgaWQ9Imh0bWxfNTI5YmRiNThkMmVlNDVlNWExNTEwMGQwOGQ4NzgxZDEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlVuaW9ucG9ydCwgQnJvbng8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzNjMjk0N2NkOWI0ZTQxMDNiZTMxNjNiYjRhNjZiNmE0LnNldENvbnRlbnQoaHRtbF81MjliZGI1OGQyZWU0NWU1YTE1MTAwZDA4ZDg3ODFkMSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl84OGJmNGJjY2E5Njk0ZmI4ODk5OTg0YTEyMjJhZWZjNi5iaW5kUG9wdXAocG9wdXBfM2MyOTQ3Y2Q5YjRlNDEwM2JlMzE2M2JiNGE2NmI2YTQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZDdlNDBlNWNlMjBjNDMwNWE0OTU0ZmQwYjFkODhiMjQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44ODQ1NjEzMDMwMzczMiwtNzMuODQ4MDgyNzE4NzcxNjhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNzZhNDcwMzJlN2MzNDljNzgzMzQ5MWZiNjJhMGE1N2UgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZDJjYThjYzhlYzEyNGIxMGI2MmQ1NTliNzQ2ZmQzNGQgPSAkKCc8ZGl2IGlkPSJodG1sX2QyY2E4Y2M4ZWMxMjRiMTBiNjJkNTU5Yjc0NmZkMzRkIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5FZGVud2FsZCwgQnJvbng8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzc2YTQ3MDMyZTdjMzQ5Yzc4MzM0OTFmYjYyYTBhNTdlLnNldENvbnRlbnQoaHRtbF9kMmNhOGNjOGVjMTI0YjEwYjYyZDU1OWI3NDZmZDM0ZCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9kN2U0MGU1Y2UyMGM0MzA1YTQ5NTRmZDBiMWQ4OGIyNC5iaW5kUG9wdXAocG9wdXBfNzZhNDcwMzJlN2MzNDljNzgzMzQ5MWZiNjJhMGE1N2UpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNmE5MjM2ZWExYzhjNGExY2EyZWNlMmFjZTY0YTM2MzggPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42MjU4MDEwNjUwMTA2NTYsLTc0LjAzMDYyMDY5MzUzODEzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzM0MGQwNDRiNjYyZDQ4OTBiNDdjMTU1NjBlNWVjYzExID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzYyYzc0NTQ0YzZjOTRjNmQ5NTExMTRhZWZkMzJjYzllID0gJCgnPGRpdiBpZD0iaHRtbF82MmM3NDU0NGM2Yzk0YzZkOTUxMTE0YWVmZDMyY2M5ZSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QmF5IFJpZGdlLCBCcm9va2x5bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMzQwZDA0NGI2NjJkNDg5MGI0N2MxNTU2MGU1ZWNjMTEuc2V0Q29udGVudChodG1sXzYyYzc0NTQ0YzZjOTRjNmQ5NTExMTRhZWZkMzJjYzllKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzZhOTIzNmVhMWM4YzRhMWNhMmVjZTJhY2U2NGEzNjM4LmJpbmRQb3B1cChwb3B1cF8zNDBkMDQ0YjY2MmQ0ODkwYjQ3YzE1NTYwZTVlY2MxMSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9mOGVhYzJmYzg4N2I0NzJlYTJlYjE5ODA5YjE1YzI1MCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYxMTAwODkwMjAyMDQ0LC03My45OTUxNzk5ODM4MDcyOV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF84YTJiMjMxOTU5OTk0YjRmODViNjA3MTBjOWUwZTdkMSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9mZGE4MDU3MWM5MzE0MWNjOGQyNmRlMjQwMWNiYTJkYSA9ICQoJzxkaXYgaWQ9Imh0bWxfZmRhODA1NzFjOTMxNDFjYzhkMjZkZTI0MDFjYmEyZGEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkJlbnNvbmh1cnN0LCBCcm9va2x5bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOGEyYjIzMTk1OTk5NGI0Zjg1YjYwNzEwYzllMGU3ZDEuc2V0Q29udGVudChodG1sX2ZkYTgwNTcxYzkzMTQxY2M4ZDI2ZGUyNDAxY2JhMmRhKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2Y4ZWFjMmZjODg3YjQ3MmVhMmViMTk4MDliMTVjMjUwLmJpbmRQb3B1cChwb3B1cF84YTJiMjMxOTU5OTk0YjRmODViNjA3MTBjOWUwZTdkMSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9jM2I4N2Y1NzJkYjc0YTM4YjZlNWYxMjJjMTFlZDkzZCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjY0NTEwMjk0OTI1NDI5LC03NC4wMTAzMTYxODUyNzc4NF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9jMzBhZDZmMTU5M2M0ODZhYThjNDE2NjA3M2EwNTg0MSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF80NzcyMWZhNjYyM2I0MjZlYTIxMTg5NTNjMjAyYmMwYSA9ICQoJzxkaXYgaWQ9Imh0bWxfNDc3MjFmYTY2MjNiNDI2ZWEyMTE4OTUzYzIwMmJjMGEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlN1bnNldCBQYXJrLCBCcm9va2x5bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYzMwYWQ2ZjE1OTNjNDg2YWE4YzQxNjYwNzNhMDU4NDEuc2V0Q29udGVudChodG1sXzQ3NzIxZmE2NjIzYjQyNmVhMjExODk1M2MyMDJiYzBhKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2MzYjg3ZjU3MmRiNzRhMzhiNmU1ZjEyMmMxMWVkOTNkLmJpbmRQb3B1cChwb3B1cF9jMzBhZDZmMTU5M2M0ODZhYThjNDE2NjA3M2EwNTg0MSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9mZjc5OTY2ZDkwMzM0MzJmOGYzNDJjYTcyZWMwYTcwNyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjczMDIwMDk4NDg2NDcsLTczLjk1NDI0MDkzMTI3MzkzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2EyNjEyYmYyZDQ1YTRkM2ZiOGQwODIzZWFlOThkNGNhID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2JiNzJlNTZhMGY3MTQ2MmNiZTdiNDc5NzUyZGNkN2JkID0gJCgnPGRpdiBpZD0iaHRtbF9iYjcyZTU2YTBmNzE0NjJjYmU3YjQ3OTc1MmRjZDdiZCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+R3JlZW5wb2ludCwgQnJvb2tseW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2EyNjEyYmYyZDQ1YTRkM2ZiOGQwODIzZWFlOThkNGNhLnNldENvbnRlbnQoaHRtbF9iYjcyZTU2YTBmNzE0NjJjYmU3YjQ3OTc1MmRjZDdiZCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9mZjc5OTY2ZDkwMzM0MzJmOGYzNDJjYTcyZWMwYTcwNy5iaW5kUG9wdXAocG9wdXBfYTI2MTJiZjJkNDVhNGQzZmI4ZDA4MjNlYWU5OGQ0Y2EpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMTZjMzYzODlhYWQ4NDI0Mzg3YjY1YjA2ZmE1NDFjOTYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41OTUyNjAwMTMwNjU5MywtNzMuOTczNDcwODc3MDg0NDVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNWU4OGI1Y2E0YWVjNGUzN2I2ZmFhNjZmMWZlMmFhMTAgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfM2E4ZGFjYzNkNDc3NDEzNWE2NjBkN2VlNzVmYTJkMjMgPSAkKCc8ZGl2IGlkPSJodG1sXzNhOGRhY2MzZDQ3NzQxMzVhNjYwZDdlZTc1ZmEyZDIzIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5HcmF2ZXNlbmQsIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF81ZTg4YjVjYTRhZWM0ZTM3YjZmYWE2NmYxZmUyYWExMC5zZXRDb250ZW50KGh0bWxfM2E4ZGFjYzNkNDc3NDEzNWE2NjBkN2VlNzVmYTJkMjMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMTZjMzYzODlhYWQ4NDI0Mzg3YjY1YjA2ZmE1NDFjOTYuYmluZFBvcHVwKHBvcHVwXzVlODhiNWNhNGFlYzRlMzdiNmZhYTY2ZjFmZTJhYTEwKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2NhNDgyMDFlY2EzYjQ1ZjFiNTQ3MWJiYTQ1NTU2OGNmID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTc2ODI1MDY1NjY2MDQsLTczLjk2NTA5NDQ4Nzg1MzM2XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzk3MWFkMmQwMzkxYTQzYTRiMjI5ODViMzg2NjBiNDVlID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzliNTA4NGU5N2YwMDQ5MGM4ZGFiYTgzN2MwM2FiZGYzID0gJCgnPGRpdiBpZD0iaHRtbF85YjUwODRlOTdmMDA0OTBjOGRhYmE4MzdjMDNhYmRmMyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QnJpZ2h0b24gQmVhY2gsIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF85NzFhZDJkMDM5MWE0M2E0YjIyOTg1YjM4NjYwYjQ1ZS5zZXRDb250ZW50KGh0bWxfOWI1MDg0ZTk3ZjAwNDkwYzhkYWJhODM3YzAzYWJkZjMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfY2E0ODIwMWVjYTNiNDVmMWI1NDcxYmJhNDU1NTY4Y2YuYmluZFBvcHVwKHBvcHVwXzk3MWFkMmQwMzkxYTQzYTRiMjI5ODViMzg2NjBiNDVlKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2MyNDlhNjdjYzc1MjQ0OTU5NDI1NjM4ODMxNWJjM2ZhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTg2ODkwMTI2NzgzODQsLTczLjk0MzE4NjQwNDgyOTc5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2Q1ZjcwZTc4ZjUwYzQyYjViZTVkOTIwZDU0ZmI5NDViID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzRmNzBlY2NjNzFmNzQwMDdiOWJiZjg4MDJiYzc0MTk2ID0gJCgnPGRpdiBpZD0iaHRtbF80ZjcwZWNjYzcxZjc0MDA3YjliYmY4ODAyYmM3NDE5NiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+U2hlZXBzaGVhZCBCYXksIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9kNWY3MGU3OGY1MGM0MmI1YmU1ZDkyMGQ1NGZiOTQ1Yi5zZXRDb250ZW50KGh0bWxfNGY3MGVjY2M3MWY3NDAwN2I5YmJmODgwMmJjNzQxOTYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYzI0OWE2N2NjNzUyNDQ5NTk0MjU2Mzg4MzE1YmMzZmEuYmluZFBvcHVwKHBvcHVwX2Q1ZjcwZTc4ZjUwYzQyYjViZTVkOTIwZDU0ZmI5NDViKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzhmODZhMzM4OTRkODQ3ZTNiNzk3ZjEzNGIyZDI4ZTc1ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjE0NDMyNTEzMzUwOTgsLTczLjk1NzQzODQwNTU5OTM5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzJiYTEwNGUwM2Q0ZjQ3M2NhODQ5ZDExZDRlODU0ZjM4ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzVmMDNlZGU1YjMxODQ1MzVhZTQ1ZjFhNWI2ZTMwYjlhID0gJCgnPGRpdiBpZD0iaHRtbF81ZjAzZWRlNWIzMTg0NTM1YWU0NWYxYTViNmUzMGI5YSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+TWFuaGF0dGFuIFRlcnJhY2UsIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8yYmExMDRlMDNkNGY0NzNjYTg0OWQxMWQ0ZTg1NGYzOC5zZXRDb250ZW50KGh0bWxfNWYwM2VkZTViMzE4NDUzNWFlNDVmMWE1YjZlMzBiOWEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOGY4NmEzMzg5NGQ4NDdlM2I3OTdmMTM0YjJkMjhlNzUuYmluZFBvcHVwKHBvcHVwXzJiYTEwNGUwM2Q0ZjQ3M2NhODQ5ZDExZDRlODU0ZjM4KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2M0MTU3YmM3ZmE1MDQ1MGQ5ZDBiMzAxMDg0Mjk1ODE3ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjM2MzI1ODkwMjY2NzcsLTczLjk1ODQwMTA2NTMzOTAzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2IxOWM4ZjNjMTAwMjQ3ZjZhNjA3MDQwODNlZGY4ZGE2ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzFkMmQ1YTNkNjIzOTQ2M2E5NjcxOGFlNTMxZjExZWRjID0gJCgnPGRpdiBpZD0iaHRtbF8xZDJkNWEzZDYyMzk0NjNhOTY3MThhZTUzMWYxMWVkYyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RmxhdGJ1c2gsIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9iMTljOGYzYzEwMDI0N2Y2YTYwNzA0MDgzZWRmOGRhNi5zZXRDb250ZW50KGh0bWxfMWQyZDVhM2Q2MjM5NDYzYTk2NzE4YWU1MzFmMTFlZGMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYzQxNTdiYzdmYTUwNDUwZDlkMGIzMDEwODQyOTU4MTcuYmluZFBvcHVwKHBvcHVwX2IxOWM4ZjNjMTAwMjQ3ZjZhNjA3MDQwODNlZGY4ZGE2KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzY5NjE1YWNiYjgzZTRjZDk4MGQ4ZTFkZWE5YTU4NTcxID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjcwODI5MTc2OTUyOTQsLTczLjk0MzI5MTE5MDczNTgyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzU1ZGM5Y2RmNWRmYzQ5YzM4NDFjNDkxNmVjZTZiZGM1ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzk5NDBiY2VlNDBkYjQ2NDNiOGMyNjZiNGMyMDZiMzc3ID0gJCgnPGRpdiBpZD0iaHRtbF85OTQwYmNlZTQwZGI0NjQzYjhjMjY2YjRjMjA2YjM3NyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q3Jvd24gSGVpZ2h0cywgQnJvb2tseW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzU1ZGM5Y2RmNWRmYzQ5YzM4NDFjNDkxNmVjZTZiZGM1LnNldENvbnRlbnQoaHRtbF85OTQwYmNlZTQwZGI0NjQzYjhjMjY2YjRjMjA2YjM3Nyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl82OTYxNWFjYmI4M2U0Y2Q5ODBkOGUxZGVhOWE1ODU3MS5iaW5kUG9wdXAocG9wdXBfNTVkYzljZGY1ZGZjNDljMzg0MWM0OTE2ZWNlNmJkYzUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfODk2ZDllODZkNGEyNDM3ZjgxY2YzMDM4YmFmZjdiMTMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42NDE3MTc3NjY2ODk2MSwtNzMuOTM2MTAyNTYxODU4MzZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfM2U2NzMzOTQ1OWFhNGMyNWIwNTAwMTkzZmNhMWMxODkgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfY2YxNWUyYjkwY2Q3NGI2Y2JjNzdhMTZlMzUxZWYwZWIgPSAkKCc8ZGl2IGlkPSJodG1sX2NmMTVlMmI5MGNkNzRiNmNiYzc3YTE2ZTM1MWVmMGViIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5FYXN0IEZsYXRidXNoLCBCcm9va2x5bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfM2U2NzMzOTQ1OWFhNGMyNWIwNTAwMTkzZmNhMWMxODkuc2V0Q29udGVudChodG1sX2NmMTVlMmI5MGNkNzRiNmNiYzc3YTE2ZTM1MWVmMGViKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzg5NmQ5ZTg2ZDRhMjQzN2Y4MWNmMzAzOGJhZmY3YjEzLmJpbmRQb3B1cChwb3B1cF8zZTY3MzM5NDU5YWE0YzI1YjA1MDAxOTNmY2ExYzE4OSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8wNDkwY2ExOGUxYmQ0NmNiOWJiMTlhM2JmZTcyZmIzYSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjY0MjM4MTk1ODAwMzUyNiwtNzMuOTgwNDIxMTA1NTk0NzRdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZmIxYTYyNjA3YjliNGMwNThjZjA2N2VhZjFjZTQ4MzkgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMzcxMzgwZTM1M2FkNDM0MGE4M2QxNWNiZjI1NDZiNGUgPSAkKCc8ZGl2IGlkPSJodG1sXzM3MTM4MGUzNTNhZDQzNDBhODNkMTVjYmYyNTQ2YjRlIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5LZW5zaW5ndG9uLCBCcm9va2x5bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZmIxYTYyNjA3YjliNGMwNThjZjA2N2VhZjFjZTQ4Mzkuc2V0Q29udGVudChodG1sXzM3MTM4MGUzNTNhZDQzNDBhODNkMTVjYmYyNTQ2YjRlKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzA0OTBjYTE4ZTFiZDQ2Y2I5YmIxOWEzYmZlNzJmYjNhLmJpbmRQb3B1cChwb3B1cF9mYjFhNjI2MDdiOWI0YzA1OGNmMDY3ZWFmMWNlNDgzOSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8xNzRhMmNiOWY5OTg0NDVkYjRjOWFjMzNhOTdlYzdlNyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjY1Njk0NTgzNTc1MTA0LC03My45ODAwNzM0MDQzMDE3Ml0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8xMjg0YjFlODIwYjU0OWE2OTIzODNkMmI0NjVlMzhlMCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8wOWRkOTA3MTlkZDQ0ODdkYWZiZGJlODAxZDgwYmJhZCA9ICQoJzxkaXYgaWQ9Imh0bWxfMDlkZDkwNzE5ZGQ0NDg3ZGFmYmRiZTgwMWQ4MGJiYWQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPldpbmRzb3IgVGVycmFjZSwgQnJvb2tseW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzEyODRiMWU4MjBiNTQ5YTY5MjM4M2QyYjQ2NWUzOGUwLnNldENvbnRlbnQoaHRtbF8wOWRkOTA3MTlkZDQ0ODdkYWZiZGJlODAxZDgwYmJhZCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8xNzRhMmNiOWY5OTg0NDVkYjRjOWFjMzNhOTdlYzdlNy5iaW5kUG9wdXAocG9wdXBfMTI4NGIxZTgyMGI1NDlhNjkyMzgzZDJiNDY1ZTM4ZTApOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYWFlNzUwNzllNzIxNDAxMmEwZjBlNTE3MmYzZDgwNjEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42NzY4MjIyNjIyNTQ3MjQsLTczLjk2NDg1OTI0MjYyNjldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNjczMWU4ODU1YzhiNDU0NDk4OTM3MTUyMDg3NzA0NWYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNjVjYjc3MjE1ZjQwNDgzMjkxZjBjOGYzYjVlMWIxMWYgPSAkKCc8ZGl2IGlkPSJodG1sXzY1Y2I3NzIxNWY0MDQ4MzI5MWYwYzhmM2I1ZTFiMTFmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Qcm9zcGVjdCBIZWlnaHRzLCBCcm9va2x5bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNjczMWU4ODU1YzhiNDU0NDk4OTM3MTUyMDg3NzA0NWYuc2V0Q29udGVudChodG1sXzY1Y2I3NzIxNWY0MDQ4MzI5MWYwYzhmM2I1ZTFiMTFmKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2FhZTc1MDc5ZTcyMTQwMTJhMGYwZTUxNzJmM2Q4MDYxLmJpbmRQb3B1cChwb3B1cF82NzMxZTg4NTVjOGI0NTQ0OTg5MzcxNTIwODc3MDQ1Zik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9hMmQ2MmNjNWY0NGI0MTQ5OWVjZjhmODZiZWU3MjBhYSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjY2Mzk0OTk0MzM5NzU1LC03My45MTAyMzUzNjE3NjYwN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF81OGMyYmE4MzFmZjI0OWZmYWZmODA4MjQzNmQwYTk0NSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9iMzA5Yzg5NDJiMTE0ODc3OGI2MWRhYWRjNzQ2N2M1MSA9ICQoJzxkaXYgaWQ9Imh0bWxfYjMwOWM4OTQyYjExNDg3NzhiNjFkYWFkYzc0NjdjNTEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkJyb3duc3ZpbGxlLCBCcm9va2x5bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNThjMmJhODMxZmYyNDlmZmFmZjgwODI0MzZkMGE5NDUuc2V0Q29udGVudChodG1sX2IzMDljODk0MmIxMTQ4Nzc4YjYxZGFhZGM3NDY3YzUxKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2EyZDYyY2M1ZjQ0YjQxNDk5ZWNmOGY4NmJlZTcyMGFhLmJpbmRQb3B1cChwb3B1cF81OGMyYmE4MzFmZjI0OWZmYWZmODA4MjQzNmQwYTk0NSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl83ZDIzMzcyOGM5ZmI0NGMyYWE0NTkyN2NjZThkNTI0YyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjcwNzE0NDM5MzQ0MjUxLC03My45NTgxMTUyOTIyMDkyN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9iNDBhODAxODk2N2E0ODgzYTFlODk4MzkyZGVjNDRlNSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9mMzBlMzYzNDJlZTk0N2E5YjZlZDMyMzNmYjU3NmZhNiA9ICQoJzxkaXYgaWQ9Imh0bWxfZjMwZTM2MzQyZWU5NDdhOWI2ZWQzMjMzZmI1NzZmYTYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPldpbGxpYW1zYnVyZywgQnJvb2tseW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2I0MGE4MDE4OTY3YTQ4ODNhMWU4OTgzOTJkZWM0NGU1LnNldENvbnRlbnQoaHRtbF9mMzBlMzYzNDJlZTk0N2E5YjZlZDMyMzNmYjU3NmZhNik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl83ZDIzMzcyOGM5ZmI0NGMyYWE0NTkyN2NjZThkNTI0Yy5iaW5kUG9wdXAocG9wdXBfYjQwYTgwMTg5NjdhNDg4M2ExZTg5ODM5MmRlYzQ0ZTUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfODlmMjdhMTU2MjI2NGZlNjg4NWZhOTNmNmYwMTA2ZWEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42OTgxMTYxMTAxNzkwMSwtNzMuOTI1MjU3OTc0ODcwNDVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYzVlMzE4MzQxYTMzNGFhMzhiYTA4MWE2ZGFlNmJiM2MgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZWIxMzRkNGYxYmY3NGJjMDgzNDdhOTY2MTM1ZDQ3N2EgPSAkKCc8ZGl2IGlkPSJodG1sX2ViMTM0ZDRmMWJmNzRiYzA4MzQ3YTk2NjEzNWQ0NzdhIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CdXNod2ljaywgQnJvb2tseW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2M1ZTMxODM0MWEzMzRhYTM4YmEwODFhNmRhZTZiYjNjLnNldENvbnRlbnQoaHRtbF9lYjEzNGQ0ZjFiZjc0YmMwODM0N2E5NjYxMzVkNDc3YSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl84OWYyN2ExNTYyMjY0ZmU2ODg1ZmE5M2Y2ZjAxMDZlYS5iaW5kUG9wdXAocG9wdXBfYzVlMzE4MzQxYTMzNGFhMzhiYTA4MWE2ZGFlNmJiM2MpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfY2UzZGYyZTMxMGRmNGYzMTkwNmUwNmE3MmU0Nzk5YzIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42ODcyMzE2MDc3MjA0NTYsLTczLjk0MTc4NDg4NjkwMjk3XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2U1OGUxNzgxZTgzMzRmNTc4YzE0ZjljMWRhZjczMjIwID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2QwYmE2MDVmYjNmYzRkODZhYzUwNzIxODAxMGE5YTQ2ID0gJCgnPGRpdiBpZD0iaHRtbF9kMGJhNjA1ZmIzZmM0ZDg2YWM1MDcyMTgwMTBhOWE0NiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QmVkZm9yZCBTdHV5dmVzYW50LCBCcm9va2x5bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZTU4ZTE3ODFlODMzNGY1NzhjMTRmOWMxZGFmNzMyMjAuc2V0Q29udGVudChodG1sX2QwYmE2MDVmYjNmYzRkODZhYzUwNzIxODAxMGE5YTQ2KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2NlM2RmMmUzMTBkZjRmMzE5MDZlMDZhNzJlNDc5OWMyLmJpbmRQb3B1cChwb3B1cF9lNThlMTc4MWU4MzM0ZjU3OGMxNGY5YzFkYWY3MzIyMCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8wOTc5ZTliMWNlMTE0MGM0OTdiMmY2M2U2Njk2MGYzOCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjY5NTg2MzcyMjcyNDA4NCwtNzMuOTkzNzgyMjU0OTY0MjRdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMmM4NTgzNjY3NjQ1NGYzMTg1YmU3YWFlNjk5NDk0ODIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZmIyNTkzNjNlNjNkNDJhOWE2NDk1YmMxNmYyYzU3YjAgPSAkKCc8ZGl2IGlkPSJodG1sX2ZiMjU5MzYzZTYzZDQyYTlhNjQ5NWJjMTZmMmM1N2IwIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Ccm9va2x5biBIZWlnaHRzLCBCcm9va2x5bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMmM4NTgzNjY3NjQ1NGYzMTg1YmU3YWFlNjk5NDk0ODIuc2V0Q29udGVudChodG1sX2ZiMjU5MzYzZTYzZDQyYTlhNjQ5NWJjMTZmMmM1N2IwKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzA5NzllOWIxY2UxMTQwYzQ5N2IyZjYzZTY2OTYwZjM4LmJpbmRQb3B1cChwb3B1cF8yYzg1ODM2Njc2NDU0ZjMxODViZTdhYWU2OTk0OTQ4Mik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9iNzBiZDlhYTI4N2E0ZTA1OWM5NDI4MGRiNjg0YTRiMyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjY4NzkxOTcyMjQ4NTU3NCwtNzMuOTk4NTYxMzkyMTg0NjNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNDE1MGMxNzBiZWEyNDQ3OGJlOWFkNDc5MDRlNzhmZjcgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZjcyZmNkMDgyY2FkNDIxM2EyYzA1ZGMxZmYyODI3YmUgPSAkKCc8ZGl2IGlkPSJodG1sX2Y3MmZjZDA4MmNhZDQyMTNhMmMwNWRjMWZmMjgyN2JlIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Db2JibGUgSGlsbCwgQnJvb2tseW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzQxNTBjMTcwYmVhMjQ0NzhiZTlhZDQ3OTA0ZTc4ZmY3LnNldENvbnRlbnQoaHRtbF9mNzJmY2QwODJjYWQ0MjEzYTJjMDVkYzFmZjI4MjdiZSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9iNzBiZDlhYTI4N2E0ZTA1OWM5NDI4MGRiNjg0YTRiMy5iaW5kUG9wdXAocG9wdXBfNDE1MGMxNzBiZWEyNDQ3OGJlOWFkNDc5MDRlNzhmZjcpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNmY5NDE4NDA3ODgwNDM0NzllMWIwNjdmMmE5MzViNDMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42ODA1NDAyMzEwNzY0ODUsLTczLjk5NDY1MzcyODI4MDA2XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2U2NjI3NTA3ZDc3ODRiOTA5NGFiYjFkMjI1NDUzNTQzID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzE4MWVjM2ZlOWRlNzQxMTQ5MWExYTFmYjMyN2Y2YmRlID0gJCgnPGRpdiBpZD0iaHRtbF8xODFlYzNmZTlkZTc0MTE0OTFhMWExZmIzMjdmNmJkZSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q2Fycm9sbCBHYXJkZW5zLCBCcm9va2x5bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZTY2Mjc1MDdkNzc4NGI5MDk0YWJiMWQyMjU0NTM1NDMuc2V0Q29udGVudChodG1sXzE4MWVjM2ZlOWRlNzQxMTQ5MWExYTFmYjMyN2Y2YmRlKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzZmOTQxODQwNzg4MDQzNDc5ZTFiMDY3ZjJhOTM1YjQzLmJpbmRQb3B1cChwb3B1cF9lNjYyNzUwN2Q3Nzg0YjkwOTRhYmIxZDIyNTQ1MzU0Myk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl85ZjQxOWU2OWZmZTE0ZmU2ODljZDdmZWMzNGQ0OTIzYiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjY3NjI1MzIzMDI1MDg4NiwtNzQuMDEyNzU4OTc0NzM1Nl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF81YzkwY2Y2M2YwOWU0N2Y5OTY0YTU4YzVlMWQ5YzA0NSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF81M2Q3YWE5YzIwMWU0NTg4YWRmOWZkZWU3YzJkM2I2NSA9ICQoJzxkaXYgaWQ9Imh0bWxfNTNkN2FhOWMyMDFlNDU4OGFkZjlmZGVlN2MyZDNiNjUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlJlZCBIb29rLCBCcm9va2x5bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNWM5MGNmNjNmMDllNDdmOTk2NGE1OGM1ZTFkOWMwNDUuc2V0Q29udGVudChodG1sXzUzZDdhYTljMjAxZTQ1ODhhZGY5ZmRlZTdjMmQzYjY1KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzlmNDE5ZTY5ZmZlMTRmZTY4OWNkN2ZlYzM0ZDQ5MjNiLmJpbmRQb3B1cChwb3B1cF81YzkwY2Y2M2YwOWU0N2Y5OTY0YTU4YzVlMWQ5YzA0NSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl83OWNiMTZmMDRmNDI0OTY4YTk3MjRjN2I5ZDk2N2ViOCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjY3MzkzMTE0MzE4NzE1NCwtNzMuOTk0NDQwODcxNDUzMzldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNGVkMGUzYjRiYzI5NDJhYWI2Nzc3NDY1YjQ3MDdjMTAgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMzNhZDIwNWU1M2FjNGM0YTk3Y2RhYjQxODQyMDM2MjcgPSAkKCc8ZGl2IGlkPSJodG1sXzMzYWQyMDVlNTNhYzRjNGE5N2NkYWI0MTg0MjAzNjI3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Hb3dhbnVzLCBCcm9va2x5bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNGVkMGUzYjRiYzI5NDJhYWI2Nzc3NDY1YjQ3MDdjMTAuc2V0Q29udGVudChodG1sXzMzYWQyMDVlNTNhYzRjNGE5N2NkYWI0MTg0MjAzNjI3KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzc5Y2IxNmYwNGY0MjQ5NjhhOTcyNGM3YjlkOTY3ZWI4LmJpbmRQb3B1cChwb3B1cF80ZWQwZTNiNGJjMjk0MmFhYjY3Nzc0NjViNDcwN2MxMCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8zYTYyYjMzYjU2MDE0YjhlODYwZmUxZGI0NWU2Njk3MSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjY4ODUyNzI2MDE4OTc3LC03My45NzI5MDU3NDM2OTA5Ml0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF80ODY3YjRjNTRkOGY0ZDE0ODdkNTBiZTYxMWNjOGE0MCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF80ODE0MTBiMTAwZDY0N2E3OTI0ODU4MGM5NDI2ZmFhZCA9ICQoJzxkaXYgaWQ9Imh0bWxfNDgxNDEwYjEwMGQ2NDdhNzkyNDg1ODBjOTQyNmZhYWQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkZvcnQgR3JlZW5lLCBCcm9va2x5bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNDg2N2I0YzU0ZDhmNGQxNDg3ZDUwYmU2MTFjYzhhNDAuc2V0Q29udGVudChodG1sXzQ4MTQxMGIxMDBkNjQ3YTc5MjQ4NTgwYzk0MjZmYWFkKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzNhNjJiMzNiNTYwMTRiOGU4NjBmZTFkYjQ1ZTY2OTcxLmJpbmRQb3B1cChwb3B1cF80ODY3YjRjNTRkOGY0ZDE0ODdkNTBiZTYxMWNjOGE0MCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8wYjM4ZWVhYTE0N2E0NDVhYmIzZDQ0ZGExNDFhNDE5ZiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjY3MjMyMDUyMjY4MTk3LC03My45NzcwNTAzMDE4MzkyNF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9mMjY1YzA2YjI4NDc0Y2ZkOWQwNGVkYjNhYTQ1ZmUwMSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF85OTQ4ZDI2NGM1MjY0OTg3OWNkYjBiNzFjZmFjNjEyNCA9ICQoJzxkaXYgaWQ9Imh0bWxfOTk0OGQyNjRjNTI2NDk4NzljZGIwYjcxY2ZhYzYxMjQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlBhcmsgU2xvcGUsIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9mMjY1YzA2YjI4NDc0Y2ZkOWQwNGVkYjNhYTQ1ZmUwMS5zZXRDb250ZW50KGh0bWxfOTk0OGQyNjRjNTI2NDk4NzljZGIwYjcxY2ZhYzYxMjQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMGIzOGVlYWExNDdhNDQ1YWJiM2Q0NGRhMTQxYTQxOWYuYmluZFBvcHVwKHBvcHVwX2YyNjVjMDZiMjg0NzRjZmQ5ZDA0ZWRiM2FhNDVmZTAxKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzIwODY1ZDM4ZTZjNDQ4YzhhMWFlNDdiMmI5NTdhZGYxID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjgyMzkxMDExNDQyMTEsLTczLjg3NjYxNTk2NDU3Mjk2XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzNlZmQxMzg2MWZlNTQxYjhhY2NlZjk4MGE0YjYzN2YxID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2ZhMDgzMmY5YTQyYzQxZDNiMTlhMWJlZmMxODVjNzI2ID0gJCgnPGRpdiBpZD0iaHRtbF9mYTA4MzJmOWE0MmM0MWQzYjE5YTFiZWZjMTg1YzcyNiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q3lwcmVzcyBIaWxscywgQnJvb2tseW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzNlZmQxMzg2MWZlNTQxYjhhY2NlZjk4MGE0YjYzN2YxLnNldENvbnRlbnQoaHRtbF9mYTA4MzJmOWE0MmM0MWQzYjE5YTFiZWZjMTg1YzcyNik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8yMDg2NWQzOGU2YzQ0OGM4YTFhZTQ3YjJiOTU3YWRmMS5iaW5kUG9wdXAocG9wdXBfM2VmZDEzODYxZmU1NDFiOGFjY2VmOTgwYTRiNjM3ZjEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOWVlZDZkZjc1NTkzNDE2MDlhYjQ2NzQzMmE5ZjlmMDIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42Njk5MjU3MDA4NDcwNDUsLTczLjg4MDY5ODYzOTE3MzY2XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzUwZjAzMjc5NjA4NzQ1YmY5Yzk5MzE1ZjNhMWQ5NmRlID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzU0MTUyODllZWI2NjQyZGM4MmU0YmIxN2ZmNGIyZTM2ID0gJCgnPGRpdiBpZD0iaHRtbF81NDE1Mjg5ZWViNjY0MmRjODJlNGJiMTdmZjRiMmUzNiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RWFzdCBOZXcgWW9yaywgQnJvb2tseW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzUwZjAzMjc5NjA4NzQ1YmY5Yzk5MzE1ZjNhMWQ5NmRlLnNldENvbnRlbnQoaHRtbF81NDE1Mjg5ZWViNjY0MmRjODJlNGJiMTdmZjRiMmUzNik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl85ZWVkNmRmNzU1OTM0MTYwOWFiNDY3NDMyYTlmOWYwMi5iaW5kUG9wdXAocG9wdXBfNTBmMDMyNzk2MDg3NDViZjljOTkzMTVmM2ExZDk2ZGUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMWM0MGZjOTE5YzMyNDgxYmI2ZGIyNmVkZjJkMGY0MTQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42NDc1ODkwNTIzMDg3NCwtNzMuODc5MzY5NzAwNDU4NzVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMDJkZjcyOTQ0OWVmNDg3Y2JkNDE1NzlhMmFmMDgzNGQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMDRkM2RhNDkxMmI5NGUzN2FjNzBmNmJiOWYxYjU1M2UgPSAkKCc8ZGl2IGlkPSJodG1sXzA0ZDNkYTQ5MTJiOTRlMzdhYzcwZjZiYjlmMWI1NTNlIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5TdGFycmV0dCBDaXR5LCBCcm9va2x5bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMDJkZjcyOTQ0OWVmNDg3Y2JkNDE1NzlhMmFmMDgzNGQuc2V0Q29udGVudChodG1sXzA0ZDNkYTQ5MTJiOTRlMzdhYzcwZjZiYjlmMWI1NTNlKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzFjNDBmYzkxOWMzMjQ4MWJiNmRiMjZlZGYyZDBmNDE0LmJpbmRQb3B1cChwb3B1cF8wMmRmNzI5NDQ5ZWY0ODdjYmQ0MTU3OWEyYWYwODM0ZCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9jNGVjYmY1NjdlYWI0NWRlOGY2NTM4MGMzMTFiYjJlNyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYzNTU2NDMyNzk3NDI4LC03My45MDIwOTI2OTc3ODk2Nl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9iYzg5NGUyNGMxODY0YjY2OWEzNmQ2YzFhZDdjNzBjNCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9lMmEzNzc0M2RmNTY0YTc0YTk5ZDEyNjNlNjkwNzY0ZCA9ICQoJzxkaXYgaWQ9Imh0bWxfZTJhMzc3NDNkZjU2NGE3NGE5OWQxMjYzZTY5MDc2NGQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNhbmFyc2llLCBCcm9va2x5bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYmM4OTRlMjRjMTg2NGI2NjlhMzZkNmMxYWQ3YzcwYzQuc2V0Q29udGVudChodG1sX2UyYTM3NzQzZGY1NjRhNzRhOTlkMTI2M2U2OTA3NjRkKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2M0ZWNiZjU2N2VhYjQ1ZGU4ZjY1MzgwYzMxMWJiMmU3LmJpbmRQb3B1cChwb3B1cF9iYzg5NGUyNGMxODY0YjY2OWEzNmQ2YzFhZDdjNzBjNCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl82ZDQ5YTQ2YmJmYjU0Yjc0OWE3OWU1ZDZlYjZlYTZhMSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYzMDQ0NjA0Mzc1NzQ2NiwtNzMuOTI5MTEzMDI2NDQ2NzRdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZTJmODFjM2JjOThiNDI1MzkwNTJlMGU1OTUyNTc5MTIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNjg3YWY4MjVlMmZkNDljMjkwNjA2NGJiODViNTNhYjAgPSAkKCc8ZGl2IGlkPSJodG1sXzY4N2FmODI1ZTJmZDQ5YzI5MDYwNjRiYjg1YjUzYWIwIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5GbGF0bGFuZHMsIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9lMmY4MWMzYmM5OGI0MjUzOTA1MmUwZTU5NTI1NzkxMi5zZXRDb250ZW50KGh0bWxfNjg3YWY4MjVlMmZkNDljMjkwNjA2NGJiODViNTNhYjApOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNmQ0OWE0NmJiZmI1NGI3NDlhNzllNWQ2ZWI2ZWE2YTEuYmluZFBvcHVwKHBvcHVwX2UyZjgxYzNiYzk4YjQyNTM5MDUyZTBlNTk1MjU3OTEyKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzUyN2Q5NGY1YjEwNDRkNGNiZjFlYzAwNjA1YjBkNDQ0ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjA2MzM2NDIxNjg1NjI2LC03My45MDgxODU3MTc3NzQyM10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF80MGI2YTgyNWQ0ZjE0YWUyOGNjMGMxMDNiYWZkN2Y2OCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9hYmViNjE2MGQwMTM0OTU3Yjg4NTExZTc4MTI5MjZiNyA9ICQoJzxkaXYgaWQ9Imh0bWxfYWJlYjYxNjBkMDEzNDk1N2I4ODUxMWU3ODEyOTI2YjciIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk1pbGwgSXNsYW5kLCBCcm9va2x5bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNDBiNmE4MjVkNGYxNGFlMjhjYzBjMTAzYmFmZDdmNjguc2V0Q29udGVudChodG1sX2FiZWI2MTYwZDAxMzQ5NTdiODg1MTFlNzgxMjkyNmI3KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzUyN2Q5NGY1YjEwNDRkNGNiZjFlYzAwNjA1YjBkNDQ0LmJpbmRQb3B1cChwb3B1cF80MGI2YTgyNWQ0ZjE0YWUyOGNjMGMxMDNiYWZkN2Y2OCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9lNjBmYzQ3MDBmNWY0NTVhOTNiNGRhZWU1ZGEyMjhjZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjU3NzkxMzUwMzA4NjU3LC03My45NDM1MzcyMjg5MTg4Nl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF80YjMwMjZjY2JiMDI0NzJlODBhM2M0YmUzMGUzNmEwZCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF84NWYzNDNiODk0MTI0ODhhOTExNTNjNTk4YjM5Y2MyZSA9ICQoJzxkaXYgaWQ9Imh0bWxfODVmMzQzYjg5NDEyNDg4YTkxMTUzYzU5OGIzOWNjMmUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk1hbmhhdHRhbiBCZWFjaCwgQnJvb2tseW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzRiMzAyNmNjYmIwMjQ3MmU4MGEzYzRiZTMwZTM2YTBkLnNldENvbnRlbnQoaHRtbF84NWYzNDNiODk0MTI0ODhhOTExNTNjNTk4YjM5Y2MyZSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9lNjBmYzQ3MDBmNWY0NTVhOTNiNGRhZWU1ZGEyMjhjZS5iaW5kUG9wdXAocG9wdXBfNGIzMDI2Y2NiYjAyNDcyZTgwYTNjNGJlMzBlMzZhMGQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOTgxOTE3ZDc5ZmJiNGZkZjk1OTFmMDM3NDI4NjRjYzEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41NzQyOTI1NjQ3MTYwMSwtNzMuOTg4NjgyOTU4MjE2MzddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfOTY2YmFkMzhiZmNlNDFkNGE3NTUzZmJmMjIzMGY2NjMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNTAwY2I4YzgyYjMzNGRkM2I1M2YyZTcyY2QxYTk4NTIgPSAkKCc8ZGl2IGlkPSJodG1sXzUwMGNiOGM4MmIzMzRkZDNiNTNmMmU3MmNkMWE5ODUyIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Db25leSBJc2xhbmQsIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF85NjZiYWQzOGJmY2U0MWQ0YTc1NTNmYmYyMjMwZjY2My5zZXRDb250ZW50KGh0bWxfNTAwY2I4YzgyYjMzNGRkM2I1M2YyZTcyY2QxYTk4NTIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOTgxOTE3ZDc5ZmJiNGZkZjk1OTFmMDM3NDI4NjRjYzEuYmluZFBvcHVwKHBvcHVwXzk2NmJhZDM4YmZjZTQxZDRhNzU1M2ZiZjIyMzBmNjYzKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzcwNWJiOGZlNDE1ZjRkZTFhNDVhODQxZmFmMjExYTk0ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTk5NTE4NzAyODIyMzgsLTczLjk5ODc1MjIxNDQzNTE5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzU2NWYxZmQyZGY3MjQ2YjZhODY0NjI2ODFmZWZiZDlkID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzEyMzNkNjY0ODNmNzRmYTRiZTRjZWRjYTU0ZDhlMjhmID0gJCgnPGRpdiBpZD0iaHRtbF8xMjMzZDY2NDgzZjc0ZmE0YmU0Y2VkY2E1NGQ4ZTI4ZiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QmF0aCBCZWFjaCwgQnJvb2tseW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzU2NWYxZmQyZGY3MjQ2YjZhODY0NjI2ODFmZWZiZDlkLnNldENvbnRlbnQoaHRtbF8xMjMzZDY2NDgzZjc0ZmE0YmU0Y2VkY2E1NGQ4ZTI4Zik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl83MDViYjhmZTQxNWY0ZGUxYTQ1YTg0MWZhZjIxMWE5NC5iaW5kUG9wdXAocG9wdXBfNTY1ZjFmZDJkZjcyNDZiNmE4NjQ2MjY4MWZlZmJkOWQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZTVjODkzOWU0MDAwNDFlZGJiMWYyOTJhMGNjZTczY2UgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42MzMxMzA1MTI3NTgwMTUsLTczLjk5MDQ5ODIzMDQ0ODExXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzYwZGQxOGZlZjFhZjQ3YTZiZmUxZjQ1ZTM1NjFiYzYxID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzM3NTdjNzNjNzg2OTRhMDU4OWM5ODkxMjhiOGExNjczID0gJCgnPGRpdiBpZD0iaHRtbF8zNzU3YzczYzc4Njk0YTA1ODljOTg5MTI4YjhhMTY3MyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Qm9yb3VnaCBQYXJrLCBCcm9va2x5bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNjBkZDE4ZmVmMWFmNDdhNmJmZTFmNDVlMzU2MWJjNjEuc2V0Q29udGVudChodG1sXzM3NTdjNzNjNzg2OTRhMDU4OWM5ODkxMjhiOGExNjczKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2U1Yzg5MzllNDAwMDQxZWRiYjFmMjkyYTBjY2U3M2NlLmJpbmRQb3B1cChwb3B1cF82MGRkMThmZWYxYWY0N2E2YmZlMWY0NWUzNTYxYmM2MSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9hODljOGZjMTEyOGM0ZmIyODEzMDQzOTM4NmViMDRjYSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYxOTIxOTQ1NzcyMjYzNiwtNzQuMDE5MzEzNzU2MzYwMjJdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMTc1M2EzOWI0YTZkNGU3Zjk5NjYwYzQzNDU5NGE1MWUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOTFiNmNjN2IwNzNjNGE0M2I4ZjAzODQ3NWE2NWNiYWEgPSAkKCc8ZGl2IGlkPSJodG1sXzkxYjZjYzdiMDczYzRhNDNiOGYwMzg0NzVhNjVjYmFhIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5EeWtlciBIZWlnaHRzLCBCcm9va2x5bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMTc1M2EzOWI0YTZkNGU3Zjk5NjYwYzQzNDU5NGE1MWUuc2V0Q29udGVudChodG1sXzkxYjZjYzdiMDczYzRhNDNiOGYwMzg0NzVhNjVjYmFhKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2E4OWM4ZmMxMTI4YzRmYjI4MTMwNDM5Mzg2ZWIwNGNhLmJpbmRQb3B1cChwb3B1cF8xNzUzYTM5YjRhNmQ0ZTdmOTk2NjBjNDM0NTk0YTUxZSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9hODIyNTg0MDQwYTQ0Mjc0OTBmZDExZGUxNjY0OTNkNCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjU5MDg0ODQzMzkwMjA0NiwtNzMuOTMwMTAxNzA2OTExOTZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYTIzYTMwZTUxNzRlNDU2YTgwNTMzYTdiMzAzN2ZkMzAgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYWYyYjk0ZWU5MmZjNDFkNTg0M2ZiZmY1ZTU2MGVhNzYgPSAkKCc8ZGl2IGlkPSJodG1sX2FmMmI5NGVlOTJmYzQxZDU4NDNmYmZmNWU1NjBlYTc2IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5HZXJyaXRzZW4gQmVhY2gsIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9hMjNhMzBlNTE3NGU0NTZhODA1MzNhN2IzMDM3ZmQzMC5zZXRDb250ZW50KGh0bWxfYWYyYjk0ZWU5MmZjNDFkNTg0M2ZiZmY1ZTU2MGVhNzYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYTgyMjU4NDA0MGE0NDI3NDkwZmQxMWRlMTY2NDkzZDQuYmluZFBvcHVwKHBvcHVwX2EyM2EzMGU1MTc0ZTQ1NmE4MDUzM2E3YjMwMzdmZDMwKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2E3Yjg4NGY2OTY3YjRiNTc4YzhmMDU5MGJjMTNiNzQ1ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjA5NzQ3Nzc5ODk0NjA0LC03My45MzEzNDQwNDEwODQ5N10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8zZjViNTg3YjM5MzQ0MjlmYTEyZDNmOTZiOTA2NmIzMSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF82OTMwN2U5YWRmODI0YjlkODE1MTJkMmVhM2I0Nzg5ZiA9ICQoJzxkaXYgaWQ9Imh0bWxfNjkzMDdlOWFkZjgyNGI5ZDgxNTEyZDJlYTNiNDc4OWYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk1hcmluZSBQYXJrLCBCcm9va2x5bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfM2Y1YjU4N2IzOTM0NDI5ZmExMmQzZjk2YjkwNjZiMzEuc2V0Q29udGVudChodG1sXzY5MzA3ZTlhZGY4MjRiOWQ4MTUxMmQyZWEzYjQ3ODlmKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2E3Yjg4NGY2OTY3YjRiNTc4YzhmMDU5MGJjMTNiNzQ1LmJpbmRQb3B1cChwb3B1cF8zZjViNTg3YjM5MzQ0MjlmYTEyZDNmOTZiOTA2NmIzMSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9mYTNlOWQxNzY1Yzc0NzhiOTA4YTM5NDEyZDM0MzZhMiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjY5MzIyOTQyMTg4MTUwNCwtNzMuOTY3ODQzMDYyMTYzNjddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMzUwMTI3NTU0YmQ5NGU0OTg4OGY5YTg3ZTQ4YzMyYmUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZTYzMDhhNWZlMDY4NDAzYjg3NWMyZDUyOGU1ZWIxM2EgPSAkKCc8ZGl2IGlkPSJodG1sX2U2MzA4YTVmZTA2ODQwM2I4NzVjMmQ1MjhlNWViMTNhIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DbGludG9uIEhpbGwsIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8zNTAxMjc1NTRiZDk0ZTQ5ODg4ZjlhODdlNDhjMzJiZS5zZXRDb250ZW50KGh0bWxfZTYzMDhhNWZlMDY4NDAzYjg3NWMyZDUyOGU1ZWIxM2EpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZmEzZTlkMTc2NWM3NDc4YjkwOGEzOTQxMmQzNDM2YTIuYmluZFBvcHVwKHBvcHVwXzM1MDEyNzU1NGJkOTRlNDk4ODhmOWE4N2U0OGMzMmJlKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzQxMTVhYjNjNTRhNjRlNTQ5MWY2M2Q5NDBiZDljNmU5ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTc2Mzc1Mzc4OTAyMjQsLTc0LjAwNzg3MzExMjAwMjRdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMjJjODYwMjJkZDM4NDNmMjkzNTcxN2E1MjFmMDc1MzIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNmFhYWJjNGI2MjE0NDBiYWI4NTg3YjkyZGJlNGVlYzcgPSAkKCc8ZGl2IGlkPSJodG1sXzZhYWFiYzRiNjIxNDQwYmFiODU4N2I5MmRiZTRlZWM3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5TZWEgR2F0ZSwgQnJvb2tseW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzIyYzg2MDIyZGQzODQzZjI5MzU3MTdhNTIxZjA3NTMyLnNldENvbnRlbnQoaHRtbF82YWFhYmM0YjYyMTQ0MGJhYjg1ODdiOTJkYmU0ZWVjNyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl80MTE1YWIzYzU0YTY0ZTU0OTFmNjNkOTQwYmQ5YzZlOS5iaW5kUG9wdXAocG9wdXBfMjJjODYwMjJkZDM4NDNmMjkzNTcxN2E1MjFmMDc1MzIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNmY1NmZmZGI2YTk3NGRkYmFhMmUwMTYxNTE2MDhjZTEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42OTA4NDQwMjEwOTgwMiwtNzMuOTgzNDYzMzc0MzEwOTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNTcwNGM5YjhhOGY2NDc0YmJiOTcwMjBjZjlkMTNiOWMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYWQxMzlkNWYzZTdjNGIzOWFlOWM4NGVlNzg0MGMwOTMgPSAkKCc8ZGl2IGlkPSJodG1sX2FkMTM5ZDVmM2U3YzRiMzlhZTljODRlZTc4NDBjMDkzIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Eb3dudG93biwgQnJvb2tseW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzU3MDRjOWI4YThmNjQ3NGJiYjk3MDIwY2Y5ZDEzYjljLnNldENvbnRlbnQoaHRtbF9hZDEzOWQ1ZjNlN2M0YjM5YWU5Yzg0ZWU3ODQwYzA5Myk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl82ZjU2ZmZkYjZhOTc0ZGRiYWEyZTAxNjE1MTYwOGNlMS5iaW5kUG9wdXAocG9wdXBfNTcwNGM5YjhhOGY2NDc0YmJiOTcwMjBjZjlkMTNiOWMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNTIyMTIzMDExZDM5NDJjOGJkMDU1M2RiN2UxNWFhYjUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42ODU2ODI5MTIwOTE0NDQsLTczLjk4Mzc0ODI0MTE1Nzk4XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2QzMjFmNzk4YTUzOTRiMTQ5MGViYzY4ZDA1OTI5OTE1ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2NmNjhhZWI4ODdkNDQxMTI5OTYyN2M5NTU2NzEyMWJlID0gJCgnPGRpdiBpZD0iaHRtbF9jZjY4YWViODg3ZDQ0MTEyOTk2MjdjOTU1NjcxMjFiZSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Qm9lcnVtIEhpbGwsIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9kMzIxZjc5OGE1Mzk0YjE0OTBlYmM2OGQwNTkyOTkxNS5zZXRDb250ZW50KGh0bWxfY2Y2OGFlYjg4N2Q0NDExMjk5NjI3Yzk1NTY3MTIxYmUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNTIyMTIzMDExZDM5NDJjOGJkMDU1M2RiN2UxNWFhYjUuYmluZFBvcHVwKHBvcHVwX2QzMjFmNzk4YTUzOTRiMTQ5MGViYzY4ZDA1OTI5OTE1KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2ZmYTNkNTU0MjM4NTQzNGZiZDZmYjI0ZjAxZjRlNjRiID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjU4NDIwMDE3NDY5ODE1LC03My45NTQ4OTg2NzA3NzcxM10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF83ZmQ0NDgyMzk2YjE0Y2M4ODdlYTBlMzk2YmMyMDllNiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8wMWVjZDdjYjNmODk0MmQwOWJmYjYzMmZkZDRlOGIxNCA9ICQoJzxkaXYgaWQ9Imh0bWxfMDFlY2Q3Y2IzZjg5NDJkMDliZmI2MzJmZGQ0ZThiMTQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlByb3NwZWN0IExlZmZlcnRzIEdhcmRlbnMsIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF83ZmQ0NDgyMzk2YjE0Y2M4ODdlYTBlMzk2YmMyMDllNi5zZXRDb250ZW50KGh0bWxfMDFlY2Q3Y2IzZjg5NDJkMDliZmI2MzJmZGQ0ZThiMTQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZmZhM2Q1NTQyMzg1NDM0ZmJkNmZiMjRmMDFmNGU2NGIuYmluZFBvcHVwKHBvcHVwXzdmZDQ0ODIzOTZiMTRjYzg4N2VhMGUzOTZiYzIwOWU2KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzkyODg0Y2I2N2UyYTQ1NTQ5NDI3ZmZiMGQyZjEyY2RjID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjc4NDAyNTU0Nzk1MzU1LC03My45MTMwNjgzMTc4NzM5NV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9mNWNmOWJkMGE3YmE0OGM4ODY3NWM3YjVkNTBhYTllNSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9iMDgzNWEzMjMzYTQ0YzdhYjZmZThkMzFkYTc0MWU5MiA9ICQoJzxkaXYgaWQ9Imh0bWxfYjA4MzVhMzIzM2E0NGM3YWI2ZmU4ZDMxZGE3NDFlOTIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk9jZWFuIEhpbGwsIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9mNWNmOWJkMGE3YmE0OGM4ODY3NWM3YjVkNTBhYTllNS5zZXRDb250ZW50KGh0bWxfYjA4MzVhMzIzM2E0NGM3YWI2ZmU4ZDMxZGE3NDFlOTIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOTI4ODRjYjY3ZTJhNDU1NDk0MjdmZmIwZDJmMTJjZGMuYmluZFBvcHVwKHBvcHVwX2Y1Y2Y5YmQwYTdiYTQ4Yzg4Njc1YzdiNWQ1MGFhOWU1KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzIxYWE4YmY3ZGRmMTQzZTU5ZjEwNzY2MzdkODgyYjRiID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjc4NTY5OTU3Mjc0NzksLTczLjg2Nzk3NTk4MDgxMzM0XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzVjYjRjYzc1MThlZjRlZDU4NjM4YjFmZTUxOTZkYTFhID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2Y5OWUzYWUyNTI2MDQ1Yjk4Yzk3MTcyZjAyNDhkZmNmID0gJCgnPGRpdiBpZD0iaHRtbF9mOTllM2FlMjUyNjA0NWI5OGM5NzE3MmYwMjQ4ZGZjZiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q2l0eSBMaW5lLCBCcm9va2x5bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNWNiNGNjNzUxOGVmNGVkNTg2MzhiMWZlNTE5NmRhMWEuc2V0Q29udGVudChodG1sX2Y5OWUzYWUyNTI2MDQ1Yjk4Yzk3MTcyZjAyNDhkZmNmKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzIxYWE4YmY3ZGRmMTQzZTU5ZjEwNzY2MzdkODgyYjRiLmJpbmRQb3B1cChwb3B1cF81Y2I0Y2M3NTE4ZWY0ZWQ1ODYzOGIxZmU1MTk2ZGExYSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8wZWU5ZGQ4MTFhNjM0MGM3YWE2OGQ3ZTBiYjg0ZWMyOSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYxNTE0OTU1MDQ1MzA4LC03My44OTg1NTYzMzYzMDMxN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF85YmI2ZTRkMDY1MmU0OTVlODc5NmRmOGE5OTcwMmQwYyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9hMjQxN2I4ZmZjZTI0ZmVjODkwN2Q3ZTcyN2M4YTA5MyA9ICQoJzxkaXYgaWQ9Imh0bWxfYTI0MTdiOGZmY2UyNGZlYzg5MDdkN2U3MjdjOGEwOTMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkJlcmdlbiBCZWFjaCwgQnJvb2tseW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzliYjZlNGQwNjUyZTQ5NWU4Nzk2ZGY4YTk5NzAyZDBjLnNldENvbnRlbnQoaHRtbF9hMjQxN2I4ZmZjZTI0ZmVjODkwN2Q3ZTcyN2M4YTA5Myk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8wZWU5ZGQ4MTFhNjM0MGM3YWE2OGQ3ZTBiYjg0ZWMyOS5iaW5kUG9wdXAocG9wdXBfOWJiNmU0ZDA2NTJlNDk1ZTg3OTZkZjhhOTk3MDJkMGMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZmZlZmUzOTJmZGY1NDM3NDgxYjhmMWMzZTQzNjlhNWYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42MjU1OTU4OTg2OTg0MywtNzMuOTU3NTk1MjM0ODk4MzhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYjFlNzg1ZjNkNGI0NDI2YmE2NTRjNDVkNDI5YWQ1NzkgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNjRiNTJjODQ1YjQ0NGZmNjk4ZjkwZWQ5YmQ0ZmU2MjggPSAkKCc8ZGl2IGlkPSJodG1sXzY0YjUyYzg0NWI0NDRmZjY5OGY5MGVkOWJkNGZlNjI4IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5NaWR3b29kLCBCcm9va2x5bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYjFlNzg1ZjNkNGI0NDI2YmE2NTRjNDVkNDI5YWQ1Nzkuc2V0Q29udGVudChodG1sXzY0YjUyYzg0NWI0NDRmZjY5OGY5MGVkOWJkNGZlNjI4KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2ZmZWZlMzkyZmRmNTQzNzQ4MWI4ZjFjM2U0MzY5YTVmLmJpbmRQb3B1cChwb3B1cF9iMWU3ODVmM2Q0YjQ0MjZiYTY1NGM0NWQ0MjlhZDU3OSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8zYTZiYmZhZTBlMjU0ZGJmODZmYjQ1YzU4YzQ2NTY1ZCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjY0NzAwODYwMzE4NTE4NSwtNzMuOTYyNjEzMTY3MTYwNDhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYWQ4OTZiMTk2YTY0NDlhY2ExMGRlNGVmOGZhMjRiZjMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZWU4NzkyZTFlMTNjNGU5ZTg2Y2RmOGYxZTk4YWJlZjMgPSAkKCc8ZGl2IGlkPSJodG1sX2VlODc5MmUxZTEzYzRlOWU4NmNkZjhmMWU5OGFiZWYzIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Qcm9zcGVjdCBQYXJrIFNvdXRoLCBCcm9va2x5bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYWQ4OTZiMTk2YTY0NDlhY2ExMGRlNGVmOGZhMjRiZjMuc2V0Q29udGVudChodG1sX2VlODc5MmUxZTEzYzRlOWU4NmNkZjhmMWU5OGFiZWYzKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzNhNmJiZmFlMGUyNTRkYmY4NmZiNDVjNThjNDY1NjVkLmJpbmRQb3B1cChwb3B1cF9hZDg5NmIxOTZhNjQ0OWFjYTEwZGU0ZWY4ZmEyNGJmMyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8yNzQ5Y2Q4ZDc0ODc0ODViYWYyNmQwZWRhZjVjMjgzNyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYyMzg0NTI0NDc4NDE5LC03My45MTYwNzQ4Mzk1MTMyNF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9jMjNjNjIyMDAyMzI0NmQ1OTdkOTgyZDViNDcxYTY1NCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF80NWUwMWFjOTczZDE0MzgzYjAxMTFiZDU5NDk5NWQ5OSA9ICQoJzxkaXYgaWQ9Imh0bWxfNDVlMDFhYzk3M2QxNDM4M2IwMTExYmQ1OTQ5OTVkOTkiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkdlb3JnZXRvd24sIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9jMjNjNjIyMDAyMzI0NmQ1OTdkOTgyZDViNDcxYTY1NC5zZXRDb250ZW50KGh0bWxfNDVlMDFhYzk3M2QxNDM4M2IwMTExYmQ1OTQ5OTVkOTkpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMjc0OWNkOGQ3NDg3NDg1YmFmMjZkMGVkYWY1YzI4MzcuYmluZFBvcHVwKHBvcHVwX2MyM2M2MjIwMDIzMjQ2ZDU5N2Q5ODJkNWI0NzFhNjU0KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2E5NjI4YWJkNDQwNTRjMTFhMTBiYjJlYTdiYjFmOTM4ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzA4NDkyNDEwNDE1NDgsLTczLjkzODg1ODE1MjY5MTk1XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzE2OGQ3NTdiNGRiOTQxZTk5NGNlYjU5NWMyZTM1ZmY5ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzEyN2UzYTE4ZGE5ODQ0ZjJhYzAxZjU5ZTg3MmNmN2YzID0gJCgnPGRpdiBpZD0iaHRtbF8xMjdlM2ExOGRhOTg0NGYyYWMwMWY1OWU4NzJjZjdmMyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RWFzdCBXaWxsaWFtc2J1cmcsIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8xNjhkNzU3YjRkYjk0MWU5OTRjZWI1OTVjMmUzNWZmOS5zZXRDb250ZW50KGh0bWxfMTI3ZTNhMThkYTk4NDRmMmFjMDFmNTllODcyY2Y3ZjMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYTk2MjhhYmQ0NDA1NGMxMWExMGJiMmVhN2JiMWY5MzguYmluZFBvcHVwKHBvcHVwXzE2OGQ3NTdiNGRiOTQxZTk5NGNlYjU5NWMyZTM1ZmY5KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2E1Y2QzODMzNDRiNTQ2NTU5YWIyNThmOTdmOGZkNDJmID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzE0ODIyOTA2NTMyMDE0LC03My45NTg4MDg1NzU4NzU4Ml0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9jM2NhYmI3NWRmNmY0MmM2YjkzZWUzNjM0NDQ4M2JlZSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF81ZmJmNTkwYjJmZmE0MjRiOGQ0ZGZmYWUxMGZiOTMxNiA9ICQoJzxkaXYgaWQ9Imh0bWxfNWZiZjU5MGIyZmZhNDI0YjhkNGRmZmFlMTBmYjkzMTYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk5vcnRoIFNpZGUsIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9jM2NhYmI3NWRmNmY0MmM2YjkzZWUzNjM0NDQ4M2JlZS5zZXRDb250ZW50KGh0bWxfNWZiZjU5MGIyZmZhNDI0YjhkNGRmZmFlMTBmYjkzMTYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYTVjZDM4MzM0NGI1NDY1NTlhYjI1OGY5N2Y4ZmQ0MmYuYmluZFBvcHVwKHBvcHVwX2MzY2FiYjc1ZGY2ZjQyYzZiOTNlZTM2MzQ0NDgzYmVlKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzNhYWRmNmY0NGEyOTQwZWQ4NDQ5MGZiMjJhMzZmYzhmID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzEwODYxNDcyNjUwNjQsLTczLjk1ODAwMDk1MTUzMzMxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzc3NmRlNWJmZGRiZjQwZjdiNDA1ZTNiZjA3YWVhNzdhID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzFhYzQwMWZmMTU4NzQwNTliNjIyNGUzNTA2YWY4YTgxID0gJCgnPGRpdiBpZD0iaHRtbF8xYWM0MDFmZjE1ODc0MDU5YjYyMjRlMzUwNmFmOGE4MSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+U291dGggU2lkZSwgQnJvb2tseW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzc3NmRlNWJmZGRiZjQwZjdiNDA1ZTNiZjA3YWVhNzdhLnNldENvbnRlbnQoaHRtbF8xYWM0MDFmZjE1ODc0MDU5YjYyMjRlMzUwNmFmOGE4MSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8zYWFkZjZmNDRhMjk0MGVkODQ0OTBmYjIyYTM2ZmM4Zi5iaW5kUG9wdXAocG9wdXBfNzc2ZGU1YmZkZGJmNDBmN2I0MDVlM2JmMDdhZWE3N2EpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMTJhNDFmYzVkYzZkNDQ2YzkwNTA5MzA3NTA1NWM5NWUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42MTMwNTk3NjY2Nzk0MiwtNzMuOTY4MzY2NzgwMzU1NDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZDM5YmI5ODUwNzc1NGE3YWE5ODVjMmNlNjc4NDdmMjcgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOTBiZWE5MTNlYjE0NDBlOGFiZmQ1MDMzMTcxNWQ2OTkgPSAkKCc8ZGl2IGlkPSJodG1sXzkwYmVhOTEzZWIxNDQwZThhYmZkNTAzMzE3MTVkNjk5IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5PY2VhbiBQYXJrd2F5LCBCcm9va2x5bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZDM5YmI5ODUwNzc1NGE3YWE5ODVjMmNlNjc4NDdmMjcuc2V0Q29udGVudChodG1sXzkwYmVhOTEzZWIxNDQwZThhYmZkNTAzMzE3MTVkNjk5KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzEyYTQxZmM1ZGM2ZDQ0NmM5MDUwOTMwNzUwNTVjOTVlLmJpbmRQb3B1cChwb3B1cF9kMzliYjk4NTA3NzU0YTdhYTk4NWMyY2U2Nzg0N2YyNyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9jZjYyYzFlN2UxNmU0ZDc3OWU5ZjIwM2I5NDJiNmZhMiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYxNDc2ODEyNjk0MjI2LC03NC4wMzE5NzkxNDUzNzk4NF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9lZjZkMDc3ODNkYTM0MDhkOTgxZGVlNjIyNDc0N2M1YSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8wN2Y2NWRhNjc4ZDc0ZWY2YjE5MmRjZjcyZTdiNTQxNiA9ICQoJzxkaXYgaWQ9Imh0bWxfMDdmNjVkYTY3OGQ3NGVmNmIxOTJkY2Y3MmU3YjU0MTYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkZvcnQgSGFtaWx0b24sIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9lZjZkMDc3ODNkYTM0MDhkOTgxZGVlNjIyNDc0N2M1YS5zZXRDb250ZW50KGh0bWxfMDdmNjVkYTY3OGQ3NGVmNmIxOTJkY2Y3MmU3YjU0MTYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfY2Y2MmMxZTdlMTZlNGQ3NzllOWYyMDNiOTQyYjZmYTIuYmluZFBvcHVwKHBvcHVwX2VmNmQwNzc4M2RhMzQwOGQ5ODFkZWU2MjI0NzQ3YzVhKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzYxYWEwZjJlMmQxZTRmYWJiNTM2NTU3NjBkZGJlZjBkID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzE1NjE4NDIyMzE0MzIsLTczLjk5NDI3OTM2MjU1OTc4XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2VkZWM2NjM3NzY0ZjQ4NGFhOTExMWNiOGEwNTgwMmFjID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzgxMmMyMzA3ZjJhOTQxZTJiMmZlYmY5MjBiYmUwNDJjID0gJCgnPGRpdiBpZD0iaHRtbF84MTJjMjMwN2YyYTk0MWUyYjJmZWJmOTIwYmJlMDQyYyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q2hpbmF0b3duLCBNYW5oYXR0YW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2VkZWM2NjM3NzY0ZjQ4NGFhOTExMWNiOGEwNTgwMmFjLnNldENvbnRlbnQoaHRtbF84MTJjMjMwN2YyYTk0MWUyYjJmZWJmOTIwYmJlMDQyYyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl82MWFhMGYyZTJkMWU0ZmFiYjUzNjU1NzYwZGRiZWYwZC5iaW5kUG9wdXAocG9wdXBfZWRlYzY2Mzc3NjRmNDg0YWE5MTExY2I4YTA1ODAyYWMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOWVjZjE4OTkxNzBmNDI4YWIxZmRiNzRhOGNmOGFkMjYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44NTE5MDI1MjU1NTMwNSwtNzMuOTM2OTAwMjc5ODUyMzRdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNDg4MzBiZjcwNTcyNGZkNWJjOGNhZDcwOTQ0MWU0ODEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYTVmNTcxOTJiNjcyNGNmZmI0ZTIxN2M0Mjk3NGFjOGEgPSAkKCc8ZGl2IGlkPSJodG1sX2E1ZjU3MTkyYjY3MjRjZmZiNGUyMTdjNDI5NzRhYzhhIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5XYXNoaW5ndG9uIEhlaWdodHMsIE1hbmhhdHRhbjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNDg4MzBiZjcwNTcyNGZkNWJjOGNhZDcwOTQ0MWU0ODEuc2V0Q29udGVudChodG1sX2E1ZjU3MTkyYjY3MjRjZmZiNGUyMTdjNDI5NzRhYzhhKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzllY2YxODk5MTcwZjQyOGFiMWZkYjc0YThjZjhhZDI2LmJpbmRQb3B1cChwb3B1cF80ODgzMGJmNzA1NzI0ZmQ1YmM4Y2FkNzA5NDQxZTQ4MSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9kYjRjM2JiNzNhOTU0NGFkOTYzMjkwYTdiNjUxMmZhNyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjg2NzY4Mzk2NDQ5OTE1LC03My45MjEyMTA0MjIwMzg5N10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF81ZTk1M2Y0N2ViYjU0YWVlOWViOTZjOWRmNzE4MDJiNSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9mMjQ1ODUwZGVkZTg0YzQxYmQwMjUzNzE2MTkyZmYyMCA9ICQoJzxkaXYgaWQ9Imh0bWxfZjI0NTg1MGRlZGU4NGM0MWJkMDI1MzcxNjE5MmZmMjAiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPklud29vZCwgTWFuaGF0dGFuPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF81ZTk1M2Y0N2ViYjU0YWVlOWViOTZjOWRmNzE4MDJiNS5zZXRDb250ZW50KGh0bWxfZjI0NTg1MGRlZGU4NGM0MWJkMDI1MzcxNjE5MmZmMjApOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZGI0YzNiYjczYTk1NDRhZDk2MzI5MGE3YjY1MTJmYTcuYmluZFBvcHVwKHBvcHVwXzVlOTUzZjQ3ZWJiNTRhZWU5ZWI5NmM5ZGY3MTgwMmI1KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzlmNmU1NjBhMmRiOTQ1M2RiNjE3NTkwNDViODQwNmIxID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODIzNjA0Mjg0ODExOTM1LC03My45NDk2ODc5MTg4MzM2Nl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8yODU3NGM4ODRjNTg0ZGMyYjcxMzFiYTc0NDJiMmMzOSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF80MDM1ODQ4MzJhMTQ0MTJkOGY4MTE0ZjMyNGQ4Yzk4YSA9ICQoJzxkaXYgaWQ9Imh0bWxfNDAzNTg0ODMyYTE0NDEyZDhmODExNGYzMjRkOGM5OGEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkhhbWlsdG9uIEhlaWdodHMsIE1hbmhhdHRhbjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMjg1NzRjODg0YzU4NGRjMmI3MTMxYmE3NDQyYjJjMzkuc2V0Q29udGVudChodG1sXzQwMzU4NDgzMmExNDQxMmQ4ZjgxMTRmMzI0ZDhjOThhKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzlmNmU1NjBhMmRiOTQ1M2RiNjE3NTkwNDViODQwNmIxLmJpbmRQb3B1cChwb3B1cF8yODU3NGM4ODRjNTg0ZGMyYjcxMzFiYTc0NDJiMmMzOSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9kY2JiMzY5YjM3MTg0ZTY1YmNiOTRkYzJiOTY3NTU2ZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjgxNjkzNDQyOTQ5NzgsLTczLjk1NzM4NTM5MzUxODhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNDBmZjc4MmI4MWY4NDZlNWFiZTg2NTg1NDczNTRkMmMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZjhhZTcxYTllOTNkNDA0NTk5Mjc3YzEzMzA0MjNlM2YgPSAkKCc8ZGl2IGlkPSJodG1sX2Y4YWU3MWE5ZTkzZDQwNDU5OTI3N2MxMzMwNDIzZTNmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5NYW5oYXR0YW52aWxsZSwgTWFuaGF0dGFuPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF80MGZmNzgyYjgxZjg0NmU1YWJlODY1ODU0NzM1NGQyYy5zZXRDb250ZW50KGh0bWxfZjhhZTcxYTllOTNkNDA0NTk5Mjc3YzEzMzA0MjNlM2YpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZGNiYjM2OWIzNzE4NGU2NWJjYjk0ZGMyYjk2NzU1NmUuYmluZFBvcHVwKHBvcHVwXzQwZmY3ODJiODFmODQ2ZTVhYmU4NjU4NTQ3MzU0ZDJjKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2ZlN2JjYzVlOWEzYTQ5MGQ5ODBmMDA5ZmJmMTI3Y2QzID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODE1OTc2MDY3NDI0MTQsLTczLjk0MzIxMTEyNjAzOTA1XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2QyNGY2MDdjN2E2NzQyNmQ4YWQ4N2M5ZGFiYTlkMzllID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzJmZmM1MDU5OTJkMTQyYjU5ZjFjMmMwNDEwZTQ1NjcxID0gJCgnPGRpdiBpZD0iaHRtbF8yZmZjNTA1OTkyZDE0MmI1OWYxYzJjMDQxMGU0NTY3MSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q2VudHJhbCBIYXJsZW0sIE1hbmhhdHRhbjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZDI0ZjYwN2M3YTY3NDI2ZDhhZDg3YzlkYWJhOWQzOWUuc2V0Q29udGVudChodG1sXzJmZmM1MDU5OTJkMTQyYjU5ZjFjMmMwNDEwZTQ1NjcxKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2ZlN2JjYzVlOWEzYTQ5MGQ5ODBmMDA5ZmJmMTI3Y2QzLmJpbmRQb3B1cChwb3B1cF9kMjRmNjA3YzdhNjc0MjZkOGFkODdjOWRhYmE5ZDM5ZSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9kNzA2OGI5YmE3MWU0N2NmYTQ1YzA5YWYwZTAyNDQ0MSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjc5MjI0OTQ2NjYzMDMzLC03My45NDQxODIyMzE0ODUyNF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9lOGFkOTcyMGNjNzI0NTFhOWIyYzQwYTc2ZDNkOTdmMiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF85MjdiMmVmZWVkMzQ0MTA2ODYyYzQ1N2RiM2NiYjUwNSA9ICQoJzxkaXYgaWQ9Imh0bWxfOTI3YjJlZmVlZDM0NDEwNjg2MmM0NTdkYjNjYmI1MDUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkVhc3QgSGFybGVtLCBNYW5oYXR0YW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2U4YWQ5NzIwY2M3MjQ1MWE5YjJjNDBhNzZkM2Q5N2YyLnNldENvbnRlbnQoaHRtbF85MjdiMmVmZWVkMzQ0MTA2ODYyYzQ1N2RiM2NiYjUwNSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9kNzA2OGI5YmE3MWU0N2NmYTQ1YzA5YWYwZTAyNDQ0MS5iaW5kUG9wdXAocG9wdXBfZThhZDk3MjBjYzcyNDUxYTliMmM0MGE3NmQzZDk3ZjIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMzA2MTEyZWEzMDg4NGU1N2I1OTY2MjMzOWQ4NWIzMGUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43NzU2Mzg1NzMzMDE4MDUsLTczLjk2MDUwNzYzMTM1XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2Y1MzBkOTE5ZWJmNjRmMmU5MDBjNWMxOGIyYzA1MDYwID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzRjMTgxOGQxMDU2OTQwMzZhZWMwNGM1MmU4MWU0YzEzID0gJCgnPGRpdiBpZD0iaHRtbF80YzE4MThkMTA1Njk0MDM2YWVjMDRjNTJlODFlNGMxMyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VXBwZXIgRWFzdCBTaWRlLCBNYW5oYXR0YW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2Y1MzBkOTE5ZWJmNjRmMmU5MDBjNWMxOGIyYzA1MDYwLnNldENvbnRlbnQoaHRtbF80YzE4MThkMTA1Njk0MDM2YWVjMDRjNTJlODFlNGMxMyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8zMDYxMTJlYTMwODg0ZTU3YjU5NjYyMzM5ZDg1YjMwZS5iaW5kUG9wdXAocG9wdXBfZjUzMGQ5MTllYmY2NGYyZTkwMGM1YzE4YjJjMDUwNjApOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYjQ4Y2Q4MDVlMmU4NGUyYTlhYTZjNGNiZGE1MDU2ZTQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43NzU5Mjk4NDk4ODQ4NzUsLTczLjk0NzExNzg0NDcxODI2XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2M1ZTZlMGQzNzAyZTQxYmM4NDE3MGVkYmQzOGI3YjY5ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2JlMThlMWNjMjJiMDQ1ZDFhMTg5YjBjZGNiYzhlNjFjID0gJCgnPGRpdiBpZD0iaHRtbF9iZTE4ZTFjYzIyYjA0NWQxYTE4OWIwY2RjYmM4ZTYxYyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+WW9ya3ZpbGxlLCBNYW5oYXR0YW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2M1ZTZlMGQzNzAyZTQxYmM4NDE3MGVkYmQzOGI3YjY5LnNldENvbnRlbnQoaHRtbF9iZTE4ZTFjYzIyYjA0NWQxYTE4OWIwY2RjYmM4ZTYxYyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9iNDhjZDgwNWUyZTg0ZTJhOWFhNmM0Y2JkYTUwNTZlNC5iaW5kUG9wdXAocG9wdXBfYzVlNmUwZDM3MDJlNDFiYzg0MTcwZWRiZDM4YjdiNjkpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZGVhMWM0Y2E2ODQxNGM2ZmIxYjA4MTA2Y2ZhNmZiODAgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43NjgxMTI2NTgyODczMywtNzMuOTU4ODU5Njg4MTM3Nl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9mNjRjNjFmOTdjMzQ0NGU2YjA3YzdjZDBjMTY3OTFmNCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9hYTk4OTM3OWU3NDM0MzNlODU0MGM2MjgyNzczNjY0OSA9ICQoJzxkaXYgaWQ9Imh0bWxfYWE5ODkzNzllNzQzNDMzZTg1NDBjNjI4Mjc3MzY2NDkiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkxlbm94IEhpbGwsIE1hbmhhdHRhbjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZjY0YzYxZjk3YzM0NDRlNmIwN2M3Y2QwYzE2NzkxZjQuc2V0Q29udGVudChodG1sX2FhOTg5Mzc5ZTc0MzQzM2U4NTQwYzYyODI3NzM2NjQ5KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2RlYTFjNGNhNjg0MTRjNmZiMWIwODEwNmNmYTZmYjgwLmJpbmRQb3B1cChwb3B1cF9mNjRjNjFmOTdjMzQ0NGU2YjA3YzdjZDBjMTY3OTFmNCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8zNzM0NjI4ZDdjNGU0YzU0YWM5MGExYTA4YWI5YTM4OSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjc2MjE1OTYwNTc2MjgzLC03My45NDkxNjc2OTIyNzk1M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9jMTkyMjFiZmZkZjI0MzRiOWEyMjBlYTFlMWY2OTlhNCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9jZjBkMjQyOWI2NzA0YzkyYjc2MjFkNDI0YjdkMmI3ZiA9ICQoJzxkaXYgaWQ9Imh0bWxfY2YwZDI0MjliNjcwNGM5MmI3NjIxZDQyNGI3ZDJiN2YiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlJvb3NldmVsdCBJc2xhbmQsIE1hbmhhdHRhbjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYzE5MjIxYmZmZGYyNDM0YjlhMjIwZWExZTFmNjk5YTQuc2V0Q29udGVudChodG1sX2NmMGQyNDI5YjY3MDRjOTJiNzYyMWQ0MjRiN2QyYjdmKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzM3MzQ2MjhkN2M0ZTRjNTRhYzkwYTFhMDhhYjlhMzg5LmJpbmRQb3B1cChwb3B1cF9jMTkyMjFiZmZkZjI0MzRiOWEyMjBlYTFlMWY2OTlhNCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl80NDYwMTcxYjg4MzM0ZjE4YjFhNzIwNjRjZjQyNjg1YyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjc4NzY1Nzk5ODUzNDg1NCwtNzMuOTc3MDU5MjM2MzA2MDNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMTA5NjE3NzBiODE2NDYxZDliODQ3YzQ5MGE1NjYzYjAgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZmE2YmY3OTFlNGE1NDBkMzg5NGI0MDBkNzYxYmFiYjkgPSAkKCc8ZGl2IGlkPSJodG1sX2ZhNmJmNzkxZTRhNTQwZDM4OTRiNDAwZDc2MWJhYmI5IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5VcHBlciBXZXN0IFNpZGUsIE1hbmhhdHRhbjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMTA5NjE3NzBiODE2NDYxZDliODQ3YzQ5MGE1NjYzYjAuc2V0Q29udGVudChodG1sX2ZhNmJmNzkxZTRhNTQwZDM4OTRiNDAwZDc2MWJhYmI5KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzQ0NjAxNzFiODgzMzRmMThiMWE3MjA2NGNmNDI2ODVjLmJpbmRQb3B1cChwb3B1cF8xMDk2MTc3MGI4MTY0NjFkOWI4NDdjNDkwYTU2NjNiMCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8xNzMzYmQwZmEyZWQ0OWY3YTYxZThlNjY0N2U2ZjRiMyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjc3MzUyODg4OTQyMTY2LC03My45ODUzMzc3NzAwMTI2Ml0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9kYzhmZGEzYjkxMGQ0OTE4OTQ0NGZmMzQwODY3NDg1MCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9hMTIzOTAzM2E2NDI0NzIwYTk5MWY0YjlhNmJmYTA4YyA9ICQoJzxkaXYgaWQ9Imh0bWxfYTEyMzkwMzNhNjQyNDcyMGE5OTFmNGI5YTZiZmEwOGMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkxpbmNvbG4gU3F1YXJlLCBNYW5oYXR0YW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2RjOGZkYTNiOTEwZDQ5MTg5NDQ0ZmYzNDA4Njc0ODUwLnNldENvbnRlbnQoaHRtbF9hMTIzOTAzM2E2NDI0NzIwYTk5MWY0YjlhNmJmYTA4Yyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8xNzMzYmQwZmEyZWQ0OWY3YTYxZThlNjY0N2U2ZjRiMy5iaW5kUG9wdXAocG9wdXBfZGM4ZmRhM2I5MTBkNDkxODk0NDRmZjM0MDg2NzQ4NTApOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMWI3OTJkYTk3MzE2NDRkYmEyNjEwODExZmNjOTRmYWUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43NTkxMDA4OTE0NjIxMiwtNzMuOTk2MTE5MzYzMDk0NzldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfODFhZWFkNDUyNWViNDMxMTk0YmM0MzE1ODUyNjJmYmEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZjUxMWVlNDEyNjgxNDgxOWJhNGY5YTRjZGFjNjc3Y2QgPSAkKCc8ZGl2IGlkPSJodG1sX2Y1MTFlZTQxMjY4MTQ4MTliYTRmOWE0Y2RhYzY3N2NkIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DbGludG9uLCBNYW5oYXR0YW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzgxYWVhZDQ1MjVlYjQzMTE5NGJjNDMxNTg1MjYyZmJhLnNldENvbnRlbnQoaHRtbF9mNTExZWU0MTI2ODE0ODE5YmE0ZjlhNGNkYWM2NzdjZCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8xYjc5MmRhOTczMTY0NGRiYTI2MTA4MTFmY2M5NGZhZS5iaW5kUG9wdXAocG9wdXBfODFhZWFkNDUyNWViNDMxMTk0YmM0MzE1ODUyNjJmYmEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOWQxODNlOTE1YjRmNGM4M2EzYTc5ZjRhM2YxMjU3MWUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43NTQ2OTExMDI3MDYyMywtNzMuOTgxNjY4ODI3MzAzMDRdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMDBlNWU2MGM2MGI1NDE1OWEyMmNkOTQ4MWM1NTkxNGYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOWQ1MmNkNzA4YTM0NDFiNDk1ZjZhM2Q5NmQ3MmY3M2YgPSAkKCc8ZGl2IGlkPSJodG1sXzlkNTJjZDcwOGEzNDQxYjQ5NWY2YTNkOTZkNzJmNzNmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5NaWR0b3duLCBNYW5oYXR0YW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzAwZTVlNjBjNjBiNTQxNTlhMjJjZDk0ODFjNTU5MTRmLnNldENvbnRlbnQoaHRtbF85ZDUyY2Q3MDhhMzQ0MWI0OTVmNmEzZDk2ZDcyZjczZik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl85ZDE4M2U5MTViNGY0YzgzYTNhNzlmNGEzZjEyNTcxZS5iaW5kUG9wdXAocG9wdXBfMDBlNWU2MGM2MGI1NDE1OWEyMmNkOTQ4MWM1NTkxNGYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNjMwMjJmOGRjZDJkNGMyYjlmYmZkMjkzYWFlMmEyOTQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43NDgzMDMwNzcyNTIxNzQsLTczLjk3ODMzMjA3OTI0MTI3XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzhjZWZhZDlhZWU3OTQ5NzBhZGJhOGMyOTM0ZTJkYWRlID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzdjZjEyMTI4ZmNmZTRlZjE5OWQ3ZTg2YTI3ZmQ3NWQ0ID0gJCgnPGRpdiBpZD0iaHRtbF83Y2YxMjEyOGZjZmU0ZWYxOTlkN2U4NmEyN2ZkNzVkNCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+TXVycmF5IEhpbGwsIE1hbmhhdHRhbjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOGNlZmFkOWFlZTc5NDk3MGFkYmE4YzI5MzRlMmRhZGUuc2V0Q29udGVudChodG1sXzdjZjEyMTI4ZmNmZTRlZjE5OWQ3ZTg2YTI3ZmQ3NWQ0KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzYzMDIyZjhkY2QyZDRjMmI5ZmJmZDI5M2FhZTJhMjk0LmJpbmRQb3B1cChwb3B1cF84Y2VmYWQ5YWVlNzk0OTcwYWRiYThjMjkzNGUyZGFkZSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl84MmY3MGZjMzllZTQ0ZTllODdhNDE2ZmZhMTQzYTY4NyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjc0NDAzNDcwNjc0Nzk3NSwtNzQuMDAzMTE2MzM0NzI4MTNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYWExZjdkM2NjY2NiNDlkNzkxYmFmMzk5NzVlOWFhMzggPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNjNiYmRjY2Y5NTlmNDk0OWEzMzllNTQ3NTNkZDEzN2YgPSAkKCc8ZGl2IGlkPSJodG1sXzYzYmJkY2NmOTU5ZjQ5NDlhMzM5ZTU0NzUzZGQxMzdmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DaGVsc2VhLCBNYW5oYXR0YW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2FhMWY3ZDNjY2NjYjQ5ZDc5MWJhZjM5OTc1ZTlhYTM4LnNldENvbnRlbnQoaHRtbF82M2JiZGNjZjk1OWY0OTQ5YTMzOWU1NDc1M2RkMTM3Zik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl84MmY3MGZjMzllZTQ0ZTllODdhNDE2ZmZhMTQzYTY4Ny5iaW5kUG9wdXAocG9wdXBfYWExZjdkM2NjY2NiNDlkNzkxYmFmMzk5NzVlOWFhMzgpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZmFlMmZhODkyOTE2NGMzYjlmYzM1ODAzZWRmMGMzOGIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MjY5MzI4ODUzNjEyOCwtNzMuOTk5OTE0MDI5NDU5MDJdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZWQ4NGQ3NmU4Mzc3NDhjY2JjYmQ4MDFmMGUyNGJmOGIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZmM2YTNjNTljOGU2NGEwN2I1OTI4MDZhNjE3MTY0ZmEgPSAkKCc8ZGl2IGlkPSJodG1sX2ZjNmEzYzU5YzhlNjRhMDdiNTkyODA2YTYxNzE2NGZhIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5HcmVlbndpY2ggVmlsbGFnZSwgTWFuaGF0dGFuPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9lZDg0ZDc2ZTgzNzc0OGNjYmNiZDgwMWYwZTI0YmY4Yi5zZXRDb250ZW50KGh0bWxfZmM2YTNjNTljOGU2NGEwN2I1OTI4MDZhNjE3MTY0ZmEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZmFlMmZhODkyOTE2NGMzYjlmYzM1ODAzZWRmMGMzOGIuYmluZFBvcHVwKHBvcHVwX2VkODRkNzZlODM3NzQ4Y2NiY2JkODAxZjBlMjRiZjhiKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2I1YmIxNmVkODZmYjQ1NjFiMzIzM2NlMDJkNWZhZWM5ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzI3ODQ2Nzc3MjcwMjQ0LC03My45ODIyMjYxNjUwNjQxNl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9lYzllOTMxYzA2ZTg0Mzg4ODEwNDlmY2FlYTBlMTc1YSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF84OThhOTVlOTFmOGY0OGY4ODJkNDk3YTQ4MmUxODg2YiA9ICQoJzxkaXYgaWQ9Imh0bWxfODk4YTk1ZTkxZjhmNDhmODgyZDQ5N2E0ODJlMTg4NmIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkVhc3QgVmlsbGFnZSwgTWFuaGF0dGFuPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9lYzllOTMxYzA2ZTg0Mzg4ODEwNDlmY2FlYTBlMTc1YS5zZXRDb250ZW50KGh0bWxfODk4YTk1ZTkxZjhmNDhmODgyZDQ5N2E0ODJlMTg4NmIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYjViYjE2ZWQ4NmZiNDU2MWIzMjMzY2UwMmQ1ZmFlYzkuYmluZFBvcHVwKHBvcHVwX2VjOWU5MzFjMDZlODQzODg4MTA0OWZjYWVhMGUxNzVhKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzNiNmY4Y2I0ZDA0MDQ1MTNiZTQ3NjlhNzg1MTk4MWRhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzE3ODA2NzQ4OTI3NjUsLTczLjk4MDg5MDMxOTk5MjkxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2Q1MWJlZjA2OTIzMzQ1MjY4NTcxODc0ZjRhZGNhOTU1ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzU4YTQyNzI3NTFmYzQ1ZDJhZTJiN2ExYWE3YzRmNTZhID0gJCgnPGRpdiBpZD0iaHRtbF81OGE0MjcyNzUxZmM0NWQyYWUyYjdhMWFhN2M0ZjU2YSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+TG93ZXIgRWFzdCBTaWRlLCBNYW5oYXR0YW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2Q1MWJlZjA2OTIzMzQ1MjY4NTcxODc0ZjRhZGNhOTU1LnNldENvbnRlbnQoaHRtbF81OGE0MjcyNzUxZmM0NWQyYWUyYjdhMWFhN2M0ZjU2YSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8zYjZmOGNiNGQwNDA0NTEzYmU0NzY5YTc4NTE5ODFkYS5iaW5kUG9wdXAocG9wdXBfZDUxYmVmMDY5MjMzNDUyNjg1NzE4NzRmNGFkY2E5NTUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNmNmNDRlNWMwNTY0NDM2YTk3OTk4ODEzNmE0Nzc3OTcgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MjE1MjE5Njc0NDMyMTYsLTc0LjAxMDY4MzI4NTU5MDg3XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2M4ZTAxZGVmMjNlNDRkM2Y5MzVkMDUyMWUyMDkzMThhID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzM2NDQzZWNhMWI1MDQ5NmM5ZTVhZDQ2NGYwMDdkZjk3ID0gJCgnPGRpdiBpZD0iaHRtbF8zNjQ0M2VjYTFiNTA0OTZjOWU1YWQ0NjRmMDA3ZGY5NyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VHJpYmVjYSwgTWFuaGF0dGFuPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9jOGUwMWRlZjIzZTQ0ZDNmOTM1ZDA1MjFlMjA5MzE4YS5zZXRDb250ZW50KGh0bWxfMzY0NDNlY2ExYjUwNDk2YzllNWFkNDY0ZjAwN2RmOTcpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNmNmNDRlNWMwNTY0NDM2YTk3OTk4ODEzNmE0Nzc3OTcuYmluZFBvcHVwKHBvcHVwX2M4ZTAxZGVmMjNlNDRkM2Y5MzVkMDUyMWUyMDkzMThhKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzNkOThhMTM1MTY4MzQzOTk4NTM4YTU5ODhlODU2ZjM2ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzE5MzIzNzkzOTU5MDcsLTczLjk5NzMwNDY3MjA4MDczXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2UzNTI4MmZlN2JhZjQ4NTViZjBmZWQ5ZGVhMmQ3YzY5ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2Y0MDJiMjcyNTJkZjQzNGFhMTM5YjFmNjM2ZGYzNzU3ID0gJCgnPGRpdiBpZD0iaHRtbF9mNDAyYjI3MjUyZGY0MzRhYTEzOWIxZjYzNmRmMzc1NyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+TGl0dGxlIEl0YWx5LCBNYW5oYXR0YW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2UzNTI4MmZlN2JhZjQ4NTViZjBmZWQ5ZGVhMmQ3YzY5LnNldENvbnRlbnQoaHRtbF9mNDAyYjI3MjUyZGY0MzRhYTEzOWIxZjYzNmRmMzc1Nyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8zZDk4YTEzNTE2ODM0Mzk5ODUzOGE1OTg4ZTg1NmYzNi5iaW5kUG9wdXAocG9wdXBfZTM1MjgyZmU3YmFmNDg1NWJmMGZlZDlkZWEyZDdjNjkpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYmYwZjUzNGI1MTU1NGM4NTk5OTllZDkzMTQ0MGVhYWUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MjIxODM4NDEzMTc5NCwtNzQuMDAwNjU2NjY5NTk3NTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMjQwZWYxY2UyZGRjNGYxN2EyNjkzYTVjMDhlZDFlYzUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNTNkZjYzZDJjZjk0NGEzMzgwNmZhYmMxZTM0NjU1ZDcgPSAkKCc8ZGl2IGlkPSJodG1sXzUzZGY2M2QyY2Y5NDRhMzM4MDZmYWJjMWUzNDY1NWQ3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Tb2hvLCBNYW5oYXR0YW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzI0MGVmMWNlMmRkYzRmMTdhMjY5M2E1YzA4ZWQxZWM1LnNldENvbnRlbnQoaHRtbF81M2RmNjNkMmNmOTQ0YTMzODA2ZmFiYzFlMzQ2NTVkNyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9iZjBmNTM0YjUxNTU0Yzg1OTk5OWVkOTMxNDQwZWFhZS5iaW5kUG9wdXAocG9wdXBfMjQwZWYxY2UyZGRjNGYxN2EyNjkzYTVjMDhlZDFlYzUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNGUxODU1ODM2MGZlNDRlNTgwZDk4NDBmYmE2ZWM3ZDUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MzQ0MzM5MzU3MjQzNCwtNzQuMDA2MTc5OTgxMjY4MTJdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMWQ4YmU2ZDczZjY0NDc2M2JmNzkxZWY2ZTgxODE2ZDQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNDJjMzAzNDA3MjZmNDRmZThiYTVmMDk0MTlhMjhkM2EgPSAkKCc8ZGl2IGlkPSJodG1sXzQyYzMwMzQwNzI2ZjQ0ZmU4YmE1ZjA5NDE5YTI4ZDNhIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5XZXN0IFZpbGxhZ2UsIE1hbmhhdHRhbjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMWQ4YmU2ZDczZjY0NDc2M2JmNzkxZWY2ZTgxODE2ZDQuc2V0Q29udGVudChodG1sXzQyYzMwMzQwNzI2ZjQ0ZmU4YmE1ZjA5NDE5YTI4ZDNhKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzRlMTg1NTgzNjBmZTQ0ZTU4MGQ5ODQwZmJhNmVjN2Q1LmJpbmRQb3B1cChwb3B1cF8xZDhiZTZkNzNmNjQ0NzYzYmY3OTFlZjZlODE4MTZkNCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl85MWNiZTNhMGFlNjY0ZDJhYTYzMWE4ZWQ2MmEyZDFjNCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjc5NzMwNzA0MTcwMjg2NSwtNzMuOTY0Mjg2MTc3NDA2NTVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfN2U3NjdjZjMwOTFlNDNkYmE1MjdhNmRhM2FjOWI3ZDIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMjI1MWZmMzA5YWVmNGFhNTg2ZTkyZTE4ZDE2ODZlN2YgPSAkKCc8ZGl2IGlkPSJodG1sXzIyNTFmZjMwOWFlZjRhYTU4NmU5MmUxOGQxNjg2ZTdmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5NYW5oYXR0YW4gVmFsbGV5LCBNYW5oYXR0YW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzdlNzY3Y2YzMDkxZTQzZGJhNTI3YTZkYTNhYzliN2QyLnNldENvbnRlbnQoaHRtbF8yMjUxZmYzMDlhZWY0YWE1ODZlOTJlMThkMTY4NmU3Zik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl85MWNiZTNhMGFlNjY0ZDJhYTYzMWE4ZWQ2MmEyZDFjNC5iaW5kUG9wdXAocG9wdXBfN2U3NjdjZjMwOTFlNDNkYmE1MjdhNmRhM2FjOWI3ZDIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMWM2MTc3NjNlOTZiNDg0OWIyNzI4NjZmNzEwNThmOTcgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44MDc5OTk3MzgxNjU4MjYsLTczLjk2Mzg5NjI3OTA1MzMyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2YzNTc3ZWY4OTVjNjRkMjg4ZWVmNzY2MWMzZjBmMDdlID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzJjYWY5MmQyYmVkMzRkYjI5MGU3NDNiMTQ2OTQzYWE3ID0gJCgnPGRpdiBpZD0iaHRtbF8yY2FmOTJkMmJlZDM0ZGIyOTBlNzQzYjE0Njk0M2FhNyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+TW9ybmluZ3NpZGUgSGVpZ2h0cywgTWFuaGF0dGFuPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9mMzU3N2VmODk1YzY0ZDI4OGVlZjc2NjFjM2YwZjA3ZS5zZXRDb250ZW50KGh0bWxfMmNhZjkyZDJiZWQzNGRiMjkwZTc0M2IxNDY5NDNhYTcpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMWM2MTc3NjNlOTZiNDg0OWIyNzI4NjZmNzEwNThmOTcuYmluZFBvcHVwKHBvcHVwX2YzNTc3ZWY4OTVjNjRkMjg4ZWVmNzY2MWMzZjBmMDdlKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzc0MWYwZjhkOWVkYTRmMzE5MDkzZjM4ZjM1MjUxNzM1ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzM3MjA5ODMyNzE1LC03My45ODEzNzU5NDgzMzU0MV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8xNmFhZmM2NWFlMTY0ZTk2ODdkY2VmN2YxM2JlOTY0OCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8yNmZjNjBlYjIyMDg0ZmIzOGJmYzAxODRhZDIwN2Y4NSA9ICQoJzxkaXYgaWQ9Imh0bWxfMjZmYzYwZWIyMjA4NGZiMzhiZmMwMTg0YWQyMDdmODUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkdyYW1lcmN5LCBNYW5oYXR0YW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzE2YWFmYzY1YWUxNjRlOTY4N2RjZWY3ZjEzYmU5NjQ4LnNldENvbnRlbnQoaHRtbF8yNmZjNjBlYjIyMDg0ZmIzOGJmYzAxODRhZDIwN2Y4NSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl83NDFmMGY4ZDllZGE0ZjMxOTA5M2YzOGYzNTI1MTczNS5iaW5kUG9wdXAocG9wdXBfMTZhYWZjNjVhZTE2NGU5Njg3ZGNlZjdmMTNiZTk2NDgpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYmM4YmVjM2JkMDUwNGEyYmFhYWY5OTRlYjczOTIzNTUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MTE5MzE5ODM5NDU2NSwtNzQuMDE2ODY5MzA1MDg2MTddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZDk0YWNmYjQyYjQ4NDRjY2E3NGMwOTJhNjE5OGM0YmYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNmYwNjM1OGFhMjc0NGM5MmEyZmM1ZmYxOWUwYzIxZTkgPSAkKCc8ZGl2IGlkPSJodG1sXzZmMDYzNThhYTI3NDRjOTJhMmZjNWZmMTllMGMyMWU5IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CYXR0ZXJ5IFBhcmsgQ2l0eSwgTWFuaGF0dGFuPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9kOTRhY2ZiNDJiNDg0NGNjYTc0YzA5MmE2MTk4YzRiZi5zZXRDb250ZW50KGh0bWxfNmYwNjM1OGFhMjc0NGM5MmEyZmM1ZmYxOWUwYzIxZTkpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYmM4YmVjM2JkMDUwNGEyYmFhYWY5OTRlYjczOTIzNTUuYmluZFBvcHVwKHBvcHVwX2Q5NGFjZmI0MmI0ODQ0Y2NhNzRjMDkyYTYxOThjNGJmKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2ZiYWUxYWRjOGU3YzQ2MDA4MWY1ZTNmNTMxNzMxMDZjID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzA3MTA3MTA3MjcwNDgsLTc0LjAxMDY2NTQ0NTIxMjddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNmUzMzc4ZWQ1ODE1NDVlZDgwOWMzYjcyNDZlYzkzNzEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMmUwYmQ0ZWIwNGE1NDhkNDhiZGQ2YWJjMTMzYjAwNTMgPSAkKCc8ZGl2IGlkPSJodG1sXzJlMGJkNGViMDRhNTQ4ZDQ4YmRkNmFiYzEzM2IwMDUzIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5GaW5hbmNpYWwgRGlzdHJpY3QsIE1hbmhhdHRhbjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNmUzMzc4ZWQ1ODE1NDVlZDgwOWMzYjcyNDZlYzkzNzEuc2V0Q29udGVudChodG1sXzJlMGJkNGViMDRhNTQ4ZDQ4YmRkNmFiYzEzM2IwMDUzKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2ZiYWUxYWRjOGU3YzQ2MDA4MWY1ZTNmNTMxNzMxMDZjLmJpbmRQb3B1cChwb3B1cF82ZTMzNzhlZDU4MTU0NWVkODA5YzNiNzI0NmVjOTM3MSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl83MWFlZDNlYjZhNjI0NDA1OTNiMjg2MDg2NGNjYzM1YyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjc2ODUwODU5MzM1NDkyLC03My45MTU2NTM3NDMwNDIzNF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9hM2Y4MWFhOTJjMjE0Y2I0ODZkNDFiMzU0YzU2ODVkMCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9lYjY2ZGQ0Y2E1Y2I0Y2YwYjEyMTMzMWVlMGNjYjAyZSA9ICQoJzxkaXYgaWQ9Imh0bWxfZWI2NmRkNGNhNWNiNGNmMGIxMjEzMzFlZTBjY2IwMmUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkFzdG9yaWEsIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYTNmODFhYTkyYzIxNGNiNDg2ZDQxYjM1NGM1Njg1ZDAuc2V0Q29udGVudChodG1sX2ViNjZkZDRjYTVjYjRjZjBiMTIxMzMxZWUwY2NiMDJlKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzcxYWVkM2ViNmE2MjQ0MDU5M2IyODYwODY0Y2NjMzVjLmJpbmRQb3B1cChwb3B1cF9hM2Y4MWFhOTJjMjE0Y2I0ODZkNDFiMzU0YzU2ODVkMCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9iN2Y5NTM1ODQ1MzQ0NTRjODk5ZjA4OTBlNTQ0ZjI3ZiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjc0NjM0OTA4ODYwMjIyLC03My45MDE4NDE2NjgzODI4NF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF83OTY5ZWM5NTAzYTk0YjUyODlmNmNhY2IxNjdmOGNiOSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9mZjM5NGNhNTQ0MDg0MDc5YWYwZDhiZDdlMzEwYjFjZiA9ICQoJzxkaXYgaWQ9Imh0bWxfZmYzOTRjYTU0NDA4NDA3OWFmMGQ4YmQ3ZTMxMGIxY2YiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPldvb2RzaWRlLCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzc5NjllYzk1MDNhOTRiNTI4OWY2Y2FjYjE2N2Y4Y2I5LnNldENvbnRlbnQoaHRtbF9mZjM5NGNhNTQ0MDg0MDc5YWYwZDhiZDdlMzEwYjFjZik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9iN2Y5NTM1ODQ1MzQ0NTRjODk5ZjA4OTBlNTQ0ZjI3Zi5iaW5kUG9wdXAocG9wdXBfNzk2OWVjOTUwM2E5NGI1Mjg5ZjZjYWNiMTY3ZjhjYjkpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMDM5MjQ0YjkwZTAwNGM5YjlhNzkyNzkwMDViOTI0Y2IgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43NTE5ODEzODAwNzM2NywtNzMuODgyODIxMDkxNjQzNjVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYTQ4ZWMxZmEwZWFjNDk0NGE1MTg4NzEyNzkxNTI1OTAgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOTMwY2YxYzBhMzk0NGE3YjhjNjRmODVjOGE5N2JlYmYgPSAkKCc8ZGl2IGlkPSJodG1sXzkzMGNmMWMwYTM5NDRhN2I4YzY0Zjg1YzhhOTdiZWJmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5KYWNrc29uIEhlaWdodHMsIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYTQ4ZWMxZmEwZWFjNDk0NGE1MTg4NzEyNzkxNTI1OTAuc2V0Q29udGVudChodG1sXzkzMGNmMWMwYTM5NDRhN2I4YzY0Zjg1YzhhOTdiZWJmKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzAzOTI0NGI5MGUwMDRjOWI5YTc5Mjc5MDA1YjkyNGNiLmJpbmRQb3B1cChwb3B1cF9hNDhlYzFmYTBlYWM0OTQ0YTUxODg3MTI3OTE1MjU5MCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8yYzcxMDE1NTQyMzg0ZTQ5YTZiZWU1MDY2MTA4NDYwZiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjc0NDA0ODUwNTEyMjAyNCwtNzMuODgxNjU2MjIyODgzODhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNDg1MTc3YWYxNzQyNGUzOGJiMTdiMWNmOWJkZThkNDAgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfM2RhYzRjN2QzMmNiNGMzODlkM2FjNTUxOGZiN2U2MzcgPSAkKCc8ZGl2IGlkPSJodG1sXzNkYWM0YzdkMzJjYjRjMzg5ZDNhYzU1MThmYjdlNjM3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5FbG1odXJzdCwgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF80ODUxNzdhZjE3NDI0ZTM4YmIxN2IxY2Y5YmRlOGQ0MC5zZXRDb250ZW50KGh0bWxfM2RhYzRjN2QzMmNiNGMzODlkM2FjNTUxOGZiN2U2MzcpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMmM3MTAxNTU0MjM4NGU0OWE2YmVlNTA2NjEwODQ2MGYuYmluZFBvcHVwKHBvcHVwXzQ4NTE3N2FmMTc0MjRlMzhiYjE3YjFjZjliZGU4ZDQwKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2E5ZjgyOTBmMzQ5NDQ3YWY4ZWEyYTAzY2EwMTJlMDAyID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjU0MjI1Mjc3Mzg0ODcsLTczLjgzODEzNzY0NjAwMjhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfODc5OWUwMjNlNjRkNGMxNjllMTZmMWE2NzMyODViY2IgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZmQyNzcyZjU5ZTQ5NDEwYmI3OWMyNjMwNmZjNDJmZjIgPSAkKCc8ZGl2IGlkPSJodG1sX2ZkMjc3MmY1OWU0OTQxMGJiNzljMjYzMDZmYzQyZmYyIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Ib3dhcmQgQmVhY2gsIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfODc5OWUwMjNlNjRkNGMxNjllMTZmMWE2NzMyODViY2Iuc2V0Q29udGVudChodG1sX2ZkMjc3MmY1OWU0OTQxMGJiNzljMjYzMDZmYzQyZmYyKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2E5ZjgyOTBmMzQ5NDQ3YWY4ZWEyYTAzY2EwMTJlMDAyLmJpbmRQb3B1cChwb3B1cF84Nzk5ZTAyM2U2NGQ0YzE2OWUxNmYxYTY3MzI4NWJjYik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl84YjZkYWY2OTIwYzQ0ZDgxYTg5NTFhMTFhMThiZDM2YiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjc0MjM4MTc1MDE1NjY3LC03My44NTY4MjQ5NzM0NTI1OF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF83MjMzOWE3YmFjMjU0N2I4OTg5NWVmZWY1MTk2ZWEzNSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF85NzI2Yzk1MDE0N2E0NWM3OWQxYjY1NTBiYThjNTgwOSA9ICQoJzxkaXYgaWQ9Imh0bWxfOTcyNmM5NTAxNDdhNDVjNzlkMWI2NTUwYmE4YzU4MDkiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNvcm9uYSwgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF83MjMzOWE3YmFjMjU0N2I4OTg5NWVmZWY1MTk2ZWEzNS5zZXRDb250ZW50KGh0bWxfOTcyNmM5NTAxNDdhNDVjNzlkMWI2NTUwYmE4YzU4MDkpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOGI2ZGFmNjkyMGM0NGQ4MWE4OTUxYTExYTE4YmQzNmIuYmluZFBvcHVwKHBvcHVwXzcyMzM5YTdiYWMyNTQ3Yjg5ODk1ZWZlZjUxOTZlYTM1KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzRiMDAzNjlhYzhkNjRiNTI5Nzk5OGE5NjFlNzBhYjNiID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzI1MjYzNzgyMTY1MDMsLTczLjg0NDQ3NTAwNzg4OTgzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzRhNzYxZDkwYjdjODQ1MzU5NWFjMWVlYzYzMTBjMmI5ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzQyOTQ1NDIxY2YzYTQyYjg4ZmY1YzI1NTg5MGQ2MzM0ID0gJCgnPGRpdiBpZD0iaHRtbF80Mjk0NTQyMWNmM2E0MmI4OGZmNWMyNTU4OTBkNjMzNCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Rm9yZXN0IEhpbGxzLCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzRhNzYxZDkwYjdjODQ1MzU5NWFjMWVlYzYzMTBjMmI5LnNldENvbnRlbnQoaHRtbF80Mjk0NTQyMWNmM2E0MmI4OGZmNWMyNTU4OTBkNjMzNCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl80YjAwMzY5YWM4ZDY0YjUyOTc5OThhOTYxZTcwYWIzYi5iaW5kUG9wdXAocG9wdXBfNGE3NjFkOTBiN2M4NDUzNTk1YWMxZWVjNjMxMGMyYjkpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYjM2YjYxNTc4ODY1NDk3NzlkZTlmNmYxNWI2ODhhMTggPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MDUxNzkwMzU0MTQ4LC03My44Mjk4MTkwNTgyNTcwM10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9jMTAwZTVkZWEyMmE0ODdmYmJlNTczZTAwZGNkZjBhZiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9kNDNjOGY1NGU4ZTg0MTU1YTQ1NTYyNWU0MWUwMjA3NCA9ICQoJzxkaXYgaWQ9Imh0bWxfZDQzYzhmNTRlOGU4NDE1NWE0NTU2MjVlNDFlMDIwNzQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPktldyBHYXJkZW5zLCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2MxMDBlNWRlYTIyYTQ4N2ZiYmU1NzNlMDBkY2RmMGFmLnNldENvbnRlbnQoaHRtbF9kNDNjOGY1NGU4ZTg0MTU1YTQ1NTYyNWU0MWUwMjA3NCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9iMzZiNjE1Nzg4NjU0OTc3OWRlOWY2ZjE1YjY4OGExOC5iaW5kUG9wdXAocG9wdXBfYzEwMGU1ZGVhMjJhNDg3ZmJiZTU3M2UwMGRjZGYwYWYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMDk1YWNkYmIzYmFjNGM2NGE1ZThlNDUxN2MzZjkxZDEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42OTc5NDczMTQ3MTc2MywtNzMuODMxODMzMjE0NDY4ODddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZTI4NzY5ZjRmNzFjNDgzZjkwY2U1ZjA0MzNiM2IwYmEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMTU0MTY2MzA3MTQ3NDQ5NDlhMTI4ODRmNjM2Y2E1YTggPSAkKCc8ZGl2IGlkPSJodG1sXzE1NDE2NjMwNzE0NzQ0OTQ5YTEyODg0ZjYzNmNhNWE4IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5SaWNobW9uZCBIaWxsLCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2UyODc2OWY0ZjcxYzQ4M2Y5MGNlNWYwNDMzYjNiMGJhLnNldENvbnRlbnQoaHRtbF8xNTQxNjYzMDcxNDc0NDk0OWExMjg4NGY2MzZjYTVhOCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8wOTVhY2RiYjNiYWM0YzY0YTVlOGU0NTE3YzNmOTFkMS5iaW5kUG9wdXAocG9wdXBfZTI4NzY5ZjRmNzFjNDgzZjkwY2U1ZjA0MzNiM2IwYmEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZDcyMmI2MzVmYzc4NGZlNzhhYzI0YTE0ZDg2ODZkYTQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43NjQ0NTQxOTY5Nzg0NiwtNzMuODMxNzczMDAzMjk1ODJdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMTczNDI2YzM5YWRiNGFkNzljZjY1ZGMzY2U3ZTkwYzggPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYTU5MTQ0ZTBkNTYwNDFiZmI5Zjg5ZThiODRkZTBkYzYgPSAkKCc8ZGl2IGlkPSJodG1sX2E1OTE0NGUwZDU2MDQxYmZiOWY4OWU4Yjg0ZGUwZGM2IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5GbHVzaGluZywgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8xNzM0MjZjMzlhZGI0YWQ3OWNmNjVkYzNjZTdlOTBjOC5zZXRDb250ZW50KGh0bWxfYTU5MTQ0ZTBkNTYwNDFiZmI5Zjg5ZThiODRkZTBkYzYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZDcyMmI2MzVmYzc4NGZlNzhhYzI0YTE0ZDg2ODZkYTQuYmluZFBvcHVwKHBvcHVwXzE3MzQyNmMzOWFkYjRhZDc5Y2Y2NWRjM2NlN2U5MGM4KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzljOTU2OGFiNDJlZjQ5YjRhMmU2OGIxMDZhMGViODU1ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzUwMjE3MzQ2MTA1MjgsLTczLjkzOTIwMjIzOTE1NTA1XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzFmZGFhODZmNzkzODQ2NDRhMjIyMDgyZDFkYWRlMmUwID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2YxYmMxYzBkYTk2ZTQ2ZDI4MDZkM2UxMGExNzY4YWVhID0gJCgnPGRpdiBpZD0iaHRtbF9mMWJjMWMwZGE5NmU0NmQyODA2ZDNlMTBhMTc2OGFlYSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+TG9uZyBJc2xhbmQgQ2l0eSwgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8xZmRhYTg2Zjc5Mzg0NjQ0YTIyMjA4MmQxZGFkZTJlMC5zZXRDb250ZW50KGh0bWxfZjFiYzFjMGRhOTZlNDZkMjgwNmQzZTEwYTE3NjhhZWEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOWM5NTY4YWI0MmVmNDliNGEyZTY4YjEwNmEwZWI4NTUuYmluZFBvcHVwKHBvcHVwXzFmZGFhODZmNzkzODQ2NDRhMjIyMDgyZDFkYWRlMmUwKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzRlN2ViNGU5ZWI4YTQ5ODhhMzAwYTA5YzY2MGM0NTAzID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzQwMTc2MjgzNTE5MjQsLTczLjkyNjkxNjE3NTYxNTc3XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzQyMTFiYzliN2YxZjQ1YWM5YzA5YjQ1OTEzMDg4YTM3ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzFiYWRhMzJiMzZmNTQ0YTZiMmNmMTExMWVhMDgwMzJkID0gJCgnPGRpdiBpZD0iaHRtbF8xYmFkYTMyYjM2ZjU0NGE2YjJjZjExMTFlYTA4MDMyZCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+U3VubnlzaWRlLCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzQyMTFiYzliN2YxZjQ1YWM5YzA5YjQ1OTEzMDg4YTM3LnNldENvbnRlbnQoaHRtbF8xYmFkYTMyYjM2ZjU0NGE2YjJjZjExMTFlYTA4MDMyZCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl80ZTdlYjRlOWViOGE0OTg4YTMwMGEwOWM2NjBjNDUwMy5iaW5kUG9wdXAocG9wdXBfNDIxMWJjOWI3ZjFmNDVhYzljMDliNDU5MTMwODhhMzcpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNDM2M2JkNDI4YTRlNDg2MTlkMWJjOTEzNWEwZWM5YTEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43NjQwNzMyMzg4MzA5MSwtNzMuODY3MDQxNDc2NTg3NzJdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfOWM2YjJjYTg1MzkwNDU3NWI0NGJjN2FjMjcyOGY2NzYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZjVlMWM3YjhjOTI5NGVkOGJjM2QzNmZiMDA0OTdkOTggPSAkKCc8ZGl2IGlkPSJodG1sX2Y1ZTFjN2I4YzkyOTRlZDhiYzNkMzZmYjAwNDk3ZDk4IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5FYXN0IEVsbWh1cnN0LCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzljNmIyY2E4NTM5MDQ1NzViNDRiYzdhYzI3MjhmNjc2LnNldENvbnRlbnQoaHRtbF9mNWUxYzdiOGM5Mjk0ZWQ4YmMzZDM2ZmIwMDQ5N2Q5OCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl80MzYzYmQ0MjhhNGU0ODYxOWQxYmM5MTM1YTBlYzlhMS5iaW5kUG9wdXAocG9wdXBfOWM2YjJjYTg1MzkwNDU3NWI0NGJjN2FjMjcyOGY2NzYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYjMwODJmMWE1M2I4NDE4MjkxMmU3NjQ0NjA4ODBmMmQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MjU0MjczNzQwOTM2MDYsLTczLjg5NjIxNzEzNjI2ODU5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzVlZWFjMTBhZGI5ODQwNTk4MzYzY2Y2NzU2Zjg1ODQzID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2FlYWJiYjhhYTA0ZTRiZTE5MDZhNjJiODA4MTQxYmI2ID0gJCgnPGRpdiBpZD0iaHRtbF9hZWFiYmI4YWEwNGU0YmUxOTA2YTYyYjgwODE0MWJiNiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+TWFzcGV0aCwgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF81ZWVhYzEwYWRiOTg0MDU5ODM2M2NmNjc1NmY4NTg0My5zZXRDb250ZW50KGh0bWxfYWVhYmJiOGFhMDRlNGJlMTkwNmE2MmI4MDgxNDFiYjYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYjMwODJmMWE1M2I4NDE4MjkxMmU3NjQ0NjA4ODBmMmQuYmluZFBvcHVwKHBvcHVwXzVlZWFjMTBhZGI5ODQwNTk4MzYzY2Y2NzU2Zjg1ODQzKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2EwOTVhZjk2M2FhYjQ0N2E4YmMzNGIxMjgxNjY1MDQ1ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzA4MzIzMTU2MTM4NTgsLTczLjkwMTQzNTE3NTU5NTg5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzFlM2I5MTE5YTY3NTQxZGFhOWRmNDY0M2IyMDJmYzVhID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzg4ODRmMjI0NzM3ODRkNjNhNTYzYmJkNDUzN2I3MTdkID0gJCgnPGRpdiBpZD0iaHRtbF84ODg0ZjIyNDczNzg0ZDYzYTU2M2JiZDQ1MzdiNzE3ZCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+UmlkZ2V3b29kLCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzFlM2I5MTE5YTY3NTQxZGFhOWRmNDY0M2IyMDJmYzVhLnNldENvbnRlbnQoaHRtbF84ODg0ZjIyNDczNzg0ZDYzYTU2M2JiZDQ1MzdiNzE3ZCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9hMDk1YWY5NjNhYWI0NDdhOGJjMzRiMTI4MTY2NTA0NS5iaW5kUG9wdXAocG9wdXBfMWUzYjkxMTlhNjc1NDFkYWE5ZGY0NjQzYjIwMmZjNWEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNmMzYzU2YjVhMWQ1NGQ1ODk0OGFkNWJiNmJkNzRkNWQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MDI3NjI0Mjk2NzgzOCwtNzMuODcwNzQxNjc0MzU2MDVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYzVmMDQ1NjJhMjE0NDE2ZWFhOTM0YjlhMmI4NWQ1NTIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZTZjMDhhMjhhMzQwNDdjM2IyMzMzZDE3N2M5ZDQ3ZTIgPSAkKCc8ZGl2IGlkPSJodG1sX2U2YzA4YTI4YTM0MDQ3YzNiMjMzM2QxNzdjOWQ0N2UyIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5HbGVuZGFsZSwgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9jNWYwNDU2MmEyMTQ0MTZlYWE5MzRiOWEyYjg1ZDU1Mi5zZXRDb250ZW50KGh0bWxfZTZjMDhhMjhhMzQwNDdjM2IyMzMzZDE3N2M5ZDQ3ZTIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNmMzYzU2YjVhMWQ1NGQ1ODk0OGFkNWJiNmJkNzRkNWQuYmluZFBvcHVwKHBvcHVwX2M1ZjA0NTYyYTIxNDQxNmVhYTkzNGI5YTJiODVkNTUyKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzFiODkyYmY0YWY3MjQ3MGNhY2U5NGVlZmVkYjUzMmNjID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzI4OTc0MDk0ODA3MzUsLTczLjg1NzgyNjg2OTA1MzddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfOTliM2YwNmYxYjkyNGQ0YTk3MDNlZWM3OGUyZTA0MmIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMzE3YTNjMzRkMjE3NDI1MWIwM2Y1YzhhMzkyMmE0YzQgPSAkKCc8ZGl2IGlkPSJodG1sXzMxN2EzYzM0ZDIxNzQyNTFiMDNmNWM4YTM5MjJhNGM0IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5SZWdvIFBhcmssIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOTliM2YwNmYxYjkyNGQ0YTk3MDNlZWM3OGUyZTA0MmIuc2V0Q29udGVudChodG1sXzMxN2EzYzM0ZDIxNzQyNTFiMDNmNWM4YTM5MjJhNGM0KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzFiODkyYmY0YWY3MjQ3MGNhY2U5NGVlZmVkYjUzMmNjLmJpbmRQb3B1cChwb3B1cF85OWIzZjA2ZjFiOTI0ZDRhOTcwM2VlYzc4ZTJlMDQyYik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9jZDIzMmQ3NTBmMTY0MWY1YjVkZDJkOWJiOWY3ZDc0NSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjY4OTg4Njg3OTE1Nzg5LC03My44NTgxMTA0NjU1NDMyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzk2YTEyY2YzNWM5MzRmOTQ4MGE5MzcwNTgzNjExNjQ5ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzcwYThkZjk3ZGQ1YTQxNjI4ZGJhYzhmZDBmMTk5ZDM1ID0gJCgnPGRpdiBpZD0iaHRtbF83MGE4ZGY5N2RkNWE0MTYyOGRiYWM4ZmQwZjE5OWQzNSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+V29vZGhhdmVuLCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzk2YTEyY2YzNWM5MzRmOTQ4MGE5MzcwNTgzNjExNjQ5LnNldENvbnRlbnQoaHRtbF83MGE4ZGY5N2RkNWE0MTYyOGRiYWM4ZmQwZjE5OWQzNSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9jZDIzMmQ3NTBmMTY0MWY1YjVkZDJkOWJiOWY3ZDc0NS5iaW5kUG9wdXAocG9wdXBfOTZhMTJjZjM1YzkzNGY5NDgwYTkzNzA1ODM2MTE2NDkpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMzMyMDEzNTkwYWYyNGMwY2E5OGRhYjg3ZGRlYTYxY2UgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42ODA3MDg0NjgyNjU0MTUsLTczLjg0MzIwMjY2MTczNDQ3XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzlhOTQyNDc4MzM0NDRlNjhhMDQ2NWQ2NmY0ZDY0NTE0ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2YxZTA5ODFhNDAwNjRkNTViZjJmOGFhZjMzMmYwYzUzID0gJCgnPGRpdiBpZD0iaHRtbF9mMWUwOTgxYTQwMDY0ZDU1YmYyZjhhYWYzMzJmMGM1MyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+T3pvbmUgUGFyaywgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF85YTk0MjQ3ODMzNDQ0ZTY4YTA0NjVkNjZmNGQ2NDUxNC5zZXRDb250ZW50KGh0bWxfZjFlMDk4MWE0MDA2NGQ1NWJmMmY4YWFmMzMyZjBjNTMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMzMyMDEzNTkwYWYyNGMwY2E5OGRhYjg3ZGRlYTYxY2UuYmluZFBvcHVwKHBvcHVwXzlhOTQyNDc4MzM0NDRlNjhhMDQ2NWQ2NmY0ZDY0NTE0KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2I5N2ExMGU2NzIzNjQ1MTA5YTY3YjA4NzZiYjA3YjgyID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjY4NTQ5NTc3NjcxOTUsLTczLjgwOTg2NDc4NjQ5MDQxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzVhYjFiYjQ3MTJhNzRlNjVhZTE5ODZjMjkwODBmNTE5ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2U1NGY1YTEyMThlMjQ2MjE5NTgwNzIyMzBkZGFjOTcwID0gJCgnPGRpdiBpZD0iaHRtbF9lNTRmNWExMjE4ZTI0NjIxOTU4MDcyMjMwZGRhYzk3MCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+U291dGggT3pvbmUgUGFyaywgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF81YWIxYmI0NzEyYTc0ZTY1YWUxOTg2YzI5MDgwZjUxOS5zZXRDb250ZW50KGh0bWxfZTU0ZjVhMTIxOGUyNDYyMTk1ODA3MjIzMGRkYWM5NzApOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYjk3YTEwZTY3MjM2NDUxMDlhNjdiMDg3NmJiMDdiODIuYmluZFBvcHVwKHBvcHVwXzVhYjFiYjQ3MTJhNzRlNjVhZTE5ODZjMjkwODBmNTE5KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzMwODk3OWE0ZGVlMTRiZGFhYmUxYTk5MTAyNzBhNTQ0ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzg0OTAyNzQ5MjYwMjA1LC03My44NDMwNDUyODg5NjEyNV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9mZjU0ZWJhNzZiNWI0NmMxYWMxZjYwNmU2ZDYwMDNjZCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF85NTE2M2Q3MjNkYjU0NmI4YTA5MmViNjhlOTdiNTNjYSA9ICQoJzxkaXYgaWQ9Imh0bWxfOTUxNjNkNzIzZGI1NDZiOGEwOTJlYjY4ZTk3YjUzY2EiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNvbGxlZ2UgUG9pbnQsIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZmY1NGViYTc2YjViNDZjMWFjMWY2MDZlNmQ2MDAzY2Quc2V0Q29udGVudChodG1sXzk1MTYzZDcyM2RiNTQ2YjhhMDkyZWI2OGU5N2I1M2NhKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzMwODk3OWE0ZGVlMTRiZGFhYmUxYTk5MTAyNzBhNTQ0LmJpbmRQb3B1cChwb3B1cF9mZjU0ZWJhNzZiNWI0NmMxYWMxZjYwNmU2ZDYwMDNjZCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9hMzAzYjI5YjgyNmU0YTBmOWI4MWRiMDhhNDI0MzVjNiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjc4MTI5MDc2NjAyNjk0LC03My44MTQyMDIxNjYxMDg2M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF83NzcxNTZmYjI3ZGM0ZDZmYjY4MjE2MDQ2NjkxYmU4MyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9jODdlZTIwZGJhMjY0MTRhOWI0OWJkOGE0ODJlYTA0YiA9ICQoJzxkaXYgaWQ9Imh0bWxfYzg3ZWUyMGRiYTI2NDE0YTliNDliZDhhNDgyZWEwNGIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPldoaXRlc3RvbmUsIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNzc3MTU2ZmIyN2RjNGQ2ZmI2ODIxNjA0NjY5MWJlODMuc2V0Q29udGVudChodG1sX2M4N2VlMjBkYmEyNjQxNGE5YjQ5YmQ4YTQ4MmVhMDRiKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2EzMDNiMjliODI2ZTRhMGY5YjgxZGIwOGE0MjQzNWM2LmJpbmRQb3B1cChwb3B1cF83NzcxNTZmYjI3ZGM0ZDZmYjY4MjE2MDQ2NjkxYmU4Myk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8zNmM4NGMxMzJhZWQ0ZmYwODFkZTk0ZTUwNmEzMTYwYyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjc2NjA0MDYzMjgxMDY0LC03My43NzQyNzM2MzA2ODY3XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2VlZDdjMTU4NmUzODRlYTU5OGYwZjU2N2VjYmMwNzc4ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzI0YjY5Y2JjMjdkMTQyMDRiYTIyOGMwOGRjYjZjZmFiID0gJCgnPGRpdiBpZD0iaHRtbF8yNGI2OWNiYzI3ZDE0MjA0YmEyMjhjMDhkY2I2Y2ZhYiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QmF5c2lkZSwgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9lZWQ3YzE1ODZlMzg0ZWE1OThmMGY1NjdlY2JjMDc3OC5zZXRDb250ZW50KGh0bWxfMjRiNjljYmMyN2QxNDIwNGJhMjI4YzA4ZGNiNmNmYWIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMzZjODRjMTMyYWVkNGZmMDgxZGU5NGU1MDZhMzE2MGMuYmluZFBvcHVwKHBvcHVwX2VlZDdjMTU4NmUzODRlYTU5OGYwZjU2N2VjYmMwNzc4KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzQ5NDU0M2FlYjNhMzQ2MjA4MDY5YTNiYTA2YzZmYTE2ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzYxNzI5NTQ5MDMyNjIsLTczLjc5MTc2MjQzNzI4MDYxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzQ5MmJlODk3ZTk2MjRiOTVhZmNiZjA0OTM3ZmFjMTRhID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2ZiZDZmODI4ZjUzYzRlNTliNGVlMDQ0NjJhYTQ2NTI2ID0gJCgnPGRpdiBpZD0iaHRtbF9mYmQ2ZjgyOGY1M2M0ZTU5YjRlZTA0NDYyYWE0NjUyNiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QXVidXJuZGFsZSwgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF80OTJiZTg5N2U5NjI0Yjk1YWZjYmYwNDkzN2ZhYzE0YS5zZXRDb250ZW50KGh0bWxfZmJkNmY4MjhmNTNjNGU1OWI0ZWUwNDQ2MmFhNDY1MjYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNDk0NTQzYWViM2EzNDYyMDgwNjlhM2JhMDZjNmZhMTYuYmluZFBvcHVwKHBvcHVwXzQ5MmJlODk3ZTk2MjRiOTVhZmNiZjA0OTM3ZmFjMTRhKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2YyYTJjNzUzMTcyZTRjY2Y4ZTU1NjhjNjQ3MjQyOTBhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzcwODI2MTkyODI2NywtNzMuNzM4ODk3NzU1ODA3NF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8xYzFiMTA2M2FkYTk0YjY5ODVmMDZhZTE3ODNiNzgxMiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8wZTZjYzVkYjUxYTU0ZmYwODIzZGZiZmEyM2EzODZlOCA9ICQoJzxkaXYgaWQ9Imh0bWxfMGU2Y2M1ZGI1MWE1NGZmMDgyM2RmYmZhMjNhMzg2ZTgiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkxpdHRsZSBOZWNrLCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzFjMWIxMDYzYWRhOTRiNjk4NWYwNmFlMTc4M2I3ODEyLnNldENvbnRlbnQoaHRtbF8wZTZjYzVkYjUxYTU0ZmYwODIzZGZiZmEyM2EzODZlOCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9mMmEyYzc1MzE3MmU0Y2NmOGU1NTY4YzY0NzI0MjkwYS5iaW5kUG9wdXAocG9wdXBfMWMxYjEwNjNhZGE5NGI2OTg1ZjA2YWUxNzgzYjc4MTIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZjQ5NDAyNjdjOGM0NGFjMGIxN2U4NTZmNzAyNThmYjMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43NjY4NDYwOTc5MDc2MywtNzMuNzQyNDk4MjA3MjczM10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF80NTRlYTliN2MwZGM0OGQ5YjRlZWZhZDI5NjVmY2ExYiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9lMzg0NzQzMGYyNTU0ZGE0OGZkNmY0NDI3YWU4YTg0MiA9ICQoJzxkaXYgaWQ9Imh0bWxfZTM4NDc0MzBmMjU1NGRhNDhmZDZmNDQyN2FlOGE4NDIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRvdWdsYXN0b24sIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNDU0ZWE5YjdjMGRjNDhkOWI0ZWVmYWQyOTY1ZmNhMWIuc2V0Q29udGVudChodG1sX2UzODQ3NDMwZjI1NTRkYTQ4ZmQ2ZjQ0MjdhZThhODQyKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2Y0OTQwMjY3YzhjNDRhYzBiMTdlODU2ZjcwMjU4ZmIzLmJpbmRQb3B1cChwb3B1cF80NTRlYTliN2MwZGM0OGQ5YjRlZWZhZDI5NjVmY2ExYik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl80ODVkMjExYzA1OWQ0OTg0YjM0MzM3M2EyNzFjMzQwZiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjc0OTQ0MDc5OTc0MzMyLC03My43MTU0ODExODk5OTE0NV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF84YTQ5OWQyODNhZGM0MzE4YTc1NGNjYWQ4NWJmODZmOCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8xOTFjMGQwMTc0ZWI0NGU3OGUxOTQ1ZDhmNmYzYjgzNSA9ICQoJzxkaXYgaWQ9Imh0bWxfMTkxYzBkMDE3NGViNDRlNzhlMTk0NWQ4ZjZmM2I4MzUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkdsZW4gT2FrcywgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF84YTQ5OWQyODNhZGM0MzE4YTc1NGNjYWQ4NWJmODZmOC5zZXRDb250ZW50KGh0bWxfMTkxYzBkMDE3NGViNDRlNzhlMTk0NWQ4ZjZmM2I4MzUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNDg1ZDIxMWMwNTlkNDk4NGIzNDMzNzNhMjcxYzM0MGYuYmluZFBvcHVwKHBvcHVwXzhhNDk5ZDI4M2FkYzQzMThhNzU0Y2NhZDg1YmY4NmY4KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzNmYjAwNGE3OGZlYzQ5ZGI4YmQ3ODNiNGUzMTEwNDRiID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzI4NTczMTgxNzY2NzUsLTczLjcyMDEyODE0ODI2OTAzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzUxOTMwNDVjYThlMTQyNzM5OWU5NTk2NDg3YmE4Mzk2ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzVkZDE1YTM4NGVhYTRkOWU4MTBiMTIwNGFmZjQ5MjU1ID0gJCgnPGRpdiBpZD0iaHRtbF81ZGQxNWEzODRlYWE0ZDllODEwYjEyMDRhZmY0OTI1NSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QmVsbGVyb3NlLCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzUxOTMwNDVjYThlMTQyNzM5OWU5NTk2NDg3YmE4Mzk2LnNldENvbnRlbnQoaHRtbF81ZGQxNWEzODRlYWE0ZDllODEwYjEyMDRhZmY0OTI1NSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8zZmIwMDRhNzhmZWM0OWRiOGJkNzgzYjRlMzExMDQ0Yi5iaW5kUG9wdXAocG9wdXBfNTE5MzA0NWNhOGUxNDI3Mzk5ZTk1OTY0ODdiYTgzOTYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMDE2YTRhOWU4NTJiNDI1N2JkM2ZiNzkxYTMyYTQ4NjkgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MjI1NzgyNDQyMjgwNDYsLTczLjgyMDg3NzY0OTMzNTY2XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2NkMGY1NzQ4ZjYzYTQ4YTZhZDViZTg4MDQwMTI5NDE2ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2ZjOGU5NjViNWYwNDRlNDZhYTM2ZTZmOTJjZDAyM2VhID0gJCgnPGRpdiBpZD0iaHRtbF9mYzhlOTY1YjVmMDQ0ZTQ2YWEzNmU2ZjkyY2QwMjNlYSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+S2V3IEdhcmRlbnMgSGlsbHMsIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfY2QwZjU3NDhmNjNhNDhhNmFkNWJlODgwNDAxMjk0MTYuc2V0Q29udGVudChodG1sX2ZjOGU5NjViNWYwNDRlNDZhYTM2ZTZmOTJjZDAyM2VhKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzAxNmE0YTllODUyYjQyNTdiZDNmYjc5MWEzMmE0ODY5LmJpbmRQb3B1cChwb3B1cF9jZDBmNTc0OGY2M2E0OGE2YWQ1YmU4ODA0MDEyOTQxNik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8xM2M5MTg3YzMwMzI0OGU3YjRlMmE1YTJjYjM0MzNmYiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjczNDM5NDQ2NTMzMTMsLTczLjc4MjcxMzM3MDAzMjY0XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2M4NTEwZjNkZWI1NTQ5NTNiZjdmOTE3OGJlNWYyNjZlID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2I3NGQyNWUwMzJlNTQ0NjBiYzY0ZjY2MTYxZGU3YWYzID0gJCgnPGRpdiBpZD0iaHRtbF9iNzRkMjVlMDMyZTU0NDYwYmM2NGY2NjE2MWRlN2FmMyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RnJlc2ggTWVhZG93cywgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9jODUxMGYzZGViNTU0OTUzYmY3ZjkxNzhiZTVmMjY2ZS5zZXRDb250ZW50KGh0bWxfYjc0ZDI1ZTAzMmU1NDQ2MGJjNjRmNjYxNjFkZTdhZjMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMTNjOTE4N2MzMDMyNDhlN2I0ZTJhNWEyY2IzNDMzZmIuYmluZFBvcHVwKHBvcHVwX2M4NTEwZjNkZWI1NTQ5NTNiZjdmOTE3OGJlNWYyNjZlKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzkxNjdhOTZlMzMyZTRhZjI5ZWM4N2VhOTRmZDY2YjAwID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzEwOTM1NDcyNTIyNzEsLTczLjgxMTc0ODIyNDU4NjM0XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2M4MDFiMzlmMGQ5NDQ5ZDg4ZmNkMDk2OWUwY2UxZmU1ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2JkZWJkZWMwNzVlZjRlNjNiYTA3ZjQ4ODg0YTdjOWM1ID0gJCgnPGRpdiBpZD0iaHRtbF9iZGViZGVjMDc1ZWY0ZTYzYmEwN2Y0ODg4NGE3YzljNSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QnJpYXJ3b29kLCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2M4MDFiMzlmMGQ5NDQ5ZDg4ZmNkMDk2OWUwY2UxZmU1LnNldENvbnRlbnQoaHRtbF9iZGViZGVjMDc1ZWY0ZTYzYmEwN2Y0ODg4NGE3YzljNSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl85MTY3YTk2ZTMzMmU0YWYyOWVjODdlYTk0ZmQ2NmIwMC5iaW5kUG9wdXAocG9wdXBfYzgwMWIzOWYwZDk0NDlkODhmY2QwOTY5ZTBjZTFmZTUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOTYxZDNjNTZlY2Q2NGE3NGJiZTcyY2FiZTQ0NDRjZjggPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MDQ2NTczNjA2ODcxNywtNzMuNzk2OTAxNjU4ODgyODldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYTU2MzQ3ZGI0NDllNDMxMjhhYzg1MzZiMjZhMTU2ODggPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfODMyMjRhZjdlYzE2NDgyYzk3NjI0NzhiNDBjZDRmNWQgPSAkKCc8ZGl2IGlkPSJodG1sXzgzMjI0YWY3ZWMxNjQ4MmM5NzYyNDc4YjQwY2Q0ZjVkIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5KYW1haWNhIENlbnRlciwgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9hNTYzNDdkYjQ0OWU0MzEyOGFjODUzNmIyNmExNTY4OC5zZXRDb250ZW50KGh0bWxfODMyMjRhZjdlYzE2NDgyYzk3NjI0NzhiNDBjZDRmNWQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOTYxZDNjNTZlY2Q2NGE3NGJiZTcyY2FiZTQ0NDRjZjguYmluZFBvcHVwKHBvcHVwX2E1NjM0N2RiNDQ5ZTQzMTI4YWM4NTM2YjI2YTE1Njg4KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzM5ZDMzYmQ2ZWVjYjRjYmFiZWViNjlmZDRmMmRhNGE1ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzQ1NjE4NTcxNDE4NTUsLTczLjc1NDk0OTc2MjM0MzMyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzY3Mjg4MWYwYjllNzQzNDk5YjQ4MTExYWM0YTY3NzliID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzUzODI3N2JhZmNiMDQxMDA4ZjNmZTM4Mzg0MTI1ODBiID0gJCgnPGRpdiBpZD0iaHRtbF81MzgyNzdiYWZjYjA0MTAwOGYzZmUzODM4NDEyNTgwYiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+T2FrbGFuZCBHYXJkZW5zLCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzY3Mjg4MWYwYjllNzQzNDk5YjQ4MTExYWM0YTY3NzliLnNldENvbnRlbnQoaHRtbF81MzgyNzdiYWZjYjA0MTAwOGYzZmUzODM4NDEyNTgwYik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8zOWQzM2JkNmVlY2I0Y2JhYmVlYjY5ZmQ0ZjJkYTRhNS5iaW5kUG9wdXAocG9wdXBfNjcyODgxZjBiOWU3NDM0OTliNDgxMTFhYzRhNjc3OWIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYzgzMmU5NzIxNGMyNGFiZGE1MDhjYTA0ZjgzN2RmMzggPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MTg4OTMwOTIxNjczNTYsLTczLjczODcxNDg0NTc4NDI0XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2EzYTVjYTZjOGJjZjQ5MWE4YmIxYjU4NmUyZmNiZTRiID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzJmYzI4NTc1ZmYwYTQ5YmU4OTgxYjI4NDkwODY1NWM1ID0gJCgnPGRpdiBpZD0iaHRtbF8yZmMyODU3NWZmMGE0OWJlODk4MWIyODQ5MDg2NTVjNSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+UXVlZW5zIFZpbGxhZ2UsIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYTNhNWNhNmM4YmNmNDkxYThiYjFiNTg2ZTJmY2JlNGIuc2V0Q29udGVudChodG1sXzJmYzI4NTc1ZmYwYTQ5YmU4OTgxYjI4NDkwODY1NWM1KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2M4MzJlOTcyMTRjMjRhYmRhNTA4Y2EwNGY4MzdkZjM4LmJpbmRQb3B1cChwb3B1cF9hM2E1Y2E2YzhiY2Y0OTFhOGJiMWI1ODZlMmZjYmU0Yik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9jYjY2MzFkZjJmMDI0ODRhODkwZjU4ZTM2Y2M4YjllMiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjcxMTI0MzQ0MTkxOTA0LC03My43NTkyNTAwOTMzNTU5NF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF85YzJjMWIwYjA3ZGM0MDhlOWFmNDRlMzQyYjZkMTEyNSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8zZWM3YTMwYjA0YzY0M2RlODEzMDNhMjdkMzNkZDdiOSA9ICQoJzxkaXYgaWQ9Imh0bWxfM2VjN2EzMGIwNGM2NDNkZTgxMzAzYTI3ZDMzZGQ3YjkiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkhvbGxpcywgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF85YzJjMWIwYjA3ZGM0MDhlOWFmNDRlMzQyYjZkMTEyNS5zZXRDb250ZW50KGh0bWxfM2VjN2EzMGIwNGM2NDNkZTgxMzAzYTI3ZDMzZGQ3YjkpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfY2I2NjMxZGYyZjAyNDg0YTg5MGY1OGUzNmNjOGI5ZTIuYmluZFBvcHVwKHBvcHVwXzljMmMxYjBiMDdkYzQwOGU5YWY0NGUzNDJiNmQxMTI1KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzQ0ZWFlNjZlOGZkNDRlNDNhYzI0MDRlM2IyN2FlYmVhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjk2OTExMjUzNzg5ODg1LC03My43OTA0MjYxMzEzNTU0XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzk0NDI1ZTI0MjczNzRiYWNhOTk2YmI2MWFjMTFhYWZlID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2ZmOTdjMDhiNWU4NTQxZjZhNGVjZGNkZTIyNWRmMzhiID0gJCgnPGRpdiBpZD0iaHRtbF9mZjk3YzA4YjVlODU0MWY2YTRlY2RjZGUyMjVkZjM4YiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+U291dGggSmFtYWljYSwgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF85NDQyNWUyNDI3Mzc0YmFjYTk5NmJiNjFhYzExYWFmZS5zZXRDb250ZW50KGh0bWxfZmY5N2MwOGI1ZTg1NDFmNmE0ZWNkY2RlMjI1ZGYzOGIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNDRlYWU2NmU4ZmQ0NGU0M2FjMjQwNGUzYjI3YWViZWEuYmluZFBvcHVwKHBvcHVwXzk0NDI1ZTI0MjczNzRiYWNhOTk2YmI2MWFjMTFhYWZlKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2MyYWFmZTBiMzFiMDRjZTU5YmRiNDNlNzk4Yzk1NTQwID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjk0NDQ1Mzg1MjIzNTksLTczLjc1ODY3NjAzNzI3NzE3XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2VmNDg4MWI0N2IwMTRhZDk5MGFjYTA3ZDYzOTY2NmEzID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzQ1ZWRmZTg1ZGMwNjRhNDk4ZDBjZTkyYTg1MGU5MmRjID0gJCgnPGRpdiBpZD0iaHRtbF80NWVkZmU4NWRjMDY0YTQ5OGQwY2U5MmE4NTBlOTJkYyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+U3QuIEFsYmFucywgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9lZjQ4ODFiNDdiMDE0YWQ5OTBhY2EwN2Q2Mzk2NjZhMy5zZXRDb250ZW50KGh0bWxfNDVlZGZlODVkYzA2NGE0OThkMGNlOTJhODUwZTkyZGMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYzJhYWZlMGIzMWIwNGNlNTliZGI0M2U3OThjOTU1NDAuYmluZFBvcHVwKHBvcHVwX2VmNDg4MWI0N2IwMTRhZDk5MGFjYTA3ZDYzOTY2NmEzKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzNmNGY4YWZhMjUwYTQ1NTk4MjgzMWQ4YWZiZDhhZDcyID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjc1MjExMzk1OTE3MzMsLTczLjc3MjU4Nzg3NjIwOTA2XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzg0Nzc5NGNmZTU2NTQ0NDY5MzQyMGYzMjA5YTE2ZWJlID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2QyOTAyNjYwYTgwZDRmZjJhZTc0MmE4MjBlNDRhYWQ1ID0gJCgnPGRpdiBpZD0iaHRtbF9kMjkwMjY2MGE4MGQ0ZmYyYWU3NDJhODIwZTQ0YWFkNSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Um9jaGRhbGUsIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfODQ3Nzk0Y2ZlNTY1NDQ0NjkzNDIwZjMyMDlhMTZlYmUuc2V0Q29udGVudChodG1sX2QyOTAyNjYwYTgwZDRmZjJhZTc0MmE4MjBlNDRhYWQ1KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzNmNGY4YWZhMjUwYTQ1NTk4MjgzMWQ4YWZiZDhhZDcyLmJpbmRQb3B1cChwb3B1cF84NDc3OTRjZmU1NjU0NDQ2OTM0MjBmMzIwOWExNmViZSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl85M2QzYTRhYzE3MzE0NTM2OWE5NTA1MDMzMGFiM2Y5ZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjY2NjIzMDQ5MDM2ODU4NCwtNzMuNzYwNDIwOTI2ODIyODddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZmIzNzM3ZmVjNDY5NDdmZGEyMzdkZjllZGQ1NDJiMjEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfY2Y4NDA1MjM3NzMyNDc1NGI3NjZmZTVhNzk1MGE4NjEgPSAkKCc8ZGl2IGlkPSJodG1sX2NmODQwNTIzNzczMjQ3NTRiNzY2ZmU1YTc5NTBhODYxIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5TcHJpbmdmaWVsZCBHYXJkZW5zLCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2ZiMzczN2ZlYzQ2OTQ3ZmRhMjM3ZGY5ZWRkNTQyYjIxLnNldENvbnRlbnQoaHRtbF9jZjg0MDUyMzc3MzI0NzU0Yjc2NmZlNWE3OTUwYTg2MSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl85M2QzYTRhYzE3MzE0NTM2OWE5NTA1MDMzMGFiM2Y5ZS5iaW5kUG9wdXAocG9wdXBfZmIzNzM3ZmVjNDY5NDdmZGEyMzdkZjllZGQ1NDJiMjEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNTlhZTZhMmNhODZlNDRiYWIxYThhMWQwZGE3OTU4NTMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42OTI3NzQ2MzkxNjA4NDUsLTczLjczNTI2ODczNzA4MDI2XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2M0NTMwYTBmMjZkMjQzOTFiMWJjNzY4NTM5YWZiZGQ0ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzU4NjMzOGI4NWQ1MzRjNjNhNWJiMWRiODFjNWU2ZGRhID0gJCgnPGRpdiBpZD0iaHRtbF81ODYzMzhiODVkNTM0YzYzYTViYjFkYjgxYzVlNmRkYSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q2FtYnJpYSBIZWlnaHRzLCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2M0NTMwYTBmMjZkMjQzOTFiMWJjNzY4NTM5YWZiZGQ0LnNldENvbnRlbnQoaHRtbF81ODYzMzhiODVkNTM0YzYzYTViYjFkYjgxYzVlNmRkYSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl81OWFlNmEyY2E4NmU0NGJhYjFhOGExZDBkYTc5NTg1My5iaW5kUG9wdXAocG9wdXBfYzQ1MzBhMGYyNmQyNDM5MWIxYmM3Njg1MzlhZmJkZDQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYzI3ZDM0ZDE2NWM3NDNlZjk1ODFkYzllZTcwYjAxOWIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42NTk4MTY0MzM0MjgwODQsLTczLjczNTI2MDc5NDI4Mjc4XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2IzOWNjNTZiZjFiZTQ0YzhiOTRhOGIxMmFjMzViNDY2ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzZhYjgyZDkyOTc2OTRjODNiNjdmZjMyMGNhN2EwYzI2ID0gJCgnPGRpdiBpZD0iaHRtbF82YWI4MmQ5Mjk3Njk0YzgzYjY3ZmYzMjBjYTdhMGMyNiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Um9zZWRhbGUsIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYjM5Y2M1NmJmMWJlNDRjOGI5NGE4YjEyYWMzNWI0NjYuc2V0Q29udGVudChodG1sXzZhYjgyZDkyOTc2OTRjODNiNjdmZjMyMGNhN2EwYzI2KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2MyN2QzNGQxNjVjNzQzZWY5NTgxZGM5ZWU3MGIwMTliLmJpbmRQb3B1cChwb3B1cF9iMzljYzU2YmYxYmU0NGM4Yjk0YThiMTJhYzM1YjQ2Nik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9jZjgzYTA3YjRjOWY0NzRiYmI0Mjc1MDBiODZlZWNjNiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYwMzEzNDQzMjUwMDg5NCwtNzMuNzU0OTc5NjgwNDM4NzJdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNTg0YTQ3MGRiMzczNDg3MThlYjA5MzRlMTE4MGFiOGUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNjZmYTkzNzhkMGQyNDdjYTkzOTVkZWE4ZjJiN2ZmNWQgPSAkKCc8ZGl2IGlkPSJodG1sXzY2ZmE5Mzc4ZDBkMjQ3Y2E5Mzk1ZGVhOGYyYjdmZjVkIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5GYXIgUm9ja2F3YXksIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNTg0YTQ3MGRiMzczNDg3MThlYjA5MzRlMTE4MGFiOGUuc2V0Q29udGVudChodG1sXzY2ZmE5Mzc4ZDBkMjQ3Y2E5Mzk1ZGVhOGYyYjdmZjVkKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2NmODNhMDdiNGM5ZjQ3NGJiYjQyNzUwMGI4NmVlY2M2LmJpbmRQb3B1cChwb3B1cF81ODRhNDcwZGIzNzM0ODcxOGViMDkzNGUxMTgwYWI4ZSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8wNTdjMmMxZDRiNzc0NmJmYTIzNGVlMDhmNzUxZmY1NCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYwMzAyNjU4MzUxMjM4LC03My44MjAwNTQ4OTExMDMyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2Y3YmI3YzJkYjIwNDQ1NGE5MWFjMzgzZWYyN2M5Mzg2ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzJmZTY1ZjIyNGJkMDRkNGZiZjc4NDhlYTUwZTJhNDQxID0gJCgnPGRpdiBpZD0iaHRtbF8yZmU2NWYyMjRiZDA0ZDRmYmY3ODQ4ZWE1MGUyYTQ0MSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QnJvYWQgQ2hhbm5lbCwgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9mN2JiN2MyZGIyMDQ0NTRhOTFhYzM4M2VmMjdjOTM4Ni5zZXRDb250ZW50KGh0bWxfMmZlNjVmMjI0YmQwNGQ0ZmJmNzg0OGVhNTBlMmE0NDEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMDU3YzJjMWQ0Yjc3NDZiZmEyMzRlZTA4Zjc1MWZmNTQuYmluZFBvcHVwKHBvcHVwX2Y3YmI3YzJkYjIwNDQ1NGE5MWFjMzgzZWYyN2M5Mzg2KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2Q2YmQ4YmJhZGU5YjRmYWJiNDBkOWEyNjljZTY3Yzc5ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTU3NDAxMjg4NDU0NTIsLTczLjkyNTUxMTk2OTk0MTY4XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzhlMGYwZjg0NWY0YTQxNTI5YjczN2RmYWVlYTA2MjkxID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzljNTc0NzMyNDA5MjRmNDdhYzhjYzg5NDdlMDVjMWJjID0gJCgnPGRpdiBpZD0iaHRtbF85YzU3NDczMjQwOTI0ZjQ3YWM4Y2M4OTQ3ZTA1YzFiYyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QnJlZXp5IFBvaW50LCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzhlMGYwZjg0NWY0YTQxNTI5YjczN2RmYWVlYTA2MjkxLnNldENvbnRlbnQoaHRtbF85YzU3NDczMjQwOTI0ZjQ3YWM4Y2M4OTQ3ZTA1YzFiYyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9kNmJkOGJiYWRlOWI0ZmFiYjQwZDlhMjY5Y2U2N2M3OS5iaW5kUG9wdXAocG9wdXBfOGUwZjBmODQ1ZjRhNDE1MjliNzM3ZGZhZWVhMDYyOTEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZjhhM2Q5ZWU5M2VhNGM2MWI0YzNmMDIwZjZlMjdjZWQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43NzU5MjMwMTU2NDI4OTYsLTczLjkwMjI4OTYwMzkxNjczXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzI0ZWQ1YjJhZjY5MTQxYzM5Y2JlN2MzNTI0NzQ3ZWFjID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzkyNjk2MzAwYTk0YjRiMDY5NDQ2ZjE4ZDRjMTA3NmE1ID0gJCgnPGRpdiBpZD0iaHRtbF85MjY5NjMwMGE5NGI0YjA2OTQ0NmYxOGQ0YzEwNzZhNSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+U3RlaW53YXksIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMjRlZDViMmFmNjkxNDFjMzljYmU3YzM1MjQ3NDdlYWMuc2V0Q29udGVudChodG1sXzkyNjk2MzAwYTk0YjRiMDY5NDQ2ZjE4ZDRjMTA3NmE1KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2Y4YTNkOWVlOTNlYTRjNjFiNGMzZjAyMGY2ZTI3Y2VkLmJpbmRQb3B1cChwb3B1cF8yNGVkNWIyYWY2OTE0MWMzOWNiZTdjMzUyNDc0N2VhYyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9jZTExYTQ5NmQzMzE0Y2E5OTY2YjU3MzM2MWFkYjgzMyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjc5Mjc4MTQwMzYwMDQ4LC03My44MDQzNjQ1MTcyMDk4OF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF85YTU5ZDg1YjlmNDA0MDdiOTIyMjc0ZjM5Y2Y2ZTEwMSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF85ZWM0YzJlZmM2N2U0YjU3YTZjYjcyNGY2NjY3NDEzNiA9ICQoJzxkaXYgaWQ9Imh0bWxfOWVjNGMyZWZjNjdlNGI1N2E2Y2I3MjRmNjY2NzQxMzYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkJlZWNoaHVyc3QsIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOWE1OWQ4NWI5ZjQwNDA3YjkyMjI3NGYzOWNmNmUxMDEuc2V0Q29udGVudChodG1sXzllYzRjMmVmYzY3ZTRiNTdhNmNiNzI0ZjY2Njc0MTM2KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2NlMTFhNDk2ZDMzMTRjYTk5NjZiNTczMzYxYWRiODMzLmJpbmRQb3B1cChwb3B1cF85YTU5ZDg1YjlmNDA0MDdiOTIyMjc0ZjM5Y2Y2ZTEwMSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9iNzcwMGNlNmZjOGY0ODFmYjAyZDVhOTViNDBkNjUzZiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjc4Mjg0MjgwNjI0NTU1NCwtNzMuNzc2ODAyMjI2MjE1OF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF80ZjE4MTE4ZTcwOWE0MWNhYWM4YzUyNzE3NzRkZTY2NCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8yOWJlZjBkMTFhMzA0NGYzYTAwZDdiYTBlZjZjNTE3ZSA9ICQoJzxkaXYgaWQ9Imh0bWxfMjliZWYwZDExYTMwNDRmM2EwMGQ3YmEwZWY2YzUxN2UiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkJheSBUZXJyYWNlLCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzRmMTgxMThlNzA5YTQxY2FhYzhjNTI3MTc3NGRlNjY0LnNldENvbnRlbnQoaHRtbF8yOWJlZjBkMTFhMzA0NGYzYTAwZDdiYTBlZjZjNTE3ZSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9iNzcwMGNlNmZjOGY0ODFmYjAyZDVhOTViNDBkNjUzZi5iaW5kUG9wdXAocG9wdXBfNGYxODExOGU3MDlhNDFjYWFjOGM1MjcxNzc0ZGU2NjQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNzQ1NDdjYzM1ODY2NGFiMmI3YzUwYjZkOGY3MWMxNjcgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41OTU2NDE4MDczNjg0OTQsLTczLjc3NjEzMjgyMzkxNzA1XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2IzZmUzZDViNTUyZjRiZGJhYjFmYzIzNjI1NzIyY2JhID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2FmZGNhYjhjNmY1MjRjZjE4NjUyMjlkZWFhMjllNWE0ID0gJCgnPGRpdiBpZD0iaHRtbF9hZmRjYWI4YzZmNTI0Y2YxODY1MjI5ZGVhYTI5ZTVhNCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RWRnZW1lcmUsIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYjNmZTNkNWI1NTJmNGJkYmFiMWZjMjM2MjU3MjJjYmEuc2V0Q29udGVudChodG1sX2FmZGNhYjhjNmY1MjRjZjE4NjUyMjlkZWFhMjllNWE0KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzc0NTQ3Y2MzNTg2NjRhYjJiN2M1MGI2ZDhmNzFjMTY3LmJpbmRQb3B1cChwb3B1cF9iM2ZlM2Q1YjU1MmY0YmRiYWIxZmMyMzYyNTcyMmNiYSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl84NGI1ZWY0ZWFiNmQ0NDg1YmE1MDI0YzllNmY3NTE4YSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjU4OTE0Mzk0MzcyOTcxLC03My43OTE5OTIzMzEzNjk0M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9lNGM1M2U3MmI0ODY0NTQxYjA1MDcxMzU2NDc4NTRlMCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8yYTQ5MmVkNTZhMTg0NTFkOGNiNjk2ZmIxMjBhNWEyMiA9ICQoJzxkaXYgaWQ9Imh0bWxfMmE0OTJlZDU2YTE4NDUxZDhjYjY5NmZiMTIwYTVhMjIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkFydmVybmUsIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZTRjNTNlNzJiNDg2NDU0MWIwNTA3MTM1NjQ3ODU0ZTAuc2V0Q29udGVudChodG1sXzJhNDkyZWQ1NmExODQ1MWQ4Y2I2OTZmYjEyMGE1YTIyKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzg0YjVlZjRlYWI2ZDQ0ODViYTUwMjRjOWU2Zjc1MThhLmJpbmRQb3B1cChwb3B1cF9lNGM1M2U3MmI0ODY0NTQxYjA1MDcxMzU2NDc4NTRlMCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl85NmQ0NTg0NWZmN2Q0ZDVkYjhlODIwZDhlMzc2MWIxMiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjU4MjgwMTY5Njg0NTU4NiwtNzMuODIyMzYxMjEwODg3NTFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMmQ2NGI0MDA1YzkzNDgxMjk1Nzk5YTQ0ZmVlZjMxYjggPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZGU4ZmNjYTFjN2M2NGQwZmE2M2JiYWQ4OTQ1NzhiNDQgPSAkKCc8ZGl2IGlkPSJodG1sX2RlOGZjY2ExYzdjNjRkMGZhNjNiYmFkODk0NTc4YjQ0IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Sb2NrYXdheSBCZWFjaCwgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8yZDY0YjQwMDVjOTM0ODEyOTU3OTlhNDRmZWVmMzFiOC5zZXRDb250ZW50KGh0bWxfZGU4ZmNjYTFjN2M2NGQwZmE2M2JiYWQ4OTQ1NzhiNDQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOTZkNDU4NDVmZjdkNGQ1ZGI4ZTgyMGQ4ZTM3NjFiMTIuYmluZFBvcHVwKHBvcHVwXzJkNjRiNDAwNWM5MzQ4MTI5NTc5OWE0NGZlZWYzMWI4KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzdmMmYyNDZiZDBhZDQzNmM5MGY2YzdjZTU0Y2IxZmIwID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTcyMDM2NzMwMjE3MDE1LC03My44NTc1NDY3MjQxMDgyN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF81OWE2ODVkOTlhNTM0MWUwYTcyNDEzNjQ4YzE3OWJhNyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9jYTc2NzAyNjc5MmI0NDhiYmE4ZDVlMGY5Mjc2YWNlYyA9ICQoJzxkaXYgaWQ9Imh0bWxfY2E3NjcwMjY3OTJiNDQ4YmJhOGQ1ZTBmOTI3NmFjZWMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk5lcG9uc2l0LCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzU5YTY4NWQ5OWE1MzQxZTBhNzI0MTM2NDhjMTc5YmE3LnNldENvbnRlbnQoaHRtbF9jYTc2NzAyNjc5MmI0NDhiYmE4ZDVlMGY5Mjc2YWNlYyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl83ZjJmMjQ2YmQwYWQ0MzZjOTBmNmM3Y2U1NGNiMWZiMC5iaW5kUG9wdXAocG9wdXBfNTlhNjg1ZDk5YTUzNDFlMGE3MjQxMzY0OGMxNzliYTcpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfODFjNTU4ZGQyOWQ1NDUyMDllZjFkOTI4ZjNlNjNmZTAgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43NjQxMjYxMjI2MTQwNjYsLTczLjgxMjc2MjY5MTM1ODY2XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzA2YTZhYjM1ZDdjMzQ1MzQ5MDVjMGM3YWM1YWZjMTEyID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2MzNDk1ZjQzZjAxZjQ4ZTdhYjVkNWMwODMzMWUwZWE5ID0gJCgnPGRpdiBpZD0iaHRtbF9jMzQ5NWY0M2YwMWY0OGU3YWI1ZDVjMDgzMzFlMGVhOSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+TXVycmF5IEhpbGwsIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMDZhNmFiMzVkN2MzNDUzNDkwNWMwYzdhYzVhZmMxMTIuc2V0Q29udGVudChodG1sX2MzNDk1ZjQzZjAxZjQ4ZTdhYjVkNWMwODMzMWUwZWE5KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzgxYzU1OGRkMjlkNTQ1MjA5ZWYxZDkyOGYzZTYzZmUwLmJpbmRQb3B1cChwb3B1cF8wNmE2YWIzNWQ3YzM0NTM0OTA1YzBjN2FjNWFmYzExMik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9lOGZiYjkzNzYyYjM0ZDAyYjU1NjBmMTY1NmNkMjM3YSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjc0MTM3ODQyMTk0NTQzNCwtNzMuNzA4ODQ3MDU4ODkyNDZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMGUwYjVlM2FmMTVjNGVjZGExMGE1ODM0ZWM3NGRiY2MgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOTI2OGYwYmI1OWU5NGFkNjg1MjQ0MmQzMDlmMTliNTUgPSAkKCc8ZGl2IGlkPSJodG1sXzkyNjhmMGJiNTllOTRhZDY4NTI0NDJkMzA5ZjE5YjU1IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5GbG9yYWwgUGFyaywgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8wZTBiNWUzYWYxNWM0ZWNkYTEwYTU4MzRlYzc0ZGJjYy5zZXRDb250ZW50KGh0bWxfOTI2OGYwYmI1OWU5NGFkNjg1MjQ0MmQzMDlmMTliNTUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZThmYmI5Mzc2MmIzNGQwMmI1NTYwZjE2NTZjZDIzN2EuYmluZFBvcHVwKHBvcHVwXzBlMGI1ZTNhZjE1YzRlY2RhMTBhNTgzNGVjNzRkYmNjKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzMxYzRjNzE4NjNlOTQyNDU5YzU2ZTlmMjIwMWQ3YTQ0ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzIwOTU3MjA3NjQ0NCwtNzMuNzY3MTQxNjY3MTQ3MjldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMzFkNDAxODdlNTNmNDAwMmIwOGY0MTdjM2E5YjU5NGYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMGM3YzMyMjVkMDJlNDI2N2JkNTUxMDk4OTE4NzNjMDcgPSAkKCc8ZGl2IGlkPSJodG1sXzBjN2MzMjI1ZDAyZTQyNjdiZDU1MTA5ODkxODczYzA3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Ib2xsaXN3b29kLCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzMxZDQwMTg3ZTUzZjQwMDJiMDhmNDE3YzNhOWI1OTRmLnNldENvbnRlbnQoaHRtbF8wYzdjMzIyNWQwMmU0MjY3YmQ1NTEwOTg5MTg3M2MwNyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8zMWM0YzcxODYzZTk0MjQ1OWM1NmU5ZjIyMDFkN2E0NC5iaW5kUG9wdXAocG9wdXBfMzFkNDAxODdlNTNmNDAwMmIwOGY0MTdjM2E5YjU5NGYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOGYxZWRiZmRiYTAxNDcyOTkwNmY4MDI3YmJjNmEwNjcgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MTY4MDQ4MzAxNDYxMywtNzMuNzg3MjI2OTY5MzY2Nl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9lMjRiNTFmNzFmM2U0MjhkOGQwNmNiNTE1OWE0ZjBkYyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9jZWI3ODczYTEyNGI0OWNjYTNiMmQ1YzE0NWJiZTA4ZiA9ICQoJzxkaXYgaWQ9Imh0bWxfY2ViNzg3M2ExMjRiNDljY2EzYjJkNWMxNDViYmUwOGYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkphbWFpY2EgRXN0YXRlcywgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9lMjRiNTFmNzFmM2U0MjhkOGQwNmNiNTE1OWE0ZjBkYy5zZXRDb250ZW50KGh0bWxfY2ViNzg3M2ExMjRiNDljY2EzYjJkNWMxNDViYmUwOGYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOGYxZWRiZmRiYTAxNDcyOTkwNmY4MDI3YmJjNmEwNjcuYmluZFBvcHVwKHBvcHVwX2UyNGI1MWY3MWYzZTQyOGQ4ZDA2Y2I1MTU5YTRmMGRjKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2Q2MDI5N2U2YzA4NjRlMzU5MzE3NTZmNWMxYjRlYjY5ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzQ0NTcyMzA5Mjg2NywtNzMuODI1ODA5MTUxMTA1NTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZmExNWVjMGI1MWFkNGFmYmI5MzU2Mzg0MjRkMWY1YjkgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZDZkNTg5ZDVhZWE0NDNmMjhlOGQwNzE3MTM0NWU5MmMgPSAkKCc8ZGl2IGlkPSJodG1sX2Q2ZDU4OWQ1YWVhNDQzZjI4ZThkMDcxNzEzNDVlOTJjIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5RdWVlbnNib3JvIEhpbGwsIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZmExNWVjMGI1MWFkNGFmYmI5MzU2Mzg0MjRkMWY1Yjkuc2V0Q29udGVudChodG1sX2Q2ZDU4OWQ1YWVhNDQzZjI4ZThkMDcxNzEzNDVlOTJjKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2Q2MDI5N2U2YzA4NjRlMzU5MzE3NTZmNWMxYjRlYjY5LmJpbmRQb3B1cChwb3B1cF9mYTE1ZWMwYjUxYWQ0YWZiYjkzNTYzODQyNGQxZjViOSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl84OTM5OTBlYTQ5NTA0OTFiODg2ZDA2ODkyN2ExZjNhYSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjcyMzgyNDkwMTgyOTIwNCwtNzMuNzk3NjAzMDA5MTI2NzJdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNjk5MDBkYWEyZjdmNGVjZmFlMTNkNDRmYjZlNjA1NjQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMzQxZjYxMGMxNjIzNGI5NzljYjJhNzY1ZGFhNWMwZDMgPSAkKCc8ZGl2IGlkPSJodG1sXzM0MWY2MTBjMTYyMzRiOTc5Y2IyYTc2NWRhYTVjMGQzIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5IaWxsY3Jlc3QsIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNjk5MDBkYWEyZjdmNGVjZmFlMTNkNDRmYjZlNjA1NjQuc2V0Q29udGVudChodG1sXzM0MWY2MTBjMTYyMzRiOTc5Y2IyYTc2NWRhYTVjMGQzKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzg5Mzk5MGVhNDk1MDQ5MWI4ODZkMDY4OTI3YTFmM2FhLmJpbmRQb3B1cChwb3B1cF82OTkwMGRhYTJmN2Y0ZWNmYWUxM2Q0NGZiNmU2MDU2NCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8yM2Y2MzhhZWEwOTk0MDI3OWUyMzFiMWY1NzkwZWUwYyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjc2MTcwNDUyNjA1NDE0NiwtNzMuOTMxNTc1MDYwNzI4NzhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZmFkMmUxOWRhZjlkNGUyNGFkODAxMmRmZWI1ODFiY2QgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOGU5NGMyZmU2ZTZmNDRhMzllYzgwNTY1ODRhNjY4ZDEgPSAkKCc8ZGl2IGlkPSJodG1sXzhlOTRjMmZlNmU2ZjQ0YTM5ZWM4MDU2NTg0YTY2OGQxIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5SYXZlbnN3b29kLCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2ZhZDJlMTlkYWY5ZDRlMjRhZDgwMTJkZmViNTgxYmNkLnNldENvbnRlbnQoaHRtbF84ZTk0YzJmZTZlNmY0NGEzOWVjODA1NjU4NGE2NjhkMSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8yM2Y2MzhhZWEwOTk0MDI3OWUyMzFiMWY1NzkwZWUwYy5iaW5kUG9wdXAocG9wdXBfZmFkMmUxOWRhZjlkNGUyNGFkODAxMmRmZWI1ODFiY2QpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZTRlZTQ4OGRiMDk4NGQzMWFjYmYxNTc5MWMwNGQ0MzcgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42NjM5MTg0MTkyNTEzOSwtNzMuODQ5NjM3ODI0MDI0NDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfM2YxNWNjNGQ1MzNkNDFiYTlhNjg3MjE1M2RiZjAwOTIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZTIxNTE0MmEzM2Y3NGE1Yjg0YWVmNmFlMDAzMjVhN2QgPSAkKCc8ZGl2IGlkPSJodG1sX2UyMTUxNDJhMzNmNzRhNWI4NGFlZjZhZTAwMzI1YTdkIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5MaW5kZW53b29kLCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzNmMTVjYzRkNTMzZDQxYmE5YTY4NzIxNTNkYmYwMDkyLnNldENvbnRlbnQoaHRtbF9lMjE1MTQyYTMzZjc0YTViODRhZWY2YWUwMDMyNWE3ZCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9lNGVlNDg4ZGIwOTg0ZDMxYWNiZjE1NzkxYzA0ZDQzNy5iaW5kUG9wdXAocG9wdXBfM2YxNWNjNGQ1MzNkNDFiYTlhNjg3MjE1M2RiZjAwOTIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNDNkYjJiZjdiYmYzNDQzNDkxZTFiOWIzZGIyZjA4MWIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42Njc4ODM4OTY2MDI0NywtNzMuNzQwMjU2MDc5ODk4MjJdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZjhkZjU4NGZhYjgzNGI0Mzg1ZTY3MDgxODE3NWUyODQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYjYzZjJmZjg4YjUwNGY3NWE2MmQ2MTZjNTc5N2E5ODEgPSAkKCc8ZGl2IGlkPSJodG1sX2I2M2YyZmY4OGI1MDRmNzVhNjJkNjE2YzU3OTdhOTgxIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5MYXVyZWx0b24sIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZjhkZjU4NGZhYjgzNGI0Mzg1ZTY3MDgxODE3NWUyODQuc2V0Q29udGVudChodG1sX2I2M2YyZmY4OGI1MDRmNzVhNjJkNjE2YzU3OTdhOTgxKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzQzZGIyYmY3YmJmMzQ0MzQ5MWUxYjliM2RiMmYwODFiLmJpbmRQb3B1cChwb3B1cF9mOGRmNTg0ZmFiODM0YjQzODVlNjcwODE4MTc1ZTI4NCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl80NzU4MzIxZWZiMWU0YWQzYWY5ZGVmNjJjNzljNzlkZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjczNjA3NDU3MDgzMDc5NSwtNzMuODYyNTI0NzE0MTM3NF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF82ZDI4ZmVkN2ZlM2I0ZWIzYTQ4NThmMDM3MGE3MzY2NyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8zMGMwZjEyYjJkMjc0MGEyYmZiNDUwMTE0YmVkODYxMSA9ICQoJzxkaXYgaWQ9Imh0bWxfMzBjMGYxMmIyZDI3NDBhMmJmYjQ1MDExNGJlZDg2MTEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkxlZnJhayBDaXR5LCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzZkMjhmZWQ3ZmUzYjRlYjNhNDg1OGYwMzcwYTczNjY3LnNldENvbnRlbnQoaHRtbF8zMGMwZjEyYjJkMjc0MGEyYmZiNDUwMTE0YmVkODYxMSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl80NzU4MzIxZWZiMWU0YWQzYWY5ZGVmNjJjNzljNzlkZS5iaW5kUG9wdXAocG9wdXBfNmQyOGZlZDdmZTNiNGViM2E0ODU4ZjAzNzBhNzM2NjcpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZGM4MjkyM2FhNzZjNGI4MmIwMThiMzRjMzc3NDBmZTMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41NzYxNTU1NjU0MzEwOSwtNzMuODU0MDE3NTAzOTI1Ml0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8xNjhiODkyNDA0M2E0NzY1ODdjM2NiZGRlYzlkNzUwMSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9mYjQxM2VhMzlhOTQ0ZDUyYTRkODI2N2M4NDdiMTZjYiA9ICQoJzxkaXYgaWQ9Imh0bWxfZmI0MTNlYTM5YTk0NGQ1MmE0ZDgyNjdjODQ3YjE2Y2IiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkJlbGxlIEhhcmJvciwgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8xNjhiODkyNDA0M2E0NzY1ODdjM2NiZGRlYzlkNzUwMS5zZXRDb250ZW50KGh0bWxfZmI0MTNlYTM5YTk0NGQ1MmE0ZDgyNjdjODQ3YjE2Y2IpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZGM4MjkyM2FhNzZjNGI4MmIwMThiMzRjMzc3NDBmZTMuYmluZFBvcHVwKHBvcHVwXzE2OGI4OTI0MDQzYTQ3NjU4N2MzY2JkZGVjOWQ3NTAxKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2U2MGRmN2IzYWVjNjQ1ZGRiM2JlNDdlYjU2MWMxZmJlID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTgwMzQyOTU2NDYxMzEsLTczLjg0MTUzMzcwMjI2MTg2XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2FkZTQ2NzViYTBkNjQwMGRiN2E3NDBhODQ3YTY1NjY2ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2EyZDMxMzNiZjk1ODQxYThhMjVjMDdjM2I4OTFiZjk0ID0gJCgnPGRpdiBpZD0iaHRtbF9hMmQzMTMzYmY5NTg0MWE4YTI1YzA3YzNiODkxYmY5NCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Um9ja2F3YXkgUGFyaywgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9hZGU0Njc1YmEwZDY0MDBkYjdhNzQwYTg0N2E2NTY2Ni5zZXRDb250ZW50KGh0bWxfYTJkMzEzM2JmOTU4NDFhOGEyNWMwN2MzYjg5MWJmOTQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZTYwZGY3YjNhZWM2NDVkZGIzYmU0N2ViNTYxYzFmYmUuYmluZFBvcHVwKHBvcHVwX2FkZTQ2NzViYTBkNjQwMGRiN2E3NDBhODQ3YTY1NjY2KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzY0NzVmN2RjMWE0NTRlYWVhNjcwOGQ0ODE1YTU5MDhjID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTk3NzEwNjE1NjU3NjgsLTczLjc5NjY0NzUwODQ0MDQ3XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzJlMmY1MzBhZjkyNDRkNDA4OWY0NWU5N2VhZTU0NzlmID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzI0ZDBkMTlkOTMyMTRkNzM5ODEwZjlmMjBiM2ViMWMwID0gJCgnPGRpdiBpZD0iaHRtbF8yNGQwZDE5ZDkzMjE0ZDczOTgxMGY5ZjIwYjNlYjFjMCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+U29tZXJ2aWxsZSwgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8yZTJmNTMwYWY5MjQ0ZDQwODlmNDVlOTdlYWU1NDc5Zi5zZXRDb250ZW50KGh0bWxfMjRkMGQxOWQ5MzIxNGQ3Mzk4MTBmOWYyMGIzZWIxYzApOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNjQ3NWY3ZGMxYTQ1NGVhZWE2NzA4ZDQ4MTVhNTkwOGMuYmluZFBvcHVwKHBvcHVwXzJlMmY1MzBhZjkyNDRkNDA4OWY0NWU5N2VhZTU0NzlmKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2MwMGYxNjNlYmFmZDQxNDdhZDMyNTM2ZjgyM2JmYjlhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjYwMDAzMjI3MzM2MTMsLTczLjc1MTc1MzEwNzMxMTUzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzE2YjE0NjgwZTViOTQ2MDNhOWZiN2ExNDA3NTJmZDViID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2IzYjYxZjA2NmJlZDQwNWZhYjYyZTA4OWQzM2VmZTA2ID0gJCgnPGRpdiBpZD0iaHRtbF9iM2I2MWYwNjZiZWQ0MDVmYWI2MmUwODlkMzNlZmUwNiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QnJvb2t2aWxsZSwgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8xNmIxNDY4MGU1Yjk0NjAzYTlmYjdhMTQwNzUyZmQ1Yi5zZXRDb250ZW50KGh0bWxfYjNiNjFmMDY2YmVkNDA1ZmFiNjJlMDg5ZDMzZWZlMDYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYzAwZjE2M2ViYWZkNDE0N2FkMzI1MzZmODIzYmZiOWEuYmluZFBvcHVwKHBvcHVwXzE2YjE0NjgwZTViOTQ2MDNhOWZiN2ExNDA3NTJmZDViKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzQyZTA1Y2JjZDQ2NjQ4ZmViMWFlMjg3ZThjMmU3Y2ZiID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzMzMDE0MDQwMjc4MzQsLTczLjczODg5MTk4OTEyNDgxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2YyZTg2ZTVjOTY4MzQ1MGQ4YmY3OTVlMDc5NDk2OWQ1ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzhhODY1YmZjNzUxZTQ0NWJiMTA1Y2Q2Zjc1OGFiMWM0ID0gJCgnPGRpdiBpZD0iaHRtbF84YTg2NWJmYzc1MWU0NDViYjEwNWNkNmY3NThhYjFjNCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QmVsbGFpcmUsIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZjJlODZlNWM5NjgzNDUwZDhiZjc5NWUwNzk0OTY5ZDUuc2V0Q29udGVudChodG1sXzhhODY1YmZjNzUxZTQ0NWJiMTA1Y2Q2Zjc1OGFiMWM0KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzQyZTA1Y2JjZDQ2NjQ4ZmViMWFlMjg3ZThjMmU3Y2ZiLmJpbmRQb3B1cChwb3B1cF9mMmU4NmU1Yzk2ODM0NTBkOGJmNzk1ZTA3OTQ5NjlkNSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8xMzExZGJhMjk0MzA0YTBiODRmYWE2ODIwYmU2ZThlNyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjc1NDA3MDk5OTA0ODksLTczLjg1NzUxNzkwNjc2NDQ3XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2U3YmU4N2NkOGMzMDRmMWZhZmI3YjQzNDI5MWQ5ODY0ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzM0MDg4ODFiNjE3YjRjM2NhY2M2YzZiMWJhMjY3YTQ5ID0gJCgnPGRpdiBpZD0iaHRtbF8zNDA4ODgxYjYxN2I0YzNjYWNjNmM2YjFiYTI2N2E0OSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Tm9ydGggQ29yb25hLCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2U3YmU4N2NkOGMzMDRmMWZhZmI3YjQzNDI5MWQ5ODY0LnNldENvbnRlbnQoaHRtbF8zNDA4ODgxYjYxN2I0YzNjYWNjNmM2YjFiYTI2N2E0OSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8xMzExZGJhMjk0MzA0YTBiODRmYWE2ODIwYmU2ZThlNy5iaW5kUG9wdXAocG9wdXBfZTdiZTg3Y2Q4YzMwNGYxZmFmYjdiNDM0MjkxZDk4NjQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYTJkYTdmMGI3Zjk4NDI4MThkNWYwMWU5MWU1MDdkMzkgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MTQ2MTEwODE1MTE3LC03My44NDEwMjIxMTIzNDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2JiYjY3ZDNjMGU3MDRjZWI5YjMyODBmNTFlYmQxZGIxID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzc1YmVlMWEwZWFlZTQ5MGNhOWMyMjZkZmNlMWYyNDUyID0gJCgnPGRpdiBpZD0iaHRtbF83NWJlZTFhMGVhZWU0OTBjYTljMjI2ZGZjZTFmMjQ1MiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Rm9yZXN0IEhpbGxzIEdhcmRlbnMsIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYmJiNjdkM2MwZTcwNGNlYjliMzI4MGY1MWViZDFkYjEuc2V0Q29udGVudChodG1sXzc1YmVlMWEwZWFlZTQ5MGNhOWMyMjZkZmNlMWYyNDUyKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2EyZGE3ZjBiN2Y5ODQyODE4ZDVmMDFlOTFlNTA3ZDM5LmJpbmRQb3B1cChwb3B1cF9iYmI2N2QzYzBlNzA0Y2ViOWIzMjgwZjUxZWJkMWRiMSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl85NWZiMzBkYjlkZDU0ZWVkYTYyNzNjNGQyYmY3MzBiZCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjY0NDk4MTU3MTAwNDQsLTc0LjA3OTM1MzEyNTEyNzk3XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzI5NTUxNjQ4YjNiZTRlNTZiM2YxODVjOThiMGFkOTZiID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2FmMjUwMGRhMTZmZDRhOTU4NWI2YjMzNGE5OGZkMDViID0gJCgnPGRpdiBpZD0iaHRtbF9hZjI1MDBkYTE2ZmQ0YTk1ODViNmIzMzRhOThmZDA1YiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+U3QuIEdlb3JnZSwgU3RhdGVuIElzbGFuZDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMjk1NTE2NDhiM2JlNGU1NmIzZjE4NWM5OGIwYWQ5NmIuc2V0Q29udGVudChodG1sX2FmMjUwMGRhMTZmZDRhOTU4NWI2YjMzNGE5OGZkMDViKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzk1ZmIzMGRiOWRkNTRlZWRhNjI3M2M0ZDJiZjczMGJkLmJpbmRQb3B1cChwb3B1cF8yOTU1MTY0OGIzYmU0ZTU2YjNmMTg1Yzk4YjBhZDk2Yik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8zMjEzOTkwOGU4M2M0Y2Y3YTcwOGJlMTEzYjNhODg2MiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjY0MDYxNDU1OTEzNTExLC03NC4wODcwMTY1MDUxNjYyNV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9mYjMwMTI2MDVlNDc0YjQ5OGY2YmUxM2VhZjkwNDliNyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF85NjY3ZDc4NGI1Y2I0OWMzYWNmMmM2NTM1MTQ5ZmU1OCA9ICQoJzxkaXYgaWQ9Imh0bWxfOTY2N2Q3ODRiNWNiNDljM2FjZjJjNjUzNTE0OWZlNTgiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk5ldyBCcmlnaHRvbiwgU3RhdGVuIElzbGFuZDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZmIzMDEyNjA1ZTQ3NGI0OThmNmJlMTNlYWY5MDQ5Yjcuc2V0Q29udGVudChodG1sXzk2NjdkNzg0YjVjYjQ5YzNhY2YyYzY1MzUxNDlmZTU4KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzMyMTM5OTA4ZTgzYzRjZjdhNzA4YmUxMTNiM2E4ODYyLmJpbmRQb3B1cChwb3B1cF9mYjMwMTI2MDVlNDc0YjQ5OGY2YmUxM2VhZjkwNDliNyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8wYzEzZGM3N2U3NTE0MDJmOGM1NWQ4NzQ5ZjhkOTdjZCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYyNjkyNzYyNTM4MTc2LC03NC4wNzc5MDE5MjY2MDA2Nl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9jY2Q1ZWEzNDIzOGU0YTllOWZlZTg3YWYzODM3ZjNlZSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF84ZWJhOTAwOGY3ZTQ0NWM3OTVhODgyNGI1ZWI5NTk1MSA9ICQoJzxkaXYgaWQ9Imh0bWxfOGViYTkwMDhmN2U0NDVjNzk1YTg4MjRiNWViOTU5NTEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlN0YXBsZXRvbiwgU3RhdGVuIElzbGFuZDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfY2NkNWVhMzQyMzhlNGE5ZTlmZWU4N2FmMzgzN2YzZWUuc2V0Q29udGVudChodG1sXzhlYmE5MDA4ZjdlNDQ1Yzc5NWE4ODI0YjVlYjk1OTUxKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzBjMTNkYzc3ZTc1MTQwMmY4YzU1ZDg3NDlmOGQ5N2NkLmJpbmRQb3B1cChwb3B1cF9jY2Q1ZWEzNDIzOGU0YTllOWZlZTg3YWYzODM3ZjNlZSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl81YWRiYTFkMjNmY2U0MTJiOTQ3ODE2MDA5NTI5YTdmNCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYxNTMwNDk0NjUyNzYxLC03NC4wNjk4MDUyNjcxNjE0MV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF81OTc4NmE5YmNjNmU0OTk2OTg2OWU1OWNiNTNjMDY0OSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9iMTlmOWU4ZDQ5YTU0YWE5OWNlYjhkNTZhMjM2NzNjMSA9ICQoJzxkaXYgaWQ9Imh0bWxfYjE5ZjllOGQ0OWE1NGFhOTljZWI4ZDU2YTIzNjczYzEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlJvc2ViYW5rLCBTdGF0ZW4gSXNsYW5kPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF81OTc4NmE5YmNjNmU0OTk2OTg2OWU1OWNiNTNjMDY0OS5zZXRDb250ZW50KGh0bWxfYjE5ZjllOGQ0OWE1NGFhOTljZWI4ZDU2YTIzNjczYzEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNWFkYmExZDIzZmNlNDEyYjk0NzgxNjAwOTUyOWE3ZjQuYmluZFBvcHVwKHBvcHVwXzU5Nzg2YTliY2M2ZTQ5OTY5ODY5ZTU5Y2I1M2MwNjQ5KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2JjNjBiZjIzY2M1ZjQyMmFhZDM2OGY1N2IwOTE0MzgzID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjMxODc4OTI2NTQ2MDcsLTc0LjEwNzE4MTc4MjY1NjFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfOTk2Y2RhMzlkNWZkNDc0MmFmZWFmZmVkNDk2MDYzYzMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMzQ2ZmVjYWQ1N2I3NGJmZGE2MGFkNjIzMzNmMTVjZGIgPSAkKCc8ZGl2IGlkPSJodG1sXzM0NmZlY2FkNTdiNzRiZmRhNjBhZDYyMzMzZjE1Y2RiIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5XZXN0IEJyaWdodG9uLCBTdGF0ZW4gSXNsYW5kPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF85OTZjZGEzOWQ1ZmQ0NzQyYWZlYWZmZWQ0OTYwNjNjMy5zZXRDb250ZW50KGh0bWxfMzQ2ZmVjYWQ1N2I3NGJmZGE2MGFkNjIzMzNmMTVjZGIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYmM2MGJmMjNjYzVmNDIyYWFkMzY4ZjU3YjA5MTQzODMuYmluZFBvcHVwKHBvcHVwXzk5NmNkYTM5ZDVmZDQ3NDJhZmVhZmZlZDQ5NjA2M2MzKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzkwNjg4ZjVmYzY0NzQ1OGNiOTYzMzA5MDkxODlhOGQ3ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjI0MTg0NzkxMzEzMDA2LC03NC4wODcyNDgxOTk4MzcyOV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF83MjllZDAwODZkZWM0MTQyOTkwMDRkNGViNzNjMTljZCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9kYzQ1ZjhlYmZlNGQ0MDZlOWMzNDhjZWU2NGQxYTFjNiA9ICQoJzxkaXYgaWQ9Imh0bWxfZGM0NWY4ZWJmZTRkNDA2ZTljMzQ4Y2VlNjRkMWExYzYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkdyeW1lcyBIaWxsLCBTdGF0ZW4gSXNsYW5kPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF83MjllZDAwODZkZWM0MTQyOTkwMDRkNGViNzNjMTljZC5zZXRDb250ZW50KGh0bWxfZGM0NWY4ZWJmZTRkNDA2ZTljMzQ4Y2VlNjRkMWExYzYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOTA2ODhmNWZjNjQ3NDU4Y2I5NjMzMDkwOTE4OWE4ZDcuYmluZFBvcHVwKHBvcHVwXzcyOWVkMDA4NmRlYzQxNDI5OTAwNGQ0ZWI3M2MxOWNkKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzg3ZDlkNjYxNjU0MzRhYzRiNDExNzZlZTU5MWZkZTY1ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTk3MDY4NTE4MTQ2NzMsLTc0LjExMTMyODgxODAwODhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZDdkZTczZTRiMzYzNGZhOTgzNzFjODBkOWIxZmIwMDIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMWY2MjY0ODE0MDdhNDIxNWIxOGQxNzg0MjgwN2Y1MDUgPSAkKCc8ZGl2IGlkPSJodG1sXzFmNjI2NDgxNDA3YTQyMTViMThkMTc4NDI4MDdmNTA1IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Ub2R0IEhpbGwsIFN0YXRlbiBJc2xhbmQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2Q3ZGU3M2U0YjM2MzRmYTk4MzcxYzgwZDliMWZiMDAyLnNldENvbnRlbnQoaHRtbF8xZjYyNjQ4MTQwN2E0MjE1YjE4ZDE3ODQyODA3ZjUwNSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl84N2Q5ZDY2MTY1NDM0YWM0YjQxMTc2ZWU1OTFmZGU2NS5iaW5kUG9wdXAocG9wdXBfZDdkZTczZTRiMzYzNGZhOTgzNzFjODBkOWIxZmIwMDIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNTM4ZDM3ZDBhZGEwNGZhMjk3MmMxMzNlNjA3Yjc1NjUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41ODAyNDc0MTM1MDk1NiwtNzQuMDc5NTUyOTI1Mzk4Ml0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9mNTFhODBmMjdkY2E0YjcwYTJjNjljMmVhOTNhMGY4MiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF80ZDg0ZjlkZGU4Mjc0OGE0ODYzMDk5OGNhZTZjN2MxMCA9ICQoJzxkaXYgaWQ9Imh0bWxfNGQ4NGY5ZGRlODI3NDhhNDg2MzA5OThjYWU2YzdjMTAiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlNvdXRoIEJlYWNoLCBTdGF0ZW4gSXNsYW5kPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9mNTFhODBmMjdkY2E0YjcwYTJjNjljMmVhOTNhMGY4Mi5zZXRDb250ZW50KGh0bWxfNGQ4NGY5ZGRlODI3NDhhNDg2MzA5OThjYWU2YzdjMTApOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNTM4ZDM3ZDBhZGEwNGZhMjk3MmMxMzNlNjA3Yjc1NjUuYmluZFBvcHVwKHBvcHVwX2Y1MWE4MGYyN2RjYTRiNzBhMmM2OWMyZWE5M2EwZjgyKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2QzYWZkMmQxMTJmNDRhZTA5ZTM0MTljMTM2OGUxZTQ0ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjMzNjY5MzA1NTQzNjUsLTc0LjEyOTQzNDI2Nzk3MDA4XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzkzMmQzODY0MDZjNDQ5ODViZTA5OTgyMGNjYmQ2M2RkID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzUyNWE4YjUxZjkzMzQ5N2RiYTVhNzIxNGRmZGVjZmJkID0gJCgnPGRpdiBpZD0iaHRtbF81MjVhOGI1MWY5MzM0OTdkYmE1YTcyMTRkZmRlY2ZiZCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+UG9ydCBSaWNobW9uZCwgU3RhdGVuIElzbGFuZDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOTMyZDM4NjQwNmM0NDk4NWJlMDk5ODIwY2NiZDYzZGQuc2V0Q29udGVudChodG1sXzUyNWE4YjUxZjkzMzQ5N2RiYTVhNzIxNGRmZGVjZmJkKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2QzYWZkMmQxMTJmNDRhZTA5ZTM0MTljMTM2OGUxZTQ0LmJpbmRQb3B1cChwb3B1cF85MzJkMzg2NDA2YzQ0OTg1YmUwOTk4MjBjY2JkNjNkZCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl80MTc4YTA3NjBiMTE0N2U0YjcwZGYwZjMyNDA3MWM5NSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYzMjU0NjM5MDQ4MTEyNCwtNzQuMTUwMDg1MzcwNDY5ODFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYmZlZmI4YmFmNjkwNDdmNGFmNzdjYTI0MzA0ZmQ1ZGMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNzVhM2JkZDc4ZDQ4NGJjOWEzYjlmNGY4NjQwNGU3YzYgPSAkKCc8ZGl2IGlkPSJodG1sXzc1YTNiZGQ3OGQ0ODRiYzlhM2I5ZjRmODY0MDRlN2M2IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5NYXJpbmVyJiMzOTtzIEhhcmJvciwgU3RhdGVuIElzbGFuZDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYmZlZmI4YmFmNjkwNDdmNGFmNzdjYTI0MzA0ZmQ1ZGMuc2V0Q29udGVudChodG1sXzc1YTNiZGQ3OGQ0ODRiYzlhM2I5ZjRmODY0MDRlN2M2KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzQxNzhhMDc2MGIxMTQ3ZTRiNzBkZjBmMzI0MDcxYzk1LmJpbmRQb3B1cChwb3B1cF9iZmVmYjhiYWY2OTA0N2Y0YWY3N2NhMjQzMDRmZDVkYyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8yM2U4YTExNzE5ZGU0MmQ2OTAxZDlkOTcxODM2YjRlNSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYzOTY4Mjk3ODQ1NTQyLC03NC4xNzQ2NDUzMjk5MzU0Ml0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF82ZTlhMjgwY2E2Y2M0ZTQwYTVkOGMzMGE0ZGVhMGI0YSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8zNWMwNWVlNGFhOGQ0OTE0OThlOTA2NjVjZWMwMTBiOSA9ICQoJzxkaXYgaWQ9Imh0bWxfMzVjMDVlZTRhYThkNDkxNDk4ZTkwNjY1Y2VjMDEwYjkiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlBvcnQgSXZvcnksIFN0YXRlbiBJc2xhbmQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzZlOWEyODBjYTZjYzRlNDBhNWQ4YzMwYTRkZWEwYjRhLnNldENvbnRlbnQoaHRtbF8zNWMwNWVlNGFhOGQ0OTE0OThlOTA2NjVjZWMwMTBiOSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8yM2U4YTExNzE5ZGU0MmQ2OTAxZDlkOTcxODM2YjRlNS5iaW5kUG9wdXAocG9wdXBfNmU5YTI4MGNhNmNjNGU0MGE1ZDhjMzBhNGRlYTBiNGEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZjNmN2VlNzAyMTIxNDQ1YWJjMWYwODE4NTAwNjk3ZmEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42MTMzMzU5Mzc2Njc0MiwtNzQuMTE5MTgwNTg1MzQ4NDJdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZDY4NTM2ZTc1NDRlNDlmZmJjMDcwNTU2MTIwMjFmYjIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfODkwNTVhZmJkNzFhNDQxZmIxNTdjNzNhNTlhMzhjZWYgPSAkKCc8ZGl2IGlkPSJodG1sXzg5MDU1YWZiZDcxYTQ0MWZiMTU3YzczYTU5YTM4Y2VmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DYXN0bGV0b24gQ29ybmVycywgU3RhdGVuIElzbGFuZDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZDY4NTM2ZTc1NDRlNDlmZmJjMDcwNTU2MTIwMjFmYjIuc2V0Q29udGVudChodG1sXzg5MDU1YWZiZDcxYTQ0MWZiMTU3YzczYTU5YTM4Y2VmKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2YzZjdlZTcwMjEyMTQ0NWFiYzFmMDgxODUwMDY5N2ZhLmJpbmRQb3B1cChwb3B1cF9kNjg1MzZlNzU0NGU0OWZmYmMwNzA1NTYxMjAyMWZiMik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8yOWY1YWQxMjJhYzY0YTM4OWVkYzMzMDg2MzAyYjA2ZCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjU5NDI1MjM3OTE2MTY5NSwtNzQuMTY0OTYwMzEzMjk4MjddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNjdkMGJkZWMwZTI5NDM1MDhkZGE2ZDRkZTk5YWU2MDUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfM2Y1YzFlZGRhNjI3NDY0OTkwOTQ1ZmZlMDMzYzgxZjUgPSAkKCc8ZGl2IGlkPSJodG1sXzNmNWMxZWRkYTYyNzQ2NDk5MDk0NWZmZTAzM2M4MWY1IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5OZXcgU3ByaW5ndmlsbGUsIFN0YXRlbiBJc2xhbmQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzY3ZDBiZGVjMGUyOTQzNTA4ZGRhNmQ0ZGU5OWFlNjA1LnNldENvbnRlbnQoaHRtbF8zZjVjMWVkZGE2Mjc0NjQ5OTA5NDVmZmUwMzNjODFmNSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8yOWY1YWQxMjJhYzY0YTM4OWVkYzMzMDg2MzAyYjA2ZC5iaW5kUG9wdXAocG9wdXBfNjdkMGJkZWMwZTI5NDM1MDhkZGE2ZDRkZTk5YWU2MDUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYjVmZWFhMTBjMmUyNDNmNTk2MGRhOTU5ZDkxYjc4MjQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41ODYzMTM3NTEwMzI4MSwtNzQuMTkwNzM3MTc1MzgxMTZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfN2ZlYjFkMGIzNGY5NDIwZDlhY2IzZTljNDJlMDNhYzggPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZDdiOTYwMzVhYWIwNDNlODhkZDVmNmNlNDExYTc1ODIgPSAkKCc8ZGl2IGlkPSJodG1sX2Q3Yjk2MDM1YWFiMDQzZTg4ZGQ1ZjZjZTQxMWE3NTgyIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UcmF2aXMsIFN0YXRlbiBJc2xhbmQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzdmZWIxZDBiMzRmOTQyMGQ5YWNiM2U5YzQyZTAzYWM4LnNldENvbnRlbnQoaHRtbF9kN2I5NjAzNWFhYjA0M2U4OGRkNWY2Y2U0MTFhNzU4Mik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9iNWZlYWExMGMyZTI0M2Y1OTYwZGE5NTlkOTFiNzgyNC5iaW5kUG9wdXAocG9wdXBfN2ZlYjFkMGIzNGY5NDIwZDlhY2IzZTljNDJlMDNhYzgpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZDBmN2YzNDU2ZWYyNDBkZTlkYzc0ZDA2NDBiYWUwNmIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41NzI1NzIzMTgyMDYzMiwtNzQuMTE2NDc5NDM2MDYzOF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF80MTlhZGFhNjI4YzE0NTkzOGE0YzViNjQzNzE1ZDEyNiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9jODU5MzdiZDA2NmU0YzFlYThiNmZhMjJhMWU4ZGU3NiA9ICQoJzxkaXYgaWQ9Imh0bWxfYzg1OTM3YmQwNjZlNGMxZWE4YjZmYTIyYTFlOGRlNzYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk5ldyBEb3JwLCBTdGF0ZW4gSXNsYW5kPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF80MTlhZGFhNjI4YzE0NTkzOGE0YzViNjQzNzE1ZDEyNi5zZXRDb250ZW50KGh0bWxfYzg1OTM3YmQwNjZlNGMxZWE4YjZmYTIyYTFlOGRlNzYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZDBmN2YzNDU2ZWYyNDBkZTlkYzc0ZDA2NDBiYWUwNmIuYmluZFBvcHVwKHBvcHVwXzQxOWFkYWE2MjhjMTQ1OTM4YTRjNWI2NDM3MTVkMTI2KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzI0OTgwZThlNjM2MjRmOGJiZGRkMDYwMTE2YmI3MTcwID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTU4NDYyMjQzMjg4OCwtNzQuMTIxNTY1OTM3NzE4OTZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfN2UyOTk4MmVlYjQ3NDA2ZWEzMTg1ZjU5ZjM3OTZiZjggPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNTliMDdlZTAwNGVhNDNmNTk2NjZmZDA4MTNhYzI3NDIgPSAkKCc8ZGl2IGlkPSJodG1sXzU5YjA3ZWUwMDRlYTQzZjU5NjY2ZmQwODEzYWMyNzQyIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5PYWt3b29kLCBTdGF0ZW4gSXNsYW5kPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF83ZTI5OTgyZWViNDc0MDZlYTMxODVmNTlmMzc5NmJmOC5zZXRDb250ZW50KGh0bWxfNTliMDdlZTAwNGVhNDNmNTk2NjZmZDA4MTNhYzI3NDIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMjQ5ODBlOGU2MzYyNGY4YmJkZGQwNjAxMTZiYjcxNzAuYmluZFBvcHVwKHBvcHVwXzdlMjk5ODJlZWI0NzQwNmVhMzE4NWY1OWYzNzk2YmY4KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2Q3OTdmZTllZTY3ZTQzZmJiOTBjYmZhNTRiMDZiZWJkID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTQ5NDgwMjI4NzEzNjA1LC03NC4xNDkzMjM4MTQ5MDk5Ml0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9jNzRhNTg5ODAxYzQ0MzhmYjdhNWYwNzZmNmU5N2JlYyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9lMmZlYmUyOTU0YWE0YTNhYTVjY2UzNmIxMDZiMjJiNCA9ICQoJzxkaXYgaWQ9Imh0bWxfZTJmZWJlMjk1NGFhNGEzYWE1Y2NlMzZiMTA2YjIyYjQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkdyZWF0IEtpbGxzLCBTdGF0ZW4gSXNsYW5kPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9jNzRhNTg5ODAxYzQ0MzhmYjdhNWYwNzZmNmU5N2JlYy5zZXRDb250ZW50KGh0bWxfZTJmZWJlMjk1NGFhNGEzYWE1Y2NlMzZiMTA2YjIyYjQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZDc5N2ZlOWVlNjdlNDNmYmI5MGNiZmE1NGIwNmJlYmQuYmluZFBvcHVwKHBvcHVwX2M3NGE1ODk4MDFjNDQzOGZiN2E1ZjA3NmY2ZTk3YmVjKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzlkMjZlMDc1Y2FiNjQzNWJhYjc3NDVlYzdmMzk1NTZhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTQyMjMwNzQ3NDUwNzQ1LC03NC4xNjQzMzA4MDQxOTM2XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzdjMzVlODgyY2NjODRlY2NhM2Q0ZGJmZjkyZWEwNjI1ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2E4YmQ1MTkyNTBjMTQ5ZDFiZDA5MDJkYWQ0MmU1MDFmID0gJCgnPGRpdiBpZD0iaHRtbF9hOGJkNTE5MjUwYzE0OWQxYmQwOTAyZGFkNDJlNTAxZiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RWx0aW5ndmlsbGUsIFN0YXRlbiBJc2xhbmQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzdjMzVlODgyY2NjODRlY2NhM2Q0ZGJmZjkyZWEwNjI1LnNldENvbnRlbnQoaHRtbF9hOGJkNTE5MjUwYzE0OWQxYmQwOTAyZGFkNDJlNTAxZik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl85ZDI2ZTA3NWNhYjY0MzViYWI3NzQ1ZWM3ZjM5NTU2YS5iaW5kUG9wdXAocG9wdXBfN2MzNWU4ODJjY2M4NGVjY2EzZDRkYmZmOTJlYTA2MjUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZWI2ZWY4ODRjOTNmNGJjNzllZWEwZGIwMjNjMmU5ZmIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41MzgxMTQxNzQ3NDUwNywtNzQuMTc4NTQ4NjYxNjU4NzhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYjk4ZGUzMzhmMGNmNGUxYjkwMTc5MzkyMzU0ZGQ4NDcgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNGMxZWRjZjRiNDM1NDdmYjg3MGViZmQzMTc1YTMzMTMgPSAkKCc8ZGl2IGlkPSJodG1sXzRjMWVkY2Y0YjQzNTQ3ZmI4NzBlYmZkMzE3NWEzMzEzIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Bbm5hZGFsZSwgU3RhdGVuIElzbGFuZDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYjk4ZGUzMzhmMGNmNGUxYjkwMTc5MzkyMzU0ZGQ4NDcuc2V0Q29udGVudChodG1sXzRjMWVkY2Y0YjQzNTQ3ZmI4NzBlYmZkMzE3NWEzMzEzKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2ViNmVmODg0YzkzZjRiYzc5ZWVhMGRiMDIzYzJlOWZiLmJpbmRQb3B1cChwb3B1cF9iOThkZTMzOGYwY2Y0ZTFiOTAxNzkzOTIzNTRkZDg0Nyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9mYWFlN2M3NDkwZWY0MTdkYWU1NmJkZDQzZjRkODc3NCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjU0MTk2NzYyMjg4ODc1NSwtNzQuMjA1MjQ1ODI0ODAzMjZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZGJlOWRhN2YyNTgyNGYyOTk5OTliMzI2YzU2MjE0OTMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNmEzNWFlNGJjNDUyNDFlMGFjOTEzODA3M2NkNDg2NTIgPSAkKCc8ZGl2IGlkPSJodG1sXzZhMzVhZTRiYzQ1MjQxZTBhYzkxMzgwNzNjZDQ4NjUyIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Xb29kcm93LCBTdGF0ZW4gSXNsYW5kPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9kYmU5ZGE3ZjI1ODI0ZjI5OTk5OWIzMjZjNTYyMTQ5My5zZXRDb250ZW50KGh0bWxfNmEzNWFlNGJjNDUyNDFlMGFjOTEzODA3M2NkNDg2NTIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZmFhZTdjNzQ5MGVmNDE3ZGFlNTZiZGQ0M2Y0ZDg3NzQuYmluZFBvcHVwKHBvcHVwX2RiZTlkYTdmMjU4MjRmMjk5OTk5YjMyNmM1NjIxNDkzKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzNiYTRmZGNmNDA4OTQxMzE4MTU4NGM5NzBmMGUwZmMwID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTA1MzMzNzYxMTU2NDIsLTc0LjI0NjU2OTM0MjM1MjgzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzljOWM2N2JlZmU3MDQ3YTA5Nzc3YWRhM2E5NTc2MzBiID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzFkNmIyY2NjNWUzNTQ5MzJhODFmZjlkNTJlY2JiZDk1ID0gJCgnPGRpdiBpZD0iaHRtbF8xZDZiMmNjYzVlMzU0OTMyYTgxZmY5ZDUyZWNiYmQ5NSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VG90dGVudmlsbGUsIFN0YXRlbiBJc2xhbmQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzljOWM2N2JlZmU3MDQ3YTA5Nzc3YWRhM2E5NTc2MzBiLnNldENvbnRlbnQoaHRtbF8xZDZiMmNjYzVlMzU0OTMyYTgxZmY5ZDUyZWNiYmQ5NSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8zYmE0ZmRjZjQwODk0MTMxODE1ODRjOTcwZjBlMGZjMC5iaW5kUG9wdXAocG9wdXBfOWM5YzY3YmVmZTcwNDdhMDk3NzdhZGEzYTk1NzYzMGIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZDNiYThjZjcyYWQzNDdkYzljYzNjYTc1NTE5MDFhOTcgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42MzczMTYwNjcxMTAzMjYsLTc0LjA4MDU1MzUxNzkwMTE1XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzFiNmQ4ZDk4YTQ5NTQ5NDg4MTcyNWY4YWVkNmQ3YjhmID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzk2NjViNzZlODk4YjQwNDViMTE1NWQ0YmMyZmNjZTcyID0gJCgnPGRpdiBpZD0iaHRtbF85NjY1Yjc2ZTg5OGI0MDQ1YjExNTVkNGJjMmZjY2U3MiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VG9tcGtpbnN2aWxsZSwgU3RhdGVuIElzbGFuZDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMWI2ZDhkOThhNDk1NDk0ODgxNzI1ZjhhZWQ2ZDdiOGYuc2V0Q29udGVudChodG1sXzk2NjViNzZlODk4YjQwNDViMTE1NWQ0YmMyZmNjZTcyKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2QzYmE4Y2Y3MmFkMzQ3ZGM5Y2MzY2E3NTUxOTAxYTk3LmJpbmRQb3B1cChwb3B1cF8xYjZkOGQ5OGE0OTU0OTQ4ODE3MjVmOGFlZDZkN2I4Zik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9kOGRiNTdkMTVkNzM0MmZhYTIyNWE1MWQyNDI5ZmIyNyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYxOTE5MzEwNzkyNjc2LC03NC4wOTYyOTAyOTIzNTQ1OF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF82MjI0M2U0OTgwNGY0YjBkODcxMTczNThiM2MwNGE3ZSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9mNDY4OTc1ZTY4NmU0YzkyODRhM2ZmZGU0NGFiMWRkMSA9ICQoJzxkaXYgaWQ9Imh0bWxfZjQ2ODk3NWU2ODZlNGM5Mjg0YTNmZmRlNDRhYjFkZDEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlNpbHZlciBMYWtlLCBTdGF0ZW4gSXNsYW5kPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF82MjI0M2U0OTgwNGY0YjBkODcxMTczNThiM2MwNGE3ZS5zZXRDb250ZW50KGh0bWxfZjQ2ODk3NWU2ODZlNGM5Mjg0YTNmZmRlNDRhYjFkZDEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZDhkYjU3ZDE1ZDczNDJmYWEyMjVhNTFkMjQyOWZiMjcuYmluZFBvcHVwKHBvcHVwXzYyMjQzZTQ5ODA0ZjRiMGQ4NzExNzM1OGIzYzA0YTdlKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2IzMzU5ZDA3ZDBjZjQ4NTM4MDA2OGE0MmFiMDk5N2VhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjEyNzYwMTU3NTY0ODksLTc0LjA5NzEyNTUyMTc4NTNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZDEwYjViMTdiYjFkNGQyOTgzOGMxNWViNWQyMmE5NzAgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMjQ0YTgzYWI5ODdlNGJmNGEyNWUwYzE5MmQ4Y2NiNzcgPSAkKCc8ZGl2IGlkPSJodG1sXzI0NGE4M2FiOTg3ZTRiZjRhMjVlMGMxOTJkOGNjYjc3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5TdW5ueXNpZGUsIFN0YXRlbiBJc2xhbmQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2QxMGI1YjE3YmIxZDRkMjk4MzhjMTVlYjVkMjJhOTcwLnNldENvbnRlbnQoaHRtbF8yNDRhODNhYjk4N2U0YmY0YTI1ZTBjMTkyZDhjY2I3Nyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9iMzM1OWQwN2QwY2Y0ODUzODAwNjhhNDJhYjA5OTdlYS5iaW5kUG9wdXAocG9wdXBfZDEwYjViMTdiYjFkNGQyOTgzOGMxNWViNWQyMmE5NzApOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMzFiN2EzOWIxOGNlNGIwMWFiOTk5NzkxOGVmNzZjYjcgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42NDM2NzUxODMzNDA5NzQsLTczLjk2MTAxMzEyNDY2Nzc5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2EyNzU3ZTEzZDlhYzQ3MWRhOTJmNDBmZDY1ZmQ1YjlmID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzljMzlhMDc3NmEzNDRkOThhMjExZmNkMzIxYzJmZjYxID0gJCgnPGRpdiBpZD0iaHRtbF85YzM5YTA3NzZhMzQ0ZDk4YTIxMWZjZDMyMWMyZmY2MSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RGl0bWFzIFBhcmssIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9hMjc1N2UxM2Q5YWM0NzFkYTkyZjQwZmQ2NWZkNWI5Zi5zZXRDb250ZW50KGh0bWxfOWMzOWEwNzc2YTM0NGQ5OGEyMTFmY2QzMjFjMmZmNjEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMzFiN2EzOWIxOGNlNGIwMWFiOTk5NzkxOGVmNzZjYjcuYmluZFBvcHVwKHBvcHVwX2EyNzU3ZTEzZDlhYzQ3MWRhOTJmNDBmZDY1ZmQ1YjlmKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzFmYjZjOGFiOWQxYzRmNWRiODc2ODY1NjFmMmU4OWY1ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjYwOTQ2NTYxODgxMTEsLTczLjkzNzE4NjgwNTU5MzE0XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzc5NWNhNDI2MjI5YTQzYjBiZGYzYjZmYzFiYzkwYzQxID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2ZlMzE4ODY5YjQyZTQ1MTQ4NmY1ODI1Yjc3OThkNGE0ID0gJCgnPGRpdiBpZD0iaHRtbF9mZTMxODg2OWI0MmU0NTE0ODZmNTgyNWI3Nzk4ZDRhNCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+V2luZ2F0ZSwgQnJvb2tseW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzc5NWNhNDI2MjI5YTQzYjBiZGYzYjZmYzFiYzkwYzQxLnNldENvbnRlbnQoaHRtbF9mZTMxODg2OWI0MmU0NTE0ODZmNTgyNWI3Nzk4ZDRhNCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8xZmI2YzhhYjlkMWM0ZjVkYjg3Njg2NTYxZjJlODlmNS5iaW5kUG9wdXAocG9wdXBfNzk1Y2E0MjYyMjlhNDNiMGJkZjNiNmZjMWJjOTBjNDEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOTU5ZTgxYmRjZDc1NGMwYWI5NjU4NjBmMmRiYmY5ZDkgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42NTU1NzIzMTMyODA3NjQsLTczLjkyNjg4MjEyNjE2OTU1XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2FhMmIxYTc1OTlkYTQwYzBiZjliNWRmZWUyODAyNGRmID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2E5MTc3NGQzZjIzYjQ3YmQ4OTBmYzNhNDU2OTRkMzlkID0gJCgnPGRpdiBpZD0iaHRtbF9hOTE3NzRkM2YyM2I0N2JkODkwZmMzYTQ1Njk0ZDM5ZCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+UnVnYnksIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9hYTJiMWE3NTk5ZGE0MGMwYmY5YjVkZmVlMjgwMjRkZi5zZXRDb250ZW50KGh0bWxfYTkxNzc0ZDNmMjNiNDdiZDg5MGZjM2E0NTY5NGQzOWQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOTU5ZTgxYmRjZDc1NGMwYWI5NjU4NjBmMmRiYmY5ZDkuYmluZFBvcHVwKHBvcHVwX2FhMmIxYTc1OTlkYTQwYzBiZjliNWRmZWUyODAyNGRmKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzg1YWY2MzVjMWNhYjQxYTNiOGI4YjY1MmUxNDIzMTJhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjA5MTkwNDQ0MzQ1NTgsLTc0LjA4MDE1NzM0OTM2Mjk2XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzUyMWQxOTYwMDc1ZDQ5MWE4NWQ4YmZhNmJiZDYzZDkzID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2IwZDAwY2RmMmRlNDQ0NDg4ZDM0YmU0ZjVhNTc3NWIyID0gJCgnPGRpdiBpZD0iaHRtbF9iMGQwMGNkZjJkZTQ0NDQ4OGQzNGJlNGY1YTU3NzViMiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+UGFyayBIaWxsLCBTdGF0ZW4gSXNsYW5kPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF81MjFkMTk2MDA3NWQ0OTFhODVkOGJmYTZiYmQ2M2Q5My5zZXRDb250ZW50KGh0bWxfYjBkMDBjZGYyZGU0NDQ0ODhkMzRiZTRmNWE1Nzc1YjIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfODVhZjYzNWMxY2FiNDFhM2I4YjhiNjUyZTE0MjMxMmEuYmluZFBvcHVwKHBvcHVwXzUyMWQxOTYwMDc1ZDQ5MWE4NWQ4YmZhNmJiZDYzZDkzKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzU2MzhmYTVhMTU3NDQ4ZmZiMTZmOTdkZTM2NjQyNzliID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjIxMDkwNDcyNzU0MDksLTc0LjEzMzA0MTQzOTUxNzA0XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2Q4ZThhZDJlY2U4ZjQ1YzliNjQwNDkxZTZjZGRiYTZhID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzAyMGQyNGEwM2YxMDRiZTE4NDMwYjgxM2Q1OGVhNjExID0gJCgnPGRpdiBpZD0iaHRtbF8wMjBkMjRhMDNmMTA0YmUxODQzMGI4MTNkNThlYTYxMSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+V2VzdGVybGVpZ2gsIFN0YXRlbiBJc2xhbmQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2Q4ZThhZDJlY2U4ZjQ1YzliNjQwNDkxZTZjZGRiYTZhLnNldENvbnRlbnQoaHRtbF8wMjBkMjRhMDNmMTA0YmUxODQzMGI4MTNkNThlYTYxMSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl81NjM4ZmE1YTE1NzQ0OGZmYjE2Zjk3ZGUzNjY0Mjc5Yi5iaW5kUG9wdXAocG9wdXBfZDhlOGFkMmVjZThmNDVjOWI2NDA0OTFlNmNkZGJhNmEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNTVkMDZlNGI0ZTA0NDQ5YmJjZjI3NWY5MTQwZmQxOWUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42MjAxNzE1MTIyMzE4ODQsLTc0LjE1MzE1MjQ2Mzg3NzYyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2IyYjdjNmE3ZWY0ZjRiMmQ5NjhlZTIyNTkzY2I4YWU0ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzNhMDQ0NTJhY2NlNDQwMzU4M2RlZDgxYmIwODAxZjM5ID0gJCgnPGRpdiBpZD0iaHRtbF8zYTA0NDUyYWNjZTQ0MDM1ODNkZWQ4MWJiMDgwMWYzOSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+R3Jhbml0ZXZpbGxlLCBTdGF0ZW4gSXNsYW5kPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9iMmI3YzZhN2VmNGY0YjJkOTY4ZWUyMjU5M2NiOGFlNC5zZXRDb250ZW50KGh0bWxfM2EwNDQ1MmFjY2U0NDAzNTgzZGVkODFiYjA4MDFmMzkpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNTVkMDZlNGI0ZTA0NDQ5YmJjZjI3NWY5MTQwZmQxOWUuYmluZFBvcHVwKHBvcHVwX2IyYjdjNmE3ZWY0ZjRiMmQ5NjhlZTIyNTkzY2I4YWU0KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzc2NDM3MTE4MWM2NTQyYWNiY2Q5NjYwYWQyZDFkMTE0ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjM1MzI1MDk5MTE0OTIsLTc0LjE2NTEwNDIwMjQxMTI0XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzBhNGU4MjM0OWY2MDQ1MDE4ZTViN2EzZTFlMGMzM2UzID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2JjMDQ5NzBkNGYzZDQ4N2JhNTU0NzQzNTI0NTY2NjE1ID0gJCgnPGRpdiBpZD0iaHRtbF9iYzA0OTcwZDRmM2Q0ODdiYTU1NDc0MzUyNDU2NjYxNSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QXJsaW5ndG9uLCBTdGF0ZW4gSXNsYW5kPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8wYTRlODIzNDlmNjA0NTAxOGU1YjdhM2UxZTBjMzNlMy5zZXRDb250ZW50KGh0bWxfYmMwNDk3MGQ0ZjNkNDg3YmE1NTQ3NDM1MjQ1NjY2MTUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNzY0MzcxMTgxYzY1NDJhY2JjZDk2NjBhZDJkMWQxMTQuYmluZFBvcHVwKHBvcHVwXzBhNGU4MjM0OWY2MDQ1MDE4ZTViN2EzZTFlMGMzM2UzKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzJmZjQ2YTA0ZGMxNDQxMzI4YTM1YWViYTkxYjM4ZTc3ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTk2MzEyNTcxMjc2NzM0LC03NC4wNjcxMjM2MzIyNTU3NF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9hZWM3OWUwOTczZGI0ZDA1OTUwYTUwODZlOTJkYzM5OCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9mNGIxZjI3NjdiMjU0NGNhOTQ0NjI2MzFmNDdhMzgyOCA9ICQoJzxkaXYgaWQ9Imh0bWxfZjRiMWYyNzY3YjI1NDRjYTk0NDYyNjMxZjQ3YTM4MjgiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkFycm9jaGFyLCBTdGF0ZW4gSXNsYW5kPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9hZWM3OWUwOTczZGI0ZDA1OTUwYTUwODZlOTJkYzM5OC5zZXRDb250ZW50KGh0bWxfZjRiMWYyNzY3YjI1NDRjYTk0NDYyNjMxZjQ3YTM4MjgpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMmZmNDZhMDRkYzE0NDEzMjhhMzVhZWJhOTFiMzhlNzcuYmluZFBvcHVwKHBvcHVwX2FlYzc5ZTA5NzNkYjRkMDU5NTBhNTA4NmU5MmRjMzk4KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzNlYzM0ODMxMTg0NTQxNjZiNGQyMmYwZmQ4NmRlMzY2ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTk4MjY4MzU5NTk5OTEsLTc0LjA3NjY3NDM2Mjc5MDVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfY2Y4N2EyNmJlNWM3NGRhMmEwZTEzMGU3NzkyOWE0ZDAgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMWIyZDc4MWZkZDI2NDFkNDkyMjQ4MDI0YzExYjIzYzUgPSAkKCc8ZGl2IGlkPSJodG1sXzFiMmQ3ODFmZGQyNjQxZDQ5MjI0ODAyNGMxMWIyM2M1IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5HcmFzbWVyZSwgU3RhdGVuIElzbGFuZDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfY2Y4N2EyNmJlNWM3NGRhMmEwZTEzMGU3NzkyOWE0ZDAuc2V0Q29udGVudChodG1sXzFiMmQ3ODFmZGQyNjQxZDQ5MjI0ODAyNGMxMWIyM2M1KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzNlYzM0ODMxMTg0NTQxNjZiNGQyMmYwZmQ4NmRlMzY2LmJpbmRQb3B1cChwb3B1cF9jZjg3YTI2YmU1Yzc0ZGEyYTBlMTMwZTc3OTI5YTRkMCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8zYmJjZmY4M2ZmMDY0Y2E2YjBmYjhiNTU4ZjIxMzgwZiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjU5NjMyODkxMzc5NTEzLC03NC4wODc1MTExODAwNTU3OF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF85NGIyODc4MTI2NDE0ZWNlYTRlZWM5ZDFlMjFkZDNhMiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF83N2ExZDZmZWY2ZWI0ZTlmOTBhYWQ1YmQwZDQwYWNjYyA9ICQoJzxkaXYgaWQ9Imh0bWxfNzdhMWQ2ZmVmNmViNGU5ZjkwYWFkNWJkMGQ0MGFjY2MiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk9sZCBUb3duLCBTdGF0ZW4gSXNsYW5kPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF85NGIyODc4MTI2NDE0ZWNlYTRlZWM5ZDFlMjFkZDNhMi5zZXRDb250ZW50KGh0bWxfNzdhMWQ2ZmVmNmViNGU5ZjkwYWFkNWJkMGQ0MGFjY2MpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfM2JiY2ZmODNmZjA2NGNhNmIwZmI4YjU1OGYyMTM4MGYuYmluZFBvcHVwKHBvcHVwXzk0YjI4NzgxMjY0MTRlY2VhNGVlYzlkMWUyMWRkM2EyKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzhlNGM0MTc5ZTM0ODQzNDFiOWU3MmQ3Yzc0M2JmZjgzID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTg4NjcyOTQ4MTk5Mjc1LC03NC4wOTYzOTkwNTMxMjUyMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8xZTdhNmM5NjVkY2Q0ZjkwYjg5NjljNTc4NTZiMGNmZSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8xYTlhNGY4ZWY5N2M0NTQzYjkwMTY2YzJiYTAwNzM2NCA9ICQoJzxkaXYgaWQ9Imh0bWxfMWE5YTRmOGVmOTdjNDU0M2I5MDE2NmMyYmEwMDczNjQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRvbmdhbiBIaWxscywgU3RhdGVuIElzbGFuZDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMWU3YTZjOTY1ZGNkNGY5MGI4OTY5YzU3ODU2YjBjZmUuc2V0Q29udGVudChodG1sXzFhOWE0ZjhlZjk3YzQ1NDNiOTAxNjZjMmJhMDA3MzY0KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzhlNGM0MTc5ZTM0ODQzNDFiOWU3MmQ3Yzc0M2JmZjgzLmJpbmRQb3B1cChwb3B1cF8xZTdhNmM5NjVkY2Q0ZjkwYjg5NjljNTc4NTZiMGNmZSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl80N2ZhNWI3NmFkNzI0MmQxYTlmOWUzOTVmNTk0ZTg1OCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjU3MzUyNjkwNTc0MjgzLC03NC4wOTM0ODI2NjMwMzU5MV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF81YWU0MjY2ZGFkNzk0NTY3ODJlODE3M2MwMmQ4OWZjZiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9hMzRiNTFhNjkyZGY0YmY0OTNkNTYxZWVkYTI3YTcwOSA9ICQoJzxkaXYgaWQ9Imh0bWxfYTM0YjUxYTY5MmRmNGJmNDkzZDU2MWVlZGEyN2E3MDkiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk1pZGxhbmQgQmVhY2gsIFN0YXRlbiBJc2xhbmQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzVhZTQyNjZkYWQ3OTQ1Njc4MmU4MTczYzAyZDg5ZmNmLnNldENvbnRlbnQoaHRtbF9hMzRiNTFhNjkyZGY0YmY0OTNkNTYxZWVkYTI3YTcwOSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl80N2ZhNWI3NmFkNzI0MmQxYTlmOWUzOTVmNTk0ZTg1OC5iaW5kUG9wdXAocG9wdXBfNWFlNDI2NmRhZDc5NDU2NzgyZTgxNzNjMDJkODlmY2YpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfM2U0NDhhNDZmMmU1NGM3ZmIxZmM2ZjQ2MGE4NTVmNzAgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41NzYyMTU1ODcxMTc4OCwtNzQuMTA1ODU1OTg1NDU0MzRdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNTdiZmZkMDIwNDhiNGUzMzgwYjVjM2UyOTA2MmIwYjUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMmM0Mzc3MzdjZGI5NDkxYmI5OGExZWM3ZWRiNTdhYjYgPSAkKCc8ZGl2IGlkPSJodG1sXzJjNDM3NzM3Y2RiOTQ5MWJiOThhMWVjN2VkYjU3YWI2IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5HcmFudCBDaXR5LCBTdGF0ZW4gSXNsYW5kPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF81N2JmZmQwMjA0OGI0ZTMzODBiNWMzZTI5MDYyYjBiNS5zZXRDb250ZW50KGh0bWxfMmM0Mzc3MzdjZGI5NDkxYmI5OGExZWM3ZWRiNTdhYjYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfM2U0NDhhNDZmMmU1NGM3ZmIxZmM2ZjQ2MGE4NTVmNzAuYmluZFBvcHVwKHBvcHVwXzU3YmZmZDAyMDQ4YjRlMzM4MGI1YzNlMjkwNjJiMGI1KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2I3NWVjZDY5ZmVlYjQ2MTY5NWRiYmI3OTUyMDczZDBiID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTY0MjU1NDkzMDczMzUsLTc0LjEwNDMyNzA3NDY5MTI0XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzVmYmYwYzgyM2FjZjQzMzliNjAzMTZiYWJiODlmNWExID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzBjNmI5Yjc3OTlmODRiMDU5OTkzODE2NzYzYTNlMzhhID0gJCgnPGRpdiBpZD0iaHRtbF8wYzZiOWI3Nzk5Zjg0YjA1OTk5MzgxNjc2M2EzZTM4YSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+TmV3IERvcnAgQmVhY2gsIFN0YXRlbiBJc2xhbmQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzVmYmYwYzgyM2FjZjQzMzliNjAzMTZiYWJiODlmNWExLnNldENvbnRlbnQoaHRtbF8wYzZiOWI3Nzk5Zjg0YjA1OTk5MzgxNjc2M2EzZTM4YSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9iNzVlY2Q2OWZlZWI0NjE2OTVkYmJiNzk1MjA3M2QwYi5iaW5kUG9wdXAocG9wdXBfNWZiZjBjODIzYWNmNDMzOWI2MDMxNmJhYmI4OWY1YTEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNzlkZTZjZmQ4MmFhNDA4MTg0ZTBhOGY3NzZiNmI5Y2UgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41NTM5ODgwMDg1ODQ2MiwtNzQuMTM5MTY2MjIxNzU3NjhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfOWRiNGE3MGE2MjAzNDNmMWE0ZjM4MzdhYzBlZTZmMjEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZTc1YTNlODI4MWQ5NGI0N2IzZDg0YjA2YTJhMjI1NTQgPSAkKCc8ZGl2IGlkPSJodG1sX2U3NWEzZTgyODFkOTRiNDdiM2Q4NGIwNmEyYTIyNTU0IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CYXkgVGVycmFjZSwgU3RhdGVuIElzbGFuZDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOWRiNGE3MGE2MjAzNDNmMWE0ZjM4MzdhYzBlZTZmMjEuc2V0Q29udGVudChodG1sX2U3NWEzZTgyODFkOTRiNDdiM2Q4NGIwNmEyYTIyNTU0KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzc5ZGU2Y2ZkODJhYTQwODE4NGUwYThmNzc2YjZiOWNlLmJpbmRQb3B1cChwb3B1cF85ZGI0YTcwYTYyMDM0M2YxYTRmMzgzN2FjMGVlNmYyMSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8xZjNkMDE3MDE3Yzg0ZmMwOThhMGYzZTlmMTZiYmEzMiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjUzMTkxMTkyMDQ4OTYwNSwtNzQuMTkxNzQxMDU3NDc4MTRdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfOGQ5ZjM1ZWJiYjg3NDM2MThlMjFhMmRkMGM0OWM0OTkgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOWMxYWY1YTdmNzcxNDZkMGFjZDRjZjVjZjFkMTdmNDggPSAkKCc8ZGl2IGlkPSJodG1sXzljMWFmNWE3Zjc3MTQ2ZDBhY2Q0Y2Y1Y2YxZDE3ZjQ4IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5IdWd1ZW5vdCwgU3RhdGVuIElzbGFuZDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOGQ5ZjM1ZWJiYjg3NDM2MThlMjFhMmRkMGM0OWM0OTkuc2V0Q29udGVudChodG1sXzljMWFmNWE3Zjc3MTQ2ZDBhY2Q0Y2Y1Y2YxZDE3ZjQ4KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzFmM2QwMTcwMTdjODRmYzA5OGEwZjNlOWYxNmJiYTMyLmJpbmRQb3B1cChwb3B1cF84ZDlmMzVlYmJiODc0MzYxOGUyMWEyZGQwYzQ5YzQ5OSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9lNzNmYzE1ZjY0M2I0NGZhYjI3ZmVlODgzODBiMDI0MiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjUyNDY5OTM3NjExODEzNiwtNzQuMjE5ODMxMDY2MTY3NzddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNTZjMzQ5M2FiMWI1NDUwZjlmMzQxMDhhYjkwMzY3ZWMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMDNmZTA4OGYzZTQ5NDQ3OTgyZWEwMDNmNGZiYjNiNzcgPSAkKCc8ZGl2IGlkPSJodG1sXzAzZmUwODhmM2U0OTQ0Nzk4MmVhMDAzZjRmYmIzYjc3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5QbGVhc2FudCBQbGFpbnMsIFN0YXRlbiBJc2xhbmQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzU2YzM0OTNhYjFiNTQ1MGY5ZjM0MTA4YWI5MDM2N2VjLnNldENvbnRlbnQoaHRtbF8wM2ZlMDg4ZjNlNDk0NDc5ODJlYTAwM2Y0ZmJiM2I3Nyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9lNzNmYzE1ZjY0M2I0NGZhYjI3ZmVlODgzODBiMDI0Mi5iaW5kUG9wdXAocG9wdXBfNTZjMzQ5M2FiMWI1NDUwZjlmMzQxMDhhYjkwMzY3ZWMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZDEzYzJlYmRjODBiNDg3NWEwMGY2MzU2MTU1MjcwNTMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41MDYwODE2NTM0NjMwNSwtNzQuMjI5NTAzNTAyNjAwMjddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNjhmZjM2OTEzMDJhNDdmZGI4ZDVhZDQ2N2Y4Yzk2MTIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMWZmMmZlNWU2NDY5NDhmZjlhMDg1ZDNiMDZlNWFkODcgPSAkKCc8ZGl2IGlkPSJodG1sXzFmZjJmZTVlNjQ2OTQ4ZmY5YTA4NWQzYjA2ZTVhZDg3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CdXRsZXIgTWFub3IsIFN0YXRlbiBJc2xhbmQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzY4ZmYzNjkxMzAyYTQ3ZmRiOGQ1YWQ0NjdmOGM5NjEyLnNldENvbnRlbnQoaHRtbF8xZmYyZmU1ZTY0Njk0OGZmOWEwODVkM2IwNmU1YWQ4Nyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9kMTNjMmViZGM4MGI0ODc1YTAwZjYzNTYxNTUyNzA1My5iaW5kUG9wdXAocG9wdXBfNjhmZjM2OTEzMDJhNDdmZGI4ZDVhZDQ2N2Y4Yzk2MTIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOTMyMWJmNDRlYjEyNDcxMTk5MWIyMGUzNGZiZmVhYmIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41MzA1MzE0ODI4MzMxNCwtNzQuMjMyMTU3NzU4OTY1MjZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfM2ZkNDYyMjliZmE0NDAxMGEwYWZmOTM0NTVhY2FkZjIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZTQ3NDYxZDdmMDFlNGUzMmE5OTc5OWYzMDI0MjE5N2IgPSAkKCc8ZGl2IGlkPSJodG1sX2U0NzQ2MWQ3ZjAxZTRlMzJhOTk3OTlmMzAyNDIxOTdiIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DaGFybGVzdG9uLCBTdGF0ZW4gSXNsYW5kPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8zZmQ0NjIyOWJmYTQ0MDEwYTBhZmY5MzQ1NWFjYWRmMi5zZXRDb250ZW50KGh0bWxfZTQ3NDYxZDdmMDFlNGUzMmE5OTc5OWYzMDI0MjE5N2IpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOTMyMWJmNDRlYjEyNDcxMTk5MWIyMGUzNGZiZmVhYmIuYmluZFBvcHVwKHBvcHVwXzNmZDQ2MjI5YmZhNDQwMTBhMGFmZjkzNDU1YWNhZGYyKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2RiYTY2OWM5NDRmYjQ0YzI4MzE2YWYwY2Y3YzUzZmMzID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTQ5NDA0MDA2NTAwNzIsLTc0LjIxNTcyODUxMTEzOTUyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzRjNmJiMzVjZmIyODQxNTVhMjk3YjU4NjIwYWJhMzRmID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzFiNzUwYmQwNTdkNjRmM2NiZTJlZThhMjUzZTU3ZGZiID0gJCgnPGRpdiBpZD0iaHRtbF8xYjc1MGJkMDU3ZDY0ZjNjYmUyZWU4YTI1M2U1N2RmYiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Um9zc3ZpbGxlLCBTdGF0ZW4gSXNsYW5kPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF80YzZiYjM1Y2ZiMjg0MTU1YTI5N2I1ODYyMGFiYTM0Zi5zZXRDb250ZW50KGh0bWxfMWI3NTBiZDA1N2Q2NGYzY2JlMmVlOGEyNTNlNTdkZmIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZGJhNjY5Yzk0NGZiNDRjMjgzMTZhZjBjZjdjNTNmYzMuYmluZFBvcHVwKHBvcHVwXzRjNmJiMzVjZmIyODQxNTVhMjk3YjU4NjIwYWJhMzRmKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2FjMzQwYjYzYWVkYzQ2ZTE5NGM5MzFkNjM4MzY5OGIwID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTQ5Mjg1ODIyNzgzMjEsLTc0LjE4NTg4Njc0NTgzODkzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2IyNjllNzFiNmQ5MTQ5MzViNDliYjBhZmE1NWEzMTA4ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzlmOWFmMjkyMWM3MjQ4MjdhZjBkYTk5ODNmOWQzYWM5ID0gJCgnPGRpdiBpZD0iaHRtbF85ZjlhZjI5MjFjNzI0ODI3YWYwZGE5OTgzZjlkM2FjOSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QXJkZW4gSGVpZ2h0cywgU3RhdGVuIElzbGFuZDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYjI2OWU3MWI2ZDkxNDkzNWI0OWJiMGFmYTU1YTMxMDguc2V0Q29udGVudChodG1sXzlmOWFmMjkyMWM3MjQ4MjdhZjBkYTk5ODNmOWQzYWM5KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2FjMzQwYjYzYWVkYzQ2ZTE5NGM5MzFkNjM4MzY5OGIwLmJpbmRQb3B1cChwb3B1cF9iMjY5ZTcxYjZkOTE0OTM1YjQ5YmIwYWZhNTVhMzEwOCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl81MzZmNWI5ODQyYjU0ODhmODhkZTVmZDdiNjNlYTgyOCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjU1NTI5NTIzNjE3MzE5NCwtNzQuMTcwNzk0MTQ3ODYwOTJdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNjU4ZDUzMzZkNGZlNGI4NmI5NmY3NDJmZjJiZmE0YzYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZWYxMTYyZGVjNzY0NDNjMDlhYzY1NmQ4ZDcyOTUzNWYgPSAkKCc8ZGl2IGlkPSJodG1sX2VmMTE2MmRlYzc2NDQzYzA5YWM2NTZkOGQ3Mjk1MzVmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5HcmVlbnJpZGdlLCBTdGF0ZW4gSXNsYW5kPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF82NThkNTMzNmQ0ZmU0Yjg2Yjk2Zjc0MmZmMmJmYTRjNi5zZXRDb250ZW50KGh0bWxfZWYxMTYyZGVjNzY0NDNjMDlhYzY1NmQ4ZDcyOTUzNWYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNTM2ZjViOTg0MmI1NDg4Zjg4ZGU1ZmQ3YjYzZWE4MjguYmluZFBvcHVwKHBvcHVwXzY1OGQ1MzM2ZDRmZTRiODZiOTZmNzQyZmYyYmZhNGM2KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2MzYmM2MWY1YjNlNjRkNzQ5NzQyZmVlNzk5ZjRjZDg2ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTg5MTM4OTQ4NzUyODEsLTc0LjE1OTAyMjA4MTU2NjAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzBlZjFjODBmMjRhYzRiMzI5MGRlOTI2MDgwMjlhOTRlID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2NjMmQ4MjBlYTliNzQ0ZDk4OWM5MTc1ZTMwNDAwNjk2ID0gJCgnPGRpdiBpZD0iaHRtbF9jYzJkODIwZWE5Yjc0NGQ5ODljOTE3NWUzMDQwMDY5NiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+SGVhcnRsYW5kIFZpbGxhZ2UsIFN0YXRlbiBJc2xhbmQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzBlZjFjODBmMjRhYzRiMzI5MGRlOTI2MDgwMjlhOTRlLnNldENvbnRlbnQoaHRtbF9jYzJkODIwZWE5Yjc0NGQ5ODljOTE3NWUzMDQwMDY5Nik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9jM2JjNjFmNWIzZTY0ZDc0OTc0MmZlZTc5OWY0Y2Q4Ni5iaW5kUG9wdXAocG9wdXBfMGVmMWM4MGYyNGFjNGIzMjkwZGU5MjYwODAyOWE5NGUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMWZhN2FjMmY0MThkNGI2ZmE1MTVjMzY1ZDc3ZWI1MzggPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41OTQ3MjYwMjc0NjI5NSwtNzQuMTg5NTYwNDU1MTk2OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF83ZmY3NTk3OGE1OTk0ZjRmOWE5ZDM0NWRlZmM2OGMzYyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8wODYzMjYwNThkNGY0MGNkYjE1ZjQ5NDY3NWFkMDRkYSA9ICQoJzxkaXYgaWQ9Imh0bWxfMDg2MzI2MDU4ZDRmNDBjZGIxNWY0OTQ2NzVhZDA0ZGEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNoZWxzZWEsIFN0YXRlbiBJc2xhbmQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzdmZjc1OTc4YTU5OTRmNGY5YTlkMzQ1ZGVmYzY4YzNjLnNldENvbnRlbnQoaHRtbF8wODYzMjYwNThkNGY0MGNkYjE1ZjQ5NDY3NWFkMDRkYSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8xZmE3YWMyZjQxOGQ0YjZmYTUxNWMzNjVkNzdlYjUzOC5iaW5kUG9wdXAocG9wdXBfN2ZmNzU5NzhhNTk5NGY0ZjlhOWQzNDVkZWZjNjhjM2MpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZDNlMjU2YTQ4ZWYzNDZhNGE0MTU2N2EyNzMxM2ZmYWIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42MDU3Nzg2ODQ1MjM1OCwtNzQuMTg3MjU2MzgzODE1NjddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfM2Q5NmQ1YTYwNzhiNDBlMjk0MzQyYzEzODUyZTA1MTIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZmNlYWIzNzFhODEyNGM4Yzg3ZTY4ZjNlYzhhMGE4MWEgPSAkKCc8ZGl2IGlkPSJodG1sX2ZjZWFiMzcxYTgxMjRjOGM4N2U2OGYzZWM4YTBhODFhIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CbG9vbWZpZWxkLCBTdGF0ZW4gSXNsYW5kPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8zZDk2ZDVhNjA3OGI0MGUyOTQzNDJjMTM4NTJlMDUxMi5zZXRDb250ZW50KGh0bWxfZmNlYWIzNzFhODEyNGM4Yzg3ZTY4ZjNlYzhhMGE4MWEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZDNlMjU2YTQ4ZWYzNDZhNGE0MTU2N2EyNzMxM2ZmYWIuYmluZFBvcHVwKHBvcHVwXzNkOTZkNWE2MDc4YjQwZTI5NDM0MmMxMzg1MmUwNTEyKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzhlMzlkYTAyODI3NDQ0YWNhNDUzZjA5ZDU5NTUwOGU1ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjA5NTkxODAwNDIwMywtNzQuMTU5NDA5NDg2NTcxMjJdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZGI3ZTlkNTRlZDhjNDFiYmEwODkyNjBiZDQwZmQxMDkgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZWRmNGIwNGVlOGQ0NDcxOWFjNmZhNjRlYTM1Yzg3MTkgPSAkKCc8ZGl2IGlkPSJodG1sX2VkZjRiMDRlZThkNDQ3MTlhYzZmYTY0ZWEzNWM4NzE5IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CdWxscyBIZWFkLCBTdGF0ZW4gSXNsYW5kPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9kYjdlOWQ1NGVkOGM0MWJiYTA4OTI2MGJkNDBmZDEwOS5zZXRDb250ZW50KGh0bWxfZWRmNGIwNGVlOGQ0NDcxOWFjNmZhNjRlYTM1Yzg3MTkpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOGUzOWRhMDI4Mjc0NDRhY2E0NTNmMDlkNTk1NTA4ZTUuYmluZFBvcHVwKHBvcHVwX2RiN2U5ZDU0ZWQ4YzQxYmJhMDg5MjYwYmQ0MGZkMTA5KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzI4MTI3ZGRhYmMzNjQ4NDhiNjY2ZDcxNjQyOWU3OGFjID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzgyNjgyNTY3MTI1NywtNzMuOTUzMjU2NDY4MzcxMTJdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZjQ2NDA3ZjI1Y2E5NDM0MjhhYzU2MDkxYzE3NTExMGQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZmU2MmE3MzQ0MTE1NDQzMzg0MWZkMTVmMGY0YjM0NjUgPSAkKCc8ZGl2IGlkPSJodG1sX2ZlNjJhNzM0NDExNTQ0MzM4NDFmZDE1ZjBmNGIzNDY1IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DYXJuZWdpZSBIaWxsLCBNYW5oYXR0YW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2Y0NjQwN2YyNWNhOTQzNDI4YWM1NjA5MWMxNzUxMTBkLnNldENvbnRlbnQoaHRtbF9mZTYyYTczNDQxMTU0NDMzODQxZmQxNWYwZjRiMzQ2NSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8yODEyN2RkYWJjMzY0ODQ4YjY2NmQ3MTY0MjllNzhhYy5iaW5kUG9wdXAocG9wdXBfZjQ2NDA3ZjI1Y2E5NDM0MjhhYzU2MDkxYzE3NTExMGQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYTZkZTBhNDFiMDMzNDE2YmIzMDNkYWU5ZDhmNGNiZTcgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MjMyNTkwMTg4NTc2OCwtNzMuOTg4NDMzNjgwMjM1OTddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfOGExMmFhNmNhMzYyNGVjMTg4MTgyZjIxNzNlODcyNzQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMTM0ZGZkNzJiNjQ0NGQyYThlNWJiNDgxMDFiMWE0NzggPSAkKCc8ZGl2IGlkPSJodG1sXzEzNGRmZDcyYjY0NDRkMmE4ZTViYjQ4MTAxYjFhNDc4IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Ob2hvLCBNYW5oYXR0YW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzhhMTJhYTZjYTM2MjRlYzE4ODE4MmYyMTczZTg3Mjc0LnNldENvbnRlbnQoaHRtbF8xMzRkZmQ3MmI2NDQ0ZDJhOGU1YmI0ODEwMWIxYTQ3OCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9hNmRlMGE0MWIwMzM0MTZiYjMwM2RhZTlkOGY0Y2JlNy5iaW5kUG9wdXAocG9wdXBfOGExMmFhNmNhMzYyNGVjMTg4MTgyZjIxNzNlODcyNzQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYzRiNjVkZmNiZjcyNDE1OTk5N2RiYzYwMzQzYmNkNzggPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MTUyMjg5MjA0NjI4MiwtNzQuMDA1NDE1Mjk4NzMzNTVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMWE4Y2QyYjZlOWQxNGJkYmI1ZjZjZTkxMGQzOThlMzcgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZjczZDEyMjMyYjA4NDEwNmJkYjg3ZWYwNWExN2VmNmQgPSAkKCc8ZGl2IGlkPSJodG1sX2Y3M2QxMjIzMmIwODQxMDZiZGI4N2VmMDVhMTdlZjZkIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DaXZpYyBDZW50ZXIsIE1hbmhhdHRhbjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMWE4Y2QyYjZlOWQxNGJkYmI1ZjZjZTkxMGQzOThlMzcuc2V0Q29udGVudChodG1sX2Y3M2QxMjIzMmIwODQxMDZiZGI4N2VmMDVhMTdlZjZkKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2M0YjY1ZGZjYmY3MjQxNTk5OTdkYmM2MDM0M2JjZDc4LmJpbmRQb3B1cChwb3B1cF8xYThjZDJiNmU5ZDE0YmRiYjVmNmNlOTEwZDM5OGUzNyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl82OWUxYTQ4YjdkMjM0OTBjOTE4MDM1NmQ4NDJlNDIyMSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjc0ODUwOTY2NDMxMjIsLTczLjk4ODcxMzEzMjg1MjQ3XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2NhZDIzMzY3MTIxZjRmYWU4MDgxODQ0NzZmMjI5NmJkID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzYyMDgwMzBkMjUxNDRlMmE4ZTZkY2MzNTE2YzI4ODI4ID0gJCgnPGRpdiBpZD0iaHRtbF82MjA4MDMwZDI1MTQ0ZTJhOGU2ZGNjMzUxNmMyODgyOCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+TWlkdG93biBTb3V0aCwgTWFuaGF0dGFuPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9jYWQyMzM2NzEyMWY0ZmFlODA4MTg0NDc2ZjIyOTZiZC5zZXRDb250ZW50KGh0bWxfNjIwODAzMGQyNTE0NGUyYThlNmRjYzM1MTZjMjg4MjgpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNjllMWE0OGI3ZDIzNDkwYzkxODAzNTZkODQyZTQyMjEuYmluZFBvcHVwKHBvcHVwX2NhZDIzMzY3MTIxZjRmYWU4MDgxODQ0NzZmMjI5NmJkKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzEwOWNmZTY5N2E3ZTQ5NTM4ZTc4M2U0YmU2ZDNiNzYwID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTY5NjA1OTQyNzU1MDUsLTc0LjEzNDA1NzI5ODYyNTddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNzc2Mjg3ZTI0ZWQ4NDBmZWE3N2E1MWU1YWI2MmRkY2IgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMTkzODM1OTI3Zjg2NDMwZGE1NTI1MDMxN2U4M2M3NDcgPSAkKCc8ZGl2IGlkPSJodG1sXzE5MzgzNTkyN2Y4NjQzMGRhNTUyNTAzMTdlODNjNzQ3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5SaWNobW9uZCBUb3duLCBTdGF0ZW4gSXNsYW5kPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF83NzYyODdlMjRlZDg0MGZlYTc3YTUxZTVhYjYyZGRjYi5zZXRDb250ZW50KGh0bWxfMTkzODM1OTI3Zjg2NDMwZGE1NTI1MDMxN2U4M2M3NDcpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMTA5Y2ZlNjk3YTdlNDk1MzhlNzgzZTRiZTZkM2I3NjAuYmluZFBvcHVwKHBvcHVwXzc3NjI4N2UyNGVkODQwZmVhNzdhNTFlNWFiNjJkZGNiKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzZjYmRhYmFiZTQ3ZjRmMGM5OGRiNWNiMDI4MTUyZjI3ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjA5NzE5MzQwNzkyODQsLTc0LjA2NjY3NzY2MDYxNzcxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2ZlNmRhY2IyMmVhYzQ3ODhhZGJkYmJiYjlmZTY3OTFiID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzY5N2M1OTI1MDY0NTQ2MWQ5MjgyYTJmNGMzMWUxODBlID0gJCgnPGRpdiBpZD0iaHRtbF82OTdjNTkyNTA2NDU0NjFkOTI4MmEyZjRjMzFlMTgwZSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+U2hvcmUgQWNyZXMsIFN0YXRlbiBJc2xhbmQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2ZlNmRhY2IyMmVhYzQ3ODhhZGJkYmJiYjlmZTY3OTFiLnNldENvbnRlbnQoaHRtbF82OTdjNTkyNTA2NDU0NjFkOTI4MmEyZjRjMzFlMTgwZSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl82Y2JkYWJhYmU0N2Y0ZjBjOThkYjVjYjAyODE1MmYyNy5iaW5kUG9wdXAocG9wdXBfZmU2ZGFjYjIyZWFjNDc4OGFkYmRiYmJiOWZlNjc5MWIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNmVhN2NlMWY2NWFiNDNkMmJiM2I4ZGY1MWIxNTUzYTggPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42MTkxNzg0NTIwMjg0MywtNzQuMDcyNjQyNDQ1NDg0XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzUzNWViNzkxNzEyMDQwN2Q4Njk2YWZlMDljZTg1NzQ1ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2RhMGJiZjJjN2Y4YjRkNWI4MjMxYjA0ZjcyYTNkYTQ2ID0gJCgnPGRpdiBpZD0iaHRtbF9kYTBiYmYyYzdmOGI0ZDViODIzMWIwNGY3MmEzZGE0NiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q2xpZnRvbiwgU3RhdGVuIElzbGFuZDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNTM1ZWI3OTE3MTIwNDA3ZDg2OTZhZmUwOWNlODU3NDUuc2V0Q29udGVudChodG1sX2RhMGJiZjJjN2Y4YjRkNWI4MjMxYjA0ZjcyYTNkYTQ2KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzZlYTdjZTFmNjVhYjQzZDJiYjNiOGRmNTFiMTU1M2E4LmJpbmRQb3B1cChwb3B1cF81MzVlYjc5MTcxMjA0MDdkODY5NmFmZTA5Y2U4NTc0NSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9lMWQ0YjYwYzgyM2Y0YmUwOTQ1Y2UxODE3ZWI3YjUzOCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYwNDQ3MzE4OTY4NzksLTc0LjA4NDAyMzY0NzQwMzU4XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzExYWM5Y2JlNTBmYTRkMDE4YTBjY2IwOTliYzhlZDAxID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzZjZmJiNGUxMzI5NTQ1MWFhZWY0MjNhNDkyZTgyYTZhID0gJCgnPGRpdiBpZD0iaHRtbF82Y2ZiYjRlMTMyOTU0NTFhYWVmNDIzYTQ5MmU4MmE2YSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q29uY29yZCwgU3RhdGVuIElzbGFuZDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMTFhYzljYmU1MGZhNGQwMThhMGNjYjA5OWJjOGVkMDEuc2V0Q29udGVudChodG1sXzZjZmJiNGUxMzI5NTQ1MWFhZWY0MjNhNDkyZTgyYTZhKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2UxZDRiNjBjODIzZjRiZTA5NDVjZTE4MTdlYjdiNTM4LmJpbmRQb3B1cChwb3B1cF8xMWFjOWNiZTUwZmE0ZDAxOGEwY2NiMDk5YmM4ZWQwMSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8zZDhjOWJiZjE1Yjg0ZjEzYjZmYWQ5OGQ1NzA4ZjU1NCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYwNjc5NDM5NDgwMSwtNzQuMDk3NzYyMDY5NzI1MjJdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYWJhMTQwZDc4YWYxNGMyOTkzYTcxNjI2NTA3MWMyZWEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMTUyODcwYjQ5Y2FmNDdkNGIyOWY3MmIwYWFkOGNjOWIgPSAkKCc8ZGl2IGlkPSJodG1sXzE1Mjg3MGI0OWNhZjQ3ZDRiMjlmNzJiMGFhZDhjYzliIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5FbWVyc29uIEhpbGwsIFN0YXRlbiBJc2xhbmQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2FiYTE0MGQ3OGFmMTRjMjk5M2E3MTYyNjUwNzFjMmVhLnNldENvbnRlbnQoaHRtbF8xNTI4NzBiNDljYWY0N2Q0YjI5ZjcyYjBhYWQ4Y2M5Yik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8zZDhjOWJiZjE1Yjg0ZjEzYjZmYWQ5OGQ1NzA4ZjU1NC5iaW5kUG9wdXAocG9wdXBfYWJhMTQwZDc4YWYxNGMyOTkzYTcxNjI2NTA3MWMyZWEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZDFkOGY2NGViMGQxNGJiNGI3NzA2ZGZlYjQwN2Y4OWQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42MzU2MzAwMDY4MTE1MSwtNzQuMDk4MDUwNjIzNzM4ODddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMTdkNjIzY2MxNDM4NDEyMDlmMjk5Y2YyOTMwMGUxNzMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMzQ5ZTk2MDZiOTE0NDEyZmEyOTRlYjZjM2U0NTFkZjAgPSAkKCc8ZGl2IGlkPSJodG1sXzM0OWU5NjA2YjkxNDQxMmZhMjk0ZWI2YzNlNDUxZGYwIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5SYW5kYWxsIE1hbm9yLCBTdGF0ZW4gSXNsYW5kPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8xN2Q2MjNjYzE0Mzg0MTIwOWYyOTljZjI5MzAwZTE3My5zZXRDb250ZW50KGh0bWxfMzQ5ZTk2MDZiOTE0NDEyZmEyOTRlYjZjM2U0NTFkZjApOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZDFkOGY2NGViMGQxNGJiNGI3NzA2ZGZlYjQwN2Y4OWQuYmluZFBvcHVwKHBvcHVwXzE3ZDYyM2NjMTQzODQxMjA5ZjI5OWNmMjkzMDBlMTczKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzY5MGMzMWI2YWRiMjQxNjdiZWUxODA3OTM0NjVjYjJmID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjM4NDMyODM3OTQ3OTUsLTc0LjE4NjIyMzMxNzQ5ODIzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2Y0ZjYyZjJiNGY1OTQ5MWRiOThhY2MyMTNiNDcyNTljID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2I5OGM5MTY2NDI5MjRkNzhhM2ZjNjgxMWZjNWI0NTg5ID0gJCgnPGRpdiBpZD0iaHRtbF9iOThjOTE2NjQyOTI0ZDc4YTNmYzY4MTFmYzViNDU4OSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+SG93bGFuZCBIb29rLCBTdGF0ZW4gSXNsYW5kPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9mNGY2MmYyYjRmNTk0OTFkYjk4YWNjMjEzYjQ3MjU5Yy5zZXRDb250ZW50KGh0bWxfYjk4YzkxNjY0MjkyNGQ3OGEzZmM2ODExZmM1YjQ1ODkpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNjkwYzMxYjZhZGIyNDE2N2JlZTE4MDc5MzQ2NWNiMmYuYmluZFBvcHVwKHBvcHVwX2Y0ZjYyZjJiNGY1OTQ5MWRiOThhY2MyMTNiNDcyNTljKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2ZlODU4MzdlMzY3NTQwYTc4Mzc3YWUxZTQ2ZjYyMDExID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjMwMTQ2NzQxMTkzODI2LC03NC4xNDE4MTY3ODk2ODg5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2RiZTkxMzc0N2YwMzRmYTQ4NzZiNjM0OGY5YTgyMzYwID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzY3ODIzM2FmZjNmZDRjY2FiYzUzZGViZGY1NGY3OWM3ID0gJCgnPGRpdiBpZD0iaHRtbF82NzgyMzNhZmYzZmQ0Y2NhYmM1M2RlYmRmNTRmNzljNyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RWxtIFBhcmssIFN0YXRlbiBJc2xhbmQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2RiZTkxMzc0N2YwMzRmYTQ4NzZiNjM0OGY5YTgyMzYwLnNldENvbnRlbnQoaHRtbF82NzgyMzNhZmYzZmQ0Y2NhYmM1M2RlYmRmNTRmNzljNyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9mZTg1ODM3ZTM2NzU0MGE3ODM3N2FlMWU0NmY2MjAxMS5iaW5kUG9wdXAocG9wdXBfZGJlOTEzNzQ3ZjAzNGZhNDg3NmI2MzQ4ZjlhODIzNjApOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZjYyOThmNzk5OWU2NDk1M2E3OTM2ZjljNDhjOWQ1ZTYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42NTIxMTc0NTE3OTM0OTQsLTczLjkxNjY1MzMxOTc4MDQ4XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2U3NTllYzM3YjBhOTRkZTM5YWU5ZTBjNzNlOWJkMjJlID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzEwMzYzNDMzMWNmMzRhMDhiN2E2MmE2YzYwODQ0NzFjID0gJCgnPGRpdiBpZD0iaHRtbF8xMDM2MzQzMzFjZjM0YTA4YjdhNjJhNmM2MDg0NDcxYyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+UmVtc2VuIFZpbGxhZ2UsIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9lNzU5ZWMzN2IwYTk0ZGUzOWFlOWUwYzczZTliZDIyZS5zZXRDb250ZW50KGh0bWxfMTAzNjM0MzMxY2YzNGEwOGI3YTYyYTZjNjA4NDQ3MWMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZjYyOThmNzk5OWU2NDk1M2E3OTM2ZjljNDhjOWQ1ZTYuYmluZFBvcHVwKHBvcHVwX2U3NTllYzM3YjBhOTRkZTM5YWU5ZTBjNzNlOWJkMjJlKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzQ5YzU1ZjQyYTFiMjRhYjJhMDZiMjEyNmE2NzVlNjZhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjYyNzQ0Mjc5Njk2NiwtNzMuODg1MTE3NzYzNzkyOTJdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYmZmNjU3Y2I5YTY0NDI1OGIxMjQ1ZWJhODY4NGZjMTIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfM2ZmNjAxY2E5NWQ4NDhjNThiMmUyNWYwZTIxYmNlODMgPSAkKCc8ZGl2IGlkPSJodG1sXzNmZjYwMWNhOTVkODQ4YzU4YjJlMjVmMGUyMWJjZTgzIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5OZXcgTG90cywgQnJvb2tseW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2JmZjY1N2NiOWE2NDQyNThiMTI0NWViYTg2ODRmYzEyLnNldENvbnRlbnQoaHRtbF8zZmY2MDFjYTk1ZDg0OGM1OGIyZTI1ZjBlMjFiY2U4Myk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl80OWM1NWY0MmExYjI0YWIyYTA2YjIxMjZhNjc1ZTY2YS5iaW5kUG9wdXAocG9wdXBfYmZmNjU3Y2I5YTY0NDI1OGIxMjQ1ZWJhODY4NGZjMTIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZTRlOTU3ZjRiMGM0NDk3ZjlhZTJiOWFlMGQwNDBmM2UgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42MzEzMTc1NTAzOTY2NywtNzMuOTAyMzM0NzQyOTU4MzZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZTg2ZTY2MmVhNTU5NGQ2NWE3MjFlZGE3ZTgwMzA0NDQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYjA4NTFhNWJmZGVkNDJkMmI0YmE4NDg1ZGE4NTdjMzQgPSAkKCc8ZGl2IGlkPSJodG1sX2IwODUxYTViZmRlZDQyZDJiNGJhODQ4NWRhODU3YzM0IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5QYWVyZGVnYXQgQmFzaW4sIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9lODZlNjYyZWE1NTk0ZDY1YTcyMWVkYTdlODAzMDQ0NC5zZXRDb250ZW50KGh0bWxfYjA4NTFhNWJmZGVkNDJkMmI0YmE4NDg1ZGE4NTdjMzQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZTRlOTU3ZjRiMGM0NDk3ZjlhZTJiOWFlMGQwNDBmM2UuYmluZFBvcHVwKHBvcHVwX2U4NmU2NjJlYTU1OTRkNjVhNzIxZWRhN2U4MDMwNDQ0KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzA5ZDBjNzU5OGI5NzQwNWI4MmZlMThkYWZhMDU5OWYzID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjE1OTc0MjM5NjIzMzYsLTczLjkxNTE1MzkxNTUwNDA0XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzJhNzI0ZjJlY2QwZDQxYjdiYzdmMTUyYTgyYjJhNWIyID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2Y3YmJmYjVlOWIxZTQ1NmY4M2FlMjAwY2YwNjY5N2RiID0gJCgnPGRpdiBpZD0iaHRtbF9mN2JiZmI1ZTliMWU0NTZmODNhZTIwMGNmMDY2OTdkYiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+TWlsbCBCYXNpbiwgQnJvb2tseW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzJhNzI0ZjJlY2QwZDQxYjdiYzdmMTUyYTgyYjJhNWIyLnNldENvbnRlbnQoaHRtbF9mN2JiZmI1ZTliMWU0NTZmODNhZTIwMGNmMDY2OTdkYik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8wOWQwYzc1OThiOTc0MDViODJmZTE4ZGFmYTA1OTlmMy5iaW5kUG9wdXAocG9wdXBfMmE3MjRmMmVjZDBkNDFiN2JjN2YxNTJhODJiMmE1YjIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOWJlMjFhZjZmNjRjNGY3ZmIxNzgyYTFjNDkxYjc0MTQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MTE0NTk2NDM3MDQ4MiwtNzMuNzk2NDY0NjIwODE1OTNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNDI5MzYwYzQ2MzYwNGVkMGFhYmE2NGFkZTRmNTQ0YTcgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNWI2OTZhMzg1Y2UxNDM2NDgzNTI3YTFmNzUyZjQ0ODcgPSAkKCc8ZGl2IGlkPSJodG1sXzViNjk2YTM4NWNlMTQzNjQ4MzUyN2ExZjc1MmY0NDg3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5KYW1haWNhIEhpbGxzLCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzQyOTM2MGM0NjM2MDRlZDBhYWJhNjRhZGU0ZjU0NGE3LnNldENvbnRlbnQoaHRtbF81YjY5NmEzODVjZTE0MzY0ODM1MjdhMWY3NTJmNDQ4Nyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl85YmUyMWFmNmY2NGM0ZjdmYjE3ODJhMWM0OTFiNzQxNC5iaW5kUG9wdXAocG9wdXBfNDI5MzYwYzQ2MzYwNGVkMGFhYmE2NGFkZTRmNTQ0YTcpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfN2UxYzI4NzFhYzg1NGFhMTk1YWJiOTlhMGNmZDdhNjggPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MzM1MDAyNTQyOTc1NywtNzMuNzk2NzE2NzgwMjgzNDldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYTk4OTFkOTUzZWRiNGEwYzk1ZTk2YWQzYzM0MThhZmUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfM2FhMjE1Yjk1NWUyNDViZDg2ZmM1ZGI0NjgyNjA0NzggPSAkKCc8ZGl2IGlkPSJodG1sXzNhYTIxNWI5NTVlMjQ1YmQ4NmZjNWRiNDY4MjYwNDc4IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5VdG9waWEsIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYTk4OTFkOTUzZWRiNGEwYzk1ZTk2YWQzYzM0MThhZmUuc2V0Q29udGVudChodG1sXzNhYTIxNWI5NTVlMjQ1YmQ4NmZjNWRiNDY4MjYwNDc4KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzdlMWMyODcxYWM4NTRhYTE5NWFiYjk5YTBjZmQ3YTY4LmJpbmRQb3B1cChwb3B1cF9hOTg5MWQ5NTNlZGI0YTBjOTVlOTZhZDNjMzQxOGFmZSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9kYzdlZWU2ZGNmMmQ0NzAwOGU5ZDYzMjE5MTI1MmNjZCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjczNDkzNjE4MDc1NDc4LC03My44MDQ4NjEyMDA0MDUzN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF80ODU2MTMzMTFmZjI0MjY0YWQ4M2UxMjY3NmFhNWRjNyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9lZGE0N2UxNmNjMTU0MjliODVlZTdiOGFjNzdmMTVmMiA9ICQoJzxkaXYgaWQ9Imh0bWxfZWRhNDdlMTZjYzE1NDI5Yjg1ZWU3YjhhYzc3ZjE1ZjIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlBvbW9ub2ssIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNDg1NjEzMzExZmYyNDI2NGFkODNlMTI2NzZhYTVkYzcuc2V0Q29udGVudChodG1sX2VkYTQ3ZTE2Y2MxNTQyOWI4NWVlN2I4YWM3N2YxNWYyKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2RjN2VlZTZkY2YyZDQ3MDA4ZTlkNjMyMTkxMjUyY2NkLmJpbmRQb3B1cChwb3B1cF80ODU2MTMzMTFmZjI0MjY0YWQ4M2UxMjY3NmFhNWRjNyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9hMGVjODVkZjVhNDg0ODJiYTViY2EwZTdiYWM3M2M5NSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjc3MDMxNzM5Mjk5ODIsLTczLjg5NDY3OTk2MjcwNTc0XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2Y4MzVjOGJhMDkwMTQyYjNhNmMzNDMyMzlhNDJlMjU1ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2RkMzI4NTg1MTYzNjQ5YTc5M2I1MDY3NTkyMThhOWM0ID0gJCgnPGRpdiBpZD0iaHRtbF9kZDMyODU4NTE2MzY0OWE3OTNiNTA2NzU5MjE4YTljNCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QXN0b3JpYSBIZWlnaHRzLCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2Y4MzVjOGJhMDkwMTQyYjNhNmMzNDMyMzlhNDJlMjU1LnNldENvbnRlbnQoaHRtbF9kZDMyODU4NTE2MzY0OWE3OTNiNTA2NzU5MjE4YTljNCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9hMGVjODVkZjVhNDg0ODJiYTViY2EwZTdiYWM3M2M5NS5iaW5kUG9wdXAocG9wdXBfZjgzNWM4YmEwOTAxNDJiM2E2YzM0MzIzOWE0MmUyNTUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYTU5Mzc0Yjc2ZjFmNDdhMWE0YWMxYjg4Mzc3OTg3MTAgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44MzE0MjgzNDE2MTU0OCwtNzMuOTAxMTk5MDMzODc2NjddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYjlkMjRmMDhlMmI4NGI2Nzk2NGE3MjdkNDRhMTNmZmYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZjc5MzBlYTAxYzk5NDViNGJkNjBlZGY3MWU2OGRlOWQgPSAkKCc8ZGl2IGlkPSJodG1sX2Y3OTMwZWEwMWM5OTQ1YjRiZDYwZWRmNzFlNjhkZTlkIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DbGFyZW1vbnQgVmlsbGFnZSwgQnJvbng8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2I5ZDI0ZjA4ZTJiODRiNjc5NjRhNzI3ZDQ0YTEzZmZmLnNldENvbnRlbnQoaHRtbF9mNzkzMGVhMDFjOTk0NWI0YmQ2MGVkZjcxZTY4ZGU5ZCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9hNTkzNzRiNzZmMWY0N2ExYTRhYzFiODgzNzc5ODcxMC5iaW5kUG9wdXAocG9wdXBfYjlkMjRmMDhlMmI4NGI2Nzk2NGE3MjdkNDRhMTNmZmYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZmZkNzY5MjJiNTY4NDdmMGE3NmViYTM3OGJkMTM4ZmIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44MjQ3ODA0OTA4NDI5MDUsLTczLjkxNTg0NjUyNzU5MDA5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzkxMTZkNGY2YmZiODRiMzlhZjNlZjdiZWM5ZjJkZTg3ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzI1NmZmNWYzNjlmODRjNmI4ZGE3MTk1NjRlOTE0OWIxID0gJCgnPGRpdiBpZD0iaHRtbF8yNTZmZjVmMzY5Zjg0YzZiOGRhNzE5NTY0ZTkxNDliMSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q29uY291cnNlIFZpbGxhZ2UsIEJyb254PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF85MTE2ZDRmNmJmYjg0YjM5YWYzZWY3YmVjOWYyZGU4Ny5zZXRDb250ZW50KGh0bWxfMjU2ZmY1ZjM2OWY4NGM2YjhkYTcxOTU2NGU5MTQ5YjEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZmZkNzY5MjJiNTY4NDdmMGE3NmViYTM3OGJkMTM4ZmIuYmluZFBvcHVwKHBvcHVwXzkxMTZkNGY2YmZiODRiMzlhZjNlZjdiZWM5ZjJkZTg3KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzdkZWMxODM5NmFhYTQzNzI4YTEwMTFlNDg2NTVmYmU4ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODQzODI2MTc2NzE2NTQsLTczLjkxNjU1NTUxOTY0NDE5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzQxMWMwOGJlYTMzZTQ0MGVhZWRiMmRjMDZlNDIxMGY3ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzQ3NDBhNjlmMWQ1MDQ5YTI4MzM3ZDNiNmFlNTJkODY3ID0gJCgnPGRpdiBpZD0iaHRtbF80NzQwYTY5ZjFkNTA0OWEyODMzN2QzYjZhZTUyZDg2NyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+TW91bnQgRWRlbiwgQnJvbng8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzQxMWMwOGJlYTMzZTQ0MGVhZWRiMmRjMDZlNDIxMGY3LnNldENvbnRlbnQoaHRtbF80NzQwYTY5ZjFkNTA0OWEyODMzN2QzYjZhZTUyZDg2Nyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl83ZGVjMTgzOTZhYWE0MzcyOGExMDExZTQ4NjU1ZmJlOC5iaW5kUG9wdXAocG9wdXBfNDExYzA4YmVhMzNlNDQwZWFlZGIyZGMwNmU0MjEwZjcpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZmFlM2M5MGU3MTFiNDg5ZjllYzYzZTJhNmNmNzE5MDMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44NDg4NDE2MDcyNDY2NSwtNzMuOTA4Mjk5MzA4ODE5ODhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfODBiZDA3MTNlMTJjNDk4ZWI2NGU5NDM3ODA5MTRlZmEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMDJkYTZmMGQ0OTk2NGFlMmIxOTM4OGRlNjM5YWYxMTAgPSAkKCc8ZGl2IGlkPSJodG1sXzAyZGE2ZjBkNDk5NjRhZTJiMTkzODhkZTYzOWFmMTEwIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Nb3VudCBIb3BlLCBCcm9ueDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfODBiZDA3MTNlMTJjNDk4ZWI2NGU5NDM3ODA5MTRlZmEuc2V0Q29udGVudChodG1sXzAyZGE2ZjBkNDk5NjRhZTJiMTkzODhkZTYzOWFmMTEwKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2ZhZTNjOTBlNzExYjQ4OWY5ZWM2M2UyYTZjZjcxOTAzLmJpbmRQb3B1cChwb3B1cF84MGJkMDcxM2UxMmM0OThlYjY0ZTk0Mzc4MDkxNGVmYSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9jMzg3MDhkMzg0OGU0OTcyYjAyODhiNzhhNjVkOWEyOSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjc2MDI4MDMzMTMxMzc0LC03My45NjM1NTYxNDA5NDMwM10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9mMTAyY2Q4ODZhNmI0MmUxYmZmZjVkM2Q5NTdhODIxZCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9jZTA2OGYzMjBjNDY0NGQyYjZhN2IzZTA5ZmQ4YmViYiA9ICQoJzxkaXYgaWQ9Imh0bWxfY2UwNjhmMzIwYzQ2NDRkMmI2YTdiM2UwOWZkOGJlYmIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlN1dHRvbiBQbGFjZSwgTWFuaGF0dGFuPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9mMTAyY2Q4ODZhNmI0MmUxYmZmZjVkM2Q5NTdhODIxZC5zZXRDb250ZW50KGh0bWxfY2UwNjhmMzIwYzQ2NDRkMmI2YTdiM2UwOWZkOGJlYmIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYzM4NzA4ZDM4NDhlNDk3MmIwMjg4Yjc4YTY1ZDlhMjkuYmluZFBvcHVwKHBvcHVwX2YxMDJjZDg4NmE2YjQyZTFiZmZmNWQzZDk1N2E4MjFkKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzE2YjU2MmEzZjdhMzQ0ZmY5OTM4MjUwNjQ4NzAwNmY1ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzQzNDE0MDkwMDczNTM2LC03My45NTM4Njc4MjEzMDc0NV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF83OWRjODcwMWUwY2M0YTFlYWZlMjc0ZmZkNmQ0YjhhZiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8yNTVkYjExNDFhNmE0ODcxOTY4NmI2NjVlNzFmNzZjOCA9ICQoJzxkaXYgaWQ9Imh0bWxfMjU1ZGIxMTQxYTZhNDg3MTk2ODZiNjY1ZTcxZjc2YzgiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkh1bnRlcnMgUG9pbnQsIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNzlkYzg3MDFlMGNjNGExZWFmZTI3NGZmZDZkNGI4YWYuc2V0Q29udGVudChodG1sXzI1NWRiMTE0MWE2YTQ4NzE5Njg2YjY2NWU3MWY3NmM4KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzE2YjU2MmEzZjdhMzQ0ZmY5OTM4MjUwNjQ4NzAwNmY1LmJpbmRQb3B1cChwb3B1cF83OWRjODcwMWUwY2M0YTFlYWZlMjc0ZmZkNmQ0YjhhZik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl84ZjI5MDJkZTVjZTg0NTJhOGNhYTQ3NDIyZmRlYWI1NSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjc1MjA0MjM2OTUwNzIyLC03My45Njc3MDgyNDU4MTgzNF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF85YTMzZDA2YmE5MDE0OWI4YjkyYzgxMzRlM2YxMGU5YiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF84MGZkZjNlYWVlOGE0Nzg1YTk5ZWQ5NzgxZTQ3M2NlMiA9ICQoJzxkaXYgaWQ9Imh0bWxfODBmZGYzZWFlZThhNDc4NWE5OWVkOTc4MWU0NzNjZTIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlR1cnRsZSBCYXksIE1hbmhhdHRhbjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOWEzM2QwNmJhOTAxNDliOGI5MmM4MTM0ZTNmMTBlOWIuc2V0Q29udGVudChodG1sXzgwZmRmM2VhZWU4YTQ3ODVhOTllZDk3ODFlNDczY2UyKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzhmMjkwMmRlNWNlODQ1MmE4Y2FhNDc0MjJmZGVhYjU1LmJpbmRQb3B1cChwb3B1cF85YTMzZDA2YmE5MDE0OWI4YjkyYzgxMzRlM2YxMGU5Yik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9mYThjMzc3YjBkNzM0NmFmOTUwMjEzMDZhZmY2ZGQ1MSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjc0NjkxNzQxMDc0MDE5NSwtNzMuOTcxMjE5Mjg3MjIyNjVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNTY2NTk0NThkMjBhNDlhMGE0Yzc4MDljZDExOTBiMWIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNzI3ZWUzNWYzMWU5NGM3Yjk3Yzk1ZWJkNzBhODJiNjkgPSAkKCc8ZGl2IGlkPSJodG1sXzcyN2VlMzVmMzFlOTRjN2I5N2M5NWViZDcwYTgyYjY5IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UdWRvciBDaXR5LCBNYW5oYXR0YW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzU2NjU5NDU4ZDIwYTQ5YTBhNGM3ODA5Y2QxMTkwYjFiLnNldENvbnRlbnQoaHRtbF83MjdlZTM1ZjMxZTk0YzdiOTdjOTVlYmQ3MGE4MmI2OSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9mYThjMzc3YjBkNzM0NmFmOTUwMjEzMDZhZmY2ZGQ1MS5iaW5kUG9wdXAocG9wdXBfNTY2NTk0NThkMjBhNDlhMGE0Yzc4MDljZDExOTBiMWIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNjQ5NTU3YzhlYjJmNDZlZjk5YjBlZmEyYjM5OWQ1NzcgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MzA5OTk1NTQ3NzA2MSwtNzMuOTc0MDUxNzA0NjkyMDNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfN2RkYTAxMjg1MDVhNDMyZWI0NTBlMzVhOWQ5YjViOTQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOGQ5YTQ2MDNkYjc4NDYwNGE5NGQzMDYzMThmNGQ4ZDIgPSAkKCc8ZGl2IGlkPSJodG1sXzhkOWE0NjAzZGI3ODQ2MDRhOTRkMzA2MzE4ZjRkOGQyIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5TdHV5dmVzYW50IFRvd24sIE1hbmhhdHRhbjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfN2RkYTAxMjg1MDVhNDMyZWI0NTBlMzVhOWQ5YjViOTQuc2V0Q29udGVudChodG1sXzhkOWE0NjAzZGI3ODQ2MDRhOTRkMzA2MzE4ZjRkOGQyKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzY0OTU1N2M4ZWIyZjQ2ZWY5OWIwZWZhMmIzOTlkNTc3LmJpbmRQb3B1cChwb3B1cF83ZGRhMDEyODUwNWE0MzJlYjQ1MGUzNWE5ZDliNWI5NCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl85MGJiZWU1ZmI3YzQ0ZmQzYjRhNzA2ZjMwOWNiNDY1MiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjczOTY3MzA0NzYzODQyNiwtNzMuOTkwOTQ3MTA1MjgyNl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF83ZWI5MTkwOWJmYjk0ZWNiYTA0NTk2Y2E3MjQzNzRjNSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF81MThjOWNiMmY0NzI0MzI3YWY1ZmY1OTBkNTJiMjc4NiA9ICQoJzxkaXYgaWQ9Imh0bWxfNTE4YzljYjJmNDcyNDMyN2FmNWZmNTkwZDUyYjI3ODYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkZsYXRpcm9uLCBNYW5oYXR0YW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzdlYjkxOTA5YmZiOTRlY2JhMDQ1OTZjYTcyNDM3NGM1LnNldENvbnRlbnQoaHRtbF81MThjOWNiMmY0NzI0MzI3YWY1ZmY1OTBkNTJiMjc4Nik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl85MGJiZWU1ZmI3YzQ0ZmQzYjRhNzA2ZjMwOWNiNDY1Mi5iaW5kUG9wdXAocG9wdXBfN2ViOTE5MDliZmI5NGVjYmEwNDU5NmNhNzI0Mzc0YzUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfN2ZmOTI2NTEyYTQ2NDdkMzk3MWUxNDUxYjE2ZDExNjMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43NDU2NTE4MDYwODA3NiwtNzMuOTE4MTkyODY0MzE2ODJdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMzY0NDJiZjBhMDg1NGEwOGJjZjk5Yjg3NGUwZGUzOWMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMDQ4OGY3OGQwMWI0NDRmY2I1Y2Q5MjQ5MWE3Y2RhYjQgPSAkKCc8ZGl2IGlkPSJodG1sXzA0ODhmNzhkMDFiNDQ0ZmNiNWNkOTI0OTFhN2NkYWI0IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5TdW5ueXNpZGUgR2FyZGVucywgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8zNjQ0MmJmMGEwODU0YTA4YmNmOTliODc0ZTBkZTM5Yy5zZXRDb250ZW50KGh0bWxfMDQ4OGY3OGQwMWI0NDRmY2I1Y2Q5MjQ5MWE3Y2RhYjQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfN2ZmOTI2NTEyYTQ2NDdkMzk3MWUxNDUxYjE2ZDExNjMuYmluZFBvcHVwKHBvcHVwXzM2NDQyYmYwYTA4NTRhMDhiY2Y5OWI4NzRlMGRlMzljKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzRkOWMxZDdiYjhkZTQyNGRiMTRlMjU4ZTIyYzE4MzFiID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzM3MjUwNzE2OTQ0OTcsLTczLjkzMjQ0MjM1MjYwMTc4XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzdjMmZmMGJjMDA2MjQ1YzZiNWJkY2UzMzkxNjEyNmIyID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzY3ZTdkYjhhMjUxNTQ1YWQ5MTEzYmM0MmQ1ODJjOTBjID0gJCgnPGRpdiBpZD0iaHRtbF82N2U3ZGI4YTI1MTU0NWFkOTExM2JjNDJkNTgyYzkwYyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Qmxpc3N2aWxsZSwgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF83YzJmZjBiYzAwNjI0NWM2YjViZGNlMzM5MTYxMjZiMi5zZXRDb250ZW50KGh0bWxfNjdlN2RiOGEyNTE1NDVhZDkxMTNiYzQyZDU4MmM5MGMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNGQ5YzFkN2JiOGRlNDI0ZGIxNGUyNThlMjJjMTgzMWIuYmluZFBvcHVwKHBvcHVwXzdjMmZmMGJjMDA2MjQ1YzZiNWJkY2UzMzkxNjEyNmIyKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzBlZDcxZWQxZWZmMTQwMTBhMjAyMmQyZjM5YTI2OWU4ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzAzMjgxMDkwOTMwMTQsLTczLjk5NTUwNzUxODg4NDE1XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2E3NjQwZWZkZGI1MzQ5NmM4ODhjNjFiNjM1MTI0MzhmID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzZlODdiYzFhZmRjODQ3NzI5MjhmYmZmYWFiNmY1OThjID0gJCgnPGRpdiBpZD0iaHRtbF82ZTg3YmMxYWZkYzg0NzcyOTI4ZmJmZmFhYjZmNTk4YyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RnVsdG9uIEZlcnJ5LCBCcm9va2x5bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYTc2NDBlZmRkYjUzNDk2Yzg4OGM2MWI2MzUxMjQzOGYuc2V0Q29udGVudChodG1sXzZlODdiYzFhZmRjODQ3NzI5MjhmYmZmYWFiNmY1OThjKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzBlZDcxZWQxZWZmMTQwMTBhMjAyMmQyZjM5YTI2OWU4LmJpbmRQb3B1cChwb3B1cF9hNzY0MGVmZGRiNTM0OTZjODg4YzYxYjYzNTEyNDM4Zik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9lNGFmYjYxOTNjODU0YzY3YTM1YjYyMmFmZGU3MDJjMiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjcwMzMyMTQ5ODgyODc0LC03My45ODExMTYwMzU5MjM5M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8yYmEzMDRjMjllMGQ0NjkzYjA2NWFiNjdkZmE2ZDhkNyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8wN2VkYjEzY2E2NDA0MzllODRmMmNmNmJlNjgxZmNlYiA9ICQoJzxkaXYgaWQ9Imh0bWxfMDdlZGIxM2NhNjQwNDM5ZTg0ZjJjZjZiZTY4MWZjZWIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlZpbmVnYXIgSGlsbCwgQnJvb2tseW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzJiYTMwNGMyOWUwZDQ2OTNiMDY1YWI2N2RmYTZkOGQ3LnNldENvbnRlbnQoaHRtbF8wN2VkYjEzY2E2NDA0MzllODRmMmNmNmJlNjgxZmNlYik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9lNGFmYjYxOTNjODU0YzY3YTM1YjYyMmFmZGU3MDJjMi5iaW5kUG9wdXAocG9wdXBfMmJhMzA0YzI5ZTBkNDY5M2IwNjVhYjY3ZGZhNmQ4ZDcpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOTMzZGNhNzBhNzZjNDA4MzkwOTZjZGM0YTlhMjA5ZmUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42NzUwMzk4NjUwMzIzNywtNzMuOTMwNTMxMDg4MTczMzhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMjU0ZmFiNjUxZTJkNGU0MjlhMjU4NTcyZDc0YjNlOGYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNzM4NDVkMjYzNmIxNDRlNzg0MDBjNjA0ZWY1MGZkNDIgPSAkKCc8ZGl2IGlkPSJodG1sXzczODQ1ZDI2MzZiMTQ0ZTc4NDAwYzYwNGVmNTBmZDQyIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5XZWVrc3ZpbGxlLCBCcm9va2x5bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMjU0ZmFiNjUxZTJkNGU0MjlhMjU4NTcyZDc0YjNlOGYuc2V0Q29udGVudChodG1sXzczODQ1ZDI2MzZiMTQ0ZTc4NDAwYzYwNGVmNTBmZDQyKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzkzM2RjYTcwYTc2YzQwODM5MDk2Y2RjNGE5YTIwOWZlLmJpbmRQb3B1cChwb3B1cF8yNTRmYWI2NTFlMmQ0ZTQyOWEyNTg1NzJkNzRiM2U4Zik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9iYTJkMmNhZDQ1NWM0NGFiODZlYzA0ZWMzMTIwMDVlZiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjY3Nzg2MTA0NzY5NTMxLC03My45MDMzMTY4NDg1MjU5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF85YjM5MTE3MWNkNDI0OGY0YjdhZDYzN2UzMDk0MzkyNCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8yZTc4ZmRiMjQ5ZGQ0MGJiODcyYTNiYTRjYTE5Mzg1MSA9ICQoJzxkaXYgaWQ9Imh0bWxfMmU3OGZkYjI0OWRkNDBiYjg3MmEzYmE0Y2ExOTM4NTEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkJyb2Fkd2F5IEp1bmN0aW9uLCBCcm9va2x5bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOWIzOTExNzFjZDQyNDhmNGI3YWQ2MzdlMzA5NDM5MjQuc2V0Q29udGVudChodG1sXzJlNzhmZGIyNDlkZDQwYmI4NzJhM2JhNGNhMTkzODUxKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2JhMmQyY2FkNDU1YzQ0YWI4NmVjMDRlYzMxMjAwNWVmLmJpbmRQb3B1cChwb3B1cF85YjM5MTE3MWNkNDI0OGY0YjdhZDYzN2UzMDk0MzkyNCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8wMDNhYzQ3M2Q3ZTk0NDdlYmZjMTUzNWExMDIwNGYzNyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjcwMzE3NjMyODIyNjkyLC03My45ODg3NTI4MDc0NTA0XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzQ4NDg5NzY2MGY3NjRlYzQ4NDczN2YzMDdiZGZlMDJlID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2M4YzNlYmQxMzkzYzQxYWJhZGU3YzgzYjk4MWMwMDY3ID0gJCgnPGRpdiBpZD0iaHRtbF9jOGMzZWJkMTM5M2M0MWFiYWRlN2M4M2I5ODFjMDA2NyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RHVtYm8sIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF80ODQ4OTc2NjBmNzY0ZWM0ODQ3MzdmMzA3YmRmZTAyZS5zZXRDb250ZW50KGh0bWxfYzhjM2ViZDEzOTNjNDFhYmFkZTdjODNiOTgxYzAwNjcpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMDAzYWM0NzNkN2U5NDQ3ZWJmYzE1MzVhMTAyMDRmMzcuYmluZFBvcHVwKHBvcHVwXzQ4NDg5NzY2MGY3NjRlYzQ4NDczN2YzMDdiZGZlMDJlKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2RmOTE3OGJlYWU5NDQ2NDRiNTJiNzgzNTYwMTgxNDhlID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjAxODA5NTc2MzE0NDQsLTc0LjEyMDU5Mzk5NzE4MDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzlmY2Q2ZmI5NWYwNTQ0MjQ5MGYzY2I0YjEyMmUyYTQzID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2JmZjZhZWVjMDlhNjQ0ODJhM2ZiODdkMWFkZGFkYTY2ID0gJCgnPGRpdiBpZD0iaHRtbF9iZmY2YWVlYzA5YTY0NDgyYTNmYjg3ZDFhZGRhZGE2NiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+TWFub3IgSGVpZ2h0cywgU3RhdGVuIElzbGFuZDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOWZjZDZmYjk1ZjA1NDQyNDkwZjNjYjRiMTIyZTJhNDMuc2V0Q29udGVudChodG1sX2JmZjZhZWVjMDlhNjQ0ODJhM2ZiODdkMWFkZGFkYTY2KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2RmOTE3OGJlYWU5NDQ2NDRiNTJiNzgzNTYwMTgxNDhlLmJpbmRQb3B1cChwb3B1cF85ZmNkNmZiOTVmMDU0NDI0OTBmM2NiNGIxMjJlMmE0Myk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8zYzNmNjE3ZmJkNjM0OGY0ODE0OWE5YzE0ZjdhYjVkYSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYwMzcwNjkyNjI3MzcxLC03NC4xMzIwODQ0NzQ4NDI5OF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF81MGRhNDk1N2VkYmU0YTc5YTgwMzg4YjA0MWU5NjFhMSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF83ZWZjODFmZmIwYzk0ZjUxODNmYWExMmM5YWRjOTE1ZCA9ICQoJzxkaXYgaWQ9Imh0bWxfN2VmYzgxZmZiMGM5NGY1MTgzZmFhMTJjOWFkYzkxNWQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPldpbGxvd2Jyb29rLCBTdGF0ZW4gSXNsYW5kPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF81MGRhNDk1N2VkYmU0YTc5YTgwMzg4YjA0MWU5NjFhMS5zZXRDb250ZW50KGh0bWxfN2VmYzgxZmZiMGM5NGY1MTgzZmFhMTJjOWFkYzkxNWQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfM2MzZjYxN2ZiZDYzNDhmNDgxNDlhOWMxNGY3YWI1ZGEuYmluZFBvcHVwKHBvcHVwXzUwZGE0OTU3ZWRiZTRhNzlhODAzODhiMDQxZTk2MWExKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzgxYTgyZTllOTc1MTQ5MzNhOWYxY2VkMWRiMzllMmJkID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTQxMTM5OTIyMDkxNzY2LC03NC4yMTc3NjYzNjA2ODU2N10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9lYjA4M2U1ZDExNzA0Njc4ODk3ZDY2Y2U3MmRmZTFmYiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8xNjE0NmM3MzY5Nzk0ZDQ5YmMzNmNiNjU3MjllNDVkZSA9ICQoJzxkaXYgaWQ9Imh0bWxfMTYxNDZjNzM2OTc5NGQ0OWJjMzZjYjY1NzI5ZTQ1ZGUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlNhbmR5IEdyb3VuZCwgU3RhdGVuIElzbGFuZDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZWIwODNlNWQxMTcwNDY3ODg5N2Q2NmNlNzJkZmUxZmIuc2V0Q29udGVudChodG1sXzE2MTQ2YzczNjk3OTRkNDliYzM2Y2I2NTcyOWU0NWRlKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzgxYTgyZTllOTc1MTQ5MzNhOWYxY2VkMWRiMzllMmJkLmJpbmRQb3B1cChwb3B1cF9lYjA4M2U1ZDExNzA0Njc4ODk3ZDY2Y2U3MmRmZTFmYik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl84ZmNkOGQ4OWY0ZjY0NmVjYjNiZjczNjYwNjdiNTE4YiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjU3OTExODc0Mjk2MTIxNCwtNzQuMTI3MjcyNDA2MDQ5NDZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYTNhNjc1YjllNTkzNDg0YzliNWNjYjgxNjhjZTI5ODcgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZThjYzQ5OGQ0NTgyNGNhYjg5YjM4MWEzNTdiYzI5MjIgPSAkKCc8ZGl2IGlkPSJodG1sX2U4Y2M0OThkNDU4MjRjYWI4OWIzODFhMzU3YmMyOTIyIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5FZ2JlcnR2aWxsZSwgU3RhdGVuIElzbGFuZDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYTNhNjc1YjllNTkzNDg0YzliNWNjYjgxNjhjZTI5ODcuc2V0Q29udGVudChodG1sX2U4Y2M0OThkNDU4MjRjYWI4OWIzODFhMzU3YmMyOTIyKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzhmY2Q4ZDg5ZjRmNjQ2ZWNiM2JmNzM2NjA2N2I1MThiLmJpbmRQb3B1cChwb3B1cF9hM2E2NzViOWU1OTM0ODRjOWI1Y2NiODE2OGNlMjk4Nyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9hNjZiMWQzZDFkZGM0N2UyODM2NjZjMjE2NTAwODFhNyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjU2NzM3NTg4OTU3MDMyLC03My44OTIxMzc2MDIzMjgyMl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9lOWE5OTkzZWI0MDI0OWFkYTlkNDc4MWIzMzUyMWZkOCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF80MzU5MzJlZGJlZjU0NWY4ODQyYjBiZjk2NmM2MWE3ZiA9ICQoJzxkaXYgaWQ9Imh0bWxfNDM1OTMyZWRiZWY1NDVmODg0MmIwYmY5NjZjNjFhN2YiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlJveGJ1cnksIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZTlhOTk5M2ViNDAyNDlhZGE5ZDQ3ODFiMzM1MjFmZDguc2V0Q29udGVudChodG1sXzQzNTkzMmVkYmVmNTQ1Zjg4NDJiMGJmOTY2YzYxYTdmKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2E2NmIxZDNkMWRkYzQ3ZTI4MzY2NmMyMTY1MDA4MWE3LmJpbmRQb3B1cChwb3B1cF9lOWE5OTkzZWI0MDI0OWFkYTlkNDc4MWIzMzUyMWZkOCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9iZTQ0MzBmNDNhNTg0NGRiOGM2OGYxYTY1YTU1MzZlYyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjU5ODUyNTA5NTEzNzI1NSwtNzMuOTU5MTg0NTk0Mjg3MDJdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZjc2MmNhMDdlOTRkNDczY2IwNDNjODA3M2UwZTVjMWEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZjJiNmI4MGViZWM4NDY0MGI3MjA0MjU0MDMyMThjNTkgPSAkKCc8ZGl2IGlkPSJodG1sX2YyYjZiODBlYmVjODQ2NDBiNzIwNDI1NDAzMjE4YzU5IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Ib21lY3Jlc3QsIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9mNzYyY2EwN2U5NGQ0NzNjYjA0M2M4MDczZTBlNWMxYS5zZXRDb250ZW50KGh0bWxfZjJiNmI4MGViZWM4NDY0MGI3MjA0MjU0MDMyMThjNTkpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYmU0NDMwZjQzYTU4NDRkYjhjNjhmMWE2NWE1NTM2ZWMuYmluZFBvcHVwKHBvcHVwX2Y3NjJjYTA3ZTk0ZDQ3M2NiMDQzYzgwNzNlMGU1YzFhKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2UwNjM3ZTNjNTA1NDQ2Y2U5YzA2MTdjZTRjYTdkNjEwID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzE2NDE0NTExMTU4MTg1LC03My44ODExNDMxOTIwMDYwNF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9mMTZhMjdhNDc2NmI0Nzc0ODFkMzY3NGQ2MjczYjkwYSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF85ZDYzZWRiZGE5YjY0OWIyYTJjMzczNzEzNzg2MWMyMSA9ICQoJzxkaXYgaWQ9Imh0bWxfOWQ2M2VkYmRhOWI2NDliMmEyYzM3MzcxMzc4NjFjMjEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk1pZGRsZSBWaWxsYWdlLCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2YxNmEyN2E0NzY2YjQ3NzQ4MWQzNjc0ZDYyNzNiOTBhLnNldENvbnRlbnQoaHRtbF85ZDYzZWRiZGE5YjY0OWIyYTJjMzczNzEzNzg2MWMyMSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9lMDYzN2UzYzUwNTQ0NmNlOWMwNjE3Y2U0Y2E3ZDYxMC5iaW5kUG9wdXAocG9wdXBfZjE2YTI3YTQ3NjZiNDc3NDgxZDM2NzRkNjI3M2I5MGEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfN2EwODQ3ZWY3MTYxNGMwMTlkOGU3MWNmY2U4NDYzYzQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41MjYyNjQwNjczNDgxMiwtNzQuMjAxNTI1NTY0NTc2NThdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNDNkNTFjOGUxZTUwNDZhZmFmMTE5MDQ5M2FkZWQ0NjcgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMWM0YjkwMmM3Y2I5NDZlNWFjM2MyMDYwM2Q3NTE1NzcgPSAkKCc8ZGl2IGlkPSJodG1sXzFjNGI5MDJjN2NiOTQ2ZTVhYzNjMjA2MDNkNzUxNTc3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5QcmluY2UmIzM5O3MgQmF5LCBTdGF0ZW4gSXNsYW5kPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF80M2Q1MWM4ZTFlNTA0NmFmYWYxMTkwNDkzYWRlZDQ2Ny5zZXRDb250ZW50KGh0bWxfMWM0YjkwMmM3Y2I5NDZlNWFjM2MyMDYwM2Q3NTE1NzcpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfN2EwODQ3ZWY3MTYxNGMwMTlkOGU3MWNmY2U4NDYzYzQuYmluZFBvcHVwKHBvcHVwXzQzZDUxYzhlMWU1MDQ2YWZhZjExOTA0OTNhZGVkNDY3KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzFhMTc5NDMxNGFlNTQ1MTE4ZWM2OWZlODFiY2VkYzhkID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTc2NTA2MjkzNzk0ODksLTc0LjEzNzkyNjYzNzcxNTY4XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2MzMGI0NTgzZjdmOTQ5MTNhYjYxMmQ3NWEwOWU3ZWIxID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzkzN2E2OGY0NzllNjQxYTliMzJkYjJkNzQ1ZjhmNTc2ID0gJCgnPGRpdiBpZD0iaHRtbF85MzdhNjhmNDc5ZTY0MWE5YjMyZGIyZDc0NWY4ZjU3NiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+TGlnaHRob3VzZSBIaWxsLCBTdGF0ZW4gSXNsYW5kPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9jMzBiNDU4M2Y3Zjk0OTEzYWI2MTJkNzVhMDllN2ViMS5zZXRDb250ZW50KGh0bWxfOTM3YTY4ZjQ3OWU2NDFhOWIzMmRiMmQ3NDVmOGY1NzYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMWExNzk0MzE0YWU1NDUxMThlYzY5ZmU4MWJjZWRjOGQuYmluZFBvcHVwKHBvcHVwX2MzMGI0NTgzZjdmOTQ5MTNhYjYxMmQ3NWEwOWU3ZWIxKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzY4YmM2YTdhOTk2MTQwMmM5MjlhOWY4NjI5ZDQ0ZDYwID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTE5NTQxNDU3NDg5MDksLTc0LjIyOTU3MDgwNjI2OTQxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzAzMTI0ZmIwNGM0OTRiYTliMTJjZmM3ZTI3YTZkNzEyID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzRhNWFlZjEzN2JhYjRmYmZhZWQwYmM5MjAzNTMxOTgzID0gJCgnPGRpdiBpZD0iaHRtbF80YTVhZWYxMzdiYWI0ZmJmYWVkMGJjOTIwMzUzMTk4MyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+UmljaG1vbmQgVmFsbGV5LCBTdGF0ZW4gSXNsYW5kPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8wMzEyNGZiMDRjNDk0YmE5YjEyY2ZjN2UyN2E2ZDcxMi5zZXRDb250ZW50KGh0bWxfNGE1YWVmMTM3YmFiNGZiZmFlZDBiYzkyMDM1MzE5ODMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNjhiYzZhN2E5OTYxNDAyYzkyOWE5Zjg2MjlkNDRkNjAuYmluZFBvcHVwKHBvcHVwXzAzMTI0ZmIwNGM0OTRiYTliMTJjZmM3ZTI3YTZkNzEyKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2RiODAwOTdlMzZiZTQ4ZmZiZjk2MDhjMmI5NTkwZGQ0ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzkwNjAxNTU2NzAxNDgsLTczLjgyNjY3NzU3MTM4NjQxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzMwYzc4YTk0ZjNhNzQwMmJiNmM0NzY3NDY1ZWRmN2UyID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzQ5ZDIyNGJhZmE4YTRiMTJhMDM0M2ZiYjJjNTM0MDNjID0gJCgnPGRpdiBpZD0iaHRtbF80OWQyMjRiYWZhOGE0YjEyYTAzNDNmYmIyYzUzNDAzYyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+TWFsYmEsIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMzBjNzhhOTRmM2E3NDAyYmI2YzQ3Njc0NjVlZGY3ZTIuc2V0Q29udGVudChodG1sXzQ5ZDIyNGJhZmE4YTRiMTJhMDM0M2ZiYjJjNTM0MDNjKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2RiODAwOTdlMzZiZTQ4ZmZiZjk2MDhjMmI5NTkwZGQ0LmJpbmRQb3B1cChwb3B1cF8zMGM3OGE5NGYzYTc0MDJiYjZjNDc2NzQ2NWVkZjdlMik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl83NzdkZmFlYWNlNjk0NGVkYWI1MmE0ZDgyZmYxZGU1ZCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjY4MTk5ODkzNDUxNzMsLTczLjg5MDM0NTcwOTg3Ml0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8xNzNlN2MyY2MzZTk0Y2NjYmYzMjA2NGU1NDJhMzRmZCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF83MmJmMGEwMTM1Yjc0YmQ1OGY3YmU2NzJjZTJjNWI0MCA9ICQoJzxkaXYgaWQ9Imh0bWxfNzJiZjBhMDEzNWI3NGJkNThmN2JlNjcyY2UyYzViNDAiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkhpZ2hsYW5kIFBhcmssIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8xNzNlN2MyY2MzZTk0Y2NjYmYzMjA2NGU1NDJhMzRmZC5zZXRDb250ZW50KGh0bWxfNzJiZjBhMDEzNWI3NGJkNThmN2JlNjcyY2UyYzViNDApOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNzc3ZGZhZWFjZTY5NDRlZGFiNTJhNGQ4MmZmMWRlNWQuYmluZFBvcHVwKHBvcHVwXzE3M2U3YzJjYzNlOTRjY2NiZjMyMDY0ZTU0MmEzNGZkKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzI0YzQzYjk3ODcyYTRhMmM4ODc3ZGZlZTg3ZWRiZjE5ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjA5Mzc3NzAxMTM3NjYsLTczLjk0ODQxNTE1MzI4ODkzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzdhYTgwNmEyNDQxYjQ5YmQ4YzI5M2YzZmZlOTc0YWRjID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzNhNTlmMmJhZDgyZDRhYWNhN2FmZTc3ZWM3MzVlZGRhID0gJCgnPGRpdiBpZD0iaHRtbF8zYTU5ZjJiYWQ4MmQ0YWFjYTdhZmU3N2VjNzM1ZWRkYSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+TWFkaXNvbiwgQnJvb2tseW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzdhYTgwNmEyNDQxYjQ5YmQ4YzI5M2YzZmZlOTc0YWRjLnNldENvbnRlbnQoaHRtbF8zYTU5ZjJiYWQ4MmQ0YWFjYTdhZmU3N2VjNzM1ZWRkYSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8yNGM0M2I5Nzg3MmE0YTJjODg3N2RmZWU4N2VkYmYxOS5iaW5kUG9wdXAocG9wdXBfN2FhODA2YTI0NDFiNDliZDhjMjkzZjNmZmU5NzRhZGMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYzQzNDEzNmEzMThhNDIwNGE3YzIzYjFlMDhjMGNhMmIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44NTI3MjI5NzYzMzAxNywtNzMuODYxNzI1Nzc1NTUxMTVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNGFkZTA2YzcyNzRlNGFkMzhhYjc0ZjlmMTVmOTNkN2YgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYThlNjVmODMxYzM0NGYyYzlhZjQyYjkyZDExYjJiYjAgPSAkKCc8ZGl2IGlkPSJodG1sX2E4ZTY1ZjgzMWMzNDRmMmM5YWY0MmI5MmQxMWIyYmIwIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Ccm9ueGRhbGUsIEJyb254PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF80YWRlMDZjNzI3NGU0YWQzOGFiNzRmOWYxNWY5M2Q3Zi5zZXRDb250ZW50KGh0bWxfYThlNjVmODMxYzM0NGYyYzlhZjQyYjkyZDExYjJiYjApOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYzQzNDEzNmEzMThhNDIwNGE3YzIzYjFlMDhjMGNhMmIuYmluZFBvcHVwKHBvcHVwXzRhZGUwNmM3Mjc0ZTRhZDM4YWI3NGY5ZjE1ZjkzZDdmKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2VmZDc2MjcwZmJjZDQ1NzBhZmMwNDk5OTUxM2QyNzRiID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODY1Nzg3ODc4MDI5ODIsLTczLjg1OTMxODYzMjIxNjQ3XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2ZkZDI5M2VlYzYxOTQ2MWVhMDM2MzY1ZTZjYjU4ODFlID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzMxZTIyNDBlYmExNTQyNjRiMDgxMGM0Y2Q4OGI1NWVmID0gJCgnPGRpdiBpZD0iaHRtbF8zMWUyMjQwZWJhMTU0MjY0YjA4MTBjNGNkODhiNTVlZiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QWxsZXJ0b24sIEJyb254PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9mZGQyOTNlZWM2MTk0NjFlYTAzNjM2NWU2Y2I1ODgxZS5zZXRDb250ZW50KGh0bWxfMzFlMjI0MGViYTE1NDI2NGIwODEwYzRjZDg4YjU1ZWYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZWZkNzYyNzBmYmNkNDU3MGFmYzA0OTk5NTEzZDI3NGIuYmluZFBvcHVwKHBvcHVwX2ZkZDI5M2VlYzYxOTQ2MWVhMDM2MzY1ZTZjYjU4ODFlKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzk4ODYzNGJlNjYzMjRiYTg5ZDU2OTQ5NTU2MzRlMGI2ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODcwMzkyMzkxNDE0NywtNzMuOTAxNTIyNjQ1MTMxNDRdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMzEzMzFmNzFlYWI0NDAxNGFjYWNjNDJmZjQ2NjZiOTggPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMGY3YjZhMTcyZjlmNDkzZTg5ZDg4MTA3MjhjNDY1OWMgPSAkKCc8ZGl2IGlkPSJodG1sXzBmN2I2YTE3MmY5ZjQ5M2U4OWQ4ODEwNzI4YzQ2NTljIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5LaW5nc2JyaWRnZSBIZWlnaHRzLCBCcm9ueDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMzEzMzFmNzFlYWI0NDAxNGFjYWNjNDJmZjQ2NjZiOTguc2V0Q29udGVudChodG1sXzBmN2I2YTE3MmY5ZjQ5M2U4OWQ4ODEwNzI4YzQ2NTljKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzk4ODYzNGJlNjYzMjRiYTg5ZDU2OTQ5NTU2MzRlMGI2LmJpbmRQb3B1cChwb3B1cF8zMTMzMWY3MWVhYjQ0MDE0YWNhY2M0MmZmNDY2NmI5OCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9hOTlmMjQ5NDIwMTk0MTlmOGJiN2JiNTgxMDJiZDFkYSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjY0NjkyNjA2NjU4NTc5LC03My45NDgxNzcwOTkyMDE4NF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OWY2MzY3Yzk5NGE0NmRiODY5MDYyYjk2ZmIzYzdiZik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF80OTc1OTg1MTE5YjU0MzQ0OGE3ZDBkOTQwZDE5MzEyNSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF83MGNjYTg3N2Y1YTE0YWQ4OWUxMzQwZGQ1NzU4M2M0MCA9ICQoJzxkaXYgaWQ9Imh0bWxfNzBjY2E4NzdmNWExNGFkODllMTM0MGRkNTc1ODNjNDAiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkVyYXNtdXMsIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF80OTc1OTg1MTE5YjU0MzQ0OGE3ZDBkOTQwZDE5MzEyNS5zZXRDb250ZW50KGh0bWxfNzBjY2E4NzdmNWExNGFkODllMTM0MGRkNTc1ODNjNDApOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYTk5ZjI0OTQyMDE5NDE5ZjhiYjdiYjU4MTAyYmQxZGEuYmluZFBvcHVwKHBvcHVwXzQ5NzU5ODUxMTliNTQzNDQ4YTdkMGQ5NDBkMTkzMTI1KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2E1MDU0YTFiNGQ1NTRmOGJhY2IyNGY2MzZiOWNlZjYzID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzU2NjU4MDgyMjc1MTksLTc0LjAwMDExMTM2MjAyNjM3XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzg1NDNjZTVlYWI4ZTRjYjc4ODI4N2M4YjkwNWY3YzgzID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2E0NmU3OGRhMGZiZDQzNmM5ZmJmNTUwYWQyYjg0MDU3ID0gJCgnPGRpdiBpZD0iaHRtbF9hNDZlNzhkYTBmYmQ0MzZjOWZiZjU1MGFkMmI4NDA1NyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+SHVkc29uIFlhcmRzLCBNYW5oYXR0YW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzg1NDNjZTVlYWI4ZTRjYjc4ODI4N2M4YjkwNWY3YzgzLnNldENvbnRlbnQoaHRtbF9hNDZlNzhkYTBmYmQ0MzZjOWZiZjU1MGFkMmI4NDA1Nyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9hNTA1NGExYjRkNTU0ZjhiYWNiMjRmNjM2YjljZWY2My5iaW5kUG9wdXAocG9wdXBfODU0M2NlNWVhYjhlNGNiNzg4Mjg3YzhiOTA1ZjdjODMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMzJhZDZkMDI1OTBiNGZmNThiOWY3ZTY2Yjk1YzZiYTUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41ODczMzc3NDAxODc0MSwtNzMuODA1NTMwMDI5Njg3MThdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNDBiNzk2YTMzYmEzNDk2ZmI3YWE2OTE4OWExY2FjYmMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMWM3NTgyYjVlYTJkNGViNzg5NDQ2OGI1MzFmMTY5OWEgPSAkKCc8ZGl2IGlkPSJodG1sXzFjNzU4MmI1ZWEyZDRlYjc4OTQ0NjhiNTMxZjE2OTlhIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5IYW1tZWxzLCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzQwYjc5NmEzM2JhMzQ5NmZiN2FhNjkxODlhMWNhY2JjLnNldENvbnRlbnQoaHRtbF8xYzc1ODJiNWVhMmQ0ZWI3ODk0NDY4YjUzMWYxNjk5YSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8zMmFkNmQwMjU5MGI0ZmY1OGI5ZjdlNjZiOTVjNmJhNS5iaW5kUG9wdXAocG9wdXBfNDBiNzk2YTMzYmEzNDk2ZmI3YWE2OTE4OWExY2FjYmMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYzVlMjZiN2VhNjk4NGZmMWIxY2NmYWM4ZGJlOGUzYWYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42MTEzMjE2OTEyODM4MzQsLTczLjc2NTk2NzgxNDQ1NjI3XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzM2ZmUyMjdkYWE5ZDQ0Y2U5N2Q4MGE2ZDcxMGQzMmFkID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2JjMzQ5NTFiYzYwODRhNzBhYjZiMjA2ODQ1ZTI1MWE4ID0gJCgnPGRpdiBpZD0iaHRtbF9iYzM0OTUxYmM2MDg0YTcwYWI2YjIwNjg0NWUyNTFhOCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QmF5c3dhdGVyLCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzM2ZmUyMjdkYWE5ZDQ0Y2U5N2Q4MGE2ZDcxMGQzMmFkLnNldENvbnRlbnQoaHRtbF9iYzM0OTUxYmM2MDg0YTcwYWI2YjIwNjg0NWUyNTFhOCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9jNWUyNmI3ZWE2OTg0ZmYxYjFjY2ZhYzhkYmU4ZTNhZi5iaW5kUG9wdXAocG9wdXBfMzZmZTIyN2RhYTlkNDRjZTk3ZDgwYTZkNzEwZDMyYWQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZDAyYTc4YmY3ZjZhNGQ4NmE4OWZlZTk2ZGY0NGQ3ZGMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43NTYwOTEyOTcwOTQ3MDYsLTczLjk0NTYzMDcwMzM0MDkxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk5ZjYzNjdjOTk0YTQ2ZGI4NjkwNjJiOTZmYjNjN2JmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2JhMjI5Njc0MTIxMzRhYThiOWQwNjZlYjM0YzQyM2FiID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2RiYzgzMDJjZTQ0YjQ1OTI5YTU5NDIwZGY1NWQ5MGQzID0gJCgnPGRpdiBpZD0iaHRtbF9kYmM4MzAyY2U0NGI0NTkyOWE1OTQyMGRmNTVkOTBkMyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+UXVlZW5zYnJpZGdlLCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2JhMjI5Njc0MTIxMzRhYThiOWQwNjZlYjM0YzQyM2FiLnNldENvbnRlbnQoaHRtbF9kYmM4MzAyY2U0NGI0NTkyOWE1OTQyMGRmNTVkOTBkMyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9kMDJhNzhiZjdmNmE0ZDg2YTg5ZmVlOTZkZjQ0ZDdkYy5iaW5kUG9wdXAocG9wdXBfYmEyMjk2NzQxMjEzNGFhOGI5ZDA2NmViMzRjNDIzYWIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNTUwNzNiNDQwNGNjNDhmMDkxMzk5YjliNzM2YzZhMDMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42MTczMTA3OTI1Mjk4MywtNzQuMDgxNzM5OTIyMTE5NjJdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTlmNjM2N2M5OTRhNDZkYjg2OTA2MmI5NmZiM2M3YmYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfY2IyN2U5ZDU2ZTY0NGE2ZTlhMjRiMzIxNTIxMDA2MDMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMGFmN2UwMjUwYmMyNGU0Y2ExY2ZlY2IzYTAxZWMyOWMgPSAkKCc8ZGl2IGlkPSJodG1sXzBhZjdlMDI1MGJjMjRlNGNhMWNmZWNiM2EwMWVjMjljIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Gb3ggSGlsbHMsIFN0YXRlbiBJc2xhbmQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2NiMjdlOWQ1NmU2NDRhNmU5YTI0YjMyMTUyMTAwNjAzLnNldENvbnRlbnQoaHRtbF8wYWY3ZTAyNTBiYzI0ZTRjYTFjZmVjYjNhMDFlYzI5Yyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl81NTA3M2I0NDA0Y2M0OGYwOTEzOTliOWI3MzZjNmEwMy5iaW5kUG9wdXAocG9wdXBfY2IyN2U5ZDU2ZTY0NGE2ZTlhMjRiMzIxNTIxMDA2MDMpOwoKICAgICAgICAgICAgCiAgICAgICAgCjwvc2NyaXB0Pg== onload="this.contentDocument.open();this.contentDocument.write(atob(this.getAttribute('data-html')));this.contentDocument.close();" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>



<h3 id="version">2. Exploaring the Neighbourhood of Staten Island our safest borough.</h3>


```python
Staten_Island = neighborhoods[neighborhoods['Borough'] == 'Staten Island'].reset_index(drop=True)
Staten_Island.head()

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Borough</th>
      <th>Neighborhood</th>
      <th>Latitude</th>
      <th>Longitude</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Staten Island</td>
      <td>St. George</td>
      <td>40.644982</td>
      <td>-74.079353</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Staten Island</td>
      <td>New Brighton</td>
      <td>40.640615</td>
      <td>-74.087017</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Staten Island</td>
      <td>Stapleton</td>
      <td>40.626928</td>
      <td>-74.077902</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Staten Island</td>
      <td>Rosebank</td>
      <td>40.615305</td>
      <td>-74.069805</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Staten Island</td>
      <td>West Brighton</td>
      <td>40.631879</td>
      <td>-74.107182</td>
    </tr>
  </tbody>
</table>
</div>




```python
address = 'Staten Island, NY'

geolocator = Nominatim(user_agent="ny_explorer")
location = geolocator.geocode(address)
latitude = location.latitude
longitude = location.longitude
print('The geograpical coordinate of Manhattan are {}, {}.'.format(latitude, longitude))
```

    The geograpical coordinate of Manhattan are 40.5834557, -74.1496048.



```python
# create map of Manhattan using latitude and longitude values
map_statenisland = folium.Map(location=[latitude, longitude], zoom_start=11)

# add markers to map
for lat, lng, label in zip(Staten_Island['Latitude'], Staten_Island['Longitude'], Staten_Island['Neighborhood']):
    label = folium.Popup(label, parse_html=True)
    folium.CircleMarker(
        [lat, lng],
        radius=5,
        popup=label,
        color='blue',
        fill=True,
        fill_color='#3186cc',
        fill_opacity=0.7,
        parse_html=False).add_to(map_statenisland)  
    
map_statenisland
```




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><span style="color:#565656">Make this Notebook Trusted to load map: File -> Trust Notebook</span><iframe src="about:blank" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" data-html=PCFET0NUWVBFIGh0bWw+CjxoZWFkPiAgICAKICAgIDxtZXRhIGh0dHAtZXF1aXY9ImNvbnRlbnQtdHlwZSIgY29udGVudD0idGV4dC9odG1sOyBjaGFyc2V0PVVURi04IiAvPgogICAgPHNjcmlwdD5MX1BSRUZFUl9DQU5WQVMgPSBmYWxzZTsgTF9OT19UT1VDSCA9IGZhbHNlOyBMX0RJU0FCTEVfM0QgPSBmYWxzZTs8L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2FqYXguZ29vZ2xlYXBpcy5jb20vYWpheC9saWJzL2pxdWVyeS8xLjExLjEvanF1ZXJ5Lm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvanMvYm9vdHN0cmFwLm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9jZG5qcy5jbG91ZGZsYXJlLmNvbS9hamF4L2xpYnMvTGVhZmxldC5hd2Vzb21lLW1hcmtlcnMvMi4wLjIvbGVhZmxldC5hd2Vzb21lLW1hcmtlcnMuanMiPjwvc2NyaXB0PgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9jc3MvYm9vdHN0cmFwLm1pbi5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvY3NzL2Jvb3RzdHJhcC10aGVtZS5taW4uY3NzIi8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vbWF4Y2RuLmJvb3RzdHJhcGNkbi5jb20vZm9udC1hd2Vzb21lLzQuNi4zL2Nzcy9mb250LWF3ZXNvbWUubWluLmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2NkbmpzLmNsb3VkZmxhcmUuY29tL2FqYXgvbGlicy9MZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy8yLjAuMi9sZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9yYXdnaXQuY29tL3B5dGhvbi12aXN1YWxpemF0aW9uL2ZvbGl1bS9tYXN0ZXIvZm9saXVtL3RlbXBsYXRlcy9sZWFmbGV0LmF3ZXNvbWUucm90YXRlLmNzcyIvPgogICAgPHN0eWxlPmh0bWwsIGJvZHkge3dpZHRoOiAxMDAlO2hlaWdodDogMTAwJTttYXJnaW46IDA7cGFkZGluZzogMDt9PC9zdHlsZT4KICAgIDxzdHlsZT4jbWFwIHtwb3NpdGlvbjphYnNvbHV0ZTt0b3A6MDtib3R0b206MDtyaWdodDowO2xlZnQ6MDt9PC9zdHlsZT4KICAgIAogICAgICAgICAgICA8c3R5bGU+ICNtYXBfOTY3YjI2ZjE5NzE2NDYwODgzMDM1NjBiNDQ5OGNlYWQgewogICAgICAgICAgICAgICAgcG9zaXRpb24gOiByZWxhdGl2ZTsKICAgICAgICAgICAgICAgIHdpZHRoIDogMTAwLjAlOwogICAgICAgICAgICAgICAgaGVpZ2h0OiAxMDAuMCU7CiAgICAgICAgICAgICAgICBsZWZ0OiAwLjAlOwogICAgICAgICAgICAgICAgdG9wOiAwLjAlOwogICAgICAgICAgICAgICAgfQogICAgICAgICAgICA8L3N0eWxlPgogICAgICAgIAo8L2hlYWQ+Cjxib2R5PiAgICAKICAgIAogICAgICAgICAgICA8ZGl2IGNsYXNzPSJmb2xpdW0tbWFwIiBpZD0ibWFwXzk2N2IyNmYxOTcxNjQ2MDg4MzAzNTYwYjQ0OThjZWFkIiA+PC9kaXY+CiAgICAgICAgCjwvYm9keT4KPHNjcmlwdD4gICAgCiAgICAKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGJvdW5kcyA9IG51bGw7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgdmFyIG1hcF85NjdiMjZmMTk3MTY0NjA4ODMwMzU2MGI0NDk4Y2VhZCA9IEwubWFwKAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJ21hcF85NjdiMjZmMTk3MTY0NjA4ODMwMzU2MGI0NDk4Y2VhZCcsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB7Y2VudGVyOiBbNDAuNTgzNDU1NywtNzQuMTQ5NjA0OF0sCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB6b29tOiAxMSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIG1heEJvdW5kczogYm91bmRzLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbGF5ZXJzOiBbXSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHdvcmxkQ29weUp1bXA6IGZhbHNlLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgY3JzOiBMLkNSUy5FUFNHMzg1NwogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB9KTsKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHRpbGVfbGF5ZXJfMGFkZTZlMTdiZjUxNGU1YzgzMTg0NzViNDFkNjM2MmYgPSBMLnRpbGVMYXllcigKICAgICAgICAgICAgICAgICdodHRwczovL3tzfS50aWxlLm9wZW5zdHJlZXRtYXAub3JnL3t6fS97eH0ve3l9LnBuZycsCiAgICAgICAgICAgICAgICB7CiAgImF0dHJpYnV0aW9uIjogbnVsbCwKICAiZGV0ZWN0UmV0aW5hIjogZmFsc2UsCiAgIm1heFpvb20iOiAxOCwKICAibWluWm9vbSI6IDEsCiAgIm5vV3JhcCI6IGZhbHNlLAogICJzdWJkb21haW5zIjogImFiYyIKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTY3YjI2ZjE5NzE2NDYwODgzMDM1NjBiNDQ5OGNlYWQpOwogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzg1Y2RiN2MxZTMzYTQyZWNiMDhlMDNhNzc2MjczNTE3ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjQ0OTgxNTcxMDA0NCwtNzQuMDc5MzUzMTI1MTI3OTddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTY3YjI2ZjE5NzE2NDYwODgzMDM1NjBiNDQ5OGNlYWQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfM2MyMTRhMWRjMWY1NDExNGI1ZjI2YzE3YThkNzk0ZmYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOTIzZjY0ZjE0NDI0NDg4NTgxNTcyOWU2ZGQ3ZmY5N2UgPSAkKCc8ZGl2IGlkPSJodG1sXzkyM2Y2NGYxNDQyNDQ4ODU4MTU3MjllNmRkN2ZmOTdlIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5TdC4gR2VvcmdlPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8zYzIxNGExZGMxZjU0MTE0YjVmMjZjMTdhOGQ3OTRmZi5zZXRDb250ZW50KGh0bWxfOTIzZjY0ZjE0NDI0NDg4NTgxNTcyOWU2ZGQ3ZmY5N2UpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfODVjZGI3YzFlMzNhNDJlY2IwOGUwM2E3NzYyNzM1MTcuYmluZFBvcHVwKHBvcHVwXzNjMjE0YTFkYzFmNTQxMTRiNWYyNmMxN2E4ZDc5NGZmKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2E1YWU3M2I1ZjU0MTQwYjBiNGRjMzVkNGU5ZDY4NjczID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjQwNjE0NTU5MTM1MTEsLTc0LjA4NzAxNjUwNTE2NjI1XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk2N2IyNmYxOTcxNjQ2MDg4MzAzNTYwYjQ0OThjZWFkKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2RlYzY0NTVhNzJkNzQ0OTFhNzc3ZWU2MjBkZjZjNTQwID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2JjNTA5ZDliNjRlOTQ4YzNiMmZhNjNhNjExOWQ5NzBlID0gJCgnPGRpdiBpZD0iaHRtbF9iYzUwOWQ5YjY0ZTk0OGMzYjJmYTYzYTYxMTlkOTcwZSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+TmV3IEJyaWdodG9uPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9kZWM2NDU1YTcyZDc0NDkxYTc3N2VlNjIwZGY2YzU0MC5zZXRDb250ZW50KGh0bWxfYmM1MDlkOWI2NGU5NDhjM2IyZmE2M2E2MTE5ZDk3MGUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYTVhZTczYjVmNTQxNDBiMGI0ZGMzNWQ0ZTlkNjg2NzMuYmluZFBvcHVwKHBvcHVwX2RlYzY0NTVhNzJkNzQ0OTFhNzc3ZWU2MjBkZjZjNTQwKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzc5YWMxMzliYTAzZDRhNTliOThjNGUzYjI0N2FjNWQxID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjI2OTI3NjI1MzgxNzYsLTc0LjA3NzkwMTkyNjYwMDY2XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk2N2IyNmYxOTcxNjQ2MDg4MzAzNTYwYjQ0OThjZWFkKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzcyMWFjZmRlMjdkMTQzYzQ5YTU5MDE1NjY4NTQyMDc2ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2E3ODVlM2E1MzA4YzQyMzE4Y2NmM2Q2OWMxZjZhMzg3ID0gJCgnPGRpdiBpZD0iaHRtbF9hNzg1ZTNhNTMwOGM0MjMxOGNjZjNkNjljMWY2YTM4NyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+U3RhcGxldG9uPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF83MjFhY2ZkZTI3ZDE0M2M0OWE1OTAxNTY2ODU0MjA3Ni5zZXRDb250ZW50KGh0bWxfYTc4NWUzYTUzMDhjNDIzMThjY2YzZDY5YzFmNmEzODcpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNzlhYzEzOWJhMDNkNGE1OWI5OGM0ZTNiMjQ3YWM1ZDEuYmluZFBvcHVwKHBvcHVwXzcyMWFjZmRlMjdkMTQzYzQ5YTU5MDE1NjY4NTQyMDc2KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2Q2ZmIwMjEzNTM2MjQ1ZTA4NjVhZjBhOGZjNjAxNTAwID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjE1MzA0OTQ2NTI3NjEsLTc0LjA2OTgwNTI2NzE2MTQxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk2N2IyNmYxOTcxNjQ2MDg4MzAzNTYwYjQ0OThjZWFkKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2U2MGZiNDFiZjBlODQ3MzViZjA1NDFiNTI1MWUxNzdjID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzE3ZGI5NWFlZTE1MzQ3OGQ4NTFmZTM2NTFkOGQ4NTYzID0gJCgnPGRpdiBpZD0iaHRtbF8xN2RiOTVhZWUxNTM0NzhkODUxZmUzNjUxZDhkODU2MyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Um9zZWJhbms8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2U2MGZiNDFiZjBlODQ3MzViZjA1NDFiNTI1MWUxNzdjLnNldENvbnRlbnQoaHRtbF8xN2RiOTVhZWUxNTM0NzhkODUxZmUzNjUxZDhkODU2Myk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9kNmZiMDIxMzUzNjI0NWUwODY1YWYwYThmYzYwMTUwMC5iaW5kUG9wdXAocG9wdXBfZTYwZmI0MWJmMGU4NDczNWJmMDU0MWI1MjUxZTE3N2MpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNGIyM2FkOTg5ZjM3NDZmNWI1YWM4NmY5YzIxNWYyYjEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42MzE4Nzg5MjY1NDYwNywtNzQuMTA3MTgxNzgyNjU2MV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NjdiMjZmMTk3MTY0NjA4ODMwMzU2MGI0NDk4Y2VhZCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF81Y2Q0ZGJiZGMwMGE0ZWQxOWY5YWM4NGVmMGJhZmQzYiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9iYjM4OGVhNDkxNDE0ZTAxYWEzOTY4NDhlNTA3YTI1OCA9ICQoJzxkaXYgaWQ9Imh0bWxfYmIzODhlYTQ5MTQxNGUwMWFhMzk2ODQ4ZTUwN2EyNTgiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPldlc3QgQnJpZ2h0b248L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzVjZDRkYmJkYzAwYTRlZDE5ZjlhYzg0ZWYwYmFmZDNiLnNldENvbnRlbnQoaHRtbF9iYjM4OGVhNDkxNDE0ZTAxYWEzOTY4NDhlNTA3YTI1OCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl80YjIzYWQ5ODlmMzc0NmY1YjVhYzg2ZjljMjE1ZjJiMS5iaW5kUG9wdXAocG9wdXBfNWNkNGRiYmRjMDBhNGVkMTlmOWFjODRlZjBiYWZkM2IpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOTY5NTNjMWU4MGQ2NDlmOGEzYjA4OGY1Mzk0ODY0NGIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42MjQxODQ3OTEzMTMwMDYsLTc0LjA4NzI0ODE5OTgzNzI5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk2N2IyNmYxOTcxNjQ2MDg4MzAzNTYwYjQ0OThjZWFkKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzI0ZTEwNDMxZTNlMTRmYmRhMTUyYWFjNmE4YTcxMTM0ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzBhZDc2ZmEyNjA0YjRhNTM4YjA4NGU0MTM2YzhkOGI4ID0gJCgnPGRpdiBpZD0iaHRtbF8wYWQ3NmZhMjYwNGI0YTUzOGIwODRlNDEzNmM4ZDhiOCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+R3J5bWVzIEhpbGw8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzI0ZTEwNDMxZTNlMTRmYmRhMTUyYWFjNmE4YTcxMTM0LnNldENvbnRlbnQoaHRtbF8wYWQ3NmZhMjYwNGI0YTUzOGIwODRlNDEzNmM4ZDhiOCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl85Njk1M2MxZTgwZDY0OWY4YTNiMDg4ZjUzOTQ4NjQ0Yi5iaW5kUG9wdXAocG9wdXBfMjRlMTA0MzFlM2UxNGZiZGExNTJhYWM2YThhNzExMzQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYjI4NzhkOTNkY2M2NDIzYzllNmQ1MmM4Y2MzMjIxNmIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41OTcwNjg1MTgxNDY3MywtNzQuMTExMzI4ODE4MDA4OF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NjdiMjZmMTk3MTY0NjA4ODMwMzU2MGI0NDk4Y2VhZCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8yYjRkMzBiNzhkZmU0ZTJjODRiZjIxNmUyMWYxODBlNyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9hNTk2MTRkNGY2YjI0ZWRhYmMyOTk5N2NiZTQ0NmI1ZSA9ICQoJzxkaXYgaWQ9Imh0bWxfYTU5NjE0ZDRmNmIyNGVkYWJjMjk5OTdjYmU0NDZiNWUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRvZHQgSGlsbDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMmI0ZDMwYjc4ZGZlNGUyYzg0YmYyMTZlMjFmMTgwZTcuc2V0Q29udGVudChodG1sX2E1OTYxNGQ0ZjZiMjRlZGFiYzI5OTk3Y2JlNDQ2YjVlKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2IyODc4ZDkzZGNjNjQyM2M5ZTZkNTJjOGNjMzIyMTZiLmJpbmRQb3B1cChwb3B1cF8yYjRkMzBiNzhkZmU0ZTJjODRiZjIxNmUyMWYxODBlNyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl85ZjFjYWNjN2E5MjY0OTlkYmNlMWFkMDIyZWY3NDUwOSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjU4MDI0NzQxMzUwOTU2LC03NC4wNzk1NTI5MjUzOTgyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk2N2IyNmYxOTcxNjQ2MDg4MzAzNTYwYjQ0OThjZWFkKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzI2ZTIwZDdiZjFkZDQ2OGM5YTY3Y2EzNGM1MDliZmU3ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2ZkMzc2NTgxYTM1NDQ4OWRhMjA3NGU1ZTlkOWZhOTZkID0gJCgnPGRpdiBpZD0iaHRtbF9mZDM3NjU4MWEzNTQ0ODlkYTIwNzRlNWU5ZDlmYTk2ZCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+U291dGggQmVhY2g8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzI2ZTIwZDdiZjFkZDQ2OGM5YTY3Y2EzNGM1MDliZmU3LnNldENvbnRlbnQoaHRtbF9mZDM3NjU4MWEzNTQ0ODlkYTIwNzRlNWU5ZDlmYTk2ZCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl85ZjFjYWNjN2E5MjY0OTlkYmNlMWFkMDIyZWY3NDUwOS5iaW5kUG9wdXAocG9wdXBfMjZlMjBkN2JmMWRkNDY4YzlhNjdjYTM0YzUwOWJmZTcpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMGM0YjRhNDIyNWVhNDdiMGFiY2U2YjU2YWQxM2EwMmMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42MzM2NjkzMDU1NDM2NSwtNzQuMTI5NDM0MjY3OTcwMDhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTY3YjI2ZjE5NzE2NDYwODgzMDM1NjBiNDQ5OGNlYWQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNWQxNmRiMWQ3MzM1NDM5OTljYzgwZjA2ODllNzI5NTcgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOTM3YmNlZGNjMGI1NGY1M2E1YTRjNTJlNzk1ZTBmMzcgPSAkKCc8ZGl2IGlkPSJodG1sXzkzN2JjZWRjYzBiNTRmNTNhNWE0YzUyZTc5NWUwZjM3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Qb3J0IFJpY2htb25kPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF81ZDE2ZGIxZDczMzU0Mzk5OWNjODBmMDY4OWU3Mjk1Ny5zZXRDb250ZW50KGh0bWxfOTM3YmNlZGNjMGI1NGY1M2E1YTRjNTJlNzk1ZTBmMzcpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMGM0YjRhNDIyNWVhNDdiMGFiY2U2YjU2YWQxM2EwMmMuYmluZFBvcHVwKHBvcHVwXzVkMTZkYjFkNzMzNTQzOTk5Y2M4MGYwNjg5ZTcyOTU3KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2I0MjNlNTdhZDIzZjRiNjk4ZWQwNzNmMjI4MjUyZDMwID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjMyNTQ2MzkwNDgxMTI0LC03NC4xNTAwODUzNzA0Njk4MV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NjdiMjZmMTk3MTY0NjA4ODMwMzU2MGI0NDk4Y2VhZCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF85YjcyYjE5YTU1NWI0OTU2OTZlMGQ4OTAyMzAxMjYzZCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF82NjI5NGNlZGI3MTQ0ZDliYTAyMTY4NjU2YjU2YTNiMCA9ICQoJzxkaXYgaWQ9Imh0bWxfNjYyOTRjZWRiNzE0NGQ5YmEwMjE2ODY1NmI1NmEzYjAiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk1hcmluZXImIzM5O3MgSGFyYm9yPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF85YjcyYjE5YTU1NWI0OTU2OTZlMGQ4OTAyMzAxMjYzZC5zZXRDb250ZW50KGh0bWxfNjYyOTRjZWRiNzE0NGQ5YmEwMjE2ODY1NmI1NmEzYjApOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYjQyM2U1N2FkMjNmNGI2OThlZDA3M2YyMjgyNTJkMzAuYmluZFBvcHVwKHBvcHVwXzliNzJiMTlhNTU1YjQ5NTY5NmUwZDg5MDIzMDEyNjNkKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2VjY2MzNmRkM2Y1YzQyYTE5MGQzZWQ4MGY2NjcwMjk1ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjM5NjgyOTc4NDU1NDIsLTc0LjE3NDY0NTMyOTkzNTQyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk2N2IyNmYxOTcxNjQ2MDg4MzAzNTYwYjQ0OThjZWFkKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzVlZGI4MjVkN2Y4MTRhN2Q4MGFhYjc2YWJhMWZiYTc0ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzU4MDlkODZmZjBlNzQ4YmQ5ZDM5MWQ3Y2ZiOTQ3OTI0ID0gJCgnPGRpdiBpZD0iaHRtbF81ODA5ZDg2ZmYwZTc0OGJkOWQzOTFkN2NmYjk0NzkyNCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+UG9ydCBJdm9yeTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNWVkYjgyNWQ3ZjgxNGE3ZDgwYWFiNzZhYmExZmJhNzQuc2V0Q29udGVudChodG1sXzU4MDlkODZmZjBlNzQ4YmQ5ZDM5MWQ3Y2ZiOTQ3OTI0KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2VjY2MzNmRkM2Y1YzQyYTE5MGQzZWQ4MGY2NjcwMjk1LmJpbmRQb3B1cChwb3B1cF81ZWRiODI1ZDdmODE0YTdkODBhYWI3NmFiYTFmYmE3NCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9lNmJkNzFmODA0ZTg0ZDVjOGUzYjcwYWY0ZjVhNmMxOCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYxMzMzNTkzNzY2NzQyLC03NC4xMTkxODA1ODUzNDg0Ml0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NjdiMjZmMTk3MTY0NjA4ODMwMzU2MGI0NDk4Y2VhZCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9jMTg5NDFlY2MyYjU0YzAyOTQ1NmY4MjVlNDUxNDNhMiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF85MTFkNTRlYzQ3OGY0MDVkOTI1NjcyYzI3OGM0MDY0NCA9ICQoJzxkaXYgaWQ9Imh0bWxfOTExZDU0ZWM0NzhmNDA1ZDkyNTY3MmMyNzhjNDA2NDQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNhc3RsZXRvbiBDb3JuZXJzPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9jMTg5NDFlY2MyYjU0YzAyOTQ1NmY4MjVlNDUxNDNhMi5zZXRDb250ZW50KGh0bWxfOTExZDU0ZWM0NzhmNDA1ZDkyNTY3MmMyNzhjNDA2NDQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZTZiZDcxZjgwNGU4NGQ1YzhlM2I3MGFmNGY1YTZjMTguYmluZFBvcHVwKHBvcHVwX2MxODk0MWVjYzJiNTRjMDI5NDU2ZjgyNWU0NTE0M2EyKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzc3OWNlYTkwOGI0YjQ5ZTNhZWM0ZmMwNWZmMWYzNDk1ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTk0MjUyMzc5MTYxNjk1LC03NC4xNjQ5NjAzMTMyOTgyN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NjdiMjZmMTk3MTY0NjA4ODMwMzU2MGI0NDk4Y2VhZCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8xZWI5MWIxZmRlMTA0ODU2ODI4MGQwMDAyOWM1YTVmYiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8zYWRmZjY3NjgzOTM0MTkzYTA3NjNmOTRkODUwN2VmZiA9ICQoJzxkaXYgaWQ9Imh0bWxfM2FkZmY2NzY4MzkzNDE5M2EwNzYzZjk0ZDg1MDdlZmYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk5ldyBTcHJpbmd2aWxsZTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMWViOTFiMWZkZTEwNDg1NjgyODBkMDAwMjljNWE1ZmIuc2V0Q29udGVudChodG1sXzNhZGZmNjc2ODM5MzQxOTNhMDc2M2Y5NGQ4NTA3ZWZmKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzc3OWNlYTkwOGI0YjQ5ZTNhZWM0ZmMwNWZmMWYzNDk1LmJpbmRQb3B1cChwb3B1cF8xZWI5MWIxZmRlMTA0ODU2ODI4MGQwMDAyOWM1YTVmYik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9iZDQ1NmY3Mjk1ZWU0ZjdmYTc3ZWRhZTViOWY5Yjc3NSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjU4NjMxMzc1MTAzMjgxLC03NC4xOTA3MzcxNzUzODExNl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NjdiMjZmMTk3MTY0NjA4ODMwMzU2MGI0NDk4Y2VhZCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8yYzc2YzU0MDQ0MzM0MTZjOTI0MTg1ZDkxMzZjMDdlZCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF83NThmYzA1MzViYTA0MzM2OWViMTg2Y2ZkOWM4YjU3ZiA9ICQoJzxkaXYgaWQ9Imh0bWxfNzU4ZmMwNTM1YmEwNDMzNjllYjE4NmNmZDljOGI1N2YiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRyYXZpczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMmM3NmM1NDA0NDMzNDE2YzkyNDE4NWQ5MTM2YzA3ZWQuc2V0Q29udGVudChodG1sXzc1OGZjMDUzNWJhMDQzMzY5ZWIxODZjZmQ5YzhiNTdmKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2JkNDU2ZjcyOTVlZTRmN2ZhNzdlZGFlNWI5ZjliNzc1LmJpbmRQb3B1cChwb3B1cF8yYzc2YzU0MDQ0MzM0MTZjOTI0MTg1ZDkxMzZjMDdlZCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl82ZTI2MDVkZTdiM2M0NWU0YTBhN2MyMTdhM2I0Y2M3NCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjU3MjU3MjMxODIwNjMyLC03NC4xMTY0Nzk0MzYwNjM4XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk2N2IyNmYxOTcxNjQ2MDg4MzAzNTYwYjQ0OThjZWFkKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2NiZTIwNWNlZjcwZDRmNmE5YzYzZmQ4MzdlZDQ2ZjFhID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2JhMDVkZTViNGJjNzQzMzdiMmFlYjAyNTAyYWRmYTQ5ID0gJCgnPGRpdiBpZD0iaHRtbF9iYTA1ZGU1YjRiYzc0MzM3YjJhZWIwMjUwMmFkZmE0OSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+TmV3IERvcnA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2NiZTIwNWNlZjcwZDRmNmE5YzYzZmQ4MzdlZDQ2ZjFhLnNldENvbnRlbnQoaHRtbF9iYTA1ZGU1YjRiYzc0MzM3YjJhZWIwMjUwMmFkZmE0OSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl82ZTI2MDVkZTdiM2M0NWU0YTBhN2MyMTdhM2I0Y2M3NC5iaW5kUG9wdXAocG9wdXBfY2JlMjA1Y2VmNzBkNGY2YTljNjNmZDgzN2VkNDZmMWEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMTRiZDUyYTU3Y2YyNGY2MjhiN2MyNzFmYzdlZTUzYjMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41NTg0NjIyNDMyODg4LC03NC4xMjE1NjU5Mzc3MTg5Nl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NjdiMjZmMTk3MTY0NjA4ODMwMzU2MGI0NDk4Y2VhZCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8xNzA0NTUyYTQwNzk0ZTIxYmVmNjBlZWE3MGQ4ZGY3MCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF83ZDI1YTQxZTA1M2I0YzQ3ODFkODViYjFkOTQ1ZjRmZCA9ICQoJzxkaXYgaWQ9Imh0bWxfN2QyNWE0MWUwNTNiNGM0NzgxZDg1YmIxZDk0NWY0ZmQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk9ha3dvb2Q8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzE3MDQ1NTJhNDA3OTRlMjFiZWY2MGVlYTcwZDhkZjcwLnNldENvbnRlbnQoaHRtbF83ZDI1YTQxZTA1M2I0YzQ3ODFkODViYjFkOTQ1ZjRmZCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8xNGJkNTJhNTdjZjI0ZjYyOGI3YzI3MWZjN2VlNTNiMy5iaW5kUG9wdXAocG9wdXBfMTcwNDU1MmE0MDc5NGUyMWJlZjYwZWVhNzBkOGRmNzApOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNzVmNmNlNDk3YWQ1NGNlNjhhNTYwYWE1MTJmMjk5YTEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41NDk0ODAyMjg3MTM2MDUsLTc0LjE0OTMyMzgxNDkwOTkyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk2N2IyNmYxOTcxNjQ2MDg4MzAzNTYwYjQ0OThjZWFkKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzNlNGJiOGM0OGI3MDQ5ZjBiMTQ2ZGI4NTExNzlhZGNlID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2JhOTU0NzM1YzUwMzRhOWQ5MjcyMWI5ODM1NWY5OGUyID0gJCgnPGRpdiBpZD0iaHRtbF9iYTk1NDczNWM1MDM0YTlkOTI3MjFiOTgzNTVmOThlMiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+R3JlYXQgS2lsbHM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzNlNGJiOGM0OGI3MDQ5ZjBiMTQ2ZGI4NTExNzlhZGNlLnNldENvbnRlbnQoaHRtbF9iYTk1NDczNWM1MDM0YTlkOTI3MjFiOTgzNTVmOThlMik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl83NWY2Y2U0OTdhZDU0Y2U2OGE1NjBhYTUxMmYyOTlhMS5iaW5kUG9wdXAocG9wdXBfM2U0YmI4YzQ4YjcwNDlmMGIxNDZkYjg1MTE3OWFkY2UpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMjhmMTQ2ODYyYTAzNDk2NThhNTk3ZjQzYzc5MmFmOGYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41NDIyMzA3NDc0NTA3NDUsLTc0LjE2NDMzMDgwNDE5MzZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTY3YjI2ZjE5NzE2NDYwODgzMDM1NjBiNDQ5OGNlYWQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMGQ2NjMyOGQ1NWNkNDhiODllNjEwOTI5YjAxYzIyN2QgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNDRiM2E2ZTE1YmZkNGIzZTk5YzhmYWJkMDRlOTIzMjUgPSAkKCc8ZGl2IGlkPSJodG1sXzQ0YjNhNmUxNWJmZDRiM2U5OWM4ZmFiZDA0ZTkyMzI1IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5FbHRpbmd2aWxsZTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMGQ2NjMyOGQ1NWNkNDhiODllNjEwOTI5YjAxYzIyN2Quc2V0Q29udGVudChodG1sXzQ0YjNhNmUxNWJmZDRiM2U5OWM4ZmFiZDA0ZTkyMzI1KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzI4ZjE0Njg2MmEwMzQ5NjU4YTU5N2Y0M2M3OTJhZjhmLmJpbmRQb3B1cChwb3B1cF8wZDY2MzI4ZDU1Y2Q0OGI4OWU2MTA5MjliMDFjMjI3ZCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9iMjEzMzhmMWQzYWQ0YWJmOWUzMWM5NWU4YTRjNGE2OCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjUzODExNDE3NDc0NTA3LC03NC4xNzg1NDg2NjE2NTg3OF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NjdiMjZmMTk3MTY0NjA4ODMwMzU2MGI0NDk4Y2VhZCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9jMTgyYzc4ZWY5MWY0ZGI1YmNkYTZlMzI2ZjU3OWQwYSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8xNWNkZWUwODFhZDQ0ZGMxYTc1NThlMTcwMWQ1ZTI2MCA9ICQoJzxkaXYgaWQ9Imh0bWxfMTVjZGVlMDgxYWQ0NGRjMWE3NTU4ZTE3MDFkNWUyNjAiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkFubmFkYWxlPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9jMTgyYzc4ZWY5MWY0ZGI1YmNkYTZlMzI2ZjU3OWQwYS5zZXRDb250ZW50KGh0bWxfMTVjZGVlMDgxYWQ0NGRjMWE3NTU4ZTE3MDFkNWUyNjApOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYjIxMzM4ZjFkM2FkNGFiZjllMzFjOTVlOGE0YzRhNjguYmluZFBvcHVwKHBvcHVwX2MxODJjNzhlZjkxZjRkYjViY2RhNmUzMjZmNTc5ZDBhKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2IwODI2ZjI1ODU5ZDRhMGNiNmM3ZjE3NjYyZDJlNjg0ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTQxOTY3NjIyODg4NzU1LC03NC4yMDUyNDU4MjQ4MDMyNl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NjdiMjZmMTk3MTY0NjA4ODMwMzU2MGI0NDk4Y2VhZCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF82ZDFiMGI4ZjRlNTE0OGRkODZiMjg4MzMzOTM4YTVhYyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF80ZjJhZGRmY2UyYTU0ODJkYTlhMjQ3N2Y2MDg4YmMyNSA9ICQoJzxkaXYgaWQ9Imh0bWxfNGYyYWRkZmNlMmE1NDgyZGE5YTI0NzdmNjA4OGJjMjUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPldvb2Ryb3c8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzZkMWIwYjhmNGU1MTQ4ZGQ4NmIyODgzMzM5MzhhNWFjLnNldENvbnRlbnQoaHRtbF80ZjJhZGRmY2UyYTU0ODJkYTlhMjQ3N2Y2MDg4YmMyNSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9iMDgyNmYyNTg1OWQ0YTBjYjZjN2YxNzY2MmQyZTY4NC5iaW5kUG9wdXAocG9wdXBfNmQxYjBiOGY0ZTUxNDhkZDg2YjI4ODMzMzkzOGE1YWMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMmRmZDg5YmI4OTE4NDE2M2E3ZjI2YTQ4ZjAyZGJiNTkgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41MDUzMzM3NjExNTY0MiwtNzQuMjQ2NTY5MzQyMzUyODNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTY3YjI2ZjE5NzE2NDYwODgzMDM1NjBiNDQ5OGNlYWQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZjg0ZjgyMTJlODA3NGQ5NzgwZDNiZWEyZjQ1OGE4YmIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNTRjMmQ0MmFlMTJjNGU3OWJkYWNjNjViNTc1YjdhYWYgPSAkKCc8ZGl2IGlkPSJodG1sXzU0YzJkNDJhZTEyYzRlNzliZGFjYzY1YjU3NWI3YWFmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Ub3R0ZW52aWxsZTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZjg0ZjgyMTJlODA3NGQ5NzgwZDNiZWEyZjQ1OGE4YmIuc2V0Q29udGVudChodG1sXzU0YzJkNDJhZTEyYzRlNzliZGFjYzY1YjU3NWI3YWFmKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzJkZmQ4OWJiODkxODQxNjNhN2YyNmE0OGYwMmRiYjU5LmJpbmRQb3B1cChwb3B1cF9mODRmODIxMmU4MDc0ZDk3ODBkM2JlYTJmNDU4YThiYik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9kYjBjNmNmYzA4M2I0YjFjYmUwZDJhMDVlMzUzYWUwMSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYzNzMxNjA2NzExMDMyNiwtNzQuMDgwNTUzNTE3OTAxMTVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTY3YjI2ZjE5NzE2NDYwODgzMDM1NjBiNDQ5OGNlYWQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMzJmODRiMzYyMTk5NGE0NWJjM2EzMzFjZmVmZTZlYjEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZWJjMzkzNzE0NThlNGNkMmEzMzFlY2M2MmQ3ZmFhMjcgPSAkKCc8ZGl2IGlkPSJodG1sX2ViYzM5MzcxNDU4ZTRjZDJhMzMxZWNjNjJkN2ZhYTI3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Ub21wa2luc3ZpbGxlPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8zMmY4NGIzNjIxOTk0YTQ1YmMzYTMzMWNmZWZlNmViMS5zZXRDb250ZW50KGh0bWxfZWJjMzkzNzE0NThlNGNkMmEzMzFlY2M2MmQ3ZmFhMjcpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZGIwYzZjZmMwODNiNGIxY2JlMGQyYTA1ZTM1M2FlMDEuYmluZFBvcHVwKHBvcHVwXzMyZjg0YjM2MjE5OTRhNDViYzNhMzMxY2ZlZmU2ZWIxKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2U0NWM4MTJkMTIzNTQ0NjZhMWYwYTQwOWVlMTA4M2E5ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjE5MTkzMTA3OTI2NzYsLTc0LjA5NjI5MDI5MjM1NDU4XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk2N2IyNmYxOTcxNjQ2MDg4MzAzNTYwYjQ0OThjZWFkKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzE0NzJjNDhhMGQzNDQyY2Q5NzllNmVhY2YzZmQ5NjlkID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzE2ODFlMmVlZDFhNzQ2MWQ5NTE2NjRmYjA2ZmUxMjhlID0gJCgnPGRpdiBpZD0iaHRtbF8xNjgxZTJlZWQxYTc0NjFkOTUxNjY0ZmIwNmZlMTI4ZSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+U2lsdmVyIExha2U8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzE0NzJjNDhhMGQzNDQyY2Q5NzllNmVhY2YzZmQ5NjlkLnNldENvbnRlbnQoaHRtbF8xNjgxZTJlZWQxYTc0NjFkOTUxNjY0ZmIwNmZlMTI4ZSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9lNDVjODEyZDEyMzU0NDY2YTFmMGE0MDllZTEwODNhOS5iaW5kUG9wdXAocG9wdXBfMTQ3MmM0OGEwZDM0NDJjZDk3OWU2ZWFjZjNmZDk2OWQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNDlmYmY3ZDM4NmRkNDlmZWFkZmUyNDBmNTc4MTdkYjYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42MTI3NjAxNTc1NjQ4OSwtNzQuMDk3MTI1NTIxNzg1M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NjdiMjZmMTk3MTY0NjA4ODMwMzU2MGI0NDk4Y2VhZCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9kMTgwNzQ5MzNkMGE0NWExOTA4NjZkNjQ3M2JlODdhOCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8wYmY5M2Y4ZjJkYzA0NWZhYjc1ZWVhMDI5ZjBmN2YwOCA9ICQoJzxkaXYgaWQ9Imh0bWxfMGJmOTNmOGYyZGMwNDVmYWI3NWVlYTAyOWYwZjdmMDgiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlN1bm55c2lkZTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZDE4MDc0OTMzZDBhNDVhMTkwODY2ZDY0NzNiZTg3YTguc2V0Q29udGVudChodG1sXzBiZjkzZjhmMmRjMDQ1ZmFiNzVlZWEwMjlmMGY3ZjA4KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzQ5ZmJmN2QzODZkZDQ5ZmVhZGZlMjQwZjU3ODE3ZGI2LmJpbmRQb3B1cChwb3B1cF9kMTgwNzQ5MzNkMGE0NWExOTA4NjZkNjQ3M2JlODdhOCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9kNWQ2NTUyNGJiYmM0NzI4ODRhYzFhMjlhNmJlNDYzNiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYwOTE5MDQ0NDM0NTU4LC03NC4wODAxNTczNDkzNjI5Nl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NjdiMjZmMTk3MTY0NjA4ODMwMzU2MGI0NDk4Y2VhZCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF80MWMxMTk3MDViZjA0NjUxODliZTcxMDMyNTNlYTk4OSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9lZWQwMGMwNjQ2NjU0NjEyYTMzNzdjOTU0NGE2ZjIwMCA9ICQoJzxkaXYgaWQ9Imh0bWxfZWVkMDBjMDY0NjY1NDYxMmEzMzc3Yzk1NDRhNmYyMDAiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlBhcmsgSGlsbDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNDFjMTE5NzA1YmYwNDY1MTg5YmU3MTAzMjUzZWE5ODkuc2V0Q29udGVudChodG1sX2VlZDAwYzA2NDY2NTQ2MTJhMzM3N2M5NTQ0YTZmMjAwKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2Q1ZDY1NTI0YmJiYzQ3Mjg4NGFjMWEyOWE2YmU0NjM2LmJpbmRQb3B1cChwb3B1cF80MWMxMTk3MDViZjA0NjUxODliZTcxMDMyNTNlYTk4OSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl81NjVhMjY3Y2E2Yzc0OWMxODdkYzY5ZDQ2MTZkN2M1ZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYyMTA5MDQ3Mjc1NDA5LC03NC4xMzMwNDE0Mzk1MTcwNF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NjdiMjZmMTk3MTY0NjA4ODMwMzU2MGI0NDk4Y2VhZCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8yMTdjOGMxOWU3OTg0OTY1YmMwMjA4Y2E1NGNlYzc4ZSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9jMmVlNTBlMDRkNTQ0OTQ4OTI0NWM4ZDQxZjgwNzdiYSA9ICQoJzxkaXYgaWQ9Imh0bWxfYzJlZTUwZTA0ZDU0NDk0ODkyNDVjOGQ0MWY4MDc3YmEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPldlc3RlcmxlaWdoPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8yMTdjOGMxOWU3OTg0OTY1YmMwMjA4Y2E1NGNlYzc4ZS5zZXRDb250ZW50KGh0bWxfYzJlZTUwZTA0ZDU0NDk0ODkyNDVjOGQ0MWY4MDc3YmEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNTY1YTI2N2NhNmM3NDljMTg3ZGM2OWQ0NjE2ZDdjNWUuYmluZFBvcHVwKHBvcHVwXzIxN2M4YzE5ZTc5ODQ5NjViYzAyMDhjYTU0Y2VjNzhlKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2FkYzI1ZjJmMWU2NjQxYzY4MWIxYWMzYzk2Mjk3M2ViID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjIwMTcxNTEyMjMxODg0LC03NC4xNTMxNTI0NjM4Nzc2Ml0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NjdiMjZmMTk3MTY0NjA4ODMwMzU2MGI0NDk4Y2VhZCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9lNjJlOGIyMTYyM2M0YjBhYjM4ZjQzZGUyZTlkMjdjOSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8xYTIwMTM2ZWY1YjI0MWRiOTgyNjRlOWUwNGM1Njc0ZiA9ICQoJzxkaXYgaWQ9Imh0bWxfMWEyMDEzNmVmNWIyNDFkYjk4MjY0ZTllMDRjNTY3NGYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkdyYW5pdGV2aWxsZTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZTYyZThiMjE2MjNjNGIwYWIzOGY0M2RlMmU5ZDI3Yzkuc2V0Q29udGVudChodG1sXzFhMjAxMzZlZjViMjQxZGI5ODI2NGU5ZTA0YzU2NzRmKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2FkYzI1ZjJmMWU2NjQxYzY4MWIxYWMzYzk2Mjk3M2ViLmJpbmRQb3B1cChwb3B1cF9lNjJlOGIyMTYyM2M0YjBhYjM4ZjQzZGUyZTlkMjdjOSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9jZmExMjk3NWUzODM0NjJhODE1YWYyZmU4MGYyMTRiZCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYzNTMyNTA5OTExNDkyLC03NC4xNjUxMDQyMDI0MTEyNF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NjdiMjZmMTk3MTY0NjA4ODMwMzU2MGI0NDk4Y2VhZCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9mMjI4YzczNmM3MTk0YmUwOWRjMzk1YTEwZjhkMjE2MiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF83NTQ5NTQyNzI4YWI0YjE5YjkwMzZkOGU0YjI5YWQ1MCA9ICQoJzxkaXYgaWQ9Imh0bWxfNzU0OTU0MjcyOGFiNGIxOWI5MDM2ZDhlNGIyOWFkNTAiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkFybGluZ3RvbjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZjIyOGM3MzZjNzE5NGJlMDlkYzM5NWExMGY4ZDIxNjIuc2V0Q29udGVudChodG1sXzc1NDk1NDI3MjhhYjRiMTliOTAzNmQ4ZTRiMjlhZDUwKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2NmYTEyOTc1ZTM4MzQ2MmE4MTVhZjJmZTgwZjIxNGJkLmJpbmRQb3B1cChwb3B1cF9mMjI4YzczNmM3MTk0YmUwOWRjMzk1YTEwZjhkMjE2Mik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9lY2Q4ODU5MjFmNDE0MjY2YjZjZTY3MmMwOWRlYzM5YyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjU5NjMxMjU3MTI3NjczNCwtNzQuMDY3MTIzNjMyMjU1NzRdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTY3YjI2ZjE5NzE2NDYwODgzMDM1NjBiNDQ5OGNlYWQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfM2Q1NWUyMzQ4ODg2NDE0ZjlkMjNmZGE4MTNkNzE0MzUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZWQyMTA4MTI1MmUxNDEwNmI1MWM0MTIyYmFhMmJlYzAgPSAkKCc8ZGl2IGlkPSJodG1sX2VkMjEwODEyNTJlMTQxMDZiNTFjNDEyMmJhYTJiZWMwIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5BcnJvY2hhcjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfM2Q1NWUyMzQ4ODg2NDE0ZjlkMjNmZGE4MTNkNzE0MzUuc2V0Q29udGVudChodG1sX2VkMjEwODEyNTJlMTQxMDZiNTFjNDEyMmJhYTJiZWMwKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2VjZDg4NTkyMWY0MTQyNjZiNmNlNjcyYzA5ZGVjMzljLmJpbmRQb3B1cChwb3B1cF8zZDU1ZTIzNDg4ODY0MTRmOWQyM2ZkYTgxM2Q3MTQzNSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl84NzQ1ZjBhYjU2NGE0NjE5OGQwYzdiMTAwYWMyZjg1NCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjU5ODI2ODM1OTU5OTkxLC03NC4wNzY2NzQzNjI3OTA1XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk2N2IyNmYxOTcxNjQ2MDg4MzAzNTYwYjQ0OThjZWFkKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2Q2ZWY1NDQyNWU2MTQ4ZGU4ZWY0NDNjNTVjNjU3NDg5ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzgyOTllMWYyZmJkZjQxODU5ZTEwYjU4MmE2ZDE0NDIwID0gJCgnPGRpdiBpZD0iaHRtbF84Mjk5ZTFmMmZiZGY0MTg1OWUxMGI1ODJhNmQxNDQyMCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+R3Jhc21lcmU8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2Q2ZWY1NDQyNWU2MTQ4ZGU4ZWY0NDNjNTVjNjU3NDg5LnNldENvbnRlbnQoaHRtbF84Mjk5ZTFmMmZiZGY0MTg1OWUxMGI1ODJhNmQxNDQyMCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl84NzQ1ZjBhYjU2NGE0NjE5OGQwYzdiMTAwYWMyZjg1NC5iaW5kUG9wdXAocG9wdXBfZDZlZjU0NDI1ZTYxNDhkZThlZjQ0M2M1NWM2NTc0ODkpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZmE0ZTZhZWMyZDIwNGY5ODhkM2VjODBjYWQ4YTY3NzQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41OTYzMjg5MTM3OTUxMywtNzQuMDg3NTExMTgwMDU1NzhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTY3YjI2ZjE5NzE2NDYwODgzMDM1NjBiNDQ5OGNlYWQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMzFkMWYyYzFlNzlhNDQ0YWJmYWNjMjY3MjA5MzYwYzcgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNzk1NzNmMzM0YjRhNDM1ZGEzOTBhZjkwNGY2NDIwM2YgPSAkKCc8ZGl2IGlkPSJodG1sXzc5NTczZjMzNGI0YTQzNWRhMzkwYWY5MDRmNjQyMDNmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5PbGQgVG93bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMzFkMWYyYzFlNzlhNDQ0YWJmYWNjMjY3MjA5MzYwYzcuc2V0Q29udGVudChodG1sXzc5NTczZjMzNGI0YTQzNWRhMzkwYWY5MDRmNjQyMDNmKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2ZhNGU2YWVjMmQyMDRmOTg4ZDNlYzgwY2FkOGE2Nzc0LmJpbmRQb3B1cChwb3B1cF8zMWQxZjJjMWU3OWE0NDRhYmZhY2MyNjcyMDkzNjBjNyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9mY2QyZTk0NmU4ZjI0OTIwOGJiNWNhZmI1ZDE0ZWZlNiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjU4ODY3Mjk0ODE5OTI3NSwtNzQuMDk2Mzk5MDUzMTI1MjFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTY3YjI2ZjE5NzE2NDYwODgzMDM1NjBiNDQ5OGNlYWQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMWQ0MDViZTc5NTgwNDkwNzg2OWVjM2M0NDQwMjQzYmIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMDFjM2M3OTdmZTY0NDhmN2I5NWIzYTY4Y2FiNGUxY2MgPSAkKCc8ZGl2IGlkPSJodG1sXzAxYzNjNzk3ZmU2NDQ4ZjdiOTViM2E2OGNhYjRlMWNjIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Eb25nYW4gSGlsbHM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzFkNDA1YmU3OTU4MDQ5MDc4NjllYzNjNDQ0MDI0M2JiLnNldENvbnRlbnQoaHRtbF8wMWMzYzc5N2ZlNjQ0OGY3Yjk1YjNhNjhjYWI0ZTFjYyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9mY2QyZTk0NmU4ZjI0OTIwOGJiNWNhZmI1ZDE0ZWZlNi5iaW5kUG9wdXAocG9wdXBfMWQ0MDViZTc5NTgwNDkwNzg2OWVjM2M0NDQwMjQzYmIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfM2IxNjg2ZmU5MjZiNDhmNzkxOWEzZDZhYjQ5MjJlMTggPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41NzM1MjY5MDU3NDI4MywtNzQuMDkzNDgyNjYzMDM1OTFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTY3YjI2ZjE5NzE2NDYwODgzMDM1NjBiNDQ5OGNlYWQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfOTFmY2Q4MzU1ZTJkNDJlMWEyZDMzNTI0MTU5N2VjYmEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMjMyYjNmNGI4ODEwNDZmY2I5ZjQ0NmNhOTM0MTgyZjMgPSAkKCc8ZGl2IGlkPSJodG1sXzIzMmIzZjRiODgxMDQ2ZmNiOWY0NDZjYTkzNDE4MmYzIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5NaWRsYW5kIEJlYWNoPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF85MWZjZDgzNTVlMmQ0MmUxYTJkMzM1MjQxNTk3ZWNiYS5zZXRDb250ZW50KGh0bWxfMjMyYjNmNGI4ODEwNDZmY2I5ZjQ0NmNhOTM0MTgyZjMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfM2IxNjg2ZmU5MjZiNDhmNzkxOWEzZDZhYjQ5MjJlMTguYmluZFBvcHVwKHBvcHVwXzkxZmNkODM1NWUyZDQyZTFhMmQzMzUyNDE1OTdlY2JhKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzFhY2M5OWY5NzVhMjQ1MDlhNzQ3ZDg1MzgzZjlkNGRhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTc2MjE1NTg3MTE3ODgsLTc0LjEwNTg1NTk4NTQ1NDM0XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk2N2IyNmYxOTcxNjQ2MDg4MzAzNTYwYjQ0OThjZWFkKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2Q1MjI2MmFiNDFmZTRjOTNiOWNjMjQ5NDkyNDVlMGJkID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzJkMDQwMTFlYWE3NTQwNDlhMTA0YTZmNjc0ZGE3ZGYzID0gJCgnPGRpdiBpZD0iaHRtbF8yZDA0MDExZWFhNzU0MDQ5YTEwNGE2ZjY3NGRhN2RmMyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+R3JhbnQgQ2l0eTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZDUyMjYyYWI0MWZlNGM5M2I5Y2MyNDk0OTI0NWUwYmQuc2V0Q29udGVudChodG1sXzJkMDQwMTFlYWE3NTQwNDlhMTA0YTZmNjc0ZGE3ZGYzKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzFhY2M5OWY5NzVhMjQ1MDlhNzQ3ZDg1MzgzZjlkNGRhLmJpbmRQb3B1cChwb3B1cF9kNTIyNjJhYjQxZmU0YzkzYjljYzI0OTQ5MjQ1ZTBiZCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl85MjUzZjlkMDhjNGI0ZWMwODVmODY2OTI0ODRlZTY3NCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjU2NDI1NTQ5MzA3MzM1LC03NC4xMDQzMjcwNzQ2OTEyNF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NjdiMjZmMTk3MTY0NjA4ODMwMzU2MGI0NDk4Y2VhZCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8yYzQ5YzRhNzgxZTI0MGRjOTA1ZDNjNmMxZDI1NmRlNCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF82NTNlMDUzNGIxOTQ0MTNhYjYxNmZiZWVhMmFkZDYxMCA9ICQoJzxkaXYgaWQ9Imh0bWxfNjUzZTA1MzRiMTk0NDEzYWI2MTZmYmVlYTJhZGQ2MTAiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk5ldyBEb3JwIEJlYWNoPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8yYzQ5YzRhNzgxZTI0MGRjOTA1ZDNjNmMxZDI1NmRlNC5zZXRDb250ZW50KGh0bWxfNjUzZTA1MzRiMTk0NDEzYWI2MTZmYmVlYTJhZGQ2MTApOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOTI1M2Y5ZDA4YzRiNGVjMDg1Zjg2NjkyNDg0ZWU2NzQuYmluZFBvcHVwKHBvcHVwXzJjNDljNGE3ODFlMjQwZGM5MDVkM2M2YzFkMjU2ZGU0KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2E0ZDZmYTU2ZDcyYjQ0NmFhZDZmOGIxN2Y2NjZhNmE4ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTUzOTg4MDA4NTg0NjIsLTc0LjEzOTE2NjIyMTc1NzY4XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk2N2IyNmYxOTcxNjQ2MDg4MzAzNTYwYjQ0OThjZWFkKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzNiNGEwNjUwOWYxNTQ3N2M4MmUzYmU4YWFmZGIzNGY5ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzJhMTMzM2ZkMTY5NTQ5ZjdiNjgxNTYxZTBhODI4Zjg5ID0gJCgnPGRpdiBpZD0iaHRtbF8yYTEzMzNmZDE2OTU0OWY3YjY4MTU2MWUwYTgyOGY4OSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QmF5IFRlcnJhY2U8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzNiNGEwNjUwOWYxNTQ3N2M4MmUzYmU4YWFmZGIzNGY5LnNldENvbnRlbnQoaHRtbF8yYTEzMzNmZDE2OTU0OWY3YjY4MTU2MWUwYTgyOGY4OSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9hNGQ2ZmE1NmQ3MmI0NDZhYWQ2ZjhiMTdmNjY2YTZhOC5iaW5kUG9wdXAocG9wdXBfM2I0YTA2NTA5ZjE1NDc3YzgyZTNiZThhYWZkYjM0ZjkpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMmZhMDhlZGFkNTI3NGQ0YzhiNzRjYWMyZDY4MTU5NzAgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41MzE5MTE5MjA0ODk2MDUsLTc0LjE5MTc0MTA1NzQ3ODE0XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk2N2IyNmYxOTcxNjQ2MDg4MzAzNTYwYjQ0OThjZWFkKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzM0NGU1NWU0MjZjMDQ3NmJhNWQ2MzM0Mjk5OTJlODJjID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2ZmYzA0MTc1ZWI5ZDQ0MWZhODE0NGM2OWNmMTFiOGFjID0gJCgnPGRpdiBpZD0iaHRtbF9mZmMwNDE3NWViOWQ0NDFmYTgxNDRjNjljZjExYjhhYyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+SHVndWVub3Q8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzM0NGU1NWU0MjZjMDQ3NmJhNWQ2MzM0Mjk5OTJlODJjLnNldENvbnRlbnQoaHRtbF9mZmMwNDE3NWViOWQ0NDFmYTgxNDRjNjljZjExYjhhYyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8yZmEwOGVkYWQ1Mjc0ZDRjOGI3NGNhYzJkNjgxNTk3MC5iaW5kUG9wdXAocG9wdXBfMzQ0ZTU1ZTQyNmMwNDc2YmE1ZDYzMzQyOTk5MmU4MmMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfN2ZkZmJiMWE3MjY2NDk1NGJmOGE1MzA5Mjk3YTRjZDMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41MjQ2OTkzNzYxMTgxMzYsLTc0LjIxOTgzMTA2NjE2Nzc3XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk2N2IyNmYxOTcxNjQ2MDg4MzAzNTYwYjQ0OThjZWFkKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzIzOTFlOGRhMjUxYzRmYTk5NzNiYTRiMGM4OTdiNDMwID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2U4NDM0NWMzZDg4ODQwZjZiYWY3YTY5MTU2ZTQ0NDI0ID0gJCgnPGRpdiBpZD0iaHRtbF9lODQzNDVjM2Q4ODg0MGY2YmFmN2E2OTE1NmU0NDQyNCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+UGxlYXNhbnQgUGxhaW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8yMzkxZThkYTI1MWM0ZmE5OTczYmE0YjBjODk3YjQzMC5zZXRDb250ZW50KGh0bWxfZTg0MzQ1YzNkODg4NDBmNmJhZjdhNjkxNTZlNDQ0MjQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfN2ZkZmJiMWE3MjY2NDk1NGJmOGE1MzA5Mjk3YTRjZDMuYmluZFBvcHVwKHBvcHVwXzIzOTFlOGRhMjUxYzRmYTk5NzNiYTRiMGM4OTdiNDMwKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzVjNjM2NGVkYzJiYzQxYmQ5MTNiYjY0ZmIwNDYzNTUyID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTA2MDgxNjUzNDYzMDUsLTc0LjIyOTUwMzUwMjYwMDI3XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk2N2IyNmYxOTcxNjQ2MDg4MzAzNTYwYjQ0OThjZWFkKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2FlMGI5MjU2M2NiNjRhNTdiZjQ4ZDM2ZTgyODc5ZWQyID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzEzZGU0Njg2YzVkNTRlMzA4YTFjYzc4M2Q0OTZjODcxID0gJCgnPGRpdiBpZD0iaHRtbF8xM2RlNDY4NmM1ZDU0ZTMwOGExY2M3ODNkNDk2Yzg3MSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QnV0bGVyIE1hbm9yPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9hZTBiOTI1NjNjYjY0YTU3YmY0OGQzNmU4Mjg3OWVkMi5zZXRDb250ZW50KGh0bWxfMTNkZTQ2ODZjNWQ1NGUzMDhhMWNjNzgzZDQ5NmM4NzEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNWM2MzY0ZWRjMmJjNDFiZDkxM2JiNjRmYjA0NjM1NTIuYmluZFBvcHVwKHBvcHVwX2FlMGI5MjU2M2NiNjRhNTdiZjQ4ZDM2ZTgyODc5ZWQyKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzZiZDYzZTBjZDYyZDQ2MjZhMTU1M2I1MmUzOTEzMDRmID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTMwNTMxNDgyODMzMTQsLTc0LjIzMjE1Nzc1ODk2NTI2XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk2N2IyNmYxOTcxNjQ2MDg4MzAzNTYwYjQ0OThjZWFkKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2Q0ZTBiMDY4MjA5YjRlYmViM2M4MzgzMjRmNDgzOTE1ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2JmZDY2MjM2OTM3NDQ5MmJhNDg1YjE3ODQ5MmVkOTQ3ID0gJCgnPGRpdiBpZD0iaHRtbF9iZmQ2NjIzNjkzNzQ0OTJiYTQ4NWIxNzg0OTJlZDk0NyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q2hhcmxlc3RvbjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZDRlMGIwNjgyMDliNGViZWIzYzgzODMyNGY0ODM5MTUuc2V0Q29udGVudChodG1sX2JmZDY2MjM2OTM3NDQ5MmJhNDg1YjE3ODQ5MmVkOTQ3KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzZiZDYzZTBjZDYyZDQ2MjZhMTU1M2I1MmUzOTEzMDRmLmJpbmRQb3B1cChwb3B1cF9kNGUwYjA2ODIwOWI0ZWJlYjNjODM4MzI0ZjQ4MzkxNSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9iYjFhMjQxY2E0NmM0MjMyOTE5NzY4NDY3OTFkMzQzMSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjU0OTQwNDAwNjUwMDcyLC03NC4yMTU3Mjg1MTExMzk1Ml0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NjdiMjZmMTk3MTY0NjA4ODMwMzU2MGI0NDk4Y2VhZCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9lODJhZDczYzU3MTE0NTY4ODk1MDM1MDRmNGVlNzVkOCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9lNWNkYjFhNjI2OTY0NjAyYjUzNDBhYWQ1OTk3NjdlMiA9ICQoJzxkaXYgaWQ9Imh0bWxfZTVjZGIxYTYyNjk2NDYwMmI1MzQwYWFkNTk5NzY3ZTIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlJvc3N2aWxsZTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZTgyYWQ3M2M1NzExNDU2ODg5NTAzNTA0ZjRlZTc1ZDguc2V0Q29udGVudChodG1sX2U1Y2RiMWE2MjY5NjQ2MDJiNTM0MGFhZDU5OTc2N2UyKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2JiMWEyNDFjYTQ2YzQyMzI5MTk3Njg0Njc5MWQzNDMxLmJpbmRQb3B1cChwb3B1cF9lODJhZDczYzU3MTE0NTY4ODk1MDM1MDRmNGVlNzVkOCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9hNmMxMjNhZmVmNTQ0NDk0OGRmZmY4YWRhODhlNDA1MCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjU0OTI4NTgyMjc4MzIxLC03NC4xODU4ODY3NDU4Mzg5M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NjdiMjZmMTk3MTY0NjA4ODMwMzU2MGI0NDk4Y2VhZCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF81ZDFmZTk2OTZjNTU0NTMxYTliNWIxMzkwMmQwNWMzOCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8xNDgwODQ4MWFkZmE0ZTQzYjIxMWM2MWE1MWJmMGQxNSA9ICQoJzxkaXYgaWQ9Imh0bWxfMTQ4MDg0ODFhZGZhNGU0M2IyMTFjNjFhNTFiZjBkMTUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkFyZGVuIEhlaWdodHM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzVkMWZlOTY5NmM1NTQ1MzFhOWI1YjEzOTAyZDA1YzM4LnNldENvbnRlbnQoaHRtbF8xNDgwODQ4MWFkZmE0ZTQzYjIxMWM2MWE1MWJmMGQxNSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9hNmMxMjNhZmVmNTQ0NDk0OGRmZmY4YWRhODhlNDA1MC5iaW5kUG9wdXAocG9wdXBfNWQxZmU5Njk2YzU1NDUzMWE5YjViMTM5MDJkMDVjMzgpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZWJjOGEzMWY5N2FmNGRhZmE3YWQ2Mzc2MWEyZmRjM2EgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41NTUyOTUyMzYxNzMxOTQsLTc0LjE3MDc5NDE0Nzg2MDkyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk2N2IyNmYxOTcxNjQ2MDg4MzAzNTYwYjQ0OThjZWFkKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzg4MDY4ZTMwZTI4ZjQxMzBiZDZmYzlmMGI0MzgyOGRkID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzFkMDdhYjI3MDQ0OTQ0M2E4NDhlNTk1YjdhZDk1N2U3ID0gJCgnPGRpdiBpZD0iaHRtbF8xZDA3YWIyNzA0NDk0NDNhODQ4ZTU5NWI3YWQ5NTdlNyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+R3JlZW5yaWRnZTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfODgwNjhlMzBlMjhmNDEzMGJkNmZjOWYwYjQzODI4ZGQuc2V0Q29udGVudChodG1sXzFkMDdhYjI3MDQ0OTQ0M2E4NDhlNTk1YjdhZDk1N2U3KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2ViYzhhMzFmOTdhZjRkYWZhN2FkNjM3NjFhMmZkYzNhLmJpbmRQb3B1cChwb3B1cF84ODA2OGUzMGUyOGY0MTMwYmQ2ZmM5ZjBiNDM4MjhkZCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9iZjZjMTA0YmY1ODg0YTE5OWZjMjE4MTlkOGExNDMyNyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjU4OTEzODk0ODc1MjgxLC03NC4xNTkwMjIwODE1NjYwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NjdiMjZmMTk3MTY0NjA4ODMwMzU2MGI0NDk4Y2VhZCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8zMjA5N2ZkY2JmMmY0NjFmODc4MDc5ZTgwOTMwMzdkZiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9mYjc3OTVjOGVhYzY0ZWI3YmQzM2MyZWFlZmUxN2JiYyA9ICQoJzxkaXYgaWQ9Imh0bWxfZmI3Nzk1YzhlYWM2NGViN2JkMzNjMmVhZWZlMTdiYmMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkhlYXJ0bGFuZCBWaWxsYWdlPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8zMjA5N2ZkY2JmMmY0NjFmODc4MDc5ZTgwOTMwMzdkZi5zZXRDb250ZW50KGh0bWxfZmI3Nzk1YzhlYWM2NGViN2JkMzNjMmVhZWZlMTdiYmMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYmY2YzEwNGJmNTg4NGExOTlmYzIxODE5ZDhhMTQzMjcuYmluZFBvcHVwKHBvcHVwXzMyMDk3ZmRjYmYyZjQ2MWY4NzgwNzllODA5MzAzN2RmKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzhhNmQzM2RkY2ExODQ5ZGViYTBiYzczOGI0NWRjYTkwID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTk0NzI2MDI3NDYyOTUsLTc0LjE4OTU2MDQ1NTE5NjldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTY3YjI2ZjE5NzE2NDYwODgzMDM1NjBiNDQ5OGNlYWQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMGUxMjQzMDE1MmFmNDhmMTk5Nzg4OGI2NWM0OWNmNWQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZTRhZWMxNmU0MWMyNDJjNTgxYWFkMTMzYmIwYWM2NTcgPSAkKCc8ZGl2IGlkPSJodG1sX2U0YWVjMTZlNDFjMjQyYzU4MWFhZDEzM2JiMGFjNjU3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DaGVsc2VhPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8wZTEyNDMwMTUyYWY0OGYxOTk3ODg4YjY1YzQ5Y2Y1ZC5zZXRDb250ZW50KGh0bWxfZTRhZWMxNmU0MWMyNDJjNTgxYWFkMTMzYmIwYWM2NTcpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOGE2ZDMzZGRjYTE4NDlkZWJhMGJjNzM4YjQ1ZGNhOTAuYmluZFBvcHVwKHBvcHVwXzBlMTI0MzAxNTJhZjQ4ZjE5OTc4ODhiNjVjNDljZjVkKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzFlMzhlNzUxMzlhMDRhNTJhZjU5ZDNhNTg1YmRiMmM4ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjA1Nzc4Njg0NTIzNTgsLTc0LjE4NzI1NjM4MzgxNTY3XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk2N2IyNmYxOTcxNjQ2MDg4MzAzNTYwYjQ0OThjZWFkKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzgzYmVlMjhhZmIwODRiYzhhYzgzZTMxMjEwMTRlZDRmID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzczYWQyYjUzNWNlODRkMDhhYTk0NTViYmY4NzNiNmJkID0gJCgnPGRpdiBpZD0iaHRtbF83M2FkMmI1MzVjZTg0ZDA4YWE5NDU1YmJmODczYjZiZCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Qmxvb21maWVsZDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfODNiZWUyOGFmYjA4NGJjOGFjODNlMzEyMTAxNGVkNGYuc2V0Q29udGVudChodG1sXzczYWQyYjUzNWNlODRkMDhhYTk0NTViYmY4NzNiNmJkKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzFlMzhlNzUxMzlhMDRhNTJhZjU5ZDNhNTg1YmRiMmM4LmJpbmRQb3B1cChwb3B1cF84M2JlZTI4YWZiMDg0YmM4YWM4M2UzMTIxMDE0ZWQ0Zik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9lNjExOWZlYmJmZTU0ZmFkOWJhNzBiMjNhMmEwZmE3NCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYwOTU5MTgwMDQyMDMsLTc0LjE1OTQwOTQ4NjU3MTIyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk2N2IyNmYxOTcxNjQ2MDg4MzAzNTYwYjQ0OThjZWFkKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2EyMmE4MmYyZjUwODQ4M2Y5NDFhOGM5ZWY5NzNmMTJiID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzNiYTZlMzlkMzA0OTQ5MmI5Mzg5NGRjZDU5N2M3YjQxID0gJCgnPGRpdiBpZD0iaHRtbF8zYmE2ZTM5ZDMwNDk0OTJiOTM4OTRkY2Q1OTdjN2I0MSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QnVsbHMgSGVhZDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYTIyYTgyZjJmNTA4NDgzZjk0MWE4YzllZjk3M2YxMmIuc2V0Q29udGVudChodG1sXzNiYTZlMzlkMzA0OTQ5MmI5Mzg5NGRjZDU5N2M3YjQxKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2U2MTE5ZmViYmZlNTRmYWQ5YmE3MGIyM2EyYTBmYTc0LmJpbmRQb3B1cChwb3B1cF9hMjJhODJmMmY1MDg0ODNmOTQxYThjOWVmOTczZjEyYik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl80NmRkN2MwNTMxNTY0NTZmOWM3ODI3NGZlZDMxZDcyNSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjU2OTYwNTk0Mjc1NTA1LC03NC4xMzQwNTcyOTg2MjU3XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk2N2IyNmYxOTcxNjQ2MDg4MzAzNTYwYjQ0OThjZWFkKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzA5MDI0Y2YxNDZmODQzYzZhN2FlM2VjOGZjMTFkOTg4ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2ViMDJhZTFiMTZiMjQ3MDA5N2I5OThiMjg3MDBmYjUxID0gJCgnPGRpdiBpZD0iaHRtbF9lYjAyYWUxYjE2YjI0NzAwOTdiOTk4YjI4NzAwZmI1MSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+UmljaG1vbmQgVG93bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMDkwMjRjZjE0NmY4NDNjNmE3YWUzZWM4ZmMxMWQ5ODguc2V0Q29udGVudChodG1sX2ViMDJhZTFiMTZiMjQ3MDA5N2I5OThiMjg3MDBmYjUxKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzQ2ZGQ3YzA1MzE1NjQ1NmY5Yzc4Mjc0ZmVkMzFkNzI1LmJpbmRQb3B1cChwb3B1cF8wOTAyNGNmMTQ2Zjg0M2M2YTdhZTNlYzhmYzExZDk4OCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8xMDA0M2I1ZTQxNWY0MDU0ODI5MDZiN2NjNWU0MzVhZiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYwOTcxOTM0MDc5Mjg0LC03NC4wNjY2Nzc2NjA2MTc3MV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NjdiMjZmMTk3MTY0NjA4ODMwMzU2MGI0NDk4Y2VhZCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF80ZTgyOWIyNTcyYjY0ZjdiYmIyZmYyYjAzMTM0MmQ4OSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF82YWU0OTI3ZDAxMDA0YzA4ODVmZWZlMGM5NDVhOTE5OCA9ICQoJzxkaXYgaWQ9Imh0bWxfNmFlNDkyN2QwMTAwNGMwODg1ZmVmZTBjOTQ1YTkxOTgiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlNob3JlIEFjcmVzPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF80ZTgyOWIyNTcyYjY0ZjdiYmIyZmYyYjAzMTM0MmQ4OS5zZXRDb250ZW50KGh0bWxfNmFlNDkyN2QwMTAwNGMwODg1ZmVmZTBjOTQ1YTkxOTgpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMTAwNDNiNWU0MTVmNDA1NDgyOTA2YjdjYzVlNDM1YWYuYmluZFBvcHVwKHBvcHVwXzRlODI5YjI1NzJiNjRmN2JiYjJmZjJiMDMxMzQyZDg5KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2U2NGM0MzI4NTAzOTRkMTQ4YjFkNDg1Njg5ZTFkOWNiID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjE5MTc4NDUyMDI4NDMsLTc0LjA3MjY0MjQ0NTQ4NF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NjdiMjZmMTk3MTY0NjA4ODMwMzU2MGI0NDk4Y2VhZCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF82YWJjNzcwNmM0ZGI0NWMxODYyYmE1NmEwNDhmNGNjMiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF84MGZjZGEwODViYTU0MGMzYTFkYWU3M2EyNTE1NmYzNSA9ICQoJzxkaXYgaWQ9Imh0bWxfODBmY2RhMDg1YmE1NDBjM2ExZGFlNzNhMjUxNTZmMzUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNsaWZ0b248L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzZhYmM3NzA2YzRkYjQ1YzE4NjJiYTU2YTA0OGY0Y2MyLnNldENvbnRlbnQoaHRtbF84MGZjZGEwODViYTU0MGMzYTFkYWU3M2EyNTE1NmYzNSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9lNjRjNDMyODUwMzk0ZDE0OGIxZDQ4NTY4OWUxZDljYi5iaW5kUG9wdXAocG9wdXBfNmFiYzc3MDZjNGRiNDVjMTg2MmJhNTZhMDQ4ZjRjYzIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMGU3M2ExNWM1MDhiNDc2YTg3MDBhZWVhZGNmOTNmYTEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42MDQ0NzMxODk2ODc5LC03NC4wODQwMjM2NDc0MDM1OF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NjdiMjZmMTk3MTY0NjA4ODMwMzU2MGI0NDk4Y2VhZCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9jZmYwMzE1YjU5ZDU0NGQzOTA0MWE0YTgxMGM2N2E3MCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9lMjE2NjZkODdmZTY0YWU4OGRmMDYzOThiZjAzOWRlYSA9ICQoJzxkaXYgaWQ9Imh0bWxfZTIxNjY2ZDg3ZmU2NGFlODhkZjA2Mzk4YmYwMzlkZWEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNvbmNvcmQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2NmZjAzMTViNTlkNTQ0ZDM5MDQxYTRhODEwYzY3YTcwLnNldENvbnRlbnQoaHRtbF9lMjE2NjZkODdmZTY0YWU4OGRmMDYzOThiZjAzOWRlYSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8wZTczYTE1YzUwOGI0NzZhODcwMGFlZWFkY2Y5M2ZhMS5iaW5kUG9wdXAocG9wdXBfY2ZmMDMxNWI1OWQ1NDRkMzkwNDFhNGE4MTBjNjdhNzApOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfODIwNDVmN2I3MTQ3NDBkMjhjZTJjMjhhMjE5ODZhNTkgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42MDY3OTQzOTQ4MDEsLTc0LjA5Nzc2MjA2OTcyNTIyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk2N2IyNmYxOTcxNjQ2MDg4MzAzNTYwYjQ0OThjZWFkKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzY2M2Q2ODI1NTQ4ODRkZTZiOWFmY2NhYmRhZTk3OTUxID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2NiZDFjYjI2MTVlYjQ3OTI5ZTY5N2Y2NjIyNzkzMTE2ID0gJCgnPGRpdiBpZD0iaHRtbF9jYmQxY2IyNjE1ZWI0NzkyOWU2OTdmNjYyMjc5MzExNiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RW1lcnNvbiBIaWxsPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF82NjNkNjgyNTU0ODg0ZGU2YjlhZmNjYWJkYWU5Nzk1MS5zZXRDb250ZW50KGh0bWxfY2JkMWNiMjYxNWViNDc5MjllNjk3ZjY2MjI3OTMxMTYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfODIwNDVmN2I3MTQ3NDBkMjhjZTJjMjhhMjE5ODZhNTkuYmluZFBvcHVwKHBvcHVwXzY2M2Q2ODI1NTQ4ODRkZTZiOWFmY2NhYmRhZTk3OTUxKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzliYjU4ZjMxYThmNDRhY2FiZGUwZWVkYTJlOTlkZDJlID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjM1NjMwMDA2ODExNTEsLTc0LjA5ODA1MDYyMzczODg3XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk2N2IyNmYxOTcxNjQ2MDg4MzAzNTYwYjQ0OThjZWFkKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzlmZTYwNzZlY2IzZjQyOGI5NzBmMDYyMGUzZDRiNDRiID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzU1ZGNlYWNiMWQ4MDRiMmM4ZWUwYjAxN2U2NTg0YWY4ID0gJCgnPGRpdiBpZD0iaHRtbF81NWRjZWFjYjFkODA0YjJjOGVlMGIwMTdlNjU4NGFmOCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+UmFuZGFsbCBNYW5vcjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOWZlNjA3NmVjYjNmNDI4Yjk3MGYwNjIwZTNkNGI0NGIuc2V0Q29udGVudChodG1sXzU1ZGNlYWNiMWQ4MDRiMmM4ZWUwYjAxN2U2NTg0YWY4KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzliYjU4ZjMxYThmNDRhY2FiZGUwZWVkYTJlOTlkZDJlLmJpbmRQb3B1cChwb3B1cF85ZmU2MDc2ZWNiM2Y0MjhiOTcwZjA2MjBlM2Q0YjQ0Yik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9jNTQ2ODlmYjRjYTQ0YzQ4YjM1ZmMxMGI0NjBlMTM3NyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYzODQzMjgzNzk0Nzk1LC03NC4xODYyMjMzMTc0OTgyM10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NjdiMjZmMTk3MTY0NjA4ODMwMzU2MGI0NDk4Y2VhZCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8wYjI4NzI5MzYyOTI0N2VhYmFkNTYxNjM2MWU5ODMzOSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9hODc3NThlZmYyOWU0OTJlOGI0MWFlNTNkMjg2MWRjMSA9ICQoJzxkaXYgaWQ9Imh0bWxfYTg3NzU4ZWZmMjllNDkyZThiNDFhZTUzZDI4NjFkYzEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkhvd2xhbmQgSG9vazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMGIyODcyOTM2MjkyNDdlYWJhZDU2MTYzNjFlOTgzMzkuc2V0Q29udGVudChodG1sX2E4Nzc1OGVmZjI5ZTQ5MmU4YjQxYWU1M2QyODYxZGMxKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2M1NDY4OWZiNGNhNDRjNDhiMzVmYzEwYjQ2MGUxMzc3LmJpbmRQb3B1cChwb3B1cF8wYjI4NzI5MzYyOTI0N2VhYmFkNTYxNjM2MWU5ODMzOSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl81YWViZDljMDExYmM0MjQwOTA5YjEzM2I4MzQ3ZWJmMSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYzMDE0Njc0MTE5MzgyNiwtNzQuMTQxODE2Nzg5Njg4OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NjdiMjZmMTk3MTY0NjA4ODMwMzU2MGI0NDk4Y2VhZCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF83OTkzZmUwNTA4NWI0NGRjOWZiYzcyZDMzZjhmODNlYSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9kMTQyNDJmYTgwZTk0YWU4YTJiM2RjN2I2NDU0NTkzZiA9ICQoJzxkaXYgaWQ9Imh0bWxfZDE0MjQyZmE4MGU5NGFlOGEyYjNkYzdiNjQ1NDU5M2YiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkVsbSBQYXJrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF83OTkzZmUwNTA4NWI0NGRjOWZiYzcyZDMzZjhmODNlYS5zZXRDb250ZW50KGh0bWxfZDE0MjQyZmE4MGU5NGFlOGEyYjNkYzdiNjQ1NDU5M2YpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNWFlYmQ5YzAxMWJjNDI0MDkwOWIxMzNiODM0N2ViZjEuYmluZFBvcHVwKHBvcHVwXzc5OTNmZTA1MDg1YjQ0ZGM5ZmJjNzJkMzNmOGY4M2VhKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzJiZGE4M2Q3ZWExNTRjYTI5Y2NkZjVjMGFlNmNhNGVmID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjAxODA5NTc2MzE0NDQsLTc0LjEyMDU5Mzk5NzE4MDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk2N2IyNmYxOTcxNjQ2MDg4MzAzNTYwYjQ0OThjZWFkKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzVkMDlkMzAyMzk2NjQyMDI4MWViZjMxMjczYzM5ZWYwID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzVjZTBjMzNjODJlMDQ0YzliMmIxMmMzZTY3MmEzZWU2ID0gJCgnPGRpdiBpZD0iaHRtbF81Y2UwYzMzYzgyZTA0NGM5YjJiMTJjM2U2NzJhM2VlNiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+TWFub3IgSGVpZ2h0czwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNWQwOWQzMDIzOTY2NDIwMjgxZWJmMzEyNzNjMzllZjAuc2V0Q29udGVudChodG1sXzVjZTBjMzNjODJlMDQ0YzliMmIxMmMzZTY3MmEzZWU2KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzJiZGE4M2Q3ZWExNTRjYTI5Y2NkZjVjMGFlNmNhNGVmLmJpbmRQb3B1cChwb3B1cF81ZDA5ZDMwMjM5NjY0MjAyODFlYmYzMTI3M2MzOWVmMCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9mNTdmN2IwZDViM2E0OWIzODM0YWUxZWM4MWE5OWUwYyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYwMzcwNjkyNjI3MzcxLC03NC4xMzIwODQ0NzQ4NDI5OF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NjdiMjZmMTk3MTY0NjA4ODMwMzU2MGI0NDk4Y2VhZCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9kOTFhNmMwZmI4ZDk0Y2NjODYwNWM3ZmVlYWEwMjRkMyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9lOTZhMDdmZWQ3OTQ0NDFmOWE2MTFkNjZjNzNlOWFkZCA9ICQoJzxkaXYgaWQ9Imh0bWxfZTk2YTA3ZmVkNzk0NDQxZjlhNjExZDY2YzczZTlhZGQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPldpbGxvd2Jyb29rPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9kOTFhNmMwZmI4ZDk0Y2NjODYwNWM3ZmVlYWEwMjRkMy5zZXRDb250ZW50KGh0bWxfZTk2YTA3ZmVkNzk0NDQxZjlhNjExZDY2YzczZTlhZGQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZjU3ZjdiMGQ1YjNhNDliMzgzNGFlMWVjODFhOTllMGMuYmluZFBvcHVwKHBvcHVwX2Q5MWE2YzBmYjhkOTRjY2M4NjA1YzdmZWVhYTAyNGQzKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2QzMGJiNjk2NDlmZTRjZDZiODQzNWQ2OWVlYTdlNzQ4ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTQxMTM5OTIyMDkxNzY2LC03NC4yMTc3NjYzNjA2ODU2N10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NjdiMjZmMTk3MTY0NjA4ODMwMzU2MGI0NDk4Y2VhZCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9jNWNlNGMyYmY2ZmE0NjQ4YWUzMTRlYTg5YWVlYTcwZSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF82MzdlNWRlNWY4YTA0NjcwYWNmN2M4YmNjOWQzNzRiYSA9ICQoJzxkaXYgaWQ9Imh0bWxfNjM3ZTVkZTVmOGEwNDY3MGFjZjdjOGJjYzlkMzc0YmEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlNhbmR5IEdyb3VuZDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYzVjZTRjMmJmNmZhNDY0OGFlMzE0ZWE4OWFlZWE3MGUuc2V0Q29udGVudChodG1sXzYzN2U1ZGU1ZjhhMDQ2NzBhY2Y3YzhiY2M5ZDM3NGJhKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2QzMGJiNjk2NDlmZTRjZDZiODQzNWQ2OWVlYTdlNzQ4LmJpbmRQb3B1cChwb3B1cF9jNWNlNGMyYmY2ZmE0NjQ4YWUzMTRlYTg5YWVlYTcwZSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl82YWQxZTJhMGEyNWU0ZjllYjBlMWQ1ZDdiMjdiNjcyZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjU3OTExODc0Mjk2MTIxNCwtNzQuMTI3MjcyNDA2MDQ5NDZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTY3YjI2ZjE5NzE2NDYwODgzMDM1NjBiNDQ5OGNlYWQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMGEwYzEyZjM5YThkNDFiN2EwZjcyZDY4MjllY2EzMDUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfODFhMTVmOTU0NzZiNGRhNzg4ZTE5ZGJkOTJmMzZiYzEgPSAkKCc8ZGl2IGlkPSJodG1sXzgxYTE1Zjk1NDc2YjRkYTc4OGUxOWRiZDkyZjM2YmMxIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5FZ2JlcnR2aWxsZTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMGEwYzEyZjM5YThkNDFiN2EwZjcyZDY4MjllY2EzMDUuc2V0Q29udGVudChodG1sXzgxYTE1Zjk1NDc2YjRkYTc4OGUxOWRiZDkyZjM2YmMxKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzZhZDFlMmEwYTI1ZTRmOWViMGUxZDVkN2IyN2I2NzJlLmJpbmRQb3B1cChwb3B1cF8wYTBjMTJmMzlhOGQ0MWI3YTBmNzJkNjgyOWVjYTMwNSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl84YzY5Zjg1MmQ0ZTU0Y2EzOTVlMjI5Y2VkZjEzMzdmYSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjUyNjI2NDA2NzM0ODEyLC03NC4yMDE1MjU1NjQ1NzY1OF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NjdiMjZmMTk3MTY0NjA4ODMwMzU2MGI0NDk4Y2VhZCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF82MmQ3MWNmZDM2M2Q0NGY3YWFkMzg5NGVhYWJlNzUzOCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF81MmM2NmQxZmJhOTQ0MjZjODZjMGEyMWVkN2I3ODQxYiA9ICQoJzxkaXYgaWQ9Imh0bWxfNTJjNjZkMWZiYTk0NDI2Yzg2YzBhMjFlZDdiNzg0MWIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlByaW5jZSYjMzk7cyBCYXk8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzYyZDcxY2ZkMzYzZDQ0ZjdhYWQzODk0ZWFhYmU3NTM4LnNldENvbnRlbnQoaHRtbF81MmM2NmQxZmJhOTQ0MjZjODZjMGEyMWVkN2I3ODQxYik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl84YzY5Zjg1MmQ0ZTU0Y2EzOTVlMjI5Y2VkZjEzMzdmYS5iaW5kUG9wdXAocG9wdXBfNjJkNzFjZmQzNjNkNDRmN2FhZDM4OTRlYWFiZTc1MzgpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNWExOGQxZTRlZDI5NGZhMmEwYzhiOTg0YzVmMWY2ODggPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41NzY1MDYyOTM3OTQ4OSwtNzQuMTM3OTI2NjM3NzE1NjhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTY3YjI2ZjE5NzE2NDYwODgzMDM1NjBiNDQ5OGNlYWQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZjM0MTE5YjAyNmUyNGJhMzhmZjU0N2I3MDljMmQ2YzkgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZTA1OTgzZmY1MGE2NGY1OTkwZTQ1MDkzNzBlOWZkZTUgPSAkKCc8ZGl2IGlkPSJodG1sX2UwNTk4M2ZmNTBhNjRmNTk5MGU0NTA5MzcwZTlmZGU1IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5MaWdodGhvdXNlIEhpbGw8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2YzNDExOWIwMjZlMjRiYTM4ZmY1NDdiNzA5YzJkNmM5LnNldENvbnRlbnQoaHRtbF9lMDU5ODNmZjUwYTY0ZjU5OTBlNDUwOTM3MGU5ZmRlNSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl81YTE4ZDFlNGVkMjk0ZmEyYTBjOGI5ODRjNWYxZjY4OC5iaW5kUG9wdXAocG9wdXBfZjM0MTE5YjAyNmUyNGJhMzhmZjU0N2I3MDljMmQ2YzkpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYTcyN2NhZjcxYzJiNGNmOThiM2NhMWUyYTZjNDJhMGQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41MTk1NDE0NTc0ODkwOSwtNzQuMjI5NTcwODA2MjY5NDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTY3YjI2ZjE5NzE2NDYwODgzMDM1NjBiNDQ5OGNlYWQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYWI5YWFmMzI0NjVmNGNiYjg0OGQyN2U1NmE0YmU1MjMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMDI1ZjZiZmIyMmE1NDc1ZjljMTljZWQyZmRmM2QyMzggPSAkKCc8ZGl2IGlkPSJodG1sXzAyNWY2YmZiMjJhNTQ3NWY5YzE5Y2VkMmZkZjNkMjM4IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5SaWNobW9uZCBWYWxsZXk8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2FiOWFhZjMyNDY1ZjRjYmI4NDhkMjdlNTZhNGJlNTIzLnNldENvbnRlbnQoaHRtbF8wMjVmNmJmYjIyYTU0NzVmOWMxOWNlZDJmZGYzZDIzOCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9hNzI3Y2FmNzFjMmI0Y2Y5OGIzY2ExZTJhNmM0MmEwZC5iaW5kUG9wdXAocG9wdXBfYWI5YWFmMzI0NjVmNGNiYjg0OGQyN2U1NmE0YmU1MjMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOTcyMzVjNTdkN2EzNDAwZjg2MjRkYzhhN2FiNzU4YzAgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42MTczMTA3OTI1Mjk4MywtNzQuMDgxNzM5OTIyMTE5NjJdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTY3YjI2ZjE5NzE2NDYwODgzMDM1NjBiNDQ5OGNlYWQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMjhjYTEzNjYwY2FlNDY2YWE2NWU1Yzk3NzAxNTMwNGEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYTZjODkyN2NjNGM4NDI4YzgxYTNmZjU1NTk4ZTUyOTUgPSAkKCc8ZGl2IGlkPSJodG1sX2E2Yzg5MjdjYzRjODQyOGM4MWEzZmY1NTU5OGU1Mjk1IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Gb3ggSGlsbHM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzI4Y2ExMzY2MGNhZTQ2NmFhNjVlNWM5NzcwMTUzMDRhLnNldENvbnRlbnQoaHRtbF9hNmM4OTI3Y2M0Yzg0MjhjODFhM2ZmNTU1OThlNTI5NSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl85NzIzNWM1N2Q3YTM0MDBmODYyNGRjOGE3YWI3NThjMC5iaW5kUG9wdXAocG9wdXBfMjhjYTEzNjYwY2FlNDY2YWE2NWU1Yzk3NzAxNTMwNGEpOwoKICAgICAgICAgICAgCiAgICAgICAgCjwvc2NyaXB0Pg== onload="this.contentDocument.open();this.contentDocument.write(atob(this.getAttribute('data-html')));this.contentDocument.close();" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>




```python
CLIENT_ID = 'X5DC02PSOJVYTXTIHFY2PGAGVOQZRAUZK3LLRJLWR3IBLLCP' 
CLIENT_SECRET = 'M0QER4RYNVWEFMV3CC3N0VAV4KSAPU5E5FE33QIBGJLGCANR' 

VERSION = '20180604'
LIMIT = 30

print('Your credentails:')
print('CLIENT_ID: ' + CLIENT_ID)
print('CLIENT_SECRET:' + CLIENT_SECRET)
```

    Your credentails:
    CLIENT_ID: X5DC02PSOJVYTXTIHFY2PGAGVOQZRAUZK3LLRJLWR3IBLLCP
    CLIENT_SECRET:M0QER4RYNVWEFMV3CC3N0VAV4KSAPU5E5FE33QIBGJLGCANR



```python
Staten_Island.loc[0, 'Neighborhood']
```




    'St. George'




```python
neighborhood_latitude = Staten_Island.loc[0, 'Latitude'] # neighborhood latitude value
neighborhood_longitude = Staten_Island.loc[0, 'Longitude'] # neighborhood longitude value

neighborhood_name = Staten_Island.loc[0, 'Neighborhood'] # neighborhood name

print('Latitude and longitude values of {} are {}, {}.'.format(neighborhood_name, 
                                                               neighborhood_latitude, 
                                                               neighborhood_longitude))
```

    Latitude and longitude values of St. George are 40.6449815710044, -74.07935312512797.



```python
# type your answer here
radius = 500 # define radius
LIMIT = 100 # limit of number of venues returned by Foursquare API
url = 'https://api.foursquare.com/v2/venues/explore?&client_id={}&client_secret={}&v={}&ll={},{}&radius={}&limit={}'.format(
    CLIENT_ID, 
    CLIENT_SECRET, 
    VERSION, 
    neighborhood_latitude, 
    neighborhood_longitude, 
    radius, 
    LIMIT)
url
```




    'https://api.foursquare.com/v2/venues/explore?&client_id=X5DC02PSOJVYTXTIHFY2PGAGVOQZRAUZK3LLRJLWR3IBLLCP&client_secret=M0QER4RYNVWEFMV3CC3N0VAV4KSAPU5E5FE33QIBGJLGCANR&v=20180604&ll=40.6449815710044,-74.07935312512797&radius=500&limit=100'




```python
import requests 
results = requests.get(url).json()
results
```




    {'meta': {'code': 200, 'requestId': '5f242e49a3822e313d0ffdcf'},
     'response': {'suggestedFilters': {'header': 'Tap to show:',
       'filters': [{'name': '$-$$$$', 'key': 'price'},
        {'name': 'Open now', 'key': 'openNow'}]},
      'headerLocation': 'Current map view',
      'headerFullLocation': 'Current map view',
      'headerLocationGranularity': 'unknown',
      'totalResults': 37,
      'suggestedBounds': {'ne': {'lat': 40.6494815755044,
        'lng': -74.07343346476772},
       'sw': {'lat': 40.6404815665044, 'lng': -74.08527278548821}},
      'groups': [{'type': 'Recommended Places',
        'name': 'recommended',
        'items': [{'reasons': {'count': 0,
           'items': [{'summary': 'This spot is popular',
             'type': 'general',
             'reasonName': 'globalInteractionReason'}]},
          'venue': {'id': '4a214841f964a520cd7c1fe3',
           'name': 'Beso',
           'location': {'address': '11 Schuyler St',
            'crossStreet': 'btwn Richmond Terrace & Stuyvesant Pl',
            'lat': 40.64330638739738,
            'lng': -74.07650808873225,
            'labeledLatLngs': [{'label': 'display',
              'lat': 40.64330638739738,
              'lng': -74.07650808873225},
             {'label': 'entrance', 'lat': 40.643278, 'lng': -74.07686}],
            'distance': 304,
            'postalCode': '10301',
            'cc': 'US',
            'city': 'Staten Island',
            'state': 'NY',
            'country': 'United States',
            'formattedAddress': ['11 Schuyler St (btwn Richmond Terrace & Stuyvesant Pl)',
             'Staten Island, NY 10301',
             'United States']},
           'categories': [{'id': '4bf58dd8d48988d1db931735',
             'name': 'Tapas Restaurant',
             'pluralName': 'Tapas Restaurants',
             'shortName': 'Tapas',
             'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/food/tapas_',
              'suffix': '.png'},
             'primary': True}],
           'delivery': {'id': '2027805',
            'url': 'https://www.seamless.com/menu/beso-11-schuyler-street-staten-island/2027805?affiliate=1131&utm_source=foursquare-affiliate-network&utm_medium=affiliate&utm_campaign=1131&utm_content=2027805',
            'provider': {'name': 'seamless',
             'icon': {'prefix': 'https://fastly.4sqi.net/img/general/cap/',
              'sizes': [40, 50],
              'name': '/delivery_provider_seamless_20180129.png'}}},
           'photos': {'count': 0, 'groups': []}},
          'referralId': 'e-0-4a214841f964a520cd7c1fe3-0'},
         {'reasons': {'count': 0,
           'items': [{'summary': 'This spot is popular',
             'type': 'general',
             'reasonName': 'globalInteractionReason'}]},
          'venue': {'id': '4bb6924c46d4a5938e7ac6c0',
           'name': 'A&S Pizzeria',
           'location': {'address': '87 Stuyvesant Pl',
            'crossStreet': 'Wall st',
            'lat': 40.64393953223924,
            'lng': -74.0776259226109,
            'labeledLatLngs': [{'label': 'display',
              'lat': 40.64393953223924,
              'lng': -74.0776259226109},
             {'label': 'entrance', 'lat': 40.643963, 'lng': -74.077595}],
            'distance': 186,
            'postalCode': '10301',
            'cc': 'US',
            'city': 'Staten Island',
            'state': 'NY',
            'country': 'United States',
            'formattedAddress': ['87 Stuyvesant Pl (Wall st)',
             'Staten Island, NY 10301',
             'United States']},
           'categories': [{'id': '4bf58dd8d48988d1ca941735',
             'name': 'Pizza Place',
             'pluralName': 'Pizza Places',
             'shortName': 'Pizza',
             'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/food/pizza_',
              'suffix': '.png'},
             'primary': True}],
           'photos': {'count': 0, 'groups': []}},
          'referralId': 'e-0-4bb6924c46d4a5938e7ac6c0-1'},
         {'reasons': {'count': 0,
           'items': [{'summary': 'This spot is popular',
             'type': 'general',
             'reasonName': 'globalInteractionReason'}]},
          'venue': {'id': '4bf9c5c08d30d13a6bce0218',
           'name': 'Staten Island September 11 Memorial',
           'location': {'lat': 40.64676748643786,
            'lng': -74.07650993161968,
            'labeledLatLngs': [{'label': 'display',
              'lat': 40.64676748643786,
              'lng': -74.07650993161968}],
            'distance': 311,
            'postalCode': '10301',
            'cc': 'US',
            'city': 'Staten Island',
            'state': 'NY',
            'country': 'United States',
            'formattedAddress': ['Staten Island, NY 10301', 'United States']},
           'categories': [{'id': '4bf58dd8d48988d12d941735',
             'name': 'Monument / Landmark',
             'pluralName': 'Monuments / Landmarks',
             'shortName': 'Landmark',
             'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/building/government_monument_',
              'suffix': '.png'},
             'primary': True}],
           'photos': {'count': 0, 'groups': []}},
          'referralId': 'e-0-4bf9c5c08d30d13a6bce0218-2'},
         {'reasons': {'count': 0,
           'items': [{'summary': 'This spot is popular',
             'type': 'general',
             'reasonName': 'globalInteractionReason'}]},
          'venue': {'id': '4e62c75a483bd9a9747d8cd8',
           'name': 'Richmond County Bank Ballpark',
           'location': {'address': '75 Richmond Ter',
            'crossStreet': 'at Wall St',
            'lat': 40.645055836227534,
            'lng': -74.07686368914352,
            'labeledLatLngs': [{'label': 'display',
              'lat': 40.645055836227534,
              'lng': -74.07686368914352}],
            'distance': 210,
            'postalCode': '10301',
            'cc': 'US',
            'city': 'Staten Island',
            'state': 'NY',
            'country': 'United States',
            'formattedAddress': ['75 Richmond Ter (at Wall St)',
             'Staten Island, NY 10301',
             'United States']},
           'categories': [{'id': '4bf58dd8d48988d18c941735',
             'name': 'Baseball Stadium',
             'pluralName': 'Baseball Stadiums',
             'shortName': 'Baseball',
             'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/arts_entertainment/stadium_baseball_',
              'suffix': '.png'},
             'primary': True}],
           'photos': {'count': 0, 'groups': []},
           'venuePage': {'id': '32831204'}},
          'referralId': 'e-0-4e62c75a483bd9a9747d8cd8-3'},
         {'reasons': {'count': 0,
           'items': [{'summary': 'This spot is popular',
             'type': 'general',
             'reasonName': 'globalInteractionReason'}]},
          'venue': {'id': '5df19589ecb0ba00082b90d3',
           'name': 'Shake Shack',
           'location': {'address': '35 Richmond Terrace, Space 323',
            'lat': 40.64366,
            'lng': -74.075891,
            'labeledLatLngs': [{'label': 'display',
              'lat': 40.64366,
              'lng': -74.075891}],
            'distance': 327,
            'postalCode': '10301',
            'cc': 'US',
            'city': 'Staten Island',
            'state': 'NY',
            'country': 'United States',
            'formattedAddress': ['35 Richmond Terrace, Space 323',
             'Staten Island, NY 10301',
             'United States']},
           'categories': [{'id': '4bf58dd8d48988d16c941735',
             'name': 'Burger Joint',
             'pluralName': 'Burger Joints',
             'shortName': 'Burgers',
             'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/food/burger_',
              'suffix': '.png'},
             'primary': True}],
           'delivery': {'id': '1532403',
            'url': 'https://www.seamless.com/menu/shake-shack-35-richmond-ter-staten-island/1532403?affiliate=1131&utm_source=foursquare-affiliate-network&utm_medium=affiliate&utm_campaign=1131&utm_content=1532403',
            'provider': {'name': 'seamless',
             'icon': {'prefix': 'https://fastly.4sqi.net/img/general/cap/',
              'sizes': [40, 50],
              'name': '/delivery_provider_seamless_20180129.png'}}},
           'photos': {'count': 0, 'groups': []}},
          'referralId': 'e-0-5df19589ecb0ba00082b90d3-4'},
         {'reasons': {'count': 0,
           'items': [{'summary': 'This spot is popular',
             'type': 'general',
             'reasonName': 'globalInteractionReason'}]},
          'venue': {'id': '42644a00f964a5202b211fe3',
           'name': 'Ruddy & Dean',
           'location': {'address': '44 Richmond Ter',
            'lat': 40.64407377863496,
            'lng': -74.07668273426954,
            'labeledLatLngs': [{'label': 'display',
              'lat': 40.64407377863496,
              'lng': -74.07668273426954}],
            'distance': 247,
            'postalCode': '10301',
            'cc': 'US',
            'city': 'Staten Island',
            'state': 'NY',
            'country': 'United States',
            'formattedAddress': ['44 Richmond Ter',
             'Staten Island, NY 10301',
             'United States']},
           'categories': [{'id': '4bf58dd8d48988d116941735',
             'name': 'Bar',
             'pluralName': 'Bars',
             'shortName': 'Bar',
             'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/nightlife/pub_',
              'suffix': '.png'},
             'primary': True}],
           'photos': {'count': 0, 'groups': []}},
          'referralId': 'e-0-42644a00f964a5202b211fe3-5'},
         {'reasons': {'count': 0,
           'items': [{'summary': 'This spot is popular',
             'type': 'general',
             'reasonName': 'globalInteractionReason'}]},
          'venue': {'id': '590928301de7651d663ae087',
           'name': "Marie's 2",
           'location': {'address': '5 Hyatt St',
            'lat': 40.642176,
            'lng': -74.076669,
            'labeledLatLngs': [{'label': 'display',
              'lat': 40.642176,
              'lng': -74.076669}],
            'distance': 385,
            'postalCode': '10301',
            'cc': 'US',
            'city': 'New York',
            'state': 'NY',
            'country': 'United States',
            'formattedAddress': ['5 Hyatt St',
             'New York, NY 10301',
             'United States']},
           'categories': [{'id': '4bf58dd8d48988d110941735',
             'name': 'Italian Restaurant',
             'pluralName': 'Italian Restaurants',
             'shortName': 'Italian',
             'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/food/italian_',
              'suffix': '.png'},
             'primary': True}],
           'photos': {'count': 0, 'groups': []}},
          'referralId': 'e-0-590928301de7651d663ae087-6'},
         {'reasons': {'count': 0,
           'items': [{'summary': 'This spot is popular',
             'type': 'general',
             'reasonName': 'globalInteractionReason'}]},
          'venue': {'id': '4b6da712f964a52080832ce3',
           'name': 'St. George Theatre',
           'location': {'address': '35 Hyatt St',
            'lat': 40.642253453825425,
            'lng': -74.0774964872446,
            'labeledLatLngs': [{'label': 'display',
              'lat': 40.642253453825425,
              'lng': -74.0774964872446},
             {'label': 'entrance', 'lat': 40.641917, 'lng': -74.077435}],
            'distance': 341,
            'postalCode': '10301',
            'cc': 'US',
            'city': 'Staten Island',
            'state': 'NY',
            'country': 'United States',
            'formattedAddress': ['35 Hyatt St',
             'Staten Island, NY 10301',
             'United States']},
           'categories': [{'id': '4bf58dd8d48988d137941735',
             'name': 'Theater',
             'pluralName': 'Theaters',
             'shortName': 'Theater',
             'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/arts_entertainment/performingarts_theater_',
              'suffix': '.png'},
             'primary': True}],
           'photos': {'count': 0, 'groups': []},
           'venuePage': {'id': '98508518'}},
          'referralId': 'e-0-4b6da712f964a52080832ce3-7'},
         {'reasons': {'count': 0,
           'items': [{'summary': 'This spot is popular',
             'type': 'general',
             'reasonName': 'globalInteractionReason'}]},
          'venue': {'id': '5d30d366e299c90008c07c7c',
           'name': 'Columbia Factory Store',
           'location': {'address': '55 Richmond Ter  Ste 209-210',
            'lat': 40.645342,
            'lng': -74.07668699999999,
            'labeledLatLngs': [{'label': 'display',
              'lat': 40.645342,
              'lng': -74.07668699999999}],
            'distance': 228,
            'postalCode': '10301',
            'cc': 'US',
            'city': 'Staten Island',
            'state': 'NY',
            'country': 'United States',
            'formattedAddress': ['55 Richmond Ter  Ste 209-210',
             'Staten Island, NY 10301',
             'United States']},
           'categories': [{'id': '4bf58dd8d48988d103951735',
             'name': 'Clothing Store',
             'pluralName': 'Clothing Stores',
             'shortName': 'Apparel',
             'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/shops/apparel_',
              'suffix': '.png'},
             'primary': True}],
           'photos': {'count': 0, 'groups': []}},
          'referralId': 'e-0-5d30d366e299c90008c07c7c-8'},
         {'reasons': {'count': 0,
           'items': [{'summary': 'This spot is popular',
             'type': 'general',
             'reasonName': 'globalInteractionReason'}]},
          'venue': {'id': '4a3bc85ef964a520c0a01fe3',
           'name': "Steiny's Pub",
           'location': {'address': '3 Hyatt St',
            'crossStreet': 'btwn Stuyvesant & St Marks Pl',
            'lat': 40.642185270821706,
            'lng': -74.07659916524223,
            'labeledLatLngs': [{'label': 'display',
              'lat': 40.642185270821706,
              'lng': -74.07659916524223},
             {'label': 'entrance', 'lat': 40.642277, 'lng': -74.076628}],
            'distance': 388,
            'postalCode': '10301',
            'cc': 'US',
            'city': 'Staten Island',
            'state': 'NY',
            'country': 'United States',
            'formattedAddress': ['3 Hyatt St (btwn Stuyvesant & St Marks Pl)',
             'Staten Island, NY 10301',
             'United States']},
           'categories': [{'id': '4bf58dd8d48988d116941735',
             'name': 'Bar',
             'pluralName': 'Bars',
             'shortName': 'Bar',
             'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/nightlife/pub_',
              'suffix': '.png'},
             'primary': True}],
           'photos': {'count': 0, 'groups': []}},
          'referralId': 'e-0-4a3bc85ef964a520c0a01fe3-9'},
         {'reasons': {'count': 0,
           'items': [{'summary': 'This spot is popular',
             'type': 'general',
             'reasonName': 'globalInteractionReason'}]},
          'venue': {'id': '515b679fe4b053e60388194e',
           'name': 'Hypno-Tronic Comics',
           'location': {'lat': 40.642476023573096,
            'lng': -74.07658737714057,
            'labeledLatLngs': [{'label': 'display',
              'lat': 40.642476023573096,
              'lng': -74.07658737714057}],
            'distance': 363,
            'cc': 'US',
            'city': 'Staten Island',
            'state': 'NY',
            'country': 'United States',
            'formattedAddress': ['Staten Island, NY', 'United States']},
           'categories': [{'id': '4bf58dd8d48988d1f3941735',
             'name': 'Toy / Game Store',
             'pluralName': 'Toy / Game Stores',
             'shortName': 'Toys & Games',
             'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/shops/toys_',
              'suffix': '.png'},
             'primary': True}],
           'photos': {'count': 0, 'groups': []}},
          'referralId': 'e-0-515b679fe4b053e60388194e-10'},
         {'reasons': {'count': 0,
           'items': [{'summary': 'This spot is popular',
             'type': 'general',
             'reasonName': 'globalInteractionReason'}]},
          'venue': {'id': '4ce9c578baa6a1cd7fbd356c',
           'name': 'The Gavel Grill',
           'location': {'address': '9 Hyatt St',
            'crossStreet': 'Styvesent Ave',
            'lat': 40.642156612084584,
            'lng': -74.07667388544122,
            'labeledLatLngs': [{'label': 'display',
              'lat': 40.642156612084584,
              'lng': -74.07667388544122},
             {'label': 'entrance', 'lat': 40.64221, 'lng': -74.07678}],
            'distance': 387,
            'postalCode': '10301',
            'cc': 'US',
            'city': 'Staten Island',
            'state': 'NY',
            'country': 'United States',
            'formattedAddress': ['9 Hyatt St (Styvesent Ave)',
             'Staten Island, NY 10301',
             'United States']},
           'categories': [{'id': '4bf58dd8d48988d14e941735',
             'name': 'American Restaurant',
             'pluralName': 'American Restaurants',
             'shortName': 'American',
             'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/food/default_',
              'suffix': '.png'},
             'primary': True}],
           'photos': {'count': 0, 'groups': []}},
          'referralId': 'e-0-4ce9c578baa6a1cd7fbd356c-11'},
         {'reasons': {'count': 0,
           'items': [{'summary': 'This spot is popular',
             'type': 'general',
             'reasonName': 'globalInteractionReason'}]},
          'venue': {'id': '4a271f0cf964a5205c911fe3',
           'name': 'Enoteca Maria',
           'location': {'address': '27 Hyatt St',
            'crossStreet': 'btwn Central Ave & St Marks Pl',
            'lat': 40.64194106346249,
            'lng': -74.07732026660736,
            'labeledLatLngs': [{'label': 'display',
              'lat': 40.64194106346249,
              'lng': -74.07732026660736},
             {'label': 'entrance', 'lat': 40.641983, 'lng': -74.077287}],
            'distance': 379,
            'postalCode': '10301',
            'cc': 'US',
            'city': 'Staten Island',
            'state': 'NY',
            'country': 'United States',
            'formattedAddress': ['27 Hyatt St (btwn Central Ave & St Marks Pl)',
             'Staten Island, NY 10301',
             'United States']},
           'categories': [{'id': '4bf58dd8d48988d110941735',
             'name': 'Italian Restaurant',
             'pluralName': 'Italian Restaurants',
             'shortName': 'Italian',
             'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/food/italian_',
              'suffix': '.png'},
             'primary': True}],
           'photos': {'count': 0, 'groups': []}},
          'referralId': 'e-0-4a271f0cf964a5205c911fe3-12'},
         {'reasons': {'count': 0,
           'items': [{'summary': 'This spot is popular',
             'type': 'general',
             'reasonName': 'globalInteractionReason'}]},
          'venue': {'id': '5dbdd128ee17d000084dee80',
           'name': 'Nike',
           'location': {'lat': 40.643615,
            'lng': -74.074738,
            'labeledLatLngs': [{'label': 'display',
              'lat': 40.643615,
              'lng': -74.074738}],
            'distance': 418,
            'postalCode': '10301',
            'cc': 'US',
            'city': 'New York',
            'state': 'NY',
            'country': 'United States',
            'formattedAddress': ['New York, NY 10301', 'United States']},
           'categories': [{'id': '4bf58dd8d48988d1f2941735',
             'name': 'Sporting Goods Shop',
             'pluralName': 'Sporting Goods Shops',
             'shortName': 'Sporting Goods',
             'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/shops/sports_outdoors_',
              'suffix': '.png'},
             'primary': True}],
           'photos': {'count': 0, 'groups': []}},
          'referralId': 'e-0-5dbdd128ee17d000084dee80-13'},
         {'reasons': {'count': 0,
           'items': [{'summary': 'This spot is popular',
             'type': 'general',
             'reasonName': 'globalInteractionReason'}]},
          'venue': {'id': '5ce50cc3065ef5002c345790',
           'name': 'Nike Factory Store',
           'location': {'address': '15 Richmond Ter Ste 300',
            'lat': 40.64332580566406,
            'lng': -74.07459259033203,
            'labeledLatLngs': [{'label': 'display',
              'lat': 40.64332580566406,
              'lng': -74.07459259033203}],
            'distance': 442,
            'postalCode': '10301',
            'cc': 'US',
            'city': 'Staten Island',
            'state': 'NY',
            'country': 'United States',
            'formattedAddress': ['15 Richmond Ter Ste 300',
             'Staten Island, NY 10301',
             'United States']},
           'categories': [{'id': '4bf58dd8d48988d1f2941735',
             'name': 'Sporting Goods Shop',
             'pluralName': 'Sporting Goods Shops',
             'shortName': 'Sporting Goods',
             'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/shops/sports_outdoors_',
              'suffix': '.png'},
             'primary': True}],
           'photos': {'count': 0, 'groups': []}},
          'referralId': 'e-0-5ce50cc3065ef5002c345790-14'},
         {'reasons': {'count': 0,
           'items': [{'summary': 'This spot is popular',
             'type': 'general',
             'reasonName': 'globalInteractionReason'}]},
          'venue': {'id': '53b87097498e83df908d3e91',
           'name': 'St. George Greenmarket',
           'location': {'address': "St. Mark's Place",
            'crossStreet': 'Fort Place',
            'lat': 40.642007314635734,
            'lng': -74.07802076119599,
            'labeledLatLngs': [{'label': 'display',
              'lat': 40.642007314635734,
              'lng': -74.07802076119599}],
            'distance': 349,
            'postalCode': '10301',
            'cc': 'US',
            'city': 'Staten Island',
            'state': 'NY',
            'country': 'United States',
            'formattedAddress': ["St. Mark's Place (Fort Place)",
             'Staten Island, NY 10301',
             'United States']},
           'categories': [{'id': '4bf58dd8d48988d1fa941735',
             'name': 'Farmers Market',
             'pluralName': 'Farmers Markets',
             'shortName': "Farmer's Market",
             'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/shops/food_farmersmarket_',
              'suffix': '.png'},
             'primary': True}],
           'photos': {'count': 0, 'groups': []}},
          'referralId': 'e-0-53b87097498e83df908d3e91-15'},
         {'reasons': {'count': 0,
           'items': [{'summary': 'This spot is popular',
             'type': 'general',
             'reasonName': 'globalInteractionReason'}]},
          'venue': {'id': '5cf3e82bf1936e002c63cf23',
           'name': 'Banana Republic Factory',
           'location': {'address': '15B Richmond Ter',
            'lat': 40.64423,
            'lng': -74.074529,
            'labeledLatLngs': [{'label': 'display',
              'lat': 40.64423,
              'lng': -74.074529}],
            'distance': 415,
            'postalCode': '10301',
            'cc': 'US',
            'city': 'Staten Island',
            'state': 'NY',
            'country': 'United States',
            'formattedAddress': ['15B Richmond Ter',
             'Staten Island, NY 10301',
             'United States']},
           'categories': [{'id': '4bf58dd8d48988d103951735',
             'name': 'Clothing Store',
             'pluralName': 'Clothing Stores',
             'shortName': 'Apparel',
             'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/shops/apparel_',
              'suffix': '.png'},
             'primary': True}],
           'photos': {'count': 0, 'groups': []}},
          'referralId': 'e-0-5cf3e82bf1936e002c63cf23-16'},
         {'reasons': {'count': 0,
           'items': [{'summary': 'This spot is popular',
             'type': 'general',
             'reasonName': 'globalInteractionReason'}]},
          'venue': {'id': '4bab7408f964a52080aa3ae3',
           'name': "Dunkin'",
           'location': {'address': '97 Stuyvesant Pl',
            'lat': 40.6438196,
            'lng': -74.0774385,
            'labeledLatLngs': [{'label': 'display',
              'lat': 40.6438196,
              'lng': -74.0774385},
             {'label': 'entrance', 'lat': 40.64378, 'lng': -74.077457}],
            'distance': 207,
            'postalCode': '10301',
            'cc': 'US',
            'city': 'Staten Island',
            'state': 'NY',
            'country': 'United States',
            'formattedAddress': ['97 Stuyvesant Pl',
             'Staten Island, NY 10301',
             'United States']},
           'categories': [{'id': '4bf58dd8d48988d148941735',
             'name': 'Donut Shop',
             'pluralName': 'Donut Shops',
             'shortName': 'Donuts',
             'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/food/donuts_',
              'suffix': '.png'},
             'primary': True}],
           'delivery': {'id': '1160131',
            'url': 'https://www.seamless.com/menu/dunkin-97-stuyvesant-pl-staten-island/1160131?affiliate=1131&utm_source=foursquare-affiliate-network&utm_medium=affiliate&utm_campaign=1131&utm_content=1160131',
            'provider': {'name': 'seamless',
             'icon': {'prefix': 'https://fastly.4sqi.net/img/general/cap/',
              'sizes': [40, 50],
              'name': '/delivery_provider_seamless_20180129.png'}}},
           'photos': {'count': 0, 'groups': []}},
          'referralId': 'e-0-4bab7408f964a52080aa3ae3-17'},
         {'reasons': {'count': 0,
           'items': [{'summary': 'This spot is popular',
             'type': 'general',
             'reasonName': 'globalInteractionReason'}]},
          'venue': {'id': '5cf3f71a51950e002c4fd1c2',
           'name': 'Old Navy Outlet',
           'location': {'address': '15B Richmond Ter',
            'lat': 40.64432,
            'lng': -74.074641,
            'labeledLatLngs': [{'label': 'display',
              'lat': 40.64432,
              'lng': -74.074641}],
            'distance': 404,
            'postalCode': '10301',
            'cc': 'US',
            'city': 'Staten Island',
            'state': 'NY',
            'country': 'United States',
            'formattedAddress': ['15B Richmond Ter',
             'Staten Island, NY 10301',
             'United States']},
           'categories': [{'id': '4bf58dd8d48988d103951735',
             'name': 'Clothing Store',
             'pluralName': 'Clothing Stores',
             'shortName': 'Apparel',
             'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/shops/apparel_',
              'suffix': '.png'},
             'primary': True}],
           'photos': {'count': 0, 'groups': []}},
          'referralId': 'e-0-5cf3f71a51950e002c4fd1c2-18'},
         {'reasons': {'count': 0,
           'items': [{'summary': 'This spot is popular',
             'type': 'general',
             'reasonName': 'globalInteractionReason'}]},
          'venue': {'id': '5cdae1b0b37e2b002c4310bd',
           'name': 'American Eagle & Aerie Store',
           'location': {'address': '35B Richmond Terrace, Second Floor (Level 3)',
            'lat': 40.64373497010803,
            'lng': -74.07578845993015,
            'labeledLatLngs': [{'label': 'display',
              'lat': 40.64373497010803,
              'lng': -74.07578845993015}],
            'distance': 331,
            'postalCode': '10301',
            'cc': 'US',
            'city': 'Staten Island',
            'state': 'NY',
            'country': 'United States',
            'formattedAddress': ['35B Richmond Terrace, Second Floor (Level 3)',
             'Staten Island, NY 10301',
             'United States']},
           'categories': [{'id': '4bf58dd8d48988d103951735',
             'name': 'Clothing Store',
             'pluralName': 'Clothing Stores',
             'shortName': 'Apparel',
             'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/shops/apparel_',
              'suffix': '.png'},
             'primary': True}],
           'photos': {'count': 0, 'groups': []}},
          'referralId': 'e-0-5cdae1b0b37e2b002c4310bd-19'},
         {'reasons': {'count': 0,
           'items': [{'summary': 'This spot is popular',
             'type': 'general',
             'reasonName': 'globalInteractionReason'}]},
          'venue': {'id': '5cf3ef53fb8e59002cc88486',
           'name': 'Gap Factory Store',
           'location': {'address': '15B Richmond Ter',
            'lat': 40.643857,
            'lng': -74.074975,
            'labeledLatLngs': [{'label': 'display',
              'lat': 40.643857,
              'lng': -74.074975}],
            'distance': 390,
            'postalCode': '10301',
            'cc': 'US',
            'city': 'Staten Island',
            'state': 'NY',
            'country': 'United States',
            'formattedAddress': ['15B Richmond Ter',
             'Staten Island, NY 10301',
             'United States']},
           'categories': [{'id': '4bf58dd8d48988d103951735',
             'name': 'Clothing Store',
             'pluralName': 'Clothing Stores',
             'shortName': 'Apparel',
             'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/shops/apparel_',
              'suffix': '.png'},
             'primary': True}],
           'photos': {'count': 0, 'groups': []}},
          'referralId': 'e-0-5cf3ef53fb8e59002cc88486-20'},
         {'reasons': {'count': 0,
           'items': [{'summary': 'This spot is popular',
             'type': 'general',
             'reasonName': 'globalInteractionReason'}]},
          'venue': {'id': '5ce097771de765002cda6a31',
           'name': 'Starbucks',
           'location': {'address': '55B Richmond Ter',
            'lat': 40.644745,
            'lng': -74.074488,
            'labeledLatLngs': [{'label': 'display',
              'lat': 40.644745,
              'lng': -74.074488}],
            'distance': 411,
            'postalCode': '10301',
            'cc': 'US',
            'city': 'Staten Island',
            'state': 'NY',
            'country': 'United States',
            'formattedAddress': ['55B Richmond Ter',
             'Staten Island, NY 10301',
             'United States']},
           'categories': [{'id': '4bf58dd8d48988d1e0931735',
             'name': 'Coffee Shop',
             'pluralName': 'Coffee Shops',
             'shortName': 'Coffee Shop',
             'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/food/coffeeshop_',
              'suffix': '.png'},
             'primary': True}],
           'photos': {'count': 0, 'groups': []}},
          'referralId': 'e-0-5ce097771de765002cda6a31-21'},
         {'reasons': {'count': 0,
           'items': [{'summary': 'This spot is popular',
             'type': 'general',
             'reasonName': 'globalInteractionReason'}]},
          'venue': {'id': '5d3a3c00bb07af000874b785',
           'name': 'H&M',
           'location': {'address': '1 Richmond Ter',
            'lat': 40.643685,
            'lng': -74.074553,
            'labeledLatLngs': [{'label': 'display',
              'lat': 40.643685,
              'lng': -74.074553}],
            'distance': 430,
            'postalCode': '10301',
            'cc': 'US',
            'city': 'Staten Island',
            'state': 'NY',
            'country': 'United States',
            'formattedAddress': ['1 Richmond Ter',
             'Staten Island, NY 10301',
             'United States']},
           'categories': [{'id': '4bf58dd8d48988d103951735',
             'name': 'Clothing Store',
             'pluralName': 'Clothing Stores',
             'shortName': 'Apparel',
             'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/shops/apparel_',
              'suffix': '.png'},
             'primary': True}],
           'photos': {'count': 0, 'groups': []}},
          'referralId': 'e-0-5d3a3c00bb07af000874b785-22'},
         {'reasons': {'count': 0,
           'items': [{'summary': 'This spot is popular',
             'type': 'general',
             'reasonName': 'globalInteractionReason'}]},
          'venue': {'id': '5d0584a1113cf1002334d4f5',
           'name': 'Walgreens',
           'location': {'address': 'Empire Outlets 55B Richmond Terrace',
            'crossStreet': 'Staten Island',
            'lat': 40.644757,
            'lng': -74.074452,
            'labeledLatLngs': [{'label': 'display',
              'lat': 40.644757,
              'lng': -74.074452}],
            'distance': 414,
            'postalCode': '10301',
            'cc': 'US',
            'city': 'New York',
            'state': 'NY',
            'country': 'United States',
            'formattedAddress': ['Empire Outlets 55B Richmond Terrace (Staten Island)',
             'New York, NY 10301',
             'United States']},
           'categories': [{'id': '4bf58dd8d48988d10f951735',
             'name': 'Pharmacy',
             'pluralName': 'Pharmacies',
             'shortName': 'Pharmacy',
             'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/shops/pharmacy_',
              'suffix': '.png'},
             'primary': True}],
           'photos': {'count': 0, 'groups': []}},
          'referralId': 'e-0-5d0584a1113cf1002334d4f5-23'},
         {'reasons': {'count': 0,
           'items': [{'summary': 'This spot is popular',
             'type': 'general',
             'reasonName': 'globalInteractionReason'}]},
          'venue': {'id': '57766d63cd102e638394762e',
           'name': 'Empire Outlets',
           'location': {'address': '55 Richmond Ter',
            'lat': 40.644016666743966,
            'lng': -74.07495368192154,
            'labeledLatLngs': [{'label': 'display',
              'lat': 40.644016666743966,
              'lng': -74.07495368192154},
             {'label': 'routing',
              'lat': 40.64391384299357,
              'lng': -74.07602548599242}],
            'distance': 386,
            'postalCode': '10301',
            'cc': 'US',
            'neighborhood': 'St. George',
            'city': 'New York',
            'state': 'NY',
            'country': 'United States',
            'formattedAddress': ['55 Richmond Ter',
             'New York, NY 10301',
             'United States']},
           'categories': [{'id': '5744ccdfe4b0c0459246b4df',
             'name': 'Outlet Mall',
             'pluralName': 'Outlet Malls',
             'shortName': 'Outlet Mall',
             'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/shops/mall_',
              'suffix': '.png'},
             'primary': True}],
           'photos': {'count': 0, 'groups': []}},
          'referralId': 'e-0-57766d63cd102e638394762e-24'},
         {'reasons': {'count': 0,
           'items': [{'summary': 'This spot is popular',
             'type': 'general',
             'reasonName': 'globalInteractionReason'}]},
          'venue': {'id': '4edad2470e011b46eef9af05',
           'name': 'Ruddy & Dean North Shore Steak Co.',
           'location': {'address': '44 Richmond Ter',
            'lat': 40.644068463768946,
            'lng': -74.07668033171674,
            'labeledLatLngs': [{'label': 'display',
              'lat': 40.644068463768946,
              'lng': -74.07668033171674},
             {'label': 'entrance', 'lat': 40.644017, 'lng': -74.076729}],
            'distance': 247,
            'postalCode': '10301',
            'cc': 'US',
            'city': 'Staten Island',
            'state': 'NY',
            'country': 'United States',
            'formattedAddress': ['44 Richmond Ter',
             'Staten Island, NY 10301',
             'United States']},
           'categories': [{'id': '4bf58dd8d48988d1cc941735',
             'name': 'Steakhouse',
             'pluralName': 'Steakhouses',
             'shortName': 'Steakhouse',
             'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/food/steakhouse_',
              'suffix': '.png'},
             'primary': True}],
           'photos': {'count': 0, 'groups': []}},
          'referralId': 'e-0-4edad2470e011b46eef9af05-25'},
         {'reasons': {'count': 0,
           'items': [{'summary': 'This spot is popular',
             'type': 'general',
             'reasonName': 'globalInteractionReason'}]},
          'venue': {'id': '504fb525e4b0fed21e040943',
           'name': 'Postcards 9/11 Memorial',
           'location': {'lat': 40.646546219541605,
            'lng': -74.07670307216092,
            'labeledLatLngs': [{'label': 'display',
              'lat': 40.646546219541605,
              'lng': -74.07670307216092}],
            'distance': 283,
            'postalCode': '10301',
            'cc': 'US',
            'city': 'Staten Island',
            'state': 'NY',
            'country': 'United States',
            'formattedAddress': ['Staten Island, NY 10301', 'United States']},
           'categories': [{'id': '4bf58dd8d48988d164941735',
             'name': 'Plaza',
             'pluralName': 'Plazas',
             'shortName': 'Plaza',
             'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/parks_outdoors/plaza_',
              'suffix': '.png'},
             'primary': True}],
           'photos': {'count': 0, 'groups': []}},
          'referralId': 'e-0-504fb525e4b0fed21e040943-26'},
         {'reasons': {'count': 0,
           'items': [{'summary': 'This spot is popular',
             'type': 'general',
             'reasonName': 'globalInteractionReason'}]},
          'venue': {'id': '56df4a05cd10691b22a83e33',
           'name': 'The Burrito Shoppe',
           'location': {'address': '100 Stuyvesant Pl',
            'crossStreet': 'Wall St.',
            'lat': 40.643639,
            'lng': -74.077919,
            'labeledLatLngs': [{'label': 'display',
              'lat': 40.643639,
              'lng': -74.077919}],
            'distance': 192,
            'postalCode': '10301',
            'cc': 'US',
            'city': 'Staten Island',
            'state': 'NY',
            'country': 'United States',
            'formattedAddress': ['100 Stuyvesant Pl (Wall St.)',
             'Staten Island, NY 10301',
             'United States']},
           'categories': [{'id': '4bf58dd8d48988d16e941735',
             'name': 'Fast Food Restaurant',
             'pluralName': 'Fast Food Restaurants',
             'shortName': 'Fast Food',
             'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/food/fastfood_',
              'suffix': '.png'},
             'primary': True}],
           'delivery': {'id': '346662',
            'url': 'https://www.seamless.com/menu/the-burrito-shoppe-100-stuyvesant-place-staten-island/346662?affiliate=1131&utm_source=foursquare-affiliate-network&utm_medium=affiliate&utm_campaign=1131&utm_content=346662',
            'provider': {'name': 'seamless',
             'icon': {'prefix': 'https://fastly.4sqi.net/img/general/cap/',
              'sizes': [40, 50],
              'name': '/delivery_provider_seamless_20180129.png'}}},
           'photos': {'count': 0, 'groups': []},
           'venuePage': {'id': '165569617'}},
          'referralId': 'e-0-56df4a05cd10691b22a83e33-27'},
         {'reasons': {'count': 0,
           'items': [{'summary': 'This spot is popular',
             'type': 'general',
             'reasonName': 'globalInteractionReason'}]},
          'venue': {'id': '4fad6179e4b017dfa57cd157',
           'name': 'North Shore Esplanade',
           'location': {'address': 'North Shore Esplanade',
            'lat': 40.64692910628257,
            'lng': -74.07679796218872,
            'labeledLatLngs': [{'label': 'display',
              'lat': 40.64692910628257,
              'lng': -74.07679796218872}],
            'distance': 305,
            'postalCode': '10301',
            'cc': 'US',
            'state': 'New York',
            'country': 'United States',
            'formattedAddress': ['North Shore Esplanade',
             'NY 10301',
             'United States']},
           'categories': [{'id': '4bf58dd8d48988d1e0941735',
             'name': 'Harbor / Marina',
             'pluralName': 'Harbors / Marinas',
             'shortName': 'Harbor / Marina',
             'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/parks_outdoors/harbor_',
              'suffix': '.png'},
             'primary': True}],
           'photos': {'count': 0, 'groups': []}},
          'referralId': 'e-0-4fad6179e4b017dfa57cd157-28'},
         {'reasons': {'count': 0,
           'items': [{'summary': 'This spot is popular',
             'type': 'general',
             'reasonName': 'globalInteractionReason'}]},
          'venue': {'id': '4eaee82329c2a9bb983da5a1',
           'name': "Guiseppe's At St. George",
           'location': {'address': '5 Hyatt St',
            'lat': 40.642357000000004,
            'lng': -74.076728,
            'labeledLatLngs': [{'label': 'display',
              'lat': 40.642357000000004,
              'lng': -74.076728},
             {'label': 'entrance', 'lat': 40.642255, 'lng': -74.076679}],
            'distance': 366,
            'postalCode': '10301',
            'cc': 'US',
            'city': 'Staten Island',
            'state': 'NY',
            'country': 'United States',
            'formattedAddress': ['5 Hyatt St',
             'Staten Island, NY 10301',
             'United States']},
           'categories': [{'id': '4bf58dd8d48988d1ca941735',
             'name': 'Pizza Place',
             'pluralName': 'Pizza Places',
             'shortName': 'Pizza',
             'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/food/pizza_',
              'suffix': '.png'},
             'primary': True}],
           'photos': {'count': 0, 'groups': []}},
          'referralId': 'e-0-4eaee82329c2a9bb983da5a1-29'},
         {'reasons': {'count': 0,
           'items': [{'summary': 'This spot is popular',
             'type': 'general',
             'reasonName': 'globalInteractionReason'}]},
          'venue': {'id': '4ea84ace30f897d8db599ffe',
           'name': 'St. George Esplanade',
           'location': {'lat': 40.64554513232871,
            'lng': -74.07493747680437,
            'labeledLatLngs': [{'label': 'display',
              'lat': 40.64554513232871,
              'lng': -74.07493747680437}],
            'distance': 378,
            'cc': 'US',
            'state': 'New York',
            'country': 'United States',
            'formattedAddress': ['New York', 'United States']},
           'categories': [{'id': '4bf58dd8d48988d165941735',
             'name': 'Scenic Lookout',
             'pluralName': 'Scenic Lookouts',
             'shortName': 'Scenic Lookout',
             'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/parks_outdoors/sceniclookout_',
              'suffix': '.png'},
             'primary': True}],
           'photos': {'count': 0, 'groups': []}},
          'referralId': 'e-0-4ea84ace30f897d8db599ffe-30'},
         {'reasons': {'count': 0,
           'items': [{'summary': 'This spot is popular',
             'type': 'general',
             'reasonName': 'globalInteractionReason'}]},
          'venue': {'id': '57b0ef3d498e6f0a5268cf1d',
           'name': 'Maritime Hospital Quarantine Cemetery',
           'location': {'lat': 40.64159293605971,
            'lng': -74.07772968664675,
            'labeledLatLngs': [{'label': 'display',
              'lat': 40.64159293605971,
              'lng': -74.07772968664675}],
            'distance': 401,
            'cc': 'US',
            'city': 'Staten Island',
            'state': 'NY',
            'country': 'United States',
            'formattedAddress': ['Staten Island, NY', 'United States']},
           'categories': [{'id': '4bf58dd8d48988d163941735',
             'name': 'Park',
             'pluralName': 'Parks',
             'shortName': 'Park',
             'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/parks_outdoors/park_',
              'suffix': '.png'},
             'primary': True}],
           'photos': {'count': 0, 'groups': []}},
          'referralId': 'e-0-57b0ef3d498e6f0a5268cf1d-31'},
         {'reasons': {'count': 0,
           'items': [{'summary': 'This spot is popular',
             'type': 'general',
             'reasonName': 'globalInteractionReason'}]},
          'venue': {'id': '4cb3acd8aef16dcbf933ca54',
           'name': 'MTA Bus - SI Ferry & Ramp D (S40/S42/S44/S52/S90/S94)',
           'location': {'address': 'St. George Terminal',
            'crossStreet': 'Bay St',
            'lat': 40.643311510335884,
            'lng': -74.0743255374318,
            'labeledLatLngs': [{'label': 'display',
              'lat': 40.643311510335884,
              'lng': -74.0743255374318}],
            'distance': 463,
            'postalCode': '10301',
            'cc': 'US',
            'city': 'Staten Island',
            'state': 'NY',
            'country': 'United States',
            'formattedAddress': ['St. George Terminal (Bay St)',
             'Staten Island, NY 10301',
             'United States']},
           'categories': [{'id': '4bf58dd8d48988d1fe931735',
             'name': 'Bus Station',
             'pluralName': 'Bus Stations',
             'shortName': 'Bus Station',
             'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/travel/busstation_',
              'suffix': '.png'},
             'primary': True}],
           'photos': {'count': 0, 'groups': []}},
          'referralId': 'e-0-4cb3acd8aef16dcbf933ca54-32'},
         {'reasons': {'count': 0,
           'items': [{'summary': 'This spot is popular',
             'type': 'general',
             'reasonName': 'globalInteractionReason'}]},
          'venue': {'id': '4b3e6419f964a520669c25e3',
           'name': 'Barrett Triangle',
           'location': {'address': '1-31 Bay St',
            'lat': 40.64173127388491,
            'lng': -74.07585918903351,
            'labeledLatLngs': [{'label': 'display',
              'lat': 40.64173127388491,
              'lng': -74.07585918903351}],
            'distance': 466,
            'postalCode': '10301',
            'cc': 'US',
            'city': 'Staten Island',
            'state': 'NY',
            'country': 'United States',
            'formattedAddress': ['1-31 Bay St',
             'Staten Island, NY 10301',
             'United States']},
           'categories': [{'id': '4bf58dd8d48988d163941735',
             'name': 'Park',
             'pluralName': 'Parks',
             'shortName': 'Park',
             'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/parks_outdoors/park_',
              'suffix': '.png'},
             'primary': True}],
           'photos': {'count': 0, 'groups': []}},
          'referralId': 'e-0-4b3e6419f964a520669c25e3-33'},
         {'reasons': {'count': 0,
           'items': [{'summary': 'This spot is popular',
             'type': 'general',
             'reasonName': 'globalInteractionReason'}]},
          'venue': {'id': '4e56abb162e123a76493b886',
           'name': 'MTA Bus - Bay St & Nick Laporte Pl (S42/S46/S48/S51/S52/S61/S62/S66/S74/S76/S78/S86/S91/S92/S96/S98)',
           'location': {'address': 'Bay St',
            'lat': 40.64167021628304,
            'lng': -74.07577872276306,
            'labeledLatLngs': [{'label': 'display',
              'lat': 40.64167021628304,
              'lng': -74.07577872276306}],
            'distance': 476,
            'cc': 'US',
            'city': 'Staten Island',
            'state': 'NY',
            'country': 'United States',
            'formattedAddress': ['Bay St', 'Staten Island, NY', 'United States']},
           'categories': [{'id': '52f2ab2ebcbc57f1066b8b4f',
             'name': 'Bus Stop',
             'pluralName': 'Bus Stops',
             'shortName': 'Bus Stop',
             'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/travel/busstation_',
              'suffix': '.png'},
             'primary': True}],
           'photos': {'count': 0, 'groups': []}},
          'referralId': 'e-0-4e56abb162e123a76493b886-34'},
         {'reasons': {'count': 0,
           'items': [{'summary': 'This spot is popular',
             'type': 'general',
             'reasonName': 'globalInteractionReason'}]},
          'venue': {'id': '515af2b6e4b08549aebb78f0',
           'name': 'Staten Island Visitor Information Booth',
           'location': {'lat': 40.64463918117021,
            'lng': -74.07364558712177,
            'labeledLatLngs': [{'label': 'display',
              'lat': 40.64463918117021,
              'lng': -74.07364558712177}],
            'distance': 483,
            'cc': 'US',
            'city': 'Staten Island',
            'state': 'NY',
            'country': 'United States',
            'formattedAddress': ['Staten Island, NY', 'United States']},
           'categories': [{'id': '4f4530164b9074f6e4fb00ff',
             'name': 'Tourist Information Center',
             'pluralName': 'Tourist Information Centers',
             'shortName': 'Tourist Information',
             'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/travel/touristinformation_',
              'suffix': '.png'},
             'primary': True}],
           'photos': {'count': 0, 'groups': []}},
          'referralId': 'e-0-515af2b6e4b08549aebb78f0-35'},
         {'reasons': {'count': 0,
           'items': [{'summary': 'This spot is popular',
             'type': 'general',
             'reasonName': 'globalInteractionReason'}]},
          'venue': {'id': '56f05339498eb6c326c20ee2',
           'name': 'Ferris Wheel Juice Bar',
           'location': {'address': 'Bay St',
            'crossStreet': 'Hyatt Pl',
            'lat': 40.642509,
            'lng': -74.074488,
            'labeledLatLngs': [{'label': 'display',
              'lat': 40.642509,
              'lng': -74.074488}],
            'distance': 494,
            'postalCode': '10305',
            'cc': 'US',
            'city': 'Staten Island',
            'state': 'NY',
            'country': 'United States',
            'formattedAddress': ['Bay St (Hyatt Pl)',
             'Staten Island, NY 10305',
             'United States']},
           'categories': [{'id': '4bf58dd8d48988d112941735',
             'name': 'Juice Bar',
             'pluralName': 'Juice Bars',
             'shortName': 'Juice Bar',
             'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/food/juicebar_',
              'suffix': '.png'},
             'primary': True}],
           'photos': {'count': 0, 'groups': []}},
          'referralId': 'e-0-56f05339498eb6c326c20ee2-36'}]}]}}




```python
# function that extracts the category of the venue
def get_category_type(row):
    try:
        categories_list = row['categories']
    except:
        categories_list = row['venue.categories']
        
    if len(categories_list) == 0:
        return None
    else:
        return categories_list[0]['name']
```


```python
from pandas.io.json import json_normalize 
venues = results['response']['groups'][0]['items']
    
nearby_venues = json_normalize(venues) # flatten JSON

# filter columns
filtered_columns = ['venue.name', 'venue.categories', 'venue.location.lat', 'venue.location.lng']
nearby_venues =nearby_venues.loc[:, filtered_columns]

# filter the category for each row
nearby_venues['venue.categories'] = nearby_venues.apply(get_category_type, axis=1)

# clean columns
nearby_venues.columns = [col.split(".")[-1] for col in nearby_venues.columns]

nearby_venues.head()
```

    /home/jupyterlab/conda/envs/python/lib/python3.6/site-packages/ipykernel_launcher.py:4: FutureWarning: pandas.io.json.json_normalize is deprecated, use pandas.json_normalize instead
      after removing the cwd from sys.path.





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>categories</th>
      <th>lat</th>
      <th>lng</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Beso</td>
      <td>Tapas Restaurant</td>
      <td>40.643306</td>
      <td>-74.076508</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A&amp;S Pizzeria</td>
      <td>Pizza Place</td>
      <td>40.643940</td>
      <td>-74.077626</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Staten Island September 11 Memorial</td>
      <td>Monument / Landmark</td>
      <td>40.646767</td>
      <td>-74.076510</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Richmond County Bank Ballpark</td>
      <td>Baseball Stadium</td>
      <td>40.645056</td>
      <td>-74.076864</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Shake Shack</td>
      <td>Burger Joint</td>
      <td>40.643660</td>
      <td>-74.075891</td>
    </tr>
  </tbody>
</table>
</div>




```python
print('{} venues were returned by Foursquare.'.format(nearby_venues.shape[0]))
```

    37 venues were returned by Foursquare.



```python
def getNearbyVenues(names, latitudes, longitudes, radius=500):
    
    venues_list=[]
    for name, lat, lng in zip(names, latitudes, longitudes):
        print(name)
            
        # create the API request URL
        url = 'https://api.foursquare.com/v2/venues/explore?&client_id={}&client_secret={}&v={}&ll={},{}&radius={}&limit={}'.format(
            CLIENT_ID, 
            CLIENT_SECRET, 
            VERSION, 
            lat, 
            lng, 
            radius, 
            LIMIT)
            
        # make the GET request
        results = requests.get(url).json()["response"]['groups'][0]['items']
        
        # return only relevant information for each nearby venue
        venues_list.append([(
            name, 
            lat, 
            lng, 
            v['venue']['name'], 
            v['venue']['location']['lat'], 
            v['venue']['location']['lng'],  
            v['venue']['categories'][0]['name']) for v in results])

    nearby_venues = pd.DataFrame([item for venue_list in venues_list for item in venue_list])
    nearby_venues.columns = ['Neighborhood', 
                  'Neighborhood Latitude', 
                  'Neighborhood Longitude', 
                  'Venue', 
                  'Venue Latitude', 
                  'Venue Longitude', 
                  'Venue Category']
    
    return(nearby_venues)
```


```python
StatenIsland_venues = getNearbyVenues(names=Staten_Island['Neighborhood'],
                                   latitudes=Staten_Island['Latitude'],
                                   longitudes=Staten_Island['Longitude']
                                  )
```

    St. George
    New Brighton
    Stapleton
    Rosebank
    West Brighton
    Grymes Hill
    Todt Hill
    South Beach
    Port Richmond
    Mariner's Harbor
    Port Ivory
    Castleton Corners
    New Springville
    Travis
    New Dorp
    Oakwood
    Great Kills
    Eltingville
    Annadale
    Woodrow
    Tottenville
    Tompkinsville
    Silver Lake
    Sunnyside
    Park Hill
    Westerleigh
    Graniteville
    Arlington
    Arrochar
    Grasmere
    Old Town
    Dongan Hills
    Midland Beach
    Grant City
    New Dorp Beach
    Bay Terrace
    Huguenot
    Pleasant Plains
    Butler Manor
    Charleston
    Rossville
    Arden Heights
    Greenridge
    Heartland Village
    Chelsea
    Bloomfield
    Bulls Head
    Richmond Town
    Shore Acres
    Clifton
    Concord
    Emerson Hill
    Randall Manor
    Howland Hook
    Elm Park
    Manor Heights
    Willowbrook
    Sandy Ground
    Egbertville
    Prince's Bay
    Lighthouse Hill
    Richmond Valley
    Fox Hills



```python
print(StatenIsland_venues.shape)
StatenIsland_venues.head()
```

    (833, 7)





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Neighborhood</th>
      <th>Neighborhood Latitude</th>
      <th>Neighborhood Longitude</th>
      <th>Venue</th>
      <th>Venue Latitude</th>
      <th>Venue Longitude</th>
      <th>Venue Category</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>St. George</td>
      <td>40.644982</td>
      <td>-74.079353</td>
      <td>Beso</td>
      <td>40.643306</td>
      <td>-74.076508</td>
      <td>Tapas Restaurant</td>
    </tr>
    <tr>
      <th>1</th>
      <td>St. George</td>
      <td>40.644982</td>
      <td>-74.079353</td>
      <td>A&amp;S Pizzeria</td>
      <td>40.643940</td>
      <td>-74.077626</td>
      <td>Pizza Place</td>
    </tr>
    <tr>
      <th>2</th>
      <td>St. George</td>
      <td>40.644982</td>
      <td>-74.079353</td>
      <td>Staten Island September 11 Memorial</td>
      <td>40.646767</td>
      <td>-74.076510</td>
      <td>Monument / Landmark</td>
    </tr>
    <tr>
      <th>3</th>
      <td>St. George</td>
      <td>40.644982</td>
      <td>-74.079353</td>
      <td>Richmond County Bank Ballpark</td>
      <td>40.645056</td>
      <td>-74.076864</td>
      <td>Baseball Stadium</td>
    </tr>
    <tr>
      <th>4</th>
      <td>St. George</td>
      <td>40.644982</td>
      <td>-74.079353</td>
      <td>Shake Shack</td>
      <td>40.643660</td>
      <td>-74.075891</td>
      <td>Burger Joint</td>
    </tr>
  </tbody>
</table>
</div>




```python
StatenIsland_venues.groupby('Neighborhood').count()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Neighborhood Latitude</th>
      <th>Neighborhood Longitude</th>
      <th>Venue</th>
      <th>Venue Latitude</th>
      <th>Venue Longitude</th>
      <th>Venue Category</th>
    </tr>
    <tr>
      <th>Neighborhood</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Annadale</th>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
    </tr>
    <tr>
      <th>Arden Heights</th>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
    </tr>
    <tr>
      <th>Arlington</th>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
    </tr>
    <tr>
      <th>Arrochar</th>
      <td>23</td>
      <td>23</td>
      <td>23</td>
      <td>23</td>
      <td>23</td>
      <td>23</td>
    </tr>
    <tr>
      <th>Bay Terrace</th>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>Travis</th>
      <td>15</td>
      <td>15</td>
      <td>15</td>
      <td>15</td>
      <td>15</td>
      <td>15</td>
    </tr>
    <tr>
      <th>West Brighton</th>
      <td>38</td>
      <td>38</td>
      <td>38</td>
      <td>38</td>
      <td>38</td>
      <td>38</td>
    </tr>
    <tr>
      <th>Westerleigh</th>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Willowbrook</th>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
    </tr>
    <tr>
      <th>Woodrow</th>
      <td>19</td>
      <td>19</td>
      <td>19</td>
      <td>19</td>
      <td>19</td>
      <td>19</td>
    </tr>
  </tbody>
</table>
<p>63 rows × 6 columns</p>
</div>




```python
print('There are {} uniques categories.'.format(len(StatenIsland_venues['Venue Category'].unique())))
```

    There are 180 uniques categories.


  <h3 id="version">3. Analyze Each Neighborhood of Staten Island.</h3>


```python
# one hot encoding
statenisland_onehot = pd.get_dummies(StatenIsland_venues[['Venue Category']], prefix="", prefix_sep="")

# add neighborhood column back to dataframe
statenisland_onehot['Neighborhood'] = StatenIsland_venues['Neighborhood'] 

# move neighborhood column to the first column
fixed_columns = [statenisland_onehot.columns[-1]] + list(statenisland_onehot.columns[:-1])
statenisland_onehot = statenisland_onehot[fixed_columns]

statenisland_onehot.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Neighborhood</th>
      <th>Accessories Store</th>
      <th>African Restaurant</th>
      <th>American Restaurant</th>
      <th>Arcade</th>
      <th>Art Gallery</th>
      <th>Art Museum</th>
      <th>Arts &amp; Crafts Store</th>
      <th>Asian Restaurant</th>
      <th>Athletics &amp; Sports</th>
      <th>...</th>
      <th>Tourist Information Center</th>
      <th>Toy / Game Store</th>
      <th>Trail</th>
      <th>Train Station</th>
      <th>Vegetarian / Vegan Restaurant</th>
      <th>Video Game Store</th>
      <th>Video Store</th>
      <th>Vietnamese Restaurant</th>
      <th>Wings Joint</th>
      <th>Yoga Studio</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>St. George</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>St. George</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>St. George</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>St. George</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>St. George</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 181 columns</p>
</div>




```python
statenisland_onehot.shape
```




    (833, 181)




```python
statenisland_grouped = statenisland_onehot.groupby('Neighborhood').mean().reset_index()
statenisland_grouped
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Neighborhood</th>
      <th>Accessories Store</th>
      <th>African Restaurant</th>
      <th>American Restaurant</th>
      <th>Arcade</th>
      <th>Art Gallery</th>
      <th>Art Museum</th>
      <th>Arts &amp; Crafts Store</th>
      <th>Asian Restaurant</th>
      <th>Athletics &amp; Sports</th>
      <th>...</th>
      <th>Tourist Information Center</th>
      <th>Toy / Game Store</th>
      <th>Trail</th>
      <th>Train Station</th>
      <th>Vegetarian / Vegan Restaurant</th>
      <th>Video Game Store</th>
      <th>Video Store</th>
      <th>Vietnamese Restaurant</th>
      <th>Wings Joint</th>
      <th>Yoga Studio</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Annadale</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.100000</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.1</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Arden Heights</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Arlington</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Arrochar</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.043478</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Bay Terrace</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.1</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>58</th>
      <td>Travis</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>59</th>
      <td>West Brighton</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.026316</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.026316</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>60</th>
      <td>Westerleigh</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.333333</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>61</th>
      <td>Willowbrook</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>62</th>
      <td>Woodrow</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
<p>63 rows × 181 columns</p>
</div>




```python
statenisland_grouped.shape
```




    (63, 181)




```python
num_top_venues = 5

for hood in statenisland_grouped['Neighborhood']:
    print("----"+hood+"----")
    temp = statenisland_grouped[statenisland_grouped['Neighborhood'] == hood].T.reset_index()
    temp.columns = ['venue','freq']
    temp = temp.iloc[1:]
    temp['freq'] = temp['freq'].astype(float)
    temp = temp.round({'freq': 2})
    print(temp.sort_values('freq', ascending=False).reset_index(drop=True).head(num_top_venues))
    print('\n')
```

    ----Annadale----
               venue  freq
    0    Pizza Place   0.2
    1     Restaurant   0.1
    2  Train Station   0.1
    3       Pharmacy   0.1
    4           Food   0.1
    
    
    ----Arden Heights----
                  venue  freq
    0            Lawyer  0.14
    1     Deli / Bodega  0.14
    2          Bus Stop  0.14
    3  Business Service  0.14
    4          Pharmacy  0.14
    
    
    ----Arlington----
                            venue  freq
    0               Deli / Bodega   0.2
    1               Boat or Ferry   0.2
    2                    Bus Stop   0.2
    3  Construction & Landscaping   0.2
    4                 Coffee Shop   0.2
    
    
    ----Arrochar----
                       venue  freq
    0               Bus Stop  0.17
    1          Deli / Bodega  0.09
    2           Liquor Store  0.09
    3     Italian Restaurant  0.09
    4  Outdoors & Recreation  0.04
    
    
    ----Bay Terrace----
                    venue  freq
    0         Supermarket   0.2
    1          Donut Shop   0.1
    2    Sushi Restaurant   0.1
    3        Liquor Store   0.1
    4  Italian Restaurant   0.1
    
    
    ----Bloomfield----
                   venue  freq
    0         Theme Park  0.25
    1  Recreation Center  0.25
    2       Burger Joint  0.25
    3           Bus Stop  0.25
    4  Accessories Store  0.00
    
    
    ----Bulls Head----
             venue  freq
    0     Bus Stop  0.08
    1  Pizza Place  0.06
    2         Café  0.04
    3    Gift Shop  0.04
    4     Pharmacy  0.04
    
    
    ----Butler Manor----
                   venue  freq
    0               Pool   0.4
    1     Baseball Field   0.4
    2  Convenience Store   0.2
    3  Accessories Store   0.0
    4        Pizza Place   0.0
    
    
    ----Castleton Corners----
               venue  freq
    0    Pizza Place  0.19
    1           Bank  0.19
    2     Bagel Shop  0.06
    3  Tattoo Parlor  0.06
    4  Go Kart Track  0.06
    
    
    ----Charleston----
                venue  freq
    0     Coffee Shop  0.07
    1  Cosmetics Shop  0.07
    2   Big Box Store  0.07
    3           Diner  0.03
    4     Music Venue  0.03
    
    
    ----Chelsea----
                    venue  freq
    0          Steakhouse   0.2
    1                Park   0.2
    2            Bus Stop   0.2
    3      Sandwich Place   0.2
    4  Spanish Restaurant   0.2
    
    
    ----Clifton----
                  venue  freq
    0     Train Station  0.12
    1     Grocery Store  0.12
    2  Storage Facility  0.06
    3            Museum  0.06
    4     Deli / Bodega  0.06
    
    
    ----Concord----
                venue  freq
    0   Deli / Bodega  0.18
    1        Bus Stop  0.09
    2            Park  0.09
    3   Grocery Store  0.09
    4  Sandwich Place  0.09
    
    
    ----Dongan Hills----
                    venue  freq
    0         Pizza Place  0.12
    1  Chinese Restaurant  0.08
    2  Italian Restaurant  0.08
    3       Jewelry Store  0.04
    4      Ice Cream Shop  0.04
    
    
    ----Egbertville----
                    venue  freq
    0  Italian Restaurant  0.25
    1      Cosmetics Shop  0.25
    2          Bagel Shop  0.25
    3      Clothing Store  0.25
    4   Accessories Store  0.00
    
    
    ----Elm Park----
                     venue  freq
    0        Deli / Bodega  0.29
    1  American Restaurant  0.14
    2   Italian Restaurant  0.14
    3             Bus Stop  0.14
    4       Ice Cream Shop  0.14
    
    
    ----Eltingville----
                      venue  freq
    0      Sushi Restaurant  0.11
    1           Pizza Place  0.11
    2  Fast Food Restaurant  0.05
    3        Sandwich Place  0.05
    4              Pharmacy  0.05
    
    
    ----Emerson Hill----
                            venue  freq
    0               Historic Site  0.25
    1  Construction & Landscaping  0.25
    2            Sculpture Garden  0.25
    3                        Food  0.25
    4           Accessories Store  0.00
    
    
    ----Fox Hills----
                    venue  freq
    0  African Restaurant   0.2
    1       Deli / Bodega   0.2
    2            Bus Stop   0.2
    3      Sandwich Place   0.2
    4       Grocery Store   0.2
    
    
    ----Graniteville----
                       venue  freq
    0          Boat or Ferry   0.5
    1          Grocery Store   0.5
    2      Accessories Store   0.0
    3           Optical Shop   0.0
    4  Outdoors & Recreation   0.0
    
    
    ----Grant City----
                             venue  freq
    0         Fast Food Restaurant  0.10
    1            Food & Drink Shop  0.10
    2  Eastern European Restaurant  0.05
    3                          Bar  0.05
    4                     Bus Stop  0.05
    
    
    ----Grasmere----
            venue  freq
    0    Bus Stop  0.20
    1  Bagel Shop  0.08
    2      Bakery  0.08
    3        Bank  0.08
    4  Restaurant  0.04
    
    
    ----Great Kills----
                    venue  freq
    0                 Bar  0.13
    1         Pizza Place  0.09
    2  Italian Restaurant  0.09
    3       Deli / Bodega  0.04
    4        Dessert Shop  0.04
    
    
    ----Greenridge----
                            venue  freq
    0                      Lawyer  0.14
    1                       Diner  0.14
    2  Construction & Landscaping  0.14
    3                   Pet Store  0.14
    4              Shipping Store  0.14
    
    
    ----Grymes Hill----
               venue  freq
    0  Deli / Bodega   0.5
    1        Dog Run   0.5
    2     Playground   0.0
    3    Outlet Mall   0.0
    4           Park   0.0
    
    
    ----Heartland Village----
                   venue  freq
    0        Coffee Shop  0.18
    1  Accessories Store  0.09
    2               Food  0.09
    3         Restaurant  0.09
    4       Optical Shop  0.09
    
    
    ----Howland Hook----
                       venue  freq
    0          Boat or Ferry   1.0
    1      Accessories Store   0.0
    2            Pizza Place   0.0
    3  Outdoors & Recreation   0.0
    4            Outlet Mall   0.0
    
    
    ----Huguenot----
                    venue  freq
    0       Deli / Bodega  0.12
    1  Italian Restaurant  0.12
    2          Donut Shop  0.12
    3       Train Station  0.12
    4      Sandwich Place  0.12
    
    
    ----Lighthouse Hill----
                    venue  freq
    0  Italian Restaurant   0.2
    1          Art Museum   0.2
    2               Trail   0.2
    3                Café   0.2
    4                 Spa   0.2
    
    
    ----Manor Heights----
                     venue  freq
    0           Donut Shop  0.15
    1         Liquor Store  0.15
    2        Deli / Bodega  0.15
    3   Chinese Restaurant  0.08
    4  American Restaurant  0.08
    
    
    ----Mariner's Harbor----
                    venue  freq
    0       Deli / Bodega  0.22
    1  Italian Restaurant  0.22
    2            Bus Stop  0.22
    3   Other Repair Shop  0.11
    4         Pizza Place  0.11
    
    
    ----Midland Beach----
                    venue  freq
    0               Beach  0.22
    1        Liquor Store  0.11
    2  Chinese Restaurant  0.11
    3           Bookstore  0.11
    4            Bus Stop  0.11
    
    
    ----New Brighton----
               venue  freq
    0  Deli / Bodega  0.25
    1       Bus Stop  0.25
    2           Park  0.17
    3    Flower Shop  0.08
    4     Playground  0.08
    
    
    ----New Dorp----
                    venue  freq
    0  Italian Restaurant  0.12
    1         Pizza Place  0.08
    2         Yoga Studio  0.04
    3          Taco Place  0.04
    4  Mexican Restaurant  0.04
    
    
    ----New Dorp Beach----
                    venue  freq
    0  Italian Restaurant  0.21
    1                Food  0.14
    2       Deli / Bodega  0.14
    3          Restaurant  0.07
    4               Diner  0.07
    
    
    ----New Springville----
                    venue  freq
    0          Bagel Shop  0.08
    1  Chinese Restaurant  0.08
    2         Coffee Shop  0.08
    3   Mobile Phone Shop  0.08
    4   Accessories Store  0.04
    
    
    ----Oakwood----
                venue  freq
    0          Lawyer  0.50
    1  Nightlife Spot  0.25
    2             Bar  0.25
    3      Playground  0.00
    4     Outlet Mall  0.00
    
    
    ----Old Town----
                    venue  freq
    0  Italian Restaurant  0.24
    1          Restaurant  0.06
    2              Bakery  0.06
    3      Mattress Store  0.06
    4       Grocery Store  0.06
    
    
    ----Park Hill----
                      venue  freq
    0              Bus Stop  0.29
    1                  Park  0.14
    2  Gym / Fitness Center  0.14
    3    Athletics & Sports  0.14
    4           Coffee Shop  0.14
    
    
    ----Pleasant Plains----
                    venue  freq
    0          Donut Shop  0.14
    1         Yoga Studio  0.07
    2          Toll Plaza  0.07
    3        Liquor Store  0.07
    4  Salon / Barbershop  0.07
    
    
    ----Port Ivory----
                   venue  freq
    0   Business Service   1.0
    1  Accessories Store   0.0
    2  Other Repair Shop   0.0
    3        Outlet Mall   0.0
    4               Park   0.0
    
    
    ----Port Richmond----
                     venue  freq
    0  Rental Car Location  0.25
    1    Martial Arts Dojo  0.25
    2           Donut Shop  0.25
    3          Pizza Place  0.25
    4           Playground  0.00
    
    
    ----Prince's Bay----
                    venue  freq
    0         Pizza Place   0.2
    1  Chinese Restaurant   0.1
    2        Liquor Store   0.1
    3    Sushi Restaurant   0.1
    4      Ice Cream Shop   0.1
    
    
    ----Randall Manor----
                  venue  freq
    0      Home Service   0.2
    1              Park   0.2
    2          Bus Stop   0.2
    3  Business Service   0.2
    4        Bagel Shop   0.2
    
    
    ----Richmond Town----
                    venue  freq
    0  Italian Restaurant  0.25
    1                Café  0.25
    2                 Spa  0.25
    3          Bagel Shop  0.25
    4   Accessories Store  0.00
    
    
    ----Richmond Valley----
                            venue  freq
    0                        Bank  0.17
    1        Fast Food Restaurant  0.17
    2          Mexican Restaurant  0.08
    3  Construction & Landscaping  0.08
    4               Smoothie Shop  0.08
    
    
    ----Rosebank----
                    venue  freq
    0            Pharmacy  0.08
    1       Grocery Store  0.08
    2  Italian Restaurant  0.08
    3      Sandwich Place  0.04
    4               Beach  0.04
    
    
    ----Rossville----
                     venue  freq
    0          Pizza Place  0.27
    1           Bagel Shop  0.20
    2    Convenience Store  0.07
    3  American Restaurant  0.07
    4        Moving Target  0.07
    
    
    ----Sandy Ground----
              venue  freq
    0    Playground  0.14
    1      Bus Stop  0.14
    2   Art Gallery  0.14
    3     Racetrack  0.14
    4  Intersection  0.14
    
    
    ----Shore Acres----
                    venue  freq
    0  Italian Restaurant  0.12
    1            Bus Stop  0.12
    2       Deli / Bodega  0.08
    3        Intersection  0.08
    4                 Bar  0.08
    
    
    ----Silver Lake----
                     venue  freq
    0          Golf Course  0.25
    1                  Gym  0.25
    2         Burger Joint  0.25
    3  American Restaurant  0.25
    4    Recreation Center  0.00
    
    
    ----South Beach----
                    venue  freq
    0               Beach  0.33
    1                Pier  0.33
    2       Deli / Bodega  0.17
    3  Athletics & Sports  0.17
    4          Playground  0.00
    
    
    ----St. George----
                     venue  freq
    0       Clothing Store  0.16
    1  Sporting Goods Shop  0.05
    2                 Park  0.05
    3          Pizza Place  0.05
    4                  Bar  0.05
    
    
    ----Stapleton----
                venue  freq
    0  Discount Store  0.09
    1     Pizza Place  0.09
    2  Sandwich Place  0.06
    3            Bank  0.06
    4      Skate Park  0.03
    
    
    ----Sunnyside----
                     venue  freq
    0  American Restaurant   0.2
    1               Market   0.2
    2        Grocery Store   0.2
    3                  Gym   0.2
    4                  Spa   0.2
    
    
    ----Todt Hill----
                       venue  freq
    0                   Park   1.0
    1      Accessories Store   0.0
    2           Optical Shop   0.0
    3  Outdoors & Recreation   0.0
    4            Outlet Mall   0.0
    
    
    ----Tompkinsville----
                     venue  freq
    0          Pizza Place  0.11
    1             Bus Stop  0.11
    2                 Park  0.07
    3              Brewery  0.07
    4  Rental Car Location  0.04
    
    
    ----Tottenville----
                    venue  freq
    0            Bus Stop  0.12
    1              Lawyer  0.12
    2  Italian Restaurant  0.12
    3       Deli / Bodega  0.12
    4      Cosmetics Shop  0.12
    
    
    ----Travis----
               venue  freq
    0          Hotel  0.20
    1  Bowling Alley  0.13
    2  Deli / Bodega  0.13
    3            Gym  0.13
    4    Sports Club  0.07
    
    
    ----West Brighton----
                venue  freq
    0     Coffee Shop  0.08
    1        Pharmacy  0.05
    2  Breakfast Spot  0.05
    3     Music Store  0.05
    4             Bar  0.05
    
    
    ----Westerleigh----
                   venue  freq
    0   Sushi Restaurant  0.33
    1             Arcade  0.33
    2  Convenience Store  0.33
    3  Accessories Store  0.00
    4         Playground  0.00
    
    
    ----Willowbrook----
                    venue  freq
    0  Chinese Restaurant   0.4
    1       Deli / Bodega   0.2
    2            Bus Stop   0.2
    3                 Spa   0.2
    4               Plaza   0.0
    
    
    ----Woodrow----
                    venue  freq
    0            Pharmacy  0.11
    1              Bakery  0.05
    2       Grocery Store  0.05
    3         Pizza Place  0.05
    4  Chinese Restaurant  0.05
    
    



```python
def return_most_common_venues(row, num_top_venues):
    row_categories = row.iloc[1:]
    row_categories_sorted = row_categories.sort_values(ascending=False)
    
    return row_categories_sorted.index.values[0:num_top_venues]
```


```python
num_top_venues = 10

indicators = ['st', 'nd', 'rd']

# create columns according to number of top venues
columns = ['Neighborhood']
for ind in np.arange(num_top_venues):
    try:
        columns.append('{}{} Most Common Venue'.format(ind+1, indicators[ind]))
    except:
        columns.append('{}th Most Common Venue'.format(ind+1))

# create a new dataframe
neighborhoods_venues_sorted = pd.DataFrame(columns=columns)
neighborhoods_venues_sorted['Neighborhood'] = statenisland_grouped['Neighborhood']

for ind in np.arange(statenisland_grouped.shape[0]):
    neighborhoods_venues_sorted.iloc[ind, 1:] = return_most_common_venues(statenisland_grouped.iloc[ind, :], num_top_venues)

neighborhoods_venues_sorted.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Neighborhood</th>
      <th>1st Most Common Venue</th>
      <th>2nd Most Common Venue</th>
      <th>3rd Most Common Venue</th>
      <th>4th Most Common Venue</th>
      <th>5th Most Common Venue</th>
      <th>6th Most Common Venue</th>
      <th>7th Most Common Venue</th>
      <th>8th Most Common Venue</th>
      <th>9th Most Common Venue</th>
      <th>10th Most Common Venue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Annadale</td>
      <td>Pizza Place</td>
      <td>Train Station</td>
      <td>Food</td>
      <td>Pharmacy</td>
      <td>Diner</td>
      <td>Restaurant</td>
      <td>Dance Studio</td>
      <td>Deli / Bodega</td>
      <td>American Restaurant</td>
      <td>Fast Food Restaurant</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Arden Heights</td>
      <td>Deli / Bodega</td>
      <td>Lawyer</td>
      <td>Bus Stop</td>
      <td>Business Service</td>
      <td>Coffee Shop</td>
      <td>Pizza Place</td>
      <td>Pharmacy</td>
      <td>Fast Food Restaurant</td>
      <td>Food Truck</td>
      <td>Food &amp; Drink Shop</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Arlington</td>
      <td>Deli / Bodega</td>
      <td>Boat or Ferry</td>
      <td>Construction &amp; Landscaping</td>
      <td>Coffee Shop</td>
      <td>Bus Stop</td>
      <td>Filipino Restaurant</td>
      <td>Furniture / Home Store</td>
      <td>French Restaurant</td>
      <td>Food Truck</td>
      <td>Food &amp; Drink Shop</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Arrochar</td>
      <td>Bus Stop</td>
      <td>Liquor Store</td>
      <td>Italian Restaurant</td>
      <td>Deli / Bodega</td>
      <td>Polish Restaurant</td>
      <td>Outdoors &amp; Recreation</td>
      <td>Supermarket</td>
      <td>Middle Eastern Restaurant</td>
      <td>Mediterranean Restaurant</td>
      <td>Sandwich Place</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Bay Terrace</td>
      <td>Supermarket</td>
      <td>Insurance Office</td>
      <td>Italian Restaurant</td>
      <td>Train Station</td>
      <td>Sushi Restaurant</td>
      <td>Liquor Store</td>
      <td>Salon / Barbershop</td>
      <td>Donut Shop</td>
      <td>Shipping Store</td>
      <td>Fast Food Restaurant</td>
    </tr>
  </tbody>
</table>
</div>



 <h3 id="version">4. Cluster Neighborhoods</h3>

<p>Run k-means to cluster the neighborhood into 5 clusters.</p>


```python
#import k-means from clustering stage
from sklearn.cluster import KMeans

# set number of clusters
kclusters = 5

statenisland_grouped_clustering = statenisland_grouped.drop('Neighborhood', 1)

# run k-means clustering
kmeans = KMeans(n_clusters=kclusters, random_state=0).fit(statenisland_grouped_clustering)

# check cluster labels generated for each row in the dataframe
kmeans.labels_[0:10] 
```




    array([2, 0, 0, 2, 2, 2, 2, 2, 2, 2], dtype=int32)




```python
# add clustering labels
neighborhoods_venues_sorted.insert(0, 'Cluster Labels', kmeans.labels_)

Staten_Island_merged = Staten_Island

# merge toronto_grouped with toronto_data to add latitude/longitude for each neighborhood
Staten_Island_merged = Staten_Island_merged.join(neighborhoods_venues_sorted.set_index('Neighborhood'), on='Neighborhood')

Staten_Island_merged.head() # check the last columns!
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Borough</th>
      <th>Neighborhood</th>
      <th>Latitude</th>
      <th>Longitude</th>
      <th>Cluster Labels</th>
      <th>1st Most Common Venue</th>
      <th>2nd Most Common Venue</th>
      <th>3rd Most Common Venue</th>
      <th>4th Most Common Venue</th>
      <th>5th Most Common Venue</th>
      <th>6th Most Common Venue</th>
      <th>7th Most Common Venue</th>
      <th>8th Most Common Venue</th>
      <th>9th Most Common Venue</th>
      <th>10th Most Common Venue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Staten Island</td>
      <td>St. George</td>
      <td>40.644982</td>
      <td>-74.079353</td>
      <td>2</td>
      <td>Clothing Store</td>
      <td>Sporting Goods Shop</td>
      <td>Italian Restaurant</td>
      <td>Park</td>
      <td>Bar</td>
      <td>Pizza Place</td>
      <td>Outlet Mall</td>
      <td>Baseball Stadium</td>
      <td>Bus Stop</td>
      <td>Bus Station</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Staten Island</td>
      <td>New Brighton</td>
      <td>40.640615</td>
      <td>-74.087017</td>
      <td>0</td>
      <td>Deli / Bodega</td>
      <td>Bus Stop</td>
      <td>Park</td>
      <td>Discount Store</td>
      <td>Playground</td>
      <td>Flower Shop</td>
      <td>Bowling Alley</td>
      <td>Filipino Restaurant</td>
      <td>French Restaurant</td>
      <td>Food Truck</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Staten Island</td>
      <td>Stapleton</td>
      <td>40.626928</td>
      <td>-74.077902</td>
      <td>2</td>
      <td>Pizza Place</td>
      <td>Discount Store</td>
      <td>Sandwich Place</td>
      <td>Bank</td>
      <td>Restaurant</td>
      <td>Spanish Restaurant</td>
      <td>Fast Food Restaurant</td>
      <td>Skate Park</td>
      <td>New American Restaurant</td>
      <td>Optical Shop</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Staten Island</td>
      <td>Rosebank</td>
      <td>40.615305</td>
      <td>-74.069805</td>
      <td>2</td>
      <td>Pharmacy</td>
      <td>Italian Restaurant</td>
      <td>Grocery Store</td>
      <td>Breakfast Spot</td>
      <td>Beach</td>
      <td>Pizza Place</td>
      <td>Deli / Bodega</td>
      <td>Cosmetics Shop</td>
      <td>Ice Cream Shop</td>
      <td>Eastern European Restaurant</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Staten Island</td>
      <td>West Brighton</td>
      <td>40.631879</td>
      <td>-74.107182</td>
      <td>2</td>
      <td>Coffee Shop</td>
      <td>Pharmacy</td>
      <td>Bank</td>
      <td>Italian Restaurant</td>
      <td>Music Store</td>
      <td>Breakfast Spot</td>
      <td>Bar</td>
      <td>Bus Stop</td>
      <td>Café</td>
      <td>Sandwich Place</td>
    </tr>
  </tbody>
</table>
</div>




```python
import matplotlib.cm as cm
import matplotlib.colors as colors

# create map
map_clusters = folium.Map(location=[latitude, longitude], zoom_start=11)

# set color scheme for the clusters
x = np.arange(kclusters)
ys = [i + x + (i*x)**2 for i in range(kclusters)]
colors_array = cm.rainbow(np.linspace(0, 1, len(ys)))
rainbow = [colors.rgb2hex(i) for i in colors_array]

# add markers to the map
markers_colors = []
for lat, lon, poi, cluster in zip(Staten_Island_merged['Latitude'], Staten_Island_merged['Longitude'], Staten_Island_merged['Neighborhood'], Staten_Island_merged['Cluster Labels']):
    label = folium.Popup(str(poi) + ' Cluster ' + str(cluster), parse_html=True)
    folium.CircleMarker(
        [lat, lon],
        radius=5,
        popup=label,
        color=rainbow[cluster-1],
        fill=True,
        fill_color=rainbow[cluster-1],
        fill_opacity=0.7).add_to(map_clusters)
       
map_clusters
```




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><span style="color:#565656">Make this Notebook Trusted to load map: File -> Trust Notebook</span><iframe src="about:blank" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" data-html=PCFET0NUWVBFIGh0bWw+CjxoZWFkPiAgICAKICAgIDxtZXRhIGh0dHAtZXF1aXY9ImNvbnRlbnQtdHlwZSIgY29udGVudD0idGV4dC9odG1sOyBjaGFyc2V0PVVURi04IiAvPgogICAgPHNjcmlwdD5MX1BSRUZFUl9DQU5WQVMgPSBmYWxzZTsgTF9OT19UT1VDSCA9IGZhbHNlOyBMX0RJU0FCTEVfM0QgPSBmYWxzZTs8L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2FqYXguZ29vZ2xlYXBpcy5jb20vYWpheC9saWJzL2pxdWVyeS8xLjExLjEvanF1ZXJ5Lm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvanMvYm9vdHN0cmFwLm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9jZG5qcy5jbG91ZGZsYXJlLmNvbS9hamF4L2xpYnMvTGVhZmxldC5hd2Vzb21lLW1hcmtlcnMvMi4wLjIvbGVhZmxldC5hd2Vzb21lLW1hcmtlcnMuanMiPjwvc2NyaXB0PgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9jc3MvYm9vdHN0cmFwLm1pbi5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvY3NzL2Jvb3RzdHJhcC10aGVtZS5taW4uY3NzIi8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vbWF4Y2RuLmJvb3RzdHJhcGNkbi5jb20vZm9udC1hd2Vzb21lLzQuNi4zL2Nzcy9mb250LWF3ZXNvbWUubWluLmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2NkbmpzLmNsb3VkZmxhcmUuY29tL2FqYXgvbGlicy9MZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy8yLjAuMi9sZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9yYXdnaXQuY29tL3B5dGhvbi12aXN1YWxpemF0aW9uL2ZvbGl1bS9tYXN0ZXIvZm9saXVtL3RlbXBsYXRlcy9sZWFmbGV0LmF3ZXNvbWUucm90YXRlLmNzcyIvPgogICAgPHN0eWxlPmh0bWwsIGJvZHkge3dpZHRoOiAxMDAlO2hlaWdodDogMTAwJTttYXJnaW46IDA7cGFkZGluZzogMDt9PC9zdHlsZT4KICAgIDxzdHlsZT4jbWFwIHtwb3NpdGlvbjphYnNvbHV0ZTt0b3A6MDtib3R0b206MDtyaWdodDowO2xlZnQ6MDt9PC9zdHlsZT4KICAgIAogICAgICAgICAgICA8c3R5bGU+ICNtYXBfZmVmMjgzYmM1YWEzNGUwYTkxNTE1YzNlNDA2ZDgxNDUgewogICAgICAgICAgICAgICAgcG9zaXRpb24gOiByZWxhdGl2ZTsKICAgICAgICAgICAgICAgIHdpZHRoIDogMTAwLjAlOwogICAgICAgICAgICAgICAgaGVpZ2h0OiAxMDAuMCU7CiAgICAgICAgICAgICAgICBsZWZ0OiAwLjAlOwogICAgICAgICAgICAgICAgdG9wOiAwLjAlOwogICAgICAgICAgICAgICAgfQogICAgICAgICAgICA8L3N0eWxlPgogICAgICAgIAo8L2hlYWQ+Cjxib2R5PiAgICAKICAgIAogICAgICAgICAgICA8ZGl2IGNsYXNzPSJmb2xpdW0tbWFwIiBpZD0ibWFwX2ZlZjI4M2JjNWFhMzRlMGE5MTUxNWMzZTQwNmQ4MTQ1IiA+PC9kaXY+CiAgICAgICAgCjwvYm9keT4KPHNjcmlwdD4gICAgCiAgICAKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGJvdW5kcyA9IG51bGw7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgdmFyIG1hcF9mZWYyODNiYzVhYTM0ZTBhOTE1MTVjM2U0MDZkODE0NSA9IEwubWFwKAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJ21hcF9mZWYyODNiYzVhYTM0ZTBhOTE1MTVjM2U0MDZkODE0NScsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB7Y2VudGVyOiBbNDAuNTgzNDU1NywtNzQuMTQ5NjA0OF0sCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB6b29tOiAxMSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIG1heEJvdW5kczogYm91bmRzLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbGF5ZXJzOiBbXSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHdvcmxkQ29weUp1bXA6IGZhbHNlLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgY3JzOiBMLkNSUy5FUFNHMzg1NwogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB9KTsKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHRpbGVfbGF5ZXJfNTU3YmY2N2M4YjVlNDgyMGI5ZjkxNGMzZDI0NmUwOTAgPSBMLnRpbGVMYXllcigKICAgICAgICAgICAgICAgICdodHRwczovL3tzfS50aWxlLm9wZW5zdHJlZXRtYXAub3JnL3t6fS97eH0ve3l9LnBuZycsCiAgICAgICAgICAgICAgICB7CiAgImF0dHJpYnV0aW9uIjogbnVsbCwKICAiZGV0ZWN0UmV0aW5hIjogZmFsc2UsCiAgIm1heFpvb20iOiAxOCwKICAibWluWm9vbSI6IDEsCiAgIm5vV3JhcCI6IGZhbHNlLAogICJzdWJkb21haW5zIjogImFiYyIKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfZmVmMjgzYmM1YWEzNGUwYTkxNTE1YzNlNDA2ZDgxNDUpOwogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzAxN2E0OWM5YzZjZTRkN2RhMmM5ODgyY2FiMmUxZjNjID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjQ0OTgxNTcxMDA0NCwtNzQuMDc5MzUzMTI1MTI3OTddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzAwYjVlYiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMwMGI1ZWIiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfZmVmMjgzYmM1YWEzNGUwYTkxNTE1YzNlNDA2ZDgxNDUpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYTFmMzA4NGM0MDY0NGI4YWFhZWMwMDZjMTMxNzY5YjggPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYzJhMjkyM2U3MjM2NDk4ZDlmNmYxYTg2ZmM2MDZkNTEgPSAkKCc8ZGl2IGlkPSJodG1sX2MyYTI5MjNlNzIzNjQ5OGQ5ZjZmMWE4NmZjNjA2ZDUxIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5TdC4gR2VvcmdlIENsdXN0ZXIgMjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYTFmMzA4NGM0MDY0NGI4YWFhZWMwMDZjMTMxNzY5Yjguc2V0Q29udGVudChodG1sX2MyYTI5MjNlNzIzNjQ5OGQ5ZjZmMWE4NmZjNjA2ZDUxKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzAxN2E0OWM5YzZjZTRkN2RhMmM5ODgyY2FiMmUxZjNjLmJpbmRQb3B1cChwb3B1cF9hMWYzMDg0YzQwNjQ0YjhhYWFlYzAwNmMxMzE3NjliOCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8yYmYyNGQ1YTRhMjY0N2Y0YWM2OTI3OTFlMmU2YzFlNiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjY0MDYxNDU1OTEzNTExLC03NC4wODcwMTY1MDUxNjYyNV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9mZWYyODNiYzVhYTM0ZTBhOTE1MTVjM2U0MDZkODE0NSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8wNGRjOTA1ZGEzODY0NDgxYjAyMWQ0YjQ1ODhhNDE4NiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9jYjc4YmYxZTg4YmU0MjY1ODRmOGM2OTQ3OTU1YWMwOCA9ICQoJzxkaXYgaWQ9Imh0bWxfY2I3OGJmMWU4OGJlNDI2NTg0ZjhjNjk0Nzk1NWFjMDgiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk5ldyBCcmlnaHRvbiBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzA0ZGM5MDVkYTM4NjQ0ODFiMDIxZDRiNDU4OGE0MTg2LnNldENvbnRlbnQoaHRtbF9jYjc4YmYxZTg4YmU0MjY1ODRmOGM2OTQ3OTU1YWMwOCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8yYmYyNGQ1YTRhMjY0N2Y0YWM2OTI3OTFlMmU2YzFlNi5iaW5kUG9wdXAocG9wdXBfMDRkYzkwNWRhMzg2NDQ4MWIwMjFkNGI0NTg4YTQxODYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfM2MxZjRlOThlMDNiNGExOTkxOGQ3YjUxN2RhMzI0NGYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42MjY5Mjc2MjUzODE3NiwtNzQuMDc3OTAxOTI2NjAwNjZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzAwYjVlYiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMwMGI1ZWIiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfZmVmMjgzYmM1YWEzNGUwYTkxNTE1YzNlNDA2ZDgxNDUpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMmEyZDExNjYwYTY5NDVlNzhhNzhkYWFiZTk1NWNlMTIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMmMxM2QxYTJlNzVhNDc1MDlhYjZkZmQxMDE0NmZiMDMgPSAkKCc8ZGl2IGlkPSJodG1sXzJjMTNkMWEyZTc1YTQ3NTA5YWI2ZGZkMTAxNDZmYjAzIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5TdGFwbGV0b24gQ2x1c3RlciAyPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8yYTJkMTE2NjBhNjk0NWU3OGE3OGRhYWJlOTU1Y2UxMi5zZXRDb250ZW50KGh0bWxfMmMxM2QxYTJlNzVhNDc1MDlhYjZkZmQxMDE0NmZiMDMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfM2MxZjRlOThlMDNiNGExOTkxOGQ3YjUxN2RhMzI0NGYuYmluZFBvcHVwKHBvcHVwXzJhMmQxMTY2MGE2OTQ1ZTc4YTc4ZGFhYmU5NTVjZTEyKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2QyYWY5ZjgyZTI1NTQyZWU5OTRiMTY0MzUxNzMxNzJlID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjE1MzA0OTQ2NTI3NjEsLTc0LjA2OTgwNTI2NzE2MTQxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiMwMGI1ZWIiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMDBiNWViIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2ZlZjI4M2JjNWFhMzRlMGE5MTUxNWMzZTQwNmQ4MTQ1KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2RlMmUyMWQ2NWFkMzQ2NjliMjc1OTA3ZDdjYzNlMzY2ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzJjOGQ0Y2EyNmUzMjQ2NjI4ZjAzZjU3YTAzOTZmMjFkID0gJCgnPGRpdiBpZD0iaHRtbF8yYzhkNGNhMjZlMzI0NjYyOGYwM2Y1N2EwMzk2ZjIxZCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Um9zZWJhbmsgQ2x1c3RlciAyPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9kZTJlMjFkNjVhZDM0NjY5YjI3NTkwN2Q3Y2MzZTM2Ni5zZXRDb250ZW50KGh0bWxfMmM4ZDRjYTI2ZTMyNDY2MjhmMDNmNTdhMDM5NmYyMWQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZDJhZjlmODJlMjU1NDJlZTk5NGIxNjQzNTE3MzE3MmUuYmluZFBvcHVwKHBvcHVwX2RlMmUyMWQ2NWFkMzQ2NjliMjc1OTA3ZDdjYzNlMzY2KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzBlNGUzZGY4NThlYjQ3YzRhYTU3NGVlMmU1NGYwMTc3ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjMxODc4OTI2NTQ2MDcsLTc0LjEwNzE4MTc4MjY1NjFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzAwYjVlYiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMwMGI1ZWIiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfZmVmMjgzYmM1YWEzNGUwYTkxNTE1YzNlNDA2ZDgxNDUpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfOTY3NTNhM2NkNzY2NGNiNmE5NDA1N2JiNmE2YjdhZmIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZWU0NzY2NjIwMDI2NDM0Yjk1NTZkZGQ1OWE2MWUxNDQgPSAkKCc8ZGl2IGlkPSJodG1sX2VlNDc2NjYyMDAyNjQzNGI5NTU2ZGRkNTlhNjFlMTQ0IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5XZXN0IEJyaWdodG9uIENsdXN0ZXIgMjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOTY3NTNhM2NkNzY2NGNiNmE5NDA1N2JiNmE2YjdhZmIuc2V0Q29udGVudChodG1sX2VlNDc2NjYyMDAyNjQzNGI5NTU2ZGRkNTlhNjFlMTQ0KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzBlNGUzZGY4NThlYjQ3YzRhYTU3NGVlMmU1NGYwMTc3LmJpbmRQb3B1cChwb3B1cF85Njc1M2EzY2Q3NjY0Y2I2YTk0MDU3YmI2YTZiN2FmYik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8xMDk4NDAxZDA3OTg0MTkzOThlOTAxNGRhNmE2Y2Q4NCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYyNDE4NDc5MTMxMzAwNiwtNzQuMDg3MjQ4MTk5ODM3MjldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfZmVmMjgzYmM1YWEzNGUwYTkxNTE1YzNlNDA2ZDgxNDUpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYjE5MmFhODliNWI2NDJiZWE0ZTg3NmVkYjQ3MjQ4ZjUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYTYxMDkzMDA4ODNlNDA2NzljNWEyMjU5NThiODNjMjYgPSAkKCc8ZGl2IGlkPSJodG1sX2E2MTA5MzAwODgzZTQwNjc5YzVhMjI1OTU4YjgzYzI2IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5HcnltZXMgSGlsbCBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2IxOTJhYTg5YjViNjQyYmVhNGU4NzZlZGI0NzI0OGY1LnNldENvbnRlbnQoaHRtbF9hNjEwOTMwMDg4M2U0MDY3OWM1YTIyNTk1OGI4M2MyNik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8xMDk4NDAxZDA3OTg0MTkzOThlOTAxNGRhNmE2Y2Q4NC5iaW5kUG9wdXAocG9wdXBfYjE5MmFhODliNWI2NDJiZWE0ZTg3NmVkYjQ3MjQ4ZjUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMmU1ZWQ0Mjc1YzA1NDQwNDlhZjRlYWQyZTJjMGM1NTAgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41OTcwNjg1MTgxNDY3MywtNzQuMTExMzI4ODE4MDA4OF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmZiMzYwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmYjM2MCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9mZWYyODNiYzVhYTM0ZTBhOTE1MTVjM2U0MDZkODE0NSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF84ZThiNWE4MzJmYmI0YjNlYjhiZWVmM2RmOWI4ZTc3MCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9jMmQ2N2ZkOTcxYTk0YzM5OGY0NWQ2YzFlYTY2OTExNiA9ICQoJzxkaXYgaWQ9Imh0bWxfYzJkNjdmZDk3MWE5NGMzOThmNDVkNmMxZWE2NjkxMTYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRvZHQgSGlsbCBDbHVzdGVyIDQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzhlOGI1YTgzMmZiYjRiM2ViOGJlZWYzZGY5YjhlNzcwLnNldENvbnRlbnQoaHRtbF9jMmQ2N2ZkOTcxYTk0YzM5OGY0NWQ2YzFlYTY2OTExNik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8yZTVlZDQyNzVjMDU0NDA0OWFmNGVhZDJlMmMwYzU1MC5iaW5kUG9wdXAocG9wdXBfOGU4YjVhODMyZmJiNGIzZWI4YmVlZjNkZjliOGU3NzApOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMTI1NDgxNDc4ODM1NGM2YmJjMmIxYzIyMjEwZWQ5NWEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41ODAyNDc0MTM1MDk1NiwtNzQuMDc5NTUyOTI1Mzk4Ml0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjMDBiNWViIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzAwYjVlYiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9mZWYyODNiYzVhYTM0ZTBhOTE1MTVjM2U0MDZkODE0NSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9iOWFjMTFjODQ3Zjk0M2QzYjNmMzgzYWViOWQ0NDhjZCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9lYWU5MjM2MDI0N2I0YjU5OGRlMGYzYjUxNWYzYzg4OCA9ICQoJzxkaXYgaWQ9Imh0bWxfZWFlOTIzNjAyNDdiNGI1OThkZTBmM2I1MTVmM2M4ODgiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlNvdXRoIEJlYWNoIENsdXN0ZXIgMjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYjlhYzExYzg0N2Y5NDNkM2IzZjM4M2FlYjlkNDQ4Y2Quc2V0Q29udGVudChodG1sX2VhZTkyMzYwMjQ3YjRiNTk4ZGUwZjNiNTE1ZjNjODg4KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzEyNTQ4MTQ3ODgzNTRjNmJiYzJiMWMyMjIxMGVkOTVhLmJpbmRQb3B1cChwb3B1cF9iOWFjMTFjODQ3Zjk0M2QzYjNmMzgzYWViOWQ0NDhjZCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl81ZmIyNTNjYWMxMmI0MTRmYWI0OGU5ZTYyODJhYzU1OSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYzMzY2OTMwNTU0MzY1LC03NC4xMjk0MzQyNjc5NzAwOF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjMDBiNWViIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzAwYjVlYiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9mZWYyODNiYzVhYTM0ZTBhOTE1MTVjM2U0MDZkODE0NSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9hZTA0ODYxN2Y4YzY0NGM4OTI2OWRmOWViYWFmZDg5NyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8wNTFlNTNkYWI5ZjM0YjVjYmRmYjkxMzBlMWVmODUzNCA9ICQoJzxkaXYgaWQ9Imh0bWxfMDUxZTUzZGFiOWYzNGI1Y2JkZmI5MTMwZTFlZjg1MzQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlBvcnQgUmljaG1vbmQgQ2x1c3RlciAyPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9hZTA0ODYxN2Y4YzY0NGM4OTI2OWRmOWViYWFmZDg5Ny5zZXRDb250ZW50KGh0bWxfMDUxZTUzZGFiOWYzNGI1Y2JkZmI5MTMwZTFlZjg1MzQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNWZiMjUzY2FjMTJiNDE0ZmFiNDhlOWU2MjgyYWM1NTkuYmluZFBvcHVwKHBvcHVwX2FlMDQ4NjE3ZjhjNjQ0Yzg5MjY5ZGY5ZWJhYWZkODk3KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2EzZmQ5ZGFiZTI2YTQ4Mjc5ZmM3YTA1MzYxNTZiYWVlID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjMyNTQ2MzkwNDgxMTI0LC03NC4xNTAwODUzNzA0Njk4MV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9mZWYyODNiYzVhYTM0ZTBhOTE1MTVjM2U0MDZkODE0NSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF83MmVlOWZjZmJiNjk0MTQ3YTVkYjk4YzdmODlmODgxYSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9mMzBkZGFhYTk5MTQ0ZGUzOGM5OTgzMzE3ZWQ2N2FmMSA9ICQoJzxkaXYgaWQ9Imh0bWxfZjMwZGRhYWE5OTE0NGRlMzhjOTk4MzMxN2VkNjdhZjEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk1hcmluZXImIzM5O3MgSGFyYm9yIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNzJlZTlmY2ZiYjY5NDE0N2E1ZGI5OGM3Zjg5Zjg4MWEuc2V0Q29udGVudChodG1sX2YzMGRkYWFhOTkxNDRkZTM4Yzk5ODMzMTdlZDY3YWYxKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2EzZmQ5ZGFiZTI2YTQ4Mjc5ZmM3YTA1MzYxNTZiYWVlLmJpbmRQb3B1cChwb3B1cF83MmVlOWZjZmJiNjk0MTQ3YTVkYjk4YzdmODlmODgxYSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl83Mjg0N2Y3YmI5NTE0NTdkOTAyMzBlZDcwZDMyMDljNyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYzOTY4Mjk3ODQ1NTQyLC03NC4xNzQ2NDUzMjk5MzU0Ml0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjODBmZmI0IiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzgwZmZiNCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9mZWYyODNiYzVhYTM0ZTBhOTE1MTVjM2U0MDZkODE0NSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF80YTYzNWU3NTA1MTM0NzQ2YmYxZWRjYWZmM2E0M2FiOSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8yZTczYTk4NzcwNzI0YTI2OWI5OTg0ZWQxOTVkNTUwNCA9ICQoJzxkaXYgaWQ9Imh0bWxfMmU3M2E5ODc3MDcyNGEyNjliOTk4NGVkMTk1ZDU1MDQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlBvcnQgSXZvcnkgQ2x1c3RlciAzPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF80YTYzNWU3NTA1MTM0NzQ2YmYxZWRjYWZmM2E0M2FiOS5zZXRDb250ZW50KGh0bWxfMmU3M2E5ODc3MDcyNGEyNjliOTk4NGVkMTk1ZDU1MDQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNzI4NDdmN2JiOTUxNDU3ZDkwMjMwZWQ3MGQzMjA5YzcuYmluZFBvcHVwKHBvcHVwXzRhNjM1ZTc1MDUxMzQ3NDZiZjFlZGNhZmYzYTQzYWI5KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2ZhNzNhNDY0MzAzZjQyMWVhMDBiMTE0OGFjNjIyMjY4ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjEzMzM1OTM3NjY3NDIsLTc0LjExOTE4MDU4NTM0ODQyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiMwMGI1ZWIiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMDBiNWViIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2ZlZjI4M2JjNWFhMzRlMGE5MTUxNWMzZTQwNmQ4MTQ1KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2M0ZmUxYzA3MDMxOTQwOGFhNDUzYTBmNDI1YTYyZGZkID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2UzYzMyYTJmMDM3NjQ5NTc5ZDY4NjUwZTM2YTE3ZWZmID0gJCgnPGRpdiBpZD0iaHRtbF9lM2MzMmEyZjAzNzY0OTU3OWQ2ODY1MGUzNmExN2VmZiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q2FzdGxldG9uIENvcm5lcnMgQ2x1c3RlciAyPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9jNGZlMWMwNzAzMTk0MDhhYTQ1M2EwZjQyNWE2MmRmZC5zZXRDb250ZW50KGh0bWxfZTNjMzJhMmYwMzc2NDk1NzlkNjg2NTBlMzZhMTdlZmYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZmE3M2E0NjQzMDNmNDIxZWEwMGIxMTQ4YWM2MjIyNjguYmluZFBvcHVwKHBvcHVwX2M0ZmUxYzA3MDMxOTQwOGFhNDUzYTBmNDI1YTYyZGZkKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzBmNjVkNDdjN2QyZDQwMzc4N2NlNDljYWZkY2JjZDYxID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTk0MjUyMzc5MTYxNjk1LC03NC4xNjQ5NjAzMTMyOTgyN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjMDBiNWViIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzAwYjVlYiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9mZWYyODNiYzVhYTM0ZTBhOTE1MTVjM2U0MDZkODE0NSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9kZDkyMzhhZTUyMWQ0MzJmYjU5OGI2MmQ3OTcwNjE4MSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF85MmU1MDMxNDk1NjA0M2MxODFiNTA3MzEyN2ZkOWRiYSA9ICQoJzxkaXYgaWQ9Imh0bWxfOTJlNTAzMTQ5NTYwNDNjMTgxYjUwNzMxMjdmZDlkYmEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk5ldyBTcHJpbmd2aWxsZSBDbHVzdGVyIDI8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2RkOTIzOGFlNTIxZDQzMmZiNTk4YjYyZDc5NzA2MTgxLnNldENvbnRlbnQoaHRtbF85MmU1MDMxNDk1NjA0M2MxODFiNTA3MzEyN2ZkOWRiYSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8wZjY1ZDQ3YzdkMmQ0MDM3ODdjZTQ5Y2FmZGNiY2Q2MS5iaW5kUG9wdXAocG9wdXBfZGQ5MjM4YWU1MjFkNDMyZmI1OThiNjJkNzk3MDYxODEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMzZhNjg0N2E3NGQ5NDU4YTlkNWQ4N2ZlZjA3ZDM1ZjUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41ODYzMTM3NTEwMzI4MSwtNzQuMTkwNzM3MTc1MzgxMTZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzAwYjVlYiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMwMGI1ZWIiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfZmVmMjgzYmM1YWEzNGUwYTkxNTE1YzNlNDA2ZDgxNDUpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMzNkNzM2NWUyODI4NDBiM2FjMjM2NzBlMTM0ZWZjZDMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZWIwM2QxMGRiYTQwNDgyOWJkNTUwNWM0ZjNmNDc1ZGQgPSAkKCc8ZGl2IGlkPSJodG1sX2ViMDNkMTBkYmE0MDQ4MjliZDU1MDVjNGYzZjQ3NWRkIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UcmF2aXMgQ2x1c3RlciAyPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8zM2Q3MzY1ZTI4Mjg0MGIzYWMyMzY3MGUxMzRlZmNkMy5zZXRDb250ZW50KGh0bWxfZWIwM2QxMGRiYTQwNDgyOWJkNTUwNWM0ZjNmNDc1ZGQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMzZhNjg0N2E3NGQ5NDU4YTlkNWQ4N2ZlZjA3ZDM1ZjUuYmluZFBvcHVwKHBvcHVwXzMzZDczNjVlMjgyODQwYjNhYzIzNjcwZTEzNGVmY2QzKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzNkMGM3ZTBmNGJhOTQxYmNhZDMyZmQwODA4Y2VkYTg3ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTcyNTcyMzE4MjA2MzIsLTc0LjExNjQ3OTQzNjA2MzhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzAwYjVlYiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMwMGI1ZWIiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfZmVmMjgzYmM1YWEzNGUwYTkxNTE1YzNlNDA2ZDgxNDUpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZDU5NjFiNzE5YjJjNDMzZDgxMWYzZTMwNmY2MzliMTYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfM2Q1ZGY2YmU1N2QxNDY5Zjg4MTc1MjczZWYxNTIzODkgPSAkKCc8ZGl2IGlkPSJodG1sXzNkNWRmNmJlNTdkMTQ2OWY4ODE3NTI3M2VmMTUyMzg5IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5OZXcgRG9ycCBDbHVzdGVyIDI8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2Q1OTYxYjcxOWIyYzQzM2Q4MTFmM2UzMDZmNjM5YjE2LnNldENvbnRlbnQoaHRtbF8zZDVkZjZiZTU3ZDE0NjlmODgxNzUyNzNlZjE1MjM4OSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8zZDBjN2UwZjRiYTk0MWJjYWQzMmZkMDgwOGNlZGE4Ny5iaW5kUG9wdXAocG9wdXBfZDU5NjFiNzE5YjJjNDMzZDgxMWYzZTMwNmY2MzliMTYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMWRkY2E4NDk3Y2NmNGVkNzliZjcyYjJhYWVmMDE4MWIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41NTg0NjIyNDMyODg4LC03NC4xMjE1NjU5Mzc3MTg5Nl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjMDBiNWViIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzAwYjVlYiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9mZWYyODNiYzVhYTM0ZTBhOTE1MTVjM2U0MDZkODE0NSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8xMjgzNDEwOTI2MzU0Y2FjOTUyMjM0N2M4ODQ5ZWU1MSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF84NjljYzMyZThlMzM0MWU0YWJkMGQ0ZTkyOTNmYTIyYSA9ICQoJzxkaXYgaWQ9Imh0bWxfODY5Y2MzMmU4ZTMzNDFlNGFiZDBkNGU5MjkzZmEyMmEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk9ha3dvb2QgQ2x1c3RlciAyPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8xMjgzNDEwOTI2MzU0Y2FjOTUyMjM0N2M4ODQ5ZWU1MS5zZXRDb250ZW50KGh0bWxfODY5Y2MzMmU4ZTMzNDFlNGFiZDBkNGU5MjkzZmEyMmEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMWRkY2E4NDk3Y2NmNGVkNzliZjcyYjJhYWVmMDE4MWIuYmluZFBvcHVwKHBvcHVwXzEyODM0MTA5MjYzNTRjYWM5NTIyMzQ3Yzg4NDllZTUxKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzlkMzlhYzA3MzVmODQxYjY5OWM5NGU0MDUxMzM0NThhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTQ5NDgwMjI4NzEzNjA1LC03NC4xNDkzMjM4MTQ5MDk5Ml0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjMDBiNWViIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzAwYjVlYiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9mZWYyODNiYzVhYTM0ZTBhOTE1MTVjM2U0MDZkODE0NSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8xYTg2YmQzYWI3ZDM0NTYxYjI2MTg3ZmM4OTU3YTJkNSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8zMWZkMDlmNGExMDI0OTAzOTNlYjcxZTViYWI3ZDIwMiA9ICQoJzxkaXYgaWQ9Imh0bWxfMzFmZDA5ZjRhMTAyNDkwMzkzZWI3MWU1YmFiN2QyMDIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkdyZWF0IEtpbGxzIENsdXN0ZXIgMjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMWE4NmJkM2FiN2QzNDU2MWIyNjE4N2ZjODk1N2EyZDUuc2V0Q29udGVudChodG1sXzMxZmQwOWY0YTEwMjQ5MDM5M2ViNzFlNWJhYjdkMjAyKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzlkMzlhYzA3MzVmODQxYjY5OWM5NGU0MDUxMzM0NThhLmJpbmRQb3B1cChwb3B1cF8xYTg2YmQzYWI3ZDM0NTYxYjI2MTg3ZmM4OTU3YTJkNSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9lNThjNDExNTRmMzE0OThmODcwYTRkYmNmNWJiZGNmOSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjU0MjIzMDc0NzQ1MDc0NSwtNzQuMTY0MzMwODA0MTkzNl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjMDBiNWViIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzAwYjVlYiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9mZWYyODNiYzVhYTM0ZTBhOTE1MTVjM2U0MDZkODE0NSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9kMTgzMDVjM2I5NzE0ZDY1OGE0N2MxMjQ4MGNiMThhMyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9hZGJlNjlkNDVmZWI0YjZiYjlmYmFmODk2ZDVjMzhkMyA9ICQoJzxkaXYgaWQ9Imh0bWxfYWRiZTY5ZDQ1ZmViNGI2YmI5ZmJhZjg5NmQ1YzM4ZDMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkVsdGluZ3ZpbGxlIENsdXN0ZXIgMjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZDE4MzA1YzNiOTcxNGQ2NThhNDdjMTI0ODBjYjE4YTMuc2V0Q29udGVudChodG1sX2FkYmU2OWQ0NWZlYjRiNmJiOWZiYWY4OTZkNWMzOGQzKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2U1OGM0MTE1NGYzMTQ5OGY4NzBhNGRiY2Y1YmJkY2Y5LmJpbmRQb3B1cChwb3B1cF9kMTgzMDVjM2I5NzE0ZDY1OGE0N2MxMjQ4MGNiMThhMyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9mYjE3YzE3NWRiYjk0NWFmYmZmMDFhNjdkNDEwNDRkNiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjUzODExNDE3NDc0NTA3LC03NC4xNzg1NDg2NjE2NTg3OF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjMDBiNWViIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzAwYjVlYiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9mZWYyODNiYzVhYTM0ZTBhOTE1MTVjM2U0MDZkODE0NSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF80ZjlkNzE2MzIzOWU0ZDk4OWE4NWYxNWEzZTI2ZDRhNCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9mN2ZmYzgzNWQxNjc0ZjNkODNjMzZmNjhiMTFiOGJhZiA9ICQoJzxkaXYgaWQ9Imh0bWxfZjdmZmM4MzVkMTY3NGYzZDgzYzM2ZjY4YjExYjhiYWYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkFubmFkYWxlIENsdXN0ZXIgMjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNGY5ZDcxNjMyMzllNGQ5ODlhODVmMTVhM2UyNmQ0YTQuc2V0Q29udGVudChodG1sX2Y3ZmZjODM1ZDE2NzRmM2Q4M2MzNmY2OGIxMWI4YmFmKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2ZiMTdjMTc1ZGJiOTQ1YWZiZmYwMWE2N2Q0MTA0NGQ2LmJpbmRQb3B1cChwb3B1cF80ZjlkNzE2MzIzOWU0ZDk4OWE4NWYxNWEzZTI2ZDRhNCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9mN2E5NTgyMDFhZTg0MzdjYmYyNDZlZjAwMDkxOTVmZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjU0MTk2NzYyMjg4ODc1NSwtNzQuMjA1MjQ1ODI0ODAzMjZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzAwYjVlYiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMwMGI1ZWIiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfZmVmMjgzYmM1YWEzNGUwYTkxNTE1YzNlNDA2ZDgxNDUpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYTM1ZWU1ZmQxN2Y1NGRlYThmMjdkNzdiMDZiNzgxYzEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfY2U2M2UwNmZkNDllNGRiYmI1ZjY3YTlhODg1MDQxMmUgPSAkKCc8ZGl2IGlkPSJodG1sX2NlNjNlMDZmZDQ5ZTRkYmJiNWY2N2E5YTg4NTA0MTJlIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Xb29kcm93IENsdXN0ZXIgMjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYTM1ZWU1ZmQxN2Y1NGRlYThmMjdkNzdiMDZiNzgxYzEuc2V0Q29udGVudChodG1sX2NlNjNlMDZmZDQ5ZTRkYmJiNWY2N2E5YTg4NTA0MTJlKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2Y3YTk1ODIwMWFlODQzN2NiZjI0NmVmMDAwOTE5NWZlLmJpbmRQb3B1cChwb3B1cF9hMzVlZTVmZDE3ZjU0ZGVhOGYyN2Q3N2IwNmI3ODFjMSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9iOWYwN2ZiNDlkMTU0M2U1OGYxMmQzZDdlZmZhYjA2YiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjUwNTMzMzc2MTE1NjQyLC03NC4yNDY1NjkzNDIzNTI4M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjMDBiNWViIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzAwYjVlYiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9mZWYyODNiYzVhYTM0ZTBhOTE1MTVjM2U0MDZkODE0NSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF83YTE4YmIxOGNlNzA0NTQwYTk5OGQyNTRhZjI0YzBkOCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF84MDFkYjNlNDJiYWI0ODEyYjMyNDIyZjY3ZmVlYjRkZSA9ICQoJzxkaXYgaWQ9Imh0bWxfODAxZGIzZTQyYmFiNDgxMmIzMjQyMmY2N2ZlZWI0ZGUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRvdHRlbnZpbGxlIENsdXN0ZXIgMjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfN2ExOGJiMThjZTcwNDU0MGE5OThkMjU0YWYyNGMwZDguc2V0Q29udGVudChodG1sXzgwMWRiM2U0MmJhYjQ4MTJiMzI0MjJmNjdmZWViNGRlKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2I5ZjA3ZmI0OWQxNTQzZTU4ZjEyZDNkN2VmZmFiMDZiLmJpbmRQb3B1cChwb3B1cF83YTE4YmIxOGNlNzA0NTQwYTk5OGQyNTRhZjI0YzBkOCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9kYWNmYTJjYTFmYjk0Y2FmODQyZDU3MzBhZmZkNGFjYyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYzNzMxNjA2NzExMDMyNiwtNzQuMDgwNTUzNTE3OTAxMTVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzAwYjVlYiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMwMGI1ZWIiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfZmVmMjgzYmM1YWEzNGUwYTkxNTE1YzNlNDA2ZDgxNDUpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZDUxYTk3MWRjZThmNGZiOTkwN2Q3OTUyZGMxYzEyNzkgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNzQxMjdmMWU2MTQzNDNjZmI5NTcwYjkzODU3NGFlNjkgPSAkKCc8ZGl2IGlkPSJodG1sXzc0MTI3ZjFlNjE0MzQzY2ZiOTU3MGI5Mzg1NzRhZTY5IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Ub21wa2luc3ZpbGxlIENsdXN0ZXIgMjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZDUxYTk3MWRjZThmNGZiOTkwN2Q3OTUyZGMxYzEyNzkuc2V0Q29udGVudChodG1sXzc0MTI3ZjFlNjE0MzQzY2ZiOTU3MGI5Mzg1NzRhZTY5KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2RhY2ZhMmNhMWZiOTRjYWY4NDJkNTczMGFmZmQ0YWNjLmJpbmRQb3B1cChwb3B1cF9kNTFhOTcxZGNlOGY0ZmI5OTA3ZDc5NTJkYzFjMTI3OSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9mYzJjZGIxYTA4MDU0ZWUyODUzNjMyNDBkNmUzMWUzOCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYxOTE5MzEwNzkyNjc2LC03NC4wOTYyOTAyOTIzNTQ1OF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjMDBiNWViIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzAwYjVlYiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9mZWYyODNiYzVhYTM0ZTBhOTE1MTVjM2U0MDZkODE0NSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9mOGFmMTg1NWE4MDg0NWU4YjkzNWZkZTgyOTI4M2UwZCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF83NzVlNDRjYjIwM2U0Mzg5OWUzNDExMGRmMjE2YTQ1YSA9ICQoJzxkaXYgaWQ9Imh0bWxfNzc1ZTQ0Y2IyMDNlNDM4OTllMzQxMTBkZjIxNmE0NWEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlNpbHZlciBMYWtlIENsdXN0ZXIgMjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZjhhZjE4NTVhODA4NDVlOGI5MzVmZGU4MjkyODNlMGQuc2V0Q29udGVudChodG1sXzc3NWU0NGNiMjAzZTQzODk5ZTM0MTEwZGYyMTZhNDVhKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2ZjMmNkYjFhMDgwNTRlZTI4NTM2MzI0MGQ2ZTMxZTM4LmJpbmRQb3B1cChwb3B1cF9mOGFmMTg1NWE4MDg0NWU4YjkzNWZkZTgyOTI4M2UwZCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl83ZjZjZDY0NWMwNmM0Mjk2YTgzMGY5NzViNzRiNTY2ZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYxMjc2MDE1NzU2NDg5LC03NC4wOTcxMjU1MjE3ODUzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiMwMGI1ZWIiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMDBiNWViIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2ZlZjI4M2JjNWFhMzRlMGE5MTUxNWMzZTQwNmQ4MTQ1KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2JlYWQ4YzVkMGJkZjQ0Y2NhMTcxODk3N2Y3NjFhYzA2ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzkwY2EwN2E4Mzg4MzQ1ZGFhNGYxZTJiOWE4MmU2MGEwID0gJCgnPGRpdiBpZD0iaHRtbF85MGNhMDdhODM4ODM0NWRhYTRmMWUyYjlhODJlNjBhMCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+U3VubnlzaWRlIENsdXN0ZXIgMjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYmVhZDhjNWQwYmRmNDRjY2ExNzE4OTc3Zjc2MWFjMDYuc2V0Q29udGVudChodG1sXzkwY2EwN2E4Mzg4MzQ1ZGFhNGYxZTJiOWE4MmU2MGEwKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzdmNmNkNjQ1YzA2YzQyOTZhODMwZjk3NWI3NGI1NjZlLmJpbmRQb3B1cChwb3B1cF9iZWFkOGM1ZDBiZGY0NGNjYTE3MTg5NzdmNzYxYWMwNik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl80MjFiYWY1OGQzZjM0MDVkODc3ZjI4OGRjNjYzYTU0ZCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYwOTE5MDQ0NDM0NTU4LC03NC4wODAxNTczNDkzNjI5Nl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjMDBiNWViIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzAwYjVlYiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9mZWYyODNiYzVhYTM0ZTBhOTE1MTVjM2U0MDZkODE0NSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9kOGY5NzcyODg2M2I0ZDFjOGExNzNkMWQyOTFiZGJkMSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF81MDcyOGIzZDdlMjY0NDBmYjRmYmI0N2U1ZmUxY2VmMSA9ICQoJzxkaXYgaWQ9Imh0bWxfNTA3MjhiM2Q3ZTI2NDQwZmI0ZmJiNDdlNWZlMWNlZjEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlBhcmsgSGlsbCBDbHVzdGVyIDI8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2Q4Zjk3NzI4ODYzYjRkMWM4YTE3M2QxZDI5MWJkYmQxLnNldENvbnRlbnQoaHRtbF81MDcyOGIzZDdlMjY0NDBmYjRmYmI0N2U1ZmUxY2VmMSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl80MjFiYWY1OGQzZjM0MDVkODc3ZjI4OGRjNjYzYTU0ZC5iaW5kUG9wdXAocG9wdXBfZDhmOTc3Mjg4NjNiNGQxYzhhMTczZDFkMjkxYmRiZDEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYjMyZTkxNDQwZmU4NGJmNjkzNjZmYmQyOTFlYWE0MmEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42MjEwOTA0NzI3NTQwOSwtNzQuMTMzMDQxNDM5NTE3MDRdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzAwYjVlYiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMwMGI1ZWIiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfZmVmMjgzYmM1YWEzNGUwYTkxNTE1YzNlNDA2ZDgxNDUpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZTNkMzQyZTEzMzc2NDZmZDgzZjg3ZDUwZTA2YTI4MjYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOGU1ZGNmYzA4YWZkNDA0NmIyMzYzMGQzZDA4NDgxNDQgPSAkKCc8ZGl2IGlkPSJodG1sXzhlNWRjZmMwOGFmZDQwNDZiMjM2MzBkM2QwODQ4MTQ0IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5XZXN0ZXJsZWlnaCBDbHVzdGVyIDI8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2UzZDM0MmUxMzM3NjQ2ZmQ4M2Y4N2Q1MGUwNmEyODI2LnNldENvbnRlbnQoaHRtbF84ZTVkY2ZjMDhhZmQ0MDQ2YjIzNjMwZDNkMDg0ODE0NCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9iMzJlOTE0NDBmZTg0YmY2OTM2NmZiZDI5MWVhYTQyYS5iaW5kUG9wdXAocG9wdXBfZTNkMzQyZTEzMzc2NDZmZDgzZjg3ZDUwZTA2YTI4MjYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMmJmOWRhMTM1YWIxNGU2YmI5ZWQ2MTJiNjI0MmZiMTkgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42MjAxNzE1MTIyMzE4ODQsLTc0LjE1MzE1MjQ2Mzg3NzYyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiM4MDAwZmYiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjODAwMGZmIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2ZlZjI4M2JjNWFhMzRlMGE5MTUxNWMzZTQwNmQ4MTQ1KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzI1MWQ3ZDFmNjIxYzRkMDk4MDU2ZmUyNTZkODQxY2Q4ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzUzMTYyYTFjODMxYTQ0NGU5YzkyNDM3Mzg2ZjkyNWNjID0gJCgnPGRpdiBpZD0iaHRtbF81MzE2MmExYzgzMWE0NDRlOWM5MjQzNzM4NmY5MjVjYyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+R3Jhbml0ZXZpbGxlIENsdXN0ZXIgMTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMjUxZDdkMWY2MjFjNGQwOTgwNTZmZTI1NmQ4NDFjZDguc2V0Q29udGVudChodG1sXzUzMTYyYTFjODMxYTQ0NGU5YzkyNDM3Mzg2ZjkyNWNjKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzJiZjlkYTEzNWFiMTRlNmJiOWVkNjEyYjYyNDJmYjE5LmJpbmRQb3B1cChwb3B1cF8yNTFkN2QxZjYyMWM0ZDA5ODA1NmZlMjU2ZDg0MWNkOCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8zMjJmY2FhMTFmNDk0YTk2ODFlYTg2NzdlODFiMzE2NSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYzNTMyNTA5OTExNDkyLC03NC4xNjUxMDQyMDI0MTEyNF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9mZWYyODNiYzVhYTM0ZTBhOTE1MTVjM2U0MDZkODE0NSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9hNjhmMGJkMDgyMTE0N2M2YTBiOTcxOTE1NzQzMzZmYiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF82YzMwYTlkMjc0NjI0ZmEwOTMwYTIwYzQ2ZjJlZWZmOCA9ICQoJzxkaXYgaWQ9Imh0bWxfNmMzMGE5ZDI3NDYyNGZhMDkzMGEyMGM0NmYyZWVmZjgiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkFybGluZ3RvbiBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2E2OGYwYmQwODIxMTQ3YzZhMGI5NzE5MTU3NDMzNmZiLnNldENvbnRlbnQoaHRtbF82YzMwYTlkMjc0NjI0ZmEwOTMwYTIwYzQ2ZjJlZWZmOCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8zMjJmY2FhMTFmNDk0YTk2ODFlYTg2NzdlODFiMzE2NS5iaW5kUG9wdXAocG9wdXBfYTY4ZjBiZDA4MjExNDdjNmEwYjk3MTkxNTc0MzM2ZmIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMzFiNjhiNjJkMWI4NDY2ZDg5ZWVjYjZkYWM1MDE5ZGYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41OTYzMTI1NzEyNzY3MzQsLTc0LjA2NzEyMzYzMjI1NTc0XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiMwMGI1ZWIiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMDBiNWViIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2ZlZjI4M2JjNWFhMzRlMGE5MTUxNWMzZTQwNmQ4MTQ1KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2NhNzA2ZWJlZDUyZjQ3Y2RiNDg5MjU2NTc2NTljZGE1ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzBjMGQ1MWE4NGUwNDQ0NDhhMDBjOWE1ZDVmZjIwMTFmID0gJCgnPGRpdiBpZD0iaHRtbF8wYzBkNTFhODRlMDQ0NDQ4YTAwYzlhNWQ1ZmYyMDExZiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QXJyb2NoYXIgQ2x1c3RlciAyPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9jYTcwNmViZWQ1MmY0N2NkYjQ4OTI1NjU3NjU5Y2RhNS5zZXRDb250ZW50KGh0bWxfMGMwZDUxYTg0ZTA0NDQ0OGEwMGM5YTVkNWZmMjAxMWYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMzFiNjhiNjJkMWI4NDY2ZDg5ZWVjYjZkYWM1MDE5ZGYuYmluZFBvcHVwKHBvcHVwX2NhNzA2ZWJlZDUyZjQ3Y2RiNDg5MjU2NTc2NTljZGE1KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzQ5NWEwZjMwNjU3MjQxNTFhZGVhOTkxZWIyNmFmM2FhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTk4MjY4MzU5NTk5OTEsLTc0LjA3NjY3NDM2Mjc5MDVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzAwYjVlYiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMwMGI1ZWIiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfZmVmMjgzYmM1YWEzNGUwYTkxNTE1YzNlNDA2ZDgxNDUpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMzRkZWE0YTMyNmU5NDZiYzk4Yzg4MGYwOGRiYzlhYzQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNzdkMzZiOTMzM2VkNGVhZGE4NTkxYjVjY2I5NzBkMjkgPSAkKCc8ZGl2IGlkPSJodG1sXzc3ZDM2YjkzMzNlZDRlYWRhODU5MWI1Y2NiOTcwZDI5IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5HcmFzbWVyZSBDbHVzdGVyIDI8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzM0ZGVhNGEzMjZlOTQ2YmM5OGM4ODBmMDhkYmM5YWM0LnNldENvbnRlbnQoaHRtbF83N2QzNmI5MzMzZWQ0ZWFkYTg1OTFiNWNjYjk3MGQyOSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl80OTVhMGYzMDY1NzI0MTUxYWRlYTk5MWViMjZhZjNhYS5iaW5kUG9wdXAocG9wdXBfMzRkZWE0YTMyNmU5NDZiYzk4Yzg4MGYwOGRiYzlhYzQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNzA2NzEwOWI4Nzc1NDU2Nzk5ZWUzMGVmOWFiMmViYmQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41OTYzMjg5MTM3OTUxMywtNzQuMDg3NTExMTgwMDU1NzhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzAwYjVlYiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMwMGI1ZWIiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfZmVmMjgzYmM1YWEzNGUwYTkxNTE1YzNlNDA2ZDgxNDUpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNTk4NDdjZmJkNjJiNDM3NjhkMWU4ZTIyNGE0NTJjYTIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfODUwZDFhZjk5YTZiNGQzZmE1ZDAwYTQ4MzE5Mjc1NWMgPSAkKCc8ZGl2IGlkPSJodG1sXzg1MGQxYWY5OWE2YjRkM2ZhNWQwMGE0ODMxOTI3NTVjIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5PbGQgVG93biBDbHVzdGVyIDI8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzU5ODQ3Y2ZiZDYyYjQzNzY4ZDFlOGUyMjRhNDUyY2EyLnNldENvbnRlbnQoaHRtbF84NTBkMWFmOTlhNmI0ZDNmYTVkMDBhNDgzMTkyNzU1Yyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl83MDY3MTA5Yjg3NzU0NTY3OTllZTMwZWY5YWIyZWJiZC5iaW5kUG9wdXAocG9wdXBfNTk4NDdjZmJkNjJiNDM3NjhkMWU4ZTIyNGE0NTJjYTIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZjZhM2YxNGYzY2E3NDY2MzljZDA5NGQ2ZTc5MmZjZmYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41ODg2NzI5NDgxOTkyNzUsLTc0LjA5NjM5OTA1MzEyNTIxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiMwMGI1ZWIiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMDBiNWViIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2ZlZjI4M2JjNWFhMzRlMGE5MTUxNWMzZTQwNmQ4MTQ1KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzRkY2VmYzZiZTIxMjQzMzliNzNmNjU4NTA1ZTRhMWZjID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzc4M2Y3Njg1MmNhYzQ0M2JhZDdkZmM4YjM4ZjUyZTQzID0gJCgnPGRpdiBpZD0iaHRtbF83ODNmNzY4NTJjYWM0NDNiYWQ3ZGZjOGIzOGY1MmU0MyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RG9uZ2FuIEhpbGxzIENsdXN0ZXIgMjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNGRjZWZjNmJlMjEyNDMzOWI3M2Y2NTg1MDVlNGExZmMuc2V0Q29udGVudChodG1sXzc4M2Y3Njg1MmNhYzQ0M2JhZDdkZmM4YjM4ZjUyZTQzKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2Y2YTNmMTRmM2NhNzQ2NjM5Y2QwOTRkNmU3OTJmY2ZmLmJpbmRQb3B1cChwb3B1cF80ZGNlZmM2YmUyMTI0MzM5YjczZjY1ODUwNWU0YTFmYyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8wOTY5ZmZhYzJlNzY0NThiYjQ1ZTNiNTRkOGU4OGU2OSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjU3MzUyNjkwNTc0MjgzLC03NC4wOTM0ODI2NjMwMzU5MV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjMDBiNWViIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzAwYjVlYiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9mZWYyODNiYzVhYTM0ZTBhOTE1MTVjM2U0MDZkODE0NSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9mYzE4ZmI3NDhjMjE0YTMzOGRhN2MwMTlkOWJkZDM2NCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9jOGIzN2RmOTEwOTI0NTlmOTlhNGZlNDgwZmJlYmU4YSA9ICQoJzxkaXYgaWQ9Imh0bWxfYzhiMzdkZjkxMDkyNDU5Zjk5YTRmZTQ4MGZiZWJlOGEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk1pZGxhbmQgQmVhY2ggQ2x1c3RlciAyPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9mYzE4ZmI3NDhjMjE0YTMzOGRhN2MwMTlkOWJkZDM2NC5zZXRDb250ZW50KGh0bWxfYzhiMzdkZjkxMDkyNDU5Zjk5YTRmZTQ4MGZiZWJlOGEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMDk2OWZmYWMyZTc2NDU4YmI0NWUzYjU0ZDhlODhlNjkuYmluZFBvcHVwKHBvcHVwX2ZjMThmYjc0OGMyMTRhMzM4ZGE3YzAxOWQ5YmRkMzY0KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2RiODU4ZWMzZTkwNzQyMmVhNTBjMGUyZTQ2NWYyZmNiID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTc2MjE1NTg3MTE3ODgsLTc0LjEwNTg1NTk4NTQ1NDM0XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiMwMGI1ZWIiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMDBiNWViIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2ZlZjI4M2JjNWFhMzRlMGE5MTUxNWMzZTQwNmQ4MTQ1KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzY4OTQ3MGU1NjhhZjQ3MTE5ZWZkNmM5YTU5ZDk0ZTZlID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2UzOWQ3NGJjODZlYzQxYjJhMGRiZjA3MTAxNWRhYzJmID0gJCgnPGRpdiBpZD0iaHRtbF9lMzlkNzRiYzg2ZWM0MWIyYTBkYmYwNzEwMTVkYWMyZiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+R3JhbnQgQ2l0eSBDbHVzdGVyIDI8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzY4OTQ3MGU1NjhhZjQ3MTE5ZWZkNmM5YTU5ZDk0ZTZlLnNldENvbnRlbnQoaHRtbF9lMzlkNzRiYzg2ZWM0MWIyYTBkYmYwNzEwMTVkYWMyZik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9kYjg1OGVjM2U5MDc0MjJlYTUwYzBlMmU0NjVmMmZjYi5iaW5kUG9wdXAocG9wdXBfNjg5NDcwZTU2OGFmNDcxMTllZmQ2YzlhNTlkOTRlNmUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNjI2ZWE2MjAxNWE0NGRiOWJmN2JjYWM0MTdmNTMwNGIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41NjQyNTU0OTMwNzMzNSwtNzQuMTA0MzI3MDc0NjkxMjRdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzAwYjVlYiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMwMGI1ZWIiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfZmVmMjgzYmM1YWEzNGUwYTkxNTE1YzNlNDA2ZDgxNDUpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNWM4NWJkMmNhOTUxNDNmOWIzZGIxMzIzZDljMThmNzUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfM2UxNzZjODk1MmY1NDJhOGI4OTdkOGExODYxODUzODIgPSAkKCc8ZGl2IGlkPSJodG1sXzNlMTc2Yzg5NTJmNTQyYThiODk3ZDhhMTg2MTg1MzgyIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5OZXcgRG9ycCBCZWFjaCBDbHVzdGVyIDI8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzVjODViZDJjYTk1MTQzZjliM2RiMTMyM2Q5YzE4Zjc1LnNldENvbnRlbnQoaHRtbF8zZTE3NmM4OTUyZjU0MmE4Yjg5N2Q4YTE4NjE4NTM4Mik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl82MjZlYTYyMDE1YTQ0ZGI5YmY3YmNhYzQxN2Y1MzA0Yi5iaW5kUG9wdXAocG9wdXBfNWM4NWJkMmNhOTUxNDNmOWIzZGIxMzIzZDljMThmNzUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMTA4NGY2MjBiMjQ1NDFkZWFjZjI0MzMyN2MzZGRhMWEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41NTM5ODgwMDg1ODQ2MiwtNzQuMTM5MTY2MjIxNzU3NjhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzAwYjVlYiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMwMGI1ZWIiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfZmVmMjgzYmM1YWEzNGUwYTkxNTE1YzNlNDA2ZDgxNDUpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYWFjMDBkNmY3YjdhNDE5NDk5NmQ4ZDE1OWZiMzU5NmYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMTNjMjg3NWVmYzhkNDQyM2EwMDIyNjM5NTE5MDg3YjAgPSAkKCc8ZGl2IGlkPSJodG1sXzEzYzI4NzVlZmM4ZDQ0MjNhMDAyMjYzOTUxOTA4N2IwIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CYXkgVGVycmFjZSBDbHVzdGVyIDI8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2FhYzAwZDZmN2I3YTQxOTQ5OTZkOGQxNTlmYjM1OTZmLnNldENvbnRlbnQoaHRtbF8xM2MyODc1ZWZjOGQ0NDIzYTAwMjI2Mzk1MTkwODdiMCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8xMDg0ZjYyMGIyNDU0MWRlYWNmMjQzMzI3YzNkZGExYS5iaW5kUG9wdXAocG9wdXBfYWFjMDBkNmY3YjdhNDE5NDk5NmQ4ZDE1OWZiMzU5NmYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNDgxNTZkYTQ2OWQ3NDAwZTg5MDAzMzQ3ZDdhMThjNDAgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41MzE5MTE5MjA0ODk2MDUsLTc0LjE5MTc0MTA1NzQ3ODE0XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiMwMGI1ZWIiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMDBiNWViIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2ZlZjI4M2JjNWFhMzRlMGE5MTUxNWMzZTQwNmQ4MTQ1KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzBmMjJmZWJlZmUxMDRjM2M5NzNmNDBhOGI4MTBhODk4ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2FlNDI0MmUwNTFlMzQxMzhhMDIwOTNjMzFkNDZmOGU2ID0gJCgnPGRpdiBpZD0iaHRtbF9hZTQyNDJlMDUxZTM0MTM4YTAyMDkzYzMxZDQ2ZjhlNiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+SHVndWVub3QgQ2x1c3RlciAyPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8wZjIyZmViZWZlMTA0YzNjOTczZjQwYThiODEwYTg5OC5zZXRDb250ZW50KGh0bWxfYWU0MjQyZTA1MWUzNDEzOGEwMjA5M2MzMWQ0NmY4ZTYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNDgxNTZkYTQ2OWQ3NDAwZTg5MDAzMzQ3ZDdhMThjNDAuYmluZFBvcHVwKHBvcHVwXzBmMjJmZWJlZmUxMDRjM2M5NzNmNDBhOGI4MTBhODk4KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2Y0MWU0YjllNzU1ZDRlNzFhYjUxMDQ0NWZjNWM5MzcyID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTI0Njk5Mzc2MTE4MTM2LC03NC4yMTk4MzEwNjYxNjc3N10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjMDBiNWViIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzAwYjVlYiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9mZWYyODNiYzVhYTM0ZTBhOTE1MTVjM2U0MDZkODE0NSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF85ZWEwYzkxYjc2OGY0OGI3OTcxZmYxZWE2YTQ2MTQyYyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9iZTM1YmQ4NGU3ZDE0MzllYTMyMjU0MjE2NDY4YjExNiA9ICQoJzxkaXYgaWQ9Imh0bWxfYmUzNWJkODRlN2QxNDM5ZWEzMjI1NDIxNjQ2OGIxMTYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlBsZWFzYW50IFBsYWlucyBDbHVzdGVyIDI8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzllYTBjOTFiNzY4ZjQ4Yjc5NzFmZjFlYTZhNDYxNDJjLnNldENvbnRlbnQoaHRtbF9iZTM1YmQ4NGU3ZDE0MzllYTMyMjU0MjE2NDY4YjExNik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9mNDFlNGI5ZTc1NWQ0ZTcxYWI1MTA0NDVmYzVjOTM3Mi5iaW5kUG9wdXAocG9wdXBfOWVhMGM5MWI3NjhmNDhiNzk3MWZmMWVhNmE0NjE0MmMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYjMxNzU1ZGFmZWI4NGZiN2E1NDI0N2YwZGUwYmFjYTcgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41MDYwODE2NTM0NjMwNSwtNzQuMjI5NTAzNTAyNjAwMjddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzAwYjVlYiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMwMGI1ZWIiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfZmVmMjgzYmM1YWEzNGUwYTkxNTE1YzNlNDA2ZDgxNDUpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMDhlN2Q5YjA2YjIwNDIxNDlkMWM1MjU1Y2U4ZjcxMGMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOWVjM2FjMTU2YmIxNDdlNGEyYjk0YTRkN2I4ZDNlYmIgPSAkKCc8ZGl2IGlkPSJodG1sXzllYzNhYzE1NmJiMTQ3ZTRhMmI5NGE0ZDdiOGQzZWJiIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CdXRsZXIgTWFub3IgQ2x1c3RlciAyPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8wOGU3ZDliMDZiMjA0MjE0OWQxYzUyNTVjZThmNzEwYy5zZXRDb250ZW50KGh0bWxfOWVjM2FjMTU2YmIxNDdlNGEyYjk0YTRkN2I4ZDNlYmIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYjMxNzU1ZGFmZWI4NGZiN2E1NDI0N2YwZGUwYmFjYTcuYmluZFBvcHVwKHBvcHVwXzA4ZTdkOWIwNmIyMDQyMTQ5ZDFjNTI1NWNlOGY3MTBjKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2VmNDk3YjUxNjE2YTQ0ZjViMzczYTNiZDdhZWI4ZDdhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTMwNTMxNDgyODMzMTQsLTc0LjIzMjE1Nzc1ODk2NTI2XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiMwMGI1ZWIiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMDBiNWViIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2ZlZjI4M2JjNWFhMzRlMGE5MTUxNWMzZTQwNmQ4MTQ1KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2RiOWZiN2ZiYjQ0ZDRkZDdiMTFlNDk0NGU5MTJlMjI2ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzY2NTQyMzFiY2E4ODRiMWY5YjE1ZmY4YzQ1ZDZiZWQ3ID0gJCgnPGRpdiBpZD0iaHRtbF82NjU0MjMxYmNhODg0YjFmOWIxNWZmOGM0NWQ2YmVkNyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q2hhcmxlc3RvbiBDbHVzdGVyIDI8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2RiOWZiN2ZiYjQ0ZDRkZDdiMTFlNDk0NGU5MTJlMjI2LnNldENvbnRlbnQoaHRtbF82NjU0MjMxYmNhODg0YjFmOWIxNWZmOGM0NWQ2YmVkNyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9lZjQ5N2I1MTYxNmE0NGY1YjM3M2EzYmQ3YWViOGQ3YS5iaW5kUG9wdXAocG9wdXBfZGI5ZmI3ZmJiNDRkNGRkN2IxMWU0OTQ0ZTkxMmUyMjYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNDhjYjlhZDJjZjI4NGI4YjllOGEzMzVkMzAwZjMwYTAgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41NDk0MDQwMDY1MDA3MiwtNzQuMjE1NzI4NTExMTM5NTJdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzAwYjVlYiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMwMGI1ZWIiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfZmVmMjgzYmM1YWEzNGUwYTkxNTE1YzNlNDA2ZDgxNDUpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfODI0ODgwMmY0N2U4NDIzMWFhYjg1MTg2YjhmYzk1NmMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfM2JmYmJlMjAzMzQyNGM1MmI2Zjg2MGIxMzJkYTkxY2IgPSAkKCc8ZGl2IGlkPSJodG1sXzNiZmJiZTIwMzM0MjRjNTJiNmY4NjBiMTMyZGE5MWNiIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Sb3NzdmlsbGUgQ2x1c3RlciAyPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF84MjQ4ODAyZjQ3ZTg0MjMxYWFiODUxODZiOGZjOTU2Yy5zZXRDb250ZW50KGh0bWxfM2JmYmJlMjAzMzQyNGM1MmI2Zjg2MGIxMzJkYTkxY2IpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNDhjYjlhZDJjZjI4NGI4YjllOGEzMzVkMzAwZjMwYTAuYmluZFBvcHVwKHBvcHVwXzgyNDg4MDJmNDdlODQyMzFhYWI4NTE4NmI4ZmM5NTZjKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzdmNGVhMzE5NWFkMDQ3YjlhMzFmNDM1YjllYTlkNjA2ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTQ5Mjg1ODIyNzgzMjEsLTc0LjE4NTg4Njc0NTgzODkzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2ZlZjI4M2JjNWFhMzRlMGE5MTUxNWMzZTQwNmQ4MTQ1KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2Q5YTkzMGI0MDJiMDQ3MThhZjg4Mjc2NjI2ZGE4N2M3ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzc2NTczOTQzZGMwZTRiMmU4YTU5MTZhYjQ5MjYxYmExID0gJCgnPGRpdiBpZD0iaHRtbF83NjU3Mzk0M2RjMGU0YjJlOGE1OTE2YWI0OTI2MWJhMSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QXJkZW4gSGVpZ2h0cyBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2Q5YTkzMGI0MDJiMDQ3MThhZjg4Mjc2NjI2ZGE4N2M3LnNldENvbnRlbnQoaHRtbF83NjU3Mzk0M2RjMGU0YjJlOGE1OTE2YWI0OTI2MWJhMSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl83ZjRlYTMxOTVhZDA0N2I5YTMxZjQzNWI5ZWE5ZDYwNi5iaW5kUG9wdXAocG9wdXBfZDlhOTMwYjQwMmIwNDcxOGFmODgyNzY2MjZkYTg3YzcpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZDM3ZTg1ZjlmZjJiNDQzYjk5ODFkYmU5ZWNmNzc0NzYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41NTUyOTUyMzYxNzMxOTQsLTc0LjE3MDc5NDE0Nzg2MDkyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiMwMGI1ZWIiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMDBiNWViIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2ZlZjI4M2JjNWFhMzRlMGE5MTUxNWMzZTQwNmQ4MTQ1KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzVmYzZjZDYyNjQ4MzQwNTBiYzQxY2MwNDY1YTk1NGZhID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzhjMWViMTNmNTA1ZDQ0ZWVhZjU1NzBjYmU2OWZmZmNjID0gJCgnPGRpdiBpZD0iaHRtbF84YzFlYjEzZjUwNWQ0NGVlYWY1NTcwY2JlNjlmZmZjYyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+R3JlZW5yaWRnZSBDbHVzdGVyIDI8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzVmYzZjZDYyNjQ4MzQwNTBiYzQxY2MwNDY1YTk1NGZhLnNldENvbnRlbnQoaHRtbF84YzFlYjEzZjUwNWQ0NGVlYWY1NTcwY2JlNjlmZmZjYyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9kMzdlODVmOWZmMmI0NDNiOTk4MWRiZTllY2Y3NzQ3Ni5iaW5kUG9wdXAocG9wdXBfNWZjNmNkNjI2NDgzNDA1MGJjNDFjYzA0NjVhOTU0ZmEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZjQyZDBkMTRlOWZjNGQzZGJkZGFhMTM2MzI1ZDNlNjEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41ODkxMzg5NDg3NTI4MSwtNzQuMTU5MDIyMDgxNTY2MDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzAwYjVlYiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMwMGI1ZWIiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfZmVmMjgzYmM1YWEzNGUwYTkxNTE1YzNlNDA2ZDgxNDUpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMTFmYTQzYzFmZTBiNDFlYjk1MmE3ZmFiYWI0ZDBmZTEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMDk2YjU4ZTBlZDgzNDllYWExZTQwM2UzMzBjNjk2N2YgPSAkKCc8ZGl2IGlkPSJodG1sXzA5NmI1OGUwZWQ4MzQ5ZWFhMWU0MDNlMzMwYzY5NjdmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5IZWFydGxhbmQgVmlsbGFnZSBDbHVzdGVyIDI8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzExZmE0M2MxZmUwYjQxZWI5NTJhN2ZhYmFiNGQwZmUxLnNldENvbnRlbnQoaHRtbF8wOTZiNThlMGVkODM0OWVhYTFlNDAzZTMzMGM2OTY3Zik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9mNDJkMGQxNGU5ZmM0ZDNkYmRkYWExMzYzMjVkM2U2MS5iaW5kUG9wdXAocG9wdXBfMTFmYTQzYzFmZTBiNDFlYjk1MmE3ZmFiYWI0ZDBmZTEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYTJlNzg2N2MxN2Q5NDliZmJiZWU3ZmYyOTE3NGM0ODMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41OTQ3MjYwMjc0NjI5NSwtNzQuMTg5NTYwNDU1MTk2OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjMDBiNWViIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzAwYjVlYiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9mZWYyODNiYzVhYTM0ZTBhOTE1MTVjM2U0MDZkODE0NSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9hN2E1MDdmZjZhNTQ0NGVhYjFmOGM4NDMyYzBiZjQyNyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8wMGM5MzljMTIzNTA0ZTk0Yjg1ZDBlOWUxNTAyZWM2MSA9ICQoJzxkaXYgaWQ9Imh0bWxfMDBjOTM5YzEyMzUwNGU5NGI4NWQwZTllMTUwMmVjNjEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNoZWxzZWEgQ2x1c3RlciAyPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9hN2E1MDdmZjZhNTQ0NGVhYjFmOGM4NDMyYzBiZjQyNy5zZXRDb250ZW50KGh0bWxfMDBjOTM5YzEyMzUwNGU5NGI4NWQwZTllMTUwMmVjNjEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYTJlNzg2N2MxN2Q5NDliZmJiZWU3ZmYyOTE3NGM0ODMuYmluZFBvcHVwKHBvcHVwX2E3YTUwN2ZmNmE1NDQ0ZWFiMWY4Yzg0MzJjMGJmNDI3KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2VhMjEzMjIwNGMxMjRkZGViNGJhMTRjNmUyM2I5Mzc4ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjA1Nzc4Njg0NTIzNTgsLTc0LjE4NzI1NjM4MzgxNTY3XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiMwMGI1ZWIiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMDBiNWViIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2ZlZjI4M2JjNWFhMzRlMGE5MTUxNWMzZTQwNmQ4MTQ1KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzdiY2UwNjBiNmEyNzQ3MTI5NzRlYTdjMzBlOTNlZGI4ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzQ2MTdhMTI1OTRhNjQxZmI4NDhmOTU0MDBlMmZlYmY2ID0gJCgnPGRpdiBpZD0iaHRtbF80NjE3YTEyNTk0YTY0MWZiODQ4Zjk1NDAwZTJmZWJmNiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Qmxvb21maWVsZCBDbHVzdGVyIDI8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzdiY2UwNjBiNmEyNzQ3MTI5NzRlYTdjMzBlOTNlZGI4LnNldENvbnRlbnQoaHRtbF80NjE3YTEyNTk0YTY0MWZiODQ4Zjk1NDAwZTJmZWJmNik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9lYTIxMzIyMDRjMTI0ZGRlYjRiYTE0YzZlMjNiOTM3OC5iaW5kUG9wdXAocG9wdXBfN2JjZTA2MGI2YTI3NDcxMjk3NGVhN2MzMGU5M2VkYjgpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOWIyNDI4ZGZhZTkyNDRkNmJkZTc4MWIwMzRlYjNjZDkgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42MDk1OTE4MDA0MjAzLC03NC4xNTk0MDk0ODY1NzEyMl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjMDBiNWViIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzAwYjVlYiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9mZWYyODNiYzVhYTM0ZTBhOTE1MTVjM2U0MDZkODE0NSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9jMTg5NzhjYTFmMzg0YmM5ODY2YjBhYTdiYmRmMzRiOCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9hMGE2NmE2ZmY4NGY0Y2M5OWMyNjVmNmVkYTNjZDVmNyA9ICQoJzxkaXYgaWQ9Imh0bWxfYTBhNjZhNmZmODRmNGNjOTljMjY1ZjZlZGEzY2Q1ZjciIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkJ1bGxzIEhlYWQgQ2x1c3RlciAyPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9jMTg5NzhjYTFmMzg0YmM5ODY2YjBhYTdiYmRmMzRiOC5zZXRDb250ZW50KGh0bWxfYTBhNjZhNmZmODRmNGNjOTljMjY1ZjZlZGEzY2Q1ZjcpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOWIyNDI4ZGZhZTkyNDRkNmJkZTc4MWIwMzRlYjNjZDkuYmluZFBvcHVwKHBvcHVwX2MxODk3OGNhMWYzODRiYzk4NjZiMGFhN2JiZGYzNGI4KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzFjYWJjNGJjODNhZDQxNzZhNmYwYmI0MjQ2Zjk5YzA4ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTY5NjA1OTQyNzU1MDUsLTc0LjEzNDA1NzI5ODYyNTddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzAwYjVlYiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMwMGI1ZWIiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfZmVmMjgzYmM1YWEzNGUwYTkxNTE1YzNlNDA2ZDgxNDUpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNjhkMDRiYTZmZDY4NDE3NmFkYzIxNmU5YmQzNWM2ODUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNTNiNWJmYTBhODk4NDllYjk5MmQwMTUzNWZkNzFhMWYgPSAkKCc8ZGl2IGlkPSJodG1sXzUzYjViZmEwYTg5ODQ5ZWI5OTJkMDE1MzVmZDcxYTFmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5SaWNobW9uZCBUb3duIENsdXN0ZXIgMjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNjhkMDRiYTZmZDY4NDE3NmFkYzIxNmU5YmQzNWM2ODUuc2V0Q29udGVudChodG1sXzUzYjViZmEwYTg5ODQ5ZWI5OTJkMDE1MzVmZDcxYTFmKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzFjYWJjNGJjODNhZDQxNzZhNmYwYmI0MjQ2Zjk5YzA4LmJpbmRQb3B1cChwb3B1cF82OGQwNGJhNmZkNjg0MTc2YWRjMjE2ZTliZDM1YzY4NSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8wOGY0N2U5ODFjMDE0NWZkODdkMWNjZmJiNDRlY2FiNyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYwOTcxOTM0MDc5Mjg0LC03NC4wNjY2Nzc2NjA2MTc3MV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjMDBiNWViIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzAwYjVlYiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9mZWYyODNiYzVhYTM0ZTBhOTE1MTVjM2U0MDZkODE0NSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF80MzdkYjIxODc1ZWY0YWNkYTNmMGJiZDg5YTYzYjVkZSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF85YmZhMzk4ZDdjNmM0ZWU4OWRiNmVlMTdmMThjY2ExNSA9ICQoJzxkaXYgaWQ9Imh0bWxfOWJmYTM5OGQ3YzZjNGVlODlkYjZlZTE3ZjE4Y2NhMTUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlNob3JlIEFjcmVzIENsdXN0ZXIgMjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNDM3ZGIyMTg3NWVmNGFjZGEzZjBiYmQ4OWE2M2I1ZGUuc2V0Q29udGVudChodG1sXzliZmEzOThkN2M2YzRlZTg5ZGI2ZWUxN2YxOGNjYTE1KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzA4ZjQ3ZTk4MWMwMTQ1ZmQ4N2QxY2NmYmI0NGVjYWI3LmJpbmRQb3B1cChwb3B1cF80MzdkYjIxODc1ZWY0YWNkYTNmMGJiZDg5YTYzYjVkZSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9lMDUzZGVlYzgyOTk0ZjE4YTY0MWNiNzMyNjA5NDc2YSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYxOTE3ODQ1MjAyODQzLC03NC4wNzI2NDI0NDU0ODRdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzAwYjVlYiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMwMGI1ZWIiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfZmVmMjgzYmM1YWEzNGUwYTkxNTE1YzNlNDA2ZDgxNDUpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZmU2ZjdhY2Q5NDRjNDgxYzkxYTM5MzVjNGFmYmRmNDEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNjVjZGZjZjcyZjY5NGQ0ZDg4MDA0ZTI5ZGMxOGU2ZGEgPSAkKCc8ZGl2IGlkPSJodG1sXzY1Y2RmY2Y3MmY2OTRkNGQ4ODAwNGUyOWRjMThlNmRhIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DbGlmdG9uIENsdXN0ZXIgMjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZmU2ZjdhY2Q5NDRjNDgxYzkxYTM5MzVjNGFmYmRmNDEuc2V0Q29udGVudChodG1sXzY1Y2RmY2Y3MmY2OTRkNGQ4ODAwNGUyOWRjMThlNmRhKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2UwNTNkZWVjODI5OTRmMThhNjQxY2I3MzI2MDk0NzZhLmJpbmRQb3B1cChwb3B1cF9mZTZmN2FjZDk0NGM0ODFjOTFhMzkzNWM0YWZiZGY0MSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8wNzdlYjY5MzE0Mjg0ODM3OTNhNGQ2MzEwYmJmZWNhOSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYwNDQ3MzE4OTY4NzksLTc0LjA4NDAyMzY0NzQwMzU4XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2ZlZjI4M2JjNWFhMzRlMGE5MTUxNWMzZTQwNmQ4MTQ1KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2NhOGNhZDUxNTJjOTRlNmViZGYzNDEzZDdlOTRhZWQ1ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2M2YTUxYzc1ZjEzNzQ2ZDQ4MWNkNzc4MTM1NTg3NjNiID0gJCgnPGRpdiBpZD0iaHRtbF9jNmE1MWM3NWYxMzc0NmQ0ODFjZDc3ODEzNTU4NzYzYiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q29uY29yZCBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2NhOGNhZDUxNTJjOTRlNmViZGYzNDEzZDdlOTRhZWQ1LnNldENvbnRlbnQoaHRtbF9jNmE1MWM3NWYxMzc0NmQ0ODFjZDc3ODEzNTU4NzYzYik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8wNzdlYjY5MzE0Mjg0ODM3OTNhNGQ2MzEwYmJmZWNhOS5iaW5kUG9wdXAocG9wdXBfY2E4Y2FkNTE1MmM5NGU2ZWJkZjM0MTNkN2U5NGFlZDUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZTFhYWE0ZTYxOGM0NDYwMjkwOTZkMDQyOGJlNGIyZmMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42MDY3OTQzOTQ4MDEsLTc0LjA5Nzc2MjA2OTcyNTIyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiMwMGI1ZWIiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMDBiNWViIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2ZlZjI4M2JjNWFhMzRlMGE5MTUxNWMzZTQwNmQ4MTQ1KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzA1ZTQwZGFhYTUzYjQ0NzhhYWI2MGVhZjZlYjAyNmZjID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzMxOGU4NWYwZTVmODRlYjg4ZjFjYThhOGFkYThlNTlkID0gJCgnPGRpdiBpZD0iaHRtbF8zMThlODVmMGU1Zjg0ZWI4OGYxY2E4YThhZGE4ZTU5ZCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RW1lcnNvbiBIaWxsIENsdXN0ZXIgMjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMDVlNDBkYWFhNTNiNDQ3OGFhYjYwZWFmNmViMDI2ZmMuc2V0Q29udGVudChodG1sXzMxOGU4NWYwZTVmODRlYjg4ZjFjYThhOGFkYThlNTlkKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2UxYWFhNGU2MThjNDQ2MDI5MDk2ZDA0MjhiZTRiMmZjLmJpbmRQb3B1cChwb3B1cF8wNWU0MGRhYWE1M2I0NDc4YWFiNjBlYWY2ZWIwMjZmYyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9jMzEyZGFjMmIyZGY0NTI0OTJkYTA0MTA2ZWViMzNmZCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYzNTYzMDAwNjgxMTUxLC03NC4wOTgwNTA2MjM3Mzg4N10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjMDBiNWViIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzAwYjVlYiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9mZWYyODNiYzVhYTM0ZTBhOTE1MTVjM2U0MDZkODE0NSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9lMGRiMTRjYTBlZjk0ZGUzODk1MmMwMDBiMmUyZDc4NiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9hYThiNTgxYjVkNTE0OTNhODgyNjQyM2JmZjU0ZDdmZSA9ICQoJzxkaXYgaWQ9Imh0bWxfYWE4YjU4MWI1ZDUxNDkzYTg4MjY0MjNiZmY1NGQ3ZmUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlJhbmRhbGwgTWFub3IgQ2x1c3RlciAyPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9lMGRiMTRjYTBlZjk0ZGUzODk1MmMwMDBiMmUyZDc4Ni5zZXRDb250ZW50KGh0bWxfYWE4YjU4MWI1ZDUxNDkzYTg4MjY0MjNiZmY1NGQ3ZmUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYzMxMmRhYzJiMmRmNDUyNDkyZGEwNDEwNmVlYjMzZmQuYmluZFBvcHVwKHBvcHVwX2UwZGIxNGNhMGVmOTRkZTM4OTUyYzAwMGIyZTJkNzg2KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2Y5M2ZmODFlZjUyMDRiOTc4NTBjMTVlOTZlMTcwZDFkID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjM4NDMyODM3OTQ3OTUsLTc0LjE4NjIyMzMxNzQ5ODIzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiM4MDAwZmYiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjODAwMGZmIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2ZlZjI4M2JjNWFhMzRlMGE5MTUxNWMzZTQwNmQ4MTQ1KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzA4NmVmYjEyZmU2MTRkODk4MzQwNDJhODhlNjA1NWIyID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2M1NjA0MWM5MmUwOTQ5ZWI5MWQ2ZjEyMDVhNzk5ZGQ4ID0gJCgnPGRpdiBpZD0iaHRtbF9jNTYwNDFjOTJlMDk0OWViOTFkNmYxMjA1YTc5OWRkOCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+SG93bGFuZCBIb29rIENsdXN0ZXIgMTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMDg2ZWZiMTJmZTYxNGQ4OTgzNDA0MmE4OGU2MDU1YjIuc2V0Q29udGVudChodG1sX2M1NjA0MWM5MmUwOTQ5ZWI5MWQ2ZjEyMDVhNzk5ZGQ4KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2Y5M2ZmODFlZjUyMDRiOTc4NTBjMTVlOTZlMTcwZDFkLmJpbmRQb3B1cChwb3B1cF8wODZlZmIxMmZlNjE0ZDg5ODM0MDQyYTg4ZTYwNTViMik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9lMWZlNDA0YjNlNjI0MDEyODZlNjNhZGE0MGU3MGYwMiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYzMDE0Njc0MTE5MzgyNiwtNzQuMTQxODE2Nzg5Njg4OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9mZWYyODNiYzVhYTM0ZTBhOTE1MTVjM2U0MDZkODE0NSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9hMmYzYWJhMjhmNDQ0MjQ2YmIyYmJkNmYzOWYwYWFjYyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF84NjhlZWQ2ODZhMzA0OWU5YWEwYzc3Yjk2ODU1MDUxYSA9ICQoJzxkaXYgaWQ9Imh0bWxfODY4ZWVkNjg2YTMwNDllOWFhMGM3N2I5Njg1NTA1MWEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkVsbSBQYXJrIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYTJmM2FiYTI4ZjQ0NDI0NmJiMmJiZDZmMzlmMGFhY2Muc2V0Q29udGVudChodG1sXzg2OGVlZDY4NmEzMDQ5ZTlhYTBjNzdiOTY4NTUwNTFhKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2UxZmU0MDRiM2U2MjQwMTI4NmU2M2FkYTQwZTcwZjAyLmJpbmRQb3B1cChwb3B1cF9hMmYzYWJhMjhmNDQ0MjQ2YmIyYmJkNmYzOWYwYWFjYyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9kNjE4Y2ZhNWQ4NGY0MzE2OGYxMzYxMDI1ODJlMGZiZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYwMTgwOTU3NjMxNDQ0LC03NC4xMjA1OTM5OTcxODAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjMDBiNWViIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzAwYjVlYiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9mZWYyODNiYzVhYTM0ZTBhOTE1MTVjM2U0MDZkODE0NSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9lYzk0YTE2YTFiNjM0NGRlYjc1YzQ3NDE4MjUwODdhMCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF82ZWUxMzIzYTlkYTE0ZGE5YmYxMjk4Y2NmNGIzOTc0NCA9ICQoJzxkaXYgaWQ9Imh0bWxfNmVlMTMyM2E5ZGExNGRhOWJmMTI5OGNjZjRiMzk3NDQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk1hbm9yIEhlaWdodHMgQ2x1c3RlciAyPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9lYzk0YTE2YTFiNjM0NGRlYjc1YzQ3NDE4MjUwODdhMC5zZXRDb250ZW50KGh0bWxfNmVlMTMyM2E5ZGExNGRhOWJmMTI5OGNjZjRiMzk3NDQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZDYxOGNmYTVkODRmNDMxNjhmMTM2MTAyNTgyZTBmYmUuYmluZFBvcHVwKHBvcHVwX2VjOTRhMTZhMWI2MzQ0ZGViNzVjNDc0MTgyNTA4N2EwKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzI2MzBkNzI2NDBlODRhMTk4MTVlZGQzZGMxMmQyZDI0ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjAzNzA2OTI2MjczNzEsLTc0LjEzMjA4NDQ3NDg0Mjk4XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2ZlZjI4M2JjNWFhMzRlMGE5MTUxNWMzZTQwNmQ4MTQ1KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzg4OWMwZGQ1NDE0MDQzMWY5Nzc4ZjAxNWU5NDZmZmU1ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzZiZGVhZmU2YzQ3YzRlYmE4MTM3Y2U1Mzc5ZGNmNGIyID0gJCgnPGRpdiBpZD0iaHRtbF82YmRlYWZlNmM0N2M0ZWJhODEzN2NlNTM3OWRjZjRiMiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+V2lsbG93YnJvb2sgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF84ODljMGRkNTQxNDA0MzFmOTc3OGYwMTVlOTQ2ZmZlNS5zZXRDb250ZW50KGh0bWxfNmJkZWFmZTZjNDdjNGViYTgxMzdjZTUzNzlkY2Y0YjIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMjYzMGQ3MjY0MGU4NGExOTgxNWVkZDNkYzEyZDJkMjQuYmluZFBvcHVwKHBvcHVwXzg4OWMwZGQ1NDE0MDQzMWY5Nzc4ZjAxNWU5NDZmZmU1KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2YwNmFhYmQxZGFmMzQ3ZTM5ZWE5NzE1OTU5YTYyODZkID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTQxMTM5OTIyMDkxNzY2LC03NC4yMTc3NjYzNjA2ODU2N10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjMDBiNWViIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzAwYjVlYiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9mZWYyODNiYzVhYTM0ZTBhOTE1MTVjM2U0MDZkODE0NSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF80M2E2Yjg2YjcxNGU0ZmJhYjMwYjM0YzY0NzExZTVmYSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF82Nzk2YjFjYjFiYjY0YjMzODViMDcwYjQxZmU2NTgwNiA9ICQoJzxkaXYgaWQ9Imh0bWxfNjc5NmIxY2IxYmI2NGIzMzg1YjA3MGI0MWZlNjU4MDYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlNhbmR5IEdyb3VuZCBDbHVzdGVyIDI8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzQzYTZiODZiNzE0ZTRmYmFiMzBiMzRjNjQ3MTFlNWZhLnNldENvbnRlbnQoaHRtbF82Nzk2YjFjYjFiYjY0YjMzODViMDcwYjQxZmU2NTgwNik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9mMDZhYWJkMWRhZjM0N2UzOWVhOTcxNTk1OWE2Mjg2ZC5iaW5kUG9wdXAocG9wdXBfNDNhNmI4NmI3MTRlNGZiYWIzMGIzNGM2NDcxMWU1ZmEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYmNiMTY2ZWU4NWNhNDliOWFmNWMyZWYzOTQ3ZDYzYWEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41NzkxMTg3NDI5NjEyMTQsLTc0LjEyNzI3MjQwNjA0OTQ2XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiMwMGI1ZWIiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMDBiNWViIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2ZlZjI4M2JjNWFhMzRlMGE5MTUxNWMzZTQwNmQ4MTQ1KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2Y4ZTMxN2RmZjcyZjQ1Mzk5YzM0YmRmNTM3ZTE0NTEzID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2YwZjQ4MzQzYTQ5NzRlY2ZiYjQ3Yzk4OGI1MGM1ZWJhID0gJCgnPGRpdiBpZD0iaHRtbF9mMGY0ODM0M2E0OTc0ZWNmYmI0N2M5ODhiNTBjNWViYSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RWdiZXJ0dmlsbGUgQ2x1c3RlciAyPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9mOGUzMTdkZmY3MmY0NTM5OWMzNGJkZjUzN2UxNDUxMy5zZXRDb250ZW50KGh0bWxfZjBmNDgzNDNhNDk3NGVjZmJiNDdjOTg4YjUwYzVlYmEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYmNiMTY2ZWU4NWNhNDliOWFmNWMyZWYzOTQ3ZDYzYWEuYmluZFBvcHVwKHBvcHVwX2Y4ZTMxN2RmZjcyZjQ1Mzk5YzM0YmRmNTM3ZTE0NTEzKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzVkOWE1NTE0ZjBjNDQxNGZiNjA4NmRkNDY4YWFjODZhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTI2MjY0MDY3MzQ4MTIsLTc0LjIwMTUyNTU2NDU3NjU4XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiMwMGI1ZWIiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMDBiNWViIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2ZlZjI4M2JjNWFhMzRlMGE5MTUxNWMzZTQwNmQ4MTQ1KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzM0ZTllNDZlODc2YTQ2NWRiNzhiN2Q5OGM4YzA0ZDIyID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzA5M2I2NmViZTBlYjRkMDE4Y2Q0ZmE0MWMxZDU5NTI3ID0gJCgnPGRpdiBpZD0iaHRtbF8wOTNiNjZlYmUwZWI0ZDAxOGNkNGZhNDFjMWQ1OTUyNyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+UHJpbmNlJiMzOTtzIEJheSBDbHVzdGVyIDI8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzM0ZTllNDZlODc2YTQ2NWRiNzhiN2Q5OGM4YzA0ZDIyLnNldENvbnRlbnQoaHRtbF8wOTNiNjZlYmUwZWI0ZDAxOGNkNGZhNDFjMWQ1OTUyNyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl81ZDlhNTUxNGYwYzQ0MTRmYjYwODZkZDQ2OGFhYzg2YS5iaW5kUG9wdXAocG9wdXBfMzRlOWU0NmU4NzZhNDY1ZGI3OGI3ZDk4YzhjMDRkMjIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfN2RhNWExOWE2NTYzNGJkODk0MjkwYTlhMjg5NjNiZjMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41NzY1MDYyOTM3OTQ4OSwtNzQuMTM3OTI2NjM3NzE1NjhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzAwYjVlYiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMwMGI1ZWIiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfZmVmMjgzYmM1YWEzNGUwYTkxNTE1YzNlNDA2ZDgxNDUpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZmViNTBhOWM5YWZhNDhiOGIzNWVkMzhkNzVlYzc1ZDAgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMmQ5OGE0NTFlNDA2NDA3Yjk0YzU2ZTczMzA2MzQxYjcgPSAkKCc8ZGl2IGlkPSJodG1sXzJkOThhNDUxZTQwNjQwN2I5NGM1NmU3MzMwNjM0MWI3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5MaWdodGhvdXNlIEhpbGwgQ2x1c3RlciAyPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9mZWI1MGE5YzlhZmE0OGI4YjM1ZWQzOGQ3NWVjNzVkMC5zZXRDb250ZW50KGh0bWxfMmQ5OGE0NTFlNDA2NDA3Yjk0YzU2ZTczMzA2MzQxYjcpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfN2RhNWExOWE2NTYzNGJkODk0MjkwYTlhMjg5NjNiZjMuYmluZFBvcHVwKHBvcHVwX2ZlYjUwYTljOWFmYTQ4YjhiMzVlZDM4ZDc1ZWM3NWQwKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2VlYzcyM2Q2NjVhMzQxZjM4ZTRjOTUzMTJmYzhiYWNlID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTE5NTQxNDU3NDg5MDksLTc0LjIyOTU3MDgwNjI2OTQxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiMwMGI1ZWIiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMDBiNWViIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2ZlZjI4M2JjNWFhMzRlMGE5MTUxNWMzZTQwNmQ4MTQ1KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2NhODY4NjgyZmZlZDQ1YWI4YTE1OTFjM2FlNDcyYTllID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2IxMTJjZWU0ZWFmNDRhYWFhZmFjY2QzNGY0NWRiMzI4ID0gJCgnPGRpdiBpZD0iaHRtbF9iMTEyY2VlNGVhZjQ0YWFhYWZhY2NkMzRmNDVkYjMyOCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+UmljaG1vbmQgVmFsbGV5IENsdXN0ZXIgMjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfY2E4Njg2ODJmZmVkNDVhYjhhMTU5MWMzYWU0NzJhOWUuc2V0Q29udGVudChodG1sX2IxMTJjZWU0ZWFmNDRhYWFhZmFjY2QzNGY0NWRiMzI4KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2VlYzcyM2Q2NjVhMzQxZjM4ZTRjOTUzMTJmYzhiYWNlLmJpbmRQb3B1cChwb3B1cF9jYTg2ODY4MmZmZWQ0NWFiOGExNTkxYzNhZTQ3MmE5ZSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl85NWUzMmUxYTE2N2Y0OWM1ODNlZTE2ZDlhZGNhNGU4YiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYxNzMxMDc5MjUyOTgzLC03NC4wODE3Mzk5MjIxMTk2Ml0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9mZWYyODNiYzVhYTM0ZTBhOTE1MTVjM2U0MDZkODE0NSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF80ZDA2NGQyMWIwNzI0ZDI3YmUyMjE3NWY0MWNmNjlkMiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF83Y2Y1MTgxODJhMmY0OWJlOWUyZGE0ODg4YTE4N2UzYyA9ICQoJzxkaXYgaWQ9Imh0bWxfN2NmNTE4MTgyYTJmNDliZTllMmRhNDg4OGExODdlM2MiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkZveCBIaWxscyBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzRkMDY0ZDIxYjA3MjRkMjdiZTIyMTc1ZjQxY2Y2OWQyLnNldENvbnRlbnQoaHRtbF83Y2Y1MTgxODJhMmY0OWJlOWUyZGE0ODg4YTE4N2UzYyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl85NWUzMmUxYTE2N2Y0OWM1ODNlZTE2ZDlhZGNhNGU4Yi5iaW5kUG9wdXAocG9wdXBfNGQwNjRkMjFiMDcyNGQyN2JlMjIxNzVmNDFjZjY5ZDIpOwoKICAgICAgICAgICAgCiAgICAgICAgCjwvc2NyaXB0Pg== onload="this.contentDocument.open();this.contentDocument.write(atob(this.getAttribute('data-html')));this.contentDocument.close();" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>



<h3 id="version">5. Examining the Clusters</h3>


```python
#CLUSTER-1

Staten_Island_merged.loc[Staten_Island_merged['Cluster Labels'] == 0, Staten_Island_merged.columns[[1] + list(range(5, Staten_Island_merged.shape[1]))]]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Neighborhood</th>
      <th>1st Most Common Venue</th>
      <th>2nd Most Common Venue</th>
      <th>3rd Most Common Venue</th>
      <th>4th Most Common Venue</th>
      <th>5th Most Common Venue</th>
      <th>6th Most Common Venue</th>
      <th>7th Most Common Venue</th>
      <th>8th Most Common Venue</th>
      <th>9th Most Common Venue</th>
      <th>10th Most Common Venue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>New Brighton</td>
      <td>Deli / Bodega</td>
      <td>Bus Stop</td>
      <td>Park</td>
      <td>Discount Store</td>
      <td>Playground</td>
      <td>Flower Shop</td>
      <td>Bowling Alley</td>
      <td>Filipino Restaurant</td>
      <td>French Restaurant</td>
      <td>Food Truck</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Grymes Hill</td>
      <td>Deli / Bodega</td>
      <td>Dog Run</td>
      <td>Fast Food Restaurant</td>
      <td>Furniture / Home Store</td>
      <td>French Restaurant</td>
      <td>Food Truck</td>
      <td>Food &amp; Drink Shop</td>
      <td>Food</td>
      <td>Flower Shop</td>
      <td>Fish &amp; Chips Shop</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Mariner's Harbor</td>
      <td>Italian Restaurant</td>
      <td>Bus Stop</td>
      <td>Deli / Bodega</td>
      <td>Supermarket</td>
      <td>Other Repair Shop</td>
      <td>Pizza Place</td>
      <td>Dim Sum Restaurant</td>
      <td>Fish &amp; Chips Shop</td>
      <td>French Restaurant</td>
      <td>Food Truck</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Arlington</td>
      <td>Deli / Bodega</td>
      <td>Boat or Ferry</td>
      <td>Construction &amp; Landscaping</td>
      <td>Coffee Shop</td>
      <td>Bus Stop</td>
      <td>Filipino Restaurant</td>
      <td>Furniture / Home Store</td>
      <td>French Restaurant</td>
      <td>Food Truck</td>
      <td>Food &amp; Drink Shop</td>
    </tr>
    <tr>
      <th>41</th>
      <td>Arden Heights</td>
      <td>Deli / Bodega</td>
      <td>Lawyer</td>
      <td>Bus Stop</td>
      <td>Business Service</td>
      <td>Coffee Shop</td>
      <td>Pizza Place</td>
      <td>Pharmacy</td>
      <td>Fast Food Restaurant</td>
      <td>Food Truck</td>
      <td>Food &amp; Drink Shop</td>
    </tr>
    <tr>
      <th>50</th>
      <td>Concord</td>
      <td>Deli / Bodega</td>
      <td>Gym / Fitness Center</td>
      <td>Bus Stop</td>
      <td>Train Station</td>
      <td>Park</td>
      <td>Coffee Shop</td>
      <td>Sandwich Place</td>
      <td>Peruvian Restaurant</td>
      <td>Bagel Shop</td>
      <td>Grocery Store</td>
    </tr>
    <tr>
      <th>54</th>
      <td>Elm Park</td>
      <td>Deli / Bodega</td>
      <td>Italian Restaurant</td>
      <td>American Restaurant</td>
      <td>Ice Cream Shop</td>
      <td>Bus Stop</td>
      <td>Pizza Place</td>
      <td>Farmers Market</td>
      <td>Food Truck</td>
      <td>Food &amp; Drink Shop</td>
      <td>Food</td>
    </tr>
    <tr>
      <th>56</th>
      <td>Willowbrook</td>
      <td>Chinese Restaurant</td>
      <td>Bus Stop</td>
      <td>Spa</td>
      <td>Deli / Bodega</td>
      <td>Yoga Studio</td>
      <td>Filipino Restaurant</td>
      <td>French Restaurant</td>
      <td>Food Truck</td>
      <td>Food &amp; Drink Shop</td>
      <td>Food</td>
    </tr>
    <tr>
      <th>62</th>
      <td>Fox Hills</td>
      <td>Deli / Bodega</td>
      <td>African Restaurant</td>
      <td>Bus Stop</td>
      <td>Sandwich Place</td>
      <td>Grocery Store</td>
      <td>Fast Food Restaurant</td>
      <td>French Restaurant</td>
      <td>Food Truck</td>
      <td>Food &amp; Drink Shop</td>
      <td>Food</td>
    </tr>
  </tbody>
</table>
</div>




```python
#CLUSTER-2

Staten_Island_merged.loc[Staten_Island_merged['Cluster Labels'] == 1, Staten_Island_merged.columns[[1] + list(range(5, Staten_Island_merged.shape[1]))]]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Neighborhood</th>
      <th>1st Most Common Venue</th>
      <th>2nd Most Common Venue</th>
      <th>3rd Most Common Venue</th>
      <th>4th Most Common Venue</th>
      <th>5th Most Common Venue</th>
      <th>6th Most Common Venue</th>
      <th>7th Most Common Venue</th>
      <th>8th Most Common Venue</th>
      <th>9th Most Common Venue</th>
      <th>10th Most Common Venue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>26</th>
      <td>Graniteville</td>
      <td>Boat or Ferry</td>
      <td>Grocery Store</td>
      <td>Filipino Restaurant</td>
      <td>Gas Station</td>
      <td>Furniture / Home Store</td>
      <td>French Restaurant</td>
      <td>Food Truck</td>
      <td>Food &amp; Drink Shop</td>
      <td>Food</td>
      <td>Flower Shop</td>
    </tr>
    <tr>
      <th>53</th>
      <td>Howland Hook</td>
      <td>Boat or Ferry</td>
      <td>German Restaurant</td>
      <td>Gas Station</td>
      <td>Furniture / Home Store</td>
      <td>French Restaurant</td>
      <td>Food Truck</td>
      <td>Food &amp; Drink Shop</td>
      <td>Food</td>
      <td>Flower Shop</td>
      <td>Fish &amp; Chips Shop</td>
    </tr>
  </tbody>
</table>
</div>




```python
#CLUSTER-3

Staten_Island_merged.loc[Staten_Island_merged['Cluster Labels'] == 2, Staten_Island_merged.columns[[1] + list(range(5, Staten_Island_merged.shape[1]))]]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Neighborhood</th>
      <th>1st Most Common Venue</th>
      <th>2nd Most Common Venue</th>
      <th>3rd Most Common Venue</th>
      <th>4th Most Common Venue</th>
      <th>5th Most Common Venue</th>
      <th>6th Most Common Venue</th>
      <th>7th Most Common Venue</th>
      <th>8th Most Common Venue</th>
      <th>9th Most Common Venue</th>
      <th>10th Most Common Venue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>St. George</td>
      <td>Clothing Store</td>
      <td>Sporting Goods Shop</td>
      <td>Italian Restaurant</td>
      <td>Park</td>
      <td>Bar</td>
      <td>Pizza Place</td>
      <td>Outlet Mall</td>
      <td>Baseball Stadium</td>
      <td>Bus Stop</td>
      <td>Bus Station</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Stapleton</td>
      <td>Pizza Place</td>
      <td>Discount Store</td>
      <td>Sandwich Place</td>
      <td>Bank</td>
      <td>Restaurant</td>
      <td>Spanish Restaurant</td>
      <td>Fast Food Restaurant</td>
      <td>Skate Park</td>
      <td>New American Restaurant</td>
      <td>Optical Shop</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Rosebank</td>
      <td>Pharmacy</td>
      <td>Italian Restaurant</td>
      <td>Grocery Store</td>
      <td>Breakfast Spot</td>
      <td>Beach</td>
      <td>Pizza Place</td>
      <td>Deli / Bodega</td>
      <td>Cosmetics Shop</td>
      <td>Ice Cream Shop</td>
      <td>Eastern European Restaurant</td>
    </tr>
    <tr>
      <th>4</th>
      <td>West Brighton</td>
      <td>Coffee Shop</td>
      <td>Pharmacy</td>
      <td>Bank</td>
      <td>Italian Restaurant</td>
      <td>Music Store</td>
      <td>Breakfast Spot</td>
      <td>Bar</td>
      <td>Bus Stop</td>
      <td>Café</td>
      <td>Sandwich Place</td>
    </tr>
    <tr>
      <th>7</th>
      <td>South Beach</td>
      <td>Pier</td>
      <td>Beach</td>
      <td>Athletics &amp; Sports</td>
      <td>Deli / Bodega</td>
      <td>Diner</td>
      <td>Discount Store</td>
      <td>Furniture / Home Store</td>
      <td>French Restaurant</td>
      <td>Food Truck</td>
      <td>Food &amp; Drink Shop</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Port Richmond</td>
      <td>Rental Car Location</td>
      <td>Martial Arts Dojo</td>
      <td>Donut Shop</td>
      <td>Pizza Place</td>
      <td>Dim Sum Restaurant</td>
      <td>Fast Food Restaurant</td>
      <td>French Restaurant</td>
      <td>Food Truck</td>
      <td>Food &amp; Drink Shop</td>
      <td>Food</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Castleton Corners</td>
      <td>Bank</td>
      <td>Pizza Place</td>
      <td>Japanese Restaurant</td>
      <td>Sandwich Place</td>
      <td>Go Kart Track</td>
      <td>Grocery Store</td>
      <td>Mini Golf</td>
      <td>Tattoo Parlor</td>
      <td>Bagel Shop</td>
      <td>Bar</td>
    </tr>
    <tr>
      <th>12</th>
      <td>New Springville</td>
      <td>Chinese Restaurant</td>
      <td>Coffee Shop</td>
      <td>Mobile Phone Shop</td>
      <td>Bagel Shop</td>
      <td>Accessories Store</td>
      <td>Donut Shop</td>
      <td>Sandwich Place</td>
      <td>Restaurant</td>
      <td>Pizza Place</td>
      <td>Pharmacy</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Travis</td>
      <td>Hotel</td>
      <td>Bowling Alley</td>
      <td>Gym</td>
      <td>Deli / Bodega</td>
      <td>Sports Club</td>
      <td>Comedy Club</td>
      <td>Spanish Restaurant</td>
      <td>Park</td>
      <td>Café</td>
      <td>Baseball Field</td>
    </tr>
    <tr>
      <th>14</th>
      <td>New Dorp</td>
      <td>Italian Restaurant</td>
      <td>Pizza Place</td>
      <td>Yoga Studio</td>
      <td>Bank</td>
      <td>Hobby Shop</td>
      <td>Mexican Restaurant</td>
      <td>Gas Station</td>
      <td>Dim Sum Restaurant</td>
      <td>Dessert Shop</td>
      <td>Deli / Bodega</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Oakwood</td>
      <td>Lawyer</td>
      <td>Nightlife Spot</td>
      <td>Bar</td>
      <td>Filipino Restaurant</td>
      <td>Gas Station</td>
      <td>Furniture / Home Store</td>
      <td>French Restaurant</td>
      <td>Food Truck</td>
      <td>Food &amp; Drink Shop</td>
      <td>Food</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Great Kills</td>
      <td>Bar</td>
      <td>Italian Restaurant</td>
      <td>Pizza Place</td>
      <td>Japanese Restaurant</td>
      <td>Basketball Court</td>
      <td>Liquor Store</td>
      <td>Mexican Restaurant</td>
      <td>Grocery Store</td>
      <td>Food &amp; Drink Shop</td>
      <td>Pharmacy</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Eltingville</td>
      <td>Pizza Place</td>
      <td>Sushi Restaurant</td>
      <td>Pharmacy</td>
      <td>Sandwich Place</td>
      <td>Gourmet Shop</td>
      <td>Fast Food Restaurant</td>
      <td>Bank</td>
      <td>Martial Arts Dojo</td>
      <td>Smoke Shop</td>
      <td>Bus Stop</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Annadale</td>
      <td>Pizza Place</td>
      <td>Train Station</td>
      <td>Food</td>
      <td>Pharmacy</td>
      <td>Diner</td>
      <td>Restaurant</td>
      <td>Dance Studio</td>
      <td>Deli / Bodega</td>
      <td>American Restaurant</td>
      <td>Fast Food Restaurant</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Woodrow</td>
      <td>Pharmacy</td>
      <td>Bakery</td>
      <td>Grocery Store</td>
      <td>Sushi Restaurant</td>
      <td>Chinese Restaurant</td>
      <td>Mexican Restaurant</td>
      <td>Diner</td>
      <td>Coffee Shop</td>
      <td>Martial Arts Dojo</td>
      <td>Bank</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Tottenville</td>
      <td>Italian Restaurant</td>
      <td>Thrift / Vintage Store</td>
      <td>Cosmetics Shop</td>
      <td>Construction &amp; Landscaping</td>
      <td>Bus Stop</td>
      <td>Mexican Restaurant</td>
      <td>Deli / Bodega</td>
      <td>Lawyer</td>
      <td>Hotel</td>
      <td>Event Space</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Tompkinsville</td>
      <td>Pizza Place</td>
      <td>Bus Stop</td>
      <td>Brewery</td>
      <td>Park</td>
      <td>Ice Cream Shop</td>
      <td>Sandwich Place</td>
      <td>Supermarket</td>
      <td>Café</td>
      <td>Caribbean Restaurant</td>
      <td>Check Cashing Service</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Silver Lake</td>
      <td>Burger Joint</td>
      <td>American Restaurant</td>
      <td>Golf Course</td>
      <td>Gym</td>
      <td>Yoga Studio</td>
      <td>Filipino Restaurant</td>
      <td>French Restaurant</td>
      <td>Food Truck</td>
      <td>Food &amp; Drink Shop</td>
      <td>Food</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Sunnyside</td>
      <td>American Restaurant</td>
      <td>Spa</td>
      <td>Market</td>
      <td>Grocery Store</td>
      <td>Gym</td>
      <td>Yoga Studio</td>
      <td>Filipino Restaurant</td>
      <td>French Restaurant</td>
      <td>Food Truck</td>
      <td>Food &amp; Drink Shop</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Park Hill</td>
      <td>Bus Stop</td>
      <td>Park</td>
      <td>Hotel</td>
      <td>Coffee Shop</td>
      <td>Athletics &amp; Sports</td>
      <td>Gym / Fitness Center</td>
      <td>Yoga Studio</td>
      <td>Filipino Restaurant</td>
      <td>Food Truck</td>
      <td>Food &amp; Drink Shop</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Westerleigh</td>
      <td>Convenience Store</td>
      <td>Arcade</td>
      <td>Sushi Restaurant</td>
      <td>Yoga Studio</td>
      <td>Fast Food Restaurant</td>
      <td>Furniture / Home Store</td>
      <td>French Restaurant</td>
      <td>Food Truck</td>
      <td>Food &amp; Drink Shop</td>
      <td>Food</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Arrochar</td>
      <td>Bus Stop</td>
      <td>Liquor Store</td>
      <td>Italian Restaurant</td>
      <td>Deli / Bodega</td>
      <td>Polish Restaurant</td>
      <td>Outdoors &amp; Recreation</td>
      <td>Supermarket</td>
      <td>Middle Eastern Restaurant</td>
      <td>Mediterranean Restaurant</td>
      <td>Sandwich Place</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Grasmere</td>
      <td>Bus Stop</td>
      <td>Bagel Shop</td>
      <td>Bakery</td>
      <td>Bank</td>
      <td>Japanese Restaurant</td>
      <td>Basketball Court</td>
      <td>Italian Restaurant</td>
      <td>IT Services</td>
      <td>Grocery Store</td>
      <td>Nail Salon</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Old Town</td>
      <td>Italian Restaurant</td>
      <td>Donut Shop</td>
      <td>Playground</td>
      <td>Mattress Store</td>
      <td>Pharmacy</td>
      <td>Bakery</td>
      <td>Pizza Place</td>
      <td>Liquor Store</td>
      <td>Restaurant</td>
      <td>Gas Station</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Dongan Hills</td>
      <td>Pizza Place</td>
      <td>Italian Restaurant</td>
      <td>Chinese Restaurant</td>
      <td>Bar</td>
      <td>Bagel Shop</td>
      <td>Smoke Shop</td>
      <td>Flower Shop</td>
      <td>Fast Food Restaurant</td>
      <td>Sandwich Place</td>
      <td>Sushi Restaurant</td>
    </tr>
    <tr>
      <th>32</th>
      <td>Midland Beach</td>
      <td>Beach</td>
      <td>Deli / Bodega</td>
      <td>Pet Store</td>
      <td>Bookstore</td>
      <td>Bus Stop</td>
      <td>Restaurant</td>
      <td>Liquor Store</td>
      <td>Chinese Restaurant</td>
      <td>Food Truck</td>
      <td>Food &amp; Drink Shop</td>
    </tr>
    <tr>
      <th>33</th>
      <td>Grant City</td>
      <td>Food &amp; Drink Shop</td>
      <td>Fast Food Restaurant</td>
      <td>Bar</td>
      <td>Health &amp; Beauty Service</td>
      <td>Dessert Shop</td>
      <td>Grocery Store</td>
      <td>Miscellaneous Shop</td>
      <td>Tanning Salon</td>
      <td>Mexican Restaurant</td>
      <td>Bus Stop</td>
    </tr>
    <tr>
      <th>34</th>
      <td>New Dorp Beach</td>
      <td>Italian Restaurant</td>
      <td>Deli / Bodega</td>
      <td>Food</td>
      <td>Scenic Lookout</td>
      <td>Other Repair Shop</td>
      <td>Beach</td>
      <td>Skating Rink</td>
      <td>Sports Bar</td>
      <td>Diner</td>
      <td>Restaurant</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Bay Terrace</td>
      <td>Supermarket</td>
      <td>Insurance Office</td>
      <td>Italian Restaurant</td>
      <td>Train Station</td>
      <td>Sushi Restaurant</td>
      <td>Liquor Store</td>
      <td>Salon / Barbershop</td>
      <td>Donut Shop</td>
      <td>Shipping Store</td>
      <td>Fast Food Restaurant</td>
    </tr>
    <tr>
      <th>36</th>
      <td>Huguenot</td>
      <td>Italian Restaurant</td>
      <td>Train Station</td>
      <td>Deli / Bodega</td>
      <td>Bank</td>
      <td>Donut Shop</td>
      <td>Sandwich Place</td>
      <td>Nail Salon</td>
      <td>Ice Cream Shop</td>
      <td>Discount Store</td>
      <td>Fish &amp; Chips Shop</td>
    </tr>
    <tr>
      <th>37</th>
      <td>Pleasant Plains</td>
      <td>Donut Shop</td>
      <td>Yoga Studio</td>
      <td>Discount Store</td>
      <td>Bus Stop</td>
      <td>Fast Food Restaurant</td>
      <td>Salon / Barbershop</td>
      <td>Toll Plaza</td>
      <td>Pizza Place</td>
      <td>Brewery</td>
      <td>Cosmetics Shop</td>
    </tr>
    <tr>
      <th>38</th>
      <td>Butler Manor</td>
      <td>Pool</td>
      <td>Baseball Field</td>
      <td>Convenience Store</td>
      <td>Yoga Studio</td>
      <td>Fast Food Restaurant</td>
      <td>French Restaurant</td>
      <td>Food Truck</td>
      <td>Food &amp; Drink Shop</td>
      <td>Food</td>
      <td>Flower Shop</td>
    </tr>
    <tr>
      <th>39</th>
      <td>Charleston</td>
      <td>Coffee Shop</td>
      <td>Cosmetics Shop</td>
      <td>Big Box Store</td>
      <td>Gym / Fitness Center</td>
      <td>Music Venue</td>
      <td>Burger Joint</td>
      <td>Furniture / Home Store</td>
      <td>Sporting Goods Shop</td>
      <td>Diner</td>
      <td>Gift Shop</td>
    </tr>
    <tr>
      <th>40</th>
      <td>Rossville</td>
      <td>Pizza Place</td>
      <td>Bagel Shop</td>
      <td>Deli / Bodega</td>
      <td>American Restaurant</td>
      <td>Ice Cream Shop</td>
      <td>Convenience Store</td>
      <td>Liquor Store</td>
      <td>Donut Shop</td>
      <td>Moving Target</td>
      <td>Grocery Store</td>
    </tr>
    <tr>
      <th>42</th>
      <td>Greenridge</td>
      <td>Shipping Store</td>
      <td>Pet Store</td>
      <td>Diner</td>
      <td>Construction &amp; Landscaping</td>
      <td>Lawyer</td>
      <td>Pizza Place</td>
      <td>Bagel Shop</td>
      <td>Food Truck</td>
      <td>Food &amp; Drink Shop</td>
      <td>Food</td>
    </tr>
    <tr>
      <th>43</th>
      <td>Heartland Village</td>
      <td>Coffee Shop</td>
      <td>Accessories Store</td>
      <td>Optical Shop</td>
      <td>Food</td>
      <td>Restaurant</td>
      <td>Spa</td>
      <td>Donut Shop</td>
      <td>Pizza Place</td>
      <td>Food Truck</td>
      <td>Pharmacy</td>
    </tr>
    <tr>
      <th>44</th>
      <td>Chelsea</td>
      <td>Steakhouse</td>
      <td>Spanish Restaurant</td>
      <td>Bus Stop</td>
      <td>Sandwich Place</td>
      <td>Park</td>
      <td>Fast Food Restaurant</td>
      <td>Food Truck</td>
      <td>Food &amp; Drink Shop</td>
      <td>Food</td>
      <td>Flower Shop</td>
    </tr>
    <tr>
      <th>45</th>
      <td>Bloomfield</td>
      <td>Recreation Center</td>
      <td>Bus Stop</td>
      <td>Burger Joint</td>
      <td>Theme Park</td>
      <td>Dim Sum Restaurant</td>
      <td>Diner</td>
      <td>French Restaurant</td>
      <td>Food Truck</td>
      <td>Department Store</td>
      <td>Food &amp; Drink Shop</td>
    </tr>
    <tr>
      <th>46</th>
      <td>Bulls Head</td>
      <td>Bus Stop</td>
      <td>Pizza Place</td>
      <td>Pharmacy</td>
      <td>Ice Cream Shop</td>
      <td>Sandwich Place</td>
      <td>Café</td>
      <td>Chinese Restaurant</td>
      <td>Gift Shop</td>
      <td>Food Truck</td>
      <td>Deli / Bodega</td>
    </tr>
    <tr>
      <th>47</th>
      <td>Richmond Town</td>
      <td>Italian Restaurant</td>
      <td>Spa</td>
      <td>Bagel Shop</td>
      <td>Café</td>
      <td>Yoga Studio</td>
      <td>Fast Food Restaurant</td>
      <td>French Restaurant</td>
      <td>Food Truck</td>
      <td>Food &amp; Drink Shop</td>
      <td>Food</td>
    </tr>
    <tr>
      <th>48</th>
      <td>Shore Acres</td>
      <td>Italian Restaurant</td>
      <td>Bus Stop</td>
      <td>Intersection</td>
      <td>Deli / Bodega</td>
      <td>Bar</td>
      <td>Baseball Field</td>
      <td>Gastropub</td>
      <td>Music Store</td>
      <td>Nail Salon</td>
      <td>Furniture / Home Store</td>
    </tr>
    <tr>
      <th>49</th>
      <td>Clifton</td>
      <td>Train Station</td>
      <td>Grocery Store</td>
      <td>Museum</td>
      <td>Martial Arts Dojo</td>
      <td>Discount Store</td>
      <td>Pizza Place</td>
      <td>Eastern European Restaurant</td>
      <td>Chinese Restaurant</td>
      <td>Cajun / Creole Restaurant</td>
      <td>Park</td>
    </tr>
    <tr>
      <th>51</th>
      <td>Emerson Hill</td>
      <td>Construction &amp; Landscaping</td>
      <td>Food</td>
      <td>Sculpture Garden</td>
      <td>Historic Site</td>
      <td>Yoga Studio</td>
      <td>Event Space</td>
      <td>Food Truck</td>
      <td>Food &amp; Drink Shop</td>
      <td>Flower Shop</td>
      <td>Fish &amp; Chips Shop</td>
    </tr>
    <tr>
      <th>52</th>
      <td>Randall Manor</td>
      <td>Bus Stop</td>
      <td>Business Service</td>
      <td>Park</td>
      <td>Home Service</td>
      <td>Bagel Shop</td>
      <td>Yoga Studio</td>
      <td>Filipino Restaurant</td>
      <td>French Restaurant</td>
      <td>Food Truck</td>
      <td>Food &amp; Drink Shop</td>
    </tr>
    <tr>
      <th>55</th>
      <td>Manor Heights</td>
      <td>Deli / Bodega</td>
      <td>Liquor Store</td>
      <td>Donut Shop</td>
      <td>Pharmacy</td>
      <td>American Restaurant</td>
      <td>Food</td>
      <td>Sushi Restaurant</td>
      <td>Home Service</td>
      <td>Chinese Restaurant</td>
      <td>Campground</td>
    </tr>
    <tr>
      <th>57</th>
      <td>Sandy Ground</td>
      <td>Intersection</td>
      <td>Food Truck</td>
      <td>Playground</td>
      <td>Fish &amp; Chips Shop</td>
      <td>Bus Stop</td>
      <td>Racetrack</td>
      <td>Art Gallery</td>
      <td>Hotel</td>
      <td>Food &amp; Drink Shop</td>
      <td>Ice Cream Shop</td>
    </tr>
    <tr>
      <th>58</th>
      <td>Egbertville</td>
      <td>Italian Restaurant</td>
      <td>Clothing Store</td>
      <td>Bagel Shop</td>
      <td>Cosmetics Shop</td>
      <td>Dim Sum Restaurant</td>
      <td>Filipino Restaurant</td>
      <td>Furniture / Home Store</td>
      <td>French Restaurant</td>
      <td>Food Truck</td>
      <td>Food &amp; Drink Shop</td>
    </tr>
    <tr>
      <th>59</th>
      <td>Prince's Bay</td>
      <td>Pizza Place</td>
      <td>Pharmacy</td>
      <td>Ice Cream Shop</td>
      <td>Sushi Restaurant</td>
      <td>Liquor Store</td>
      <td>Chinese Restaurant</td>
      <td>Bagel Shop</td>
      <td>Tanning Salon</td>
      <td>Pet Store</td>
      <td>Farmers Market</td>
    </tr>
    <tr>
      <th>60</th>
      <td>Lighthouse Hill</td>
      <td>Italian Restaurant</td>
      <td>Art Museum</td>
      <td>Trail</td>
      <td>Spa</td>
      <td>Café</td>
      <td>Yoga Studio</td>
      <td>Fast Food Restaurant</td>
      <td>French Restaurant</td>
      <td>Food Truck</td>
      <td>Food &amp; Drink Shop</td>
    </tr>
    <tr>
      <th>61</th>
      <td>Richmond Valley</td>
      <td>Fast Food Restaurant</td>
      <td>Bank</td>
      <td>Deli / Bodega</td>
      <td>Construction &amp; Landscaping</td>
      <td>Food</td>
      <td>Train Station</td>
      <td>Coffee Shop</td>
      <td>Smoothie Shop</td>
      <td>Sandwich Place</td>
      <td>Mexican Restaurant</td>
    </tr>
  </tbody>
</table>
</div>




```python
#CLUSTER-4

Staten_Island_merged.loc[Staten_Island_merged['Cluster Labels'] == 3, Staten_Island_merged.columns[[1] + list(range(5, Staten_Island_merged.shape[1]))]]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Neighborhood</th>
      <th>1st Most Common Venue</th>
      <th>2nd Most Common Venue</th>
      <th>3rd Most Common Venue</th>
      <th>4th Most Common Venue</th>
      <th>5th Most Common Venue</th>
      <th>6th Most Common Venue</th>
      <th>7th Most Common Venue</th>
      <th>8th Most Common Venue</th>
      <th>9th Most Common Venue</th>
      <th>10th Most Common Venue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10</th>
      <td>Port Ivory</td>
      <td>Business Service</td>
      <td>Yoga Studio</td>
      <td>Gastropub</td>
      <td>Furniture / Home Store</td>
      <td>French Restaurant</td>
      <td>Food Truck</td>
      <td>Food &amp; Drink Shop</td>
      <td>Food</td>
      <td>Flower Shop</td>
      <td>Fish &amp; Chips Shop</td>
    </tr>
  </tbody>
</table>
</div>




```python
#CLUSTER-5

Staten_Island_merged.loc[Staten_Island_merged['Cluster Labels'] == 4, Staten_Island_merged.columns[[1] + list(range(5, Staten_Island_merged.shape[1]))]]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Neighborhood</th>
      <th>1st Most Common Venue</th>
      <th>2nd Most Common Venue</th>
      <th>3rd Most Common Venue</th>
      <th>4th Most Common Venue</th>
      <th>5th Most Common Venue</th>
      <th>6th Most Common Venue</th>
      <th>7th Most Common Venue</th>
      <th>8th Most Common Venue</th>
      <th>9th Most Common Venue</th>
      <th>10th Most Common Venue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>6</th>
      <td>Todt Hill</td>
      <td>Park</td>
      <td>Yoga Studio</td>
      <td>Gas Station</td>
      <td>French Restaurant</td>
      <td>Food Truck</td>
      <td>Food &amp; Drink Shop</td>
      <td>Food</td>
      <td>Flower Shop</td>
      <td>Fish &amp; Chips Shop</td>
      <td>Filipino Restaurant</td>
    </tr>
  </tbody>
</table>
</div>



<h3 id="version">Results and Discussion</h3>

<p>
The vision of this project is to help indivuduals/families who want to relocate to the safest borough in New York City, anyone can explore the neighborhoods to which they want to relocate based on the most common venues in it. </p>
<p>In the clusters formed after the data is explored a individual can look for a neighborhood with good public transportation, food places we can see that Clusters 2 has bus stops, restaurants as the most common venues. If a person is looking for a neighborhood with stores and restaurants in a close proximity then the neighborhoods in the cluster 3 is suitable for them. For a family looking for a neighborhood the Cluster 3 is more suitable as it shows parks, beach, grocery stores and Gyms. 
</p>

<h3 id="version">Conclusion</h3>

<p>
This project helps an individual to get a better exposure to the neighborhoods in terms of the crimes occuring in the borough and the most common venues in that neighborhood. A project like this will be helpful to many people, it is always helpful to make use of technology and to understnad about the location online instead of being present there in the location itself or even before moving to the new place. </p>
<p>
   We have just taken safety as a primary concern of everyone and has shortlisted to the safest borough in New york city and then finding the most common places in the neighbourhoods and presenting the different clusters to choose from according to once preferences. 
    </p>


```python

```


```python

```
