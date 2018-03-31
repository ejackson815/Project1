import requests
import json
#Code Library:https://download.bls.gov/pub/time.series/le
#Dataset Database: https://download.bls.gov/pub/time.series/le/le.series

headers = {'Content-type': 'application/json'}
data = json.dumps({"seriesid": ['LEU0252888900'],"startyear":"2009", "endyear":"2012"})
p = requests.post('https://api.bls.gov/publicAPI/v1/timeseries/data/', data=data, headers=headers)
json_data = json.loads(p.text)
print(json_data)