import requests
import pickle
from pathlib import Path
import os

version = 'dev'


class RequestClient:
    def __init__(self):
        self.url = None
        self.dev_url = 'http://localhost:8000/api/'
        self.prod_url = 'https://dev2.selva-research.com/api/'
        if version == 'prod':
            self.url = self.prod_url
        else:
            self.url = self.dev_url

        # --> Session Data
        root_file_path = os.path.dirname(os.path.realpath(__file__))
        self.session_file_path = os.path.join(root_file_path, 'profile', 'session.pickle')
        # self.session = self.get_or_create_session()
        self.session = requests.session()

    def __del__(self):
        self.save_session()

    """
       _____               _             
      / ____|             (_)            
     | (___   ___  ___ ___ _  ___  _ __  
      \___ \ / _ \/ __/ __| |/ _ \| '_ \ 
      ____) |  __/\__ \__ \ | (_) | | | |
     |_____/ \___||___/___/_|\___/|_| |_|
    """


    def get_or_create_session(self):
        # --> 1. Check to see if session already exists
        session_file = Path(self.session_file_path)
        if not session_file.is_file():
            return requests.session()
        else:
            session_file_obj = session_file.open(mode='rb')
            return pickle.load(session_file_obj)

    def delete_session(self):
        session_file = Path(self.session_file_path)
        if session_file.is_file():
            print('--> DELETING SESSION FILE')
            os.remove(self.session_file_path)

    def save_session(self):
        session_file = Path(self.session_file_path)
        session_file_obj = session_file.open(mode='wb')
        pickle.dump(self.session, session_file_obj)

    """
      ______                     _       
     |  ____|                   | |      
     | |__  __  _____  ___ _   _| |_ ___ 
     |  __| \ \/ / _ \/ __| | | | __/ _ \
     | |____ >  <  __/ (__| |_| | ||  __/
     |______/_/\_\___|\___|\__,_|\__\___|                              
    """

    def execute(self, extension, reqData):
        request_url = self.url + extension
        result = None
        try:
            result = self.session.post(request_url, data=reqData)
        except Exception as e:
            print('--> CONNECTION ERROR', e)
            pass
        print('--> REQUEST RESULT:', type(result), result)
        return result.json()






