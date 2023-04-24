import requests
import json

# replace this with your own API key
api_key = '28f8ac0c4ba5b1d57b24916d7a18121a'


# set the URL for the FRED API
url = 'https://api.stlouisfed.org/fred/series/observations?series_id=PAYEMS&api_key={0}&file_type=json'.format(api_key)

# make a request to the API and get the JSON response
response = requests.get(url)
json_data = json.loads(response.text)

# get the most recent observation and its release date
observation = json_data['observations'][-1]
release_date = observation['date']

# retrieve the data for the most recent release from the FRED API
release_url = 'https://api.stlouisfed.org/fred/release/series?series_id=PAYEMS&api_key={0}&file_type=json&release_date={1}'.format(api_key, release_date)
release_response = requests.get(release_url)
release_data = json.loads(release_response.text)

# get the forecast and actual values, if available
if 'releases' in release_data and len(release_data['releases']) > 0:
    release = release_data['releases'][0]
    forecast_value = None
    actual_value = None
    
    for release_value in release['release_values']:
        if release_value['value_type'] == 'Forecast':
            forecast_value = release_value['value']
        elif release_value['value_type'] == 'Actual':
            actual_value = release_value['value']
    
    # print the data for the most recent release
    print("Release Date:", release_date)
    print("Forecast Value:", forecast_value)
    print("Actual Value:", actual_value)
else:
    print("No release data available for the most recent observation.")





