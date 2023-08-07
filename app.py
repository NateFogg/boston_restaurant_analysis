import requests
import json
import pandas as pd
from flatten_json import flatten


TOKEN = ''

url = 'https://api.yelp.com/v3/businesses/search?location=Allston%2C%20Boston&term=restaurants&sort_by=distance&limit=50&offset=0'

headers = {
    'accept': 'application/json',
    'Authorization': 'Bearer ' + TOKEN
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    json_data = response.json()
else:
    # Handle the API request error here
    print('Failed to retrieve data from the API.')
    json_data = None

if json_data:
    businesses = pd.DataFrame()

    for dict in json_data['businesses']:
        print(dict)
        # flatten the data
        bus_row = pd.json_normalize(dict, 'categories', ['id', 'alias', 'name', 'image_url', 'is_closed', 'url', 'review_count',
                                                          'rating', 'coordinates', 'transactions', 'price', 'location', 'phone',
                                                            'display_phone', 'distance']) 
        

        # append the new row to data frame
        businesses = pd.concat([businesses, bus_row], ignore_index=True)

    print(businesses)

    #df_nested_list = pd.json_normalize(json_data['businesses'], record_path='categories')
    #print(df_nested_list.iloc[0])

    #flat_df = pd.DataFrame(flatten(json_data['businesses']))
    #print(flat_df.iloc[0])





['Allston', 'Brighton', 'Arlington Center', 'Arlington Heights', 'Back Bay' , 'Beacon Hill',
  'Brookline Village', 'Central Square', 'Charlestown', 'Chinatown', 'Coolidge Corner', 'Davis Square',
  'Dorchester', 'Downtown', 'Huron Village' , 'Hyde Park', 'Inman Square', 'Jamaica Plain', 'Kendall Square', 'MIT'
  'Leather District', 'Mattapan', 'Mattapan Square', 'Mission Hill', 'North Cambridge', 'North End', 'Porter Square',
  'Roslindale', 'Dudley Square', 'East Arlington', 'East Boston', 'East Cambridge', 'Egleston Square', 'Fenway', 'Fields Corner'
  'Financial District', 'Harvard Square', 'Roslindale Village', 'South Boston', 'South End', 'Teele Square', 'Uphams Corner', 
  'Waterfront', 'West End', 'West Roxbury', 'West Roxbury Center']