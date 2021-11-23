import requests

version = 'dev'

class RequestClient:
    def __init__(self):
        self.url = None
        self.dev_url = 'http://localhost:8080/api/'
        self.prod_url = 'https://dev2.selva-research.com/api/'
        if version == 'prod':
            self.url = self.prod_url
        else:
            self.url = self.dev_url

    def execute(self, extension, reqData):
        request_url = self.url + extension
        result = None
        try:
            result = requests.post(request_url, data=reqData)
        except Exception as e:
            print('--> CONNECTION ERROR', e)
            pass
        return result
