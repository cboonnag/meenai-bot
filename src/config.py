import json
import os 

os.chdir(os.path.dirname(os.path.abspath(__file__))) 

#open JSON file 
with open("../config.json") as f: 
    data = json.load(f)\
    
    CHANNEL_SECRET = data['line_config'][0]['CHANNEL_SECRET']
    CHANNEL_ACCESS_TOKEN = data['line_config'][0]['CHANNEL_ACCESS_TOKEN']
    BASIC_ID = data['line_config'][0]['BASIC_ID']

    USERNAME = data['db_config'][0]['USER']
    DATABASE_NAME = data['db_config'][0]['DATABASE']
    PASSWORD = data['db_config'][0]['PASSWORD']
    HOST = data['db_config'][0]['HOST']
    PORT = data['db_config'][0]['PORT']
    
    f.close()