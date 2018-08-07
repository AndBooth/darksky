
import requests
import pandas as pd
import json





outputjson = json.loads(test.text)

with open('test2.json', 'w') as outfile:
    json.dump(outputjson, outfile)

