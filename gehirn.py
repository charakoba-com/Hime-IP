import json
import config
import requests

def update(current_ip_val):

    records = []
    data = {
            "records": records,
            "enable_alias":False,
            "type":"A",
            "ttl":30,
            "name":"*"
            }
    record = {
            "address":current_ip_val
            }
    records.append(record)
    payload = json.dumps(data)
    
    res = requests.put(config.GEHIRN_URL, auth=(config.GEHIRN_API_KEY,config.GEHIRN_API_SECRET), data=payload)
