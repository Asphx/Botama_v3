import requests


class IGDB():

    def __init__(self, api_key):
        self.api_key = str(api_key)
        self.url = 'https://api-v3.igdb.com/'
        self.headers = {'user-key':self.api_key}


    def call_endpoint(self, endpoint):
        endpoint = str(endpoint)
        if endpoint[-1] == '/':
            call_url = self.url + endpoint
        else:
            call_url = self.url + endpoint + '/'
        return call_url

    def games(self, gameName):
        ReqUrl = self.call_endpoint('games/' + gameName)
        res = requests.post(ReqUrl, headers=self.headers,
                            json="fields age_ratings")
        return res