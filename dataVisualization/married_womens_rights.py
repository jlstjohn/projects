'''
For this project we are going to explore data looking at married women's economic rights reform from 1835-1920 (data gathered by Sara Chatfield).
We will be exploring this data visually.
The goal is to provide a set of choropleth visualizations for each of the columns containing dates such that the resulting visualizations tell
the story by conveying through color, texture, or both the time lines of achievement of each milestone/column in the dataset (for the contiguous
48 states only.)
'''

### import libraries
import numpy as np
import pandas as pd
import geopandas as gpd
import json
import folium

import matplotlib.pyplot as plt

# read in and view codebook info (i.e., readme for the dataset)
print('\n')
file_name = 'sturmcodebook.txt'
with open(file_name, 'r') as f:
    lines = f.read()
    print(lines)

# read the data into a pandas dataframe
sturm_data = pd.read_csv('SturmData.csv')

print('Head of sturm_data: ')
print(sturm_data.head())
print(f'\nNotice the presence of \'Nan\' values as well as the out of order \'fips\' code column.')

# swap rows 1 and 2 so that the data will line up with the geojson data later
temp1, temp2 = sturm_data.iloc[2].copy(), sturm_data.iloc[1].copy()
sturm_data.iloc[1], sturm_data.iloc[2] = temp1, temp2
print('\nHead of sturm_data after row swap: ')
print(sturm_data.head())

# take a look at data for FL, since according to info from dataset, we should display its entries as 'NaN'
fl = sturm_data.loc[sturm_data['state'] == 'FL']
print(f'\nFL data: \n{fl}')

# update FL values to 'NaN'
cols = ['debtfree', 'effectivemwpa', 'earnings', 'wills']
for col in cols:
    sturm_data.loc[sturm_data.state.eq('FL'), col] = np.nan
print(f'\nFL data updated to reflect \'NaN\' values per codebook recommendation:')
print(f'\n{sturm_data.iloc[7]}')

# prep state geo data for map
states = gpd.read_file('states_geo.json')
print(f'\nHead of states geopandas dataframe: ')
print(states.head())

# drop density column as it is not needed for this project
states.drop(columns= ['density'], inplace= True)
print(f'\nHead of states geodata after \'density\' column dropped: ')
print(states.head())

# drop states/territories contained in geodata that we know we do not need
drop_states = ['Alaska', 'Hawaii', 'District of Columbia', 'Puerto Rico']
for to_drop in drop_states:
    states.drop(states[states['name'] == to_drop].index, inplace= True)

# reindex geodataframe
states.reset_index(drop= True, inplace= True)

# add features to geopandas data
new_features = ['fips', 'debtfree', 'effectivemwpa', 'earnings', 'wills', 'soletrader']
for feature in new_features:
    states[new_features] = sturm_data[new_features]

print(f'\nHead of states geodata after cleanup and addition of features: ')
print(states.head())

# can uncomment and run this line of code if wanting to revisit and compare to sturm_data
#print(sturm_data.head())

# convert geopandas data back to json
states_json = states.to_json()

# this line gives us back the actual json object, not just the string representation
states2 = json.loads(states_json)

print('\nData is cleaned up. \nGeodata is set as a json object. \nMap set up starting.')
print('\n...\n')

# set up base layer
m = folium.Map(locations= [39.83, -98,58],   # location is set to continental center of the U.S.
                tiles= None,
                overlay= False,
                zoom_start= 4)

# set up tile layer
folium.TileLayer('CartoDB Positron',
                    overlay= True,
                    control= False).add_to(m)

# set up title
title_html = '''
            <h3 align="center" style="font-size:20px"><b>Married Women's Economic Rights Reform 1835-1920</b></h3>
            '''
m.get_root().html.add_child(folium.Element(title_html))

# set up choropleths for each feature
fg1 = folium.FeatureGroup(name= 'Separate Debts', overlay= False).add_to(m)
fg2 = folium.FeatureGroup(name= 'Property Rights', overlay= False).add_to(m)
fg3 = folium.FeatureGroup(name= 'Ownership of Wages/Earnings', overlay= False).add_to(m)
fg4 = folium.FeatureGroup(name= 'Ability to Write Wills', overlay= False).add_to(m)
fg5 = folium.FeatureGroup(name= 'Right to Sign Contracts/Engage in Business', overlay= False).add_to(m)

