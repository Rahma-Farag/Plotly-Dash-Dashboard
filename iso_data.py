import json

def get_world_iso():
    iso_dict = {}
    # Opening JSON file
    f = open('world-countries.json')
    
    # returns JSON object as
    # a dictionary
    data = json.load(f)
    
    # Iterating through the json
    # list
    for i in data['features']:
        iso_dict[i['properties']['name']] = i['id']
    
    # Closing file
    f.close()
    return iso_dict
