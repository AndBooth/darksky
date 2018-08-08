
from azure.storage.blob import BlockBlobService
from datetime import datetime
import darksky

listdate = [1420070400]

for i in range(1,800):
    listdate.append(listdate[i-1] + 86400)

ACCOUNT_NAME = 'andrew1blob'
ACCOUNT_KEY = ''
blobaccount = BlockBlobService(account_name= ACCOUNT_NAME, account_key= ACCOUNT_KEY)
created = blobaccount.create_container(container_name = 'bordersweather')

print(created)

darkskyconn = darksky.darksky_api()

key = ''
latitude = 55.6
longitude = -2.8

for time in listdate:
    
    print(time)

    request = darkskyconn.build_historical_request(key, latitude, longitude, time = time)
    response = darkskyconn.send_darksky_request(request)

    if response == False:
        continue 

    output = darkskyconn.get_darksky_json_two(response)
    blobname = str(time) + ".json"

    blobaccount.create_blob_from_text('bordersweather', blob_name = blobname, text = output)