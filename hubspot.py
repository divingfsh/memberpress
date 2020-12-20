import numbers
import os
from dotenv import load_dotenv
import requests
import json
from utils import check, hs_templates, validate_hs_property

load_dotenv()

class HubSpot:
    key = os.getenv('HUBSPOT_KEY')
    endpoint = os.getenv('HUBSPOT_ENDPOINT')
    headers = {'Content-Type': 'application/json'}
    params = {"hapikey": os.getenv('HUBSPOT_KEY')}


    def get_contact_by_email(self, email):
        if check(email):
            url = f"{self.endpoint}/email/{email}/profile"
            r = requests.get(url=url, params=self.params)
            return r
        else:
            raise Exception("Please provide a valid email address")


    def create_contact(self, arr):
        if validate_hs_property(action="create", data=arr):
            data = hs_templates(arr)
            url = f'{self.endpoint}/'
            r = requests.post(url=url, headers=self.headers, params=self.params, data=json.dumps(data))
            return r
        else:
            raise Exception("Email required")


    def update_property(self, email, arr):
        if check(email) and validate_hs_property(action="update", data=arr):
            data = hs_templates(arr)
            url = f'{self.endpoint}/email/{email}/profile'
            r = requests.post(url, headers=self.headers, params=self.params, data=json.dumps(data))
            return r
        else:
            raise Exception("Invalid Email")

    
    def del_contact(self, id):
        if isinstance(id, numbers.Number):
            url = f'{self.endpoint}/vid/{id}'
            r = requests.delete(url=url, params=self.params)
            return r
        else:
            raise Exception("id must be interger")
