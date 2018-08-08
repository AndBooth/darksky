import json
import requests

class darksky_api:

    def build_historical_request(self, key, latitude, longitude, time):
        
        url_string = 'https://api.darksky.net/forecast/{0}/{1},{2},{3}'

        request = url_string.format(key, latitude, longitude, time)

        return request

    def build__request(self, key, latitude, longitude):
        
        url_string = 'https://api.darksky.net/forecast/{0}/{1},{2}'

        request = url_string.format(key, latitude, longitude)

        return request

    def send_darksky_request(self, request):

        response = requests.get(request)

        if response.status_code != 200:
            response = False

        return response

    def get_darksky_json(self, response):

        responsetext = response.text

        return json.loads(responsetext)

    def get_darksky_json_two(self, response):

        return(response.text)






# if __name__ == '__main__':
    
#     ds = darksky_api()

#     key = ''
#     latitude = 55.6
#     longitude = -2.8
#     time = 1532995200

#     request = ds.build_historical_request(key, latitude, longitude, time)
#     response = ds.send_darksky_request(request)

#     print(ds.get_darksky_json(response))