# since we are only displaying one legend, set up a year_span that will be stable across all choropleths
year_span = np.arange(1800.0, 1995.0, 15.0).tolist()

sep_debts = folium.Choropleth(geo_data= states2,
                                name= 'Separate Debts',
                                data= sturm_data,
                                columns= ['fips', 'debtfree'],
                                threshold_scale= year_span,
                                key_on= 'properties.fips',
                                fill_color= 'PuRd',
                                nan_fill_color= 'white',
                                fill_opacity= 0.7,
                                highlight= True,
                                control= True,
                                overlay= False,
                                legend_name= 'Year',
                                ).add_to(m)

prop_rights = folium.Choropleth(geo_data= states2,
                                name= 'Property Rights',
                                data= sturm_data,
                                columns= ['fips', 'effectivemwpa'],
                                threshold_scale= year_span,
                                key_on= 'properties.fips',
                                fill_color= 'PuRd',
                                nan_fill_color= 'white',
                                fill_opacity= 0.7,
                                highlight= True,
                                control= True,
                                overlay= False,
                                ).add_to(m)

earnings = folium.Choropleth(geo_data= states2,
                                name= 'Ownership of Wages/Earnings',
                                data= sturm_data,
                                columns= ['fips', 'earnings'],
                                threshold_scale= year_span,
                                key_on= 'properties.fips',
                                fill_color= 'PuRd',
                                nan_fill_color= 'white',
                                fill_opacity= 0.7,
                                highlight= True,
                                control= True,
                                overlay= False,
                                ).add_to(m)

wills = folium.Choropleth(geo_data= states2,
                            name= 'Ability to Write Wills',
                            data= sturm_data,
                            columns= ['fips', 'wills'],
                            threshold_scale= year_span,
                            key_on= 'properties.fips',
                            fill_color= 'PuRd',
                            nan_fill_color= 'white',
                            fill_opacity= 0.7,
                            highlight= True,
                            control= True,
                            overlay= False,
                            ).add_to(m)

contracts = folium.Choropleth(geo_data= states2,
                                name= 'Right to Sign Contracts/Engage in Business',
                                data= sturm_data,
                                columns= ['fips', 'soletrader'],
                                threshold_scale= year_span,
                                key_on= 'properties.fips',
                                fill_color= 'PuRd',
                                nan_fill_color= 'white',
                                fill_opacity= 0.7,
                                highlight= True,
                                control= True,
                                overlay= False,
                                ).add_to(m)

sep_debts.geojson.add_to(fg1)

# add tooltips
sep_debts.geojson.add_child(folium.features.GeoJsonTooltip(['name', 'debtfree'], aliases= ['State', 'Yr Protecting Property from Husband\'s Debts']))
prop_rights.geojson.add_child(folium.features.GeoJsonTooltip(['name', 'effectivemwpa'], aliases= ['State', 'Yr Control Over Separate Property Rights']))
earnings.geojson.add_child(folium.features.GeoJsonTooltip(['name', 'earnings'], aliases= ['State', 'Yr Ownership of Wages/Earnings']))
wills.geojson.add_child(folium.features.GeoJsonTooltip(['name', 'wills'], aliases= ['State', 'Yr Right to Write Wills w/out Husband Consent']))
contracts.geojson.add_child(folium.features.GeoJsonTooltip(['name', 'soletrader'], aliases= ['State', 'Yr Right to Engage in Business w/out Husband Consent']))

# supress other legends
for p in [prop_rights, earnings, wills, contracts]:
    for key in p._children:
        if key.startswith('color_map'):
            del(p._children[key])

# layer control toggle
folium.LayerControl(collapsed= True).add_to(m)

# save figure
save_file_name = 'mwrr_cmap.html'
m.save(save_file_name)
m

print(f'map saved as: \'{save_file_name}\'')
