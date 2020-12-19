import os
import json
import numbers
import requests
from dotenv import load_dotenv
from datetime import datetime
from dateutil.relativedelta import relativedelta
from utils import check, chars_generator, datetime_generator, keys_match

load_dotenv()

class MemberPress:
    def __init__(self, tgt_url, api_key):
        self.tgt_url = tgt_url
        self.mepr_headers = {
            'MEMBERPRESS-API-KEY': api_key,
            'Content-Type': 'application/json'
        }
        self.routes = ["transactions", "members"]


    def test_authentication(self):
        url = f'{self.tgt_url}/me'
        r = requests.get(url=url, headers=self.mepr_headers)
        return r.json()


    def get_member(self, email):
        if check(email):
            url = f'{self.tgt_url}/members?search={email}'
            r = requests.get(url, headers=self.mepr_headers)
            d = dict()
            d['status'] = len(r.json())
            d['response'] = r.json()
            return d
        else:
            raise Exception("Please provide a valid email.")
            

    def create_member(self, email, fname="John", lname="Doe", welcome_email=False, password_email=False):
        if check(email):
            url = f'{self.tgt_url}/members'
            data = {
                'first_name': fname,
                'last_name': lname,
                'email': email,
                'username': email,
                'send_welcome_email': welcome_email,
                'send_password_email': password_email
            }
            r = requests.post(url=url, headers=self.mepr_headers, data=json.dumps(data))
            return r.json()
        else:
            raise Exception("Please provide a valid email.")


    def create_transaction(self, userid, membership, duration=0, send_receipt=False):
        if isinstance(membership, numbers.Number):
            timing = datetime_generator()
            prefix = os.getenv('TRANS_PREFIX') if os.getenv('TRANS_PREFIX') else "trans"
            b = chars_generator()
            trans_num = f'{prefix}-{timing["created_at_tz"]}-{b}'
            
            trans_url = f'{self.tgt_url}/transactions'
            data = {
                'member': userid,
                'membership': membership,
                'trans_num': trans_num,
                'status': 'complete',
                'created_at': timing["created_at"],
                'expires_at': timing["expires_at"],
                'send_receipt_email': send_receipt
            }

            r = requests.post(trans_url, headers=self.mepr_headers, data=json.dumps(data))
            return r.json()
        else:
            raise Exception("Please provide a valid membership")

    ##############
    ## ADVANCED ##
    ##############

    def get_items(self, route, params):
        if isinstance(params, dict) and route in self.routes:
            url = f'{self.tgt_url}/{route}'
            r = requests.get(url, headers=self.mepr_headers, params=params)
            d = dict()
            d['status'] = len(r.json())
            d['response'] = r.json()
            return d
        else:
            raise Exception("Error")


    def get_item(self, route, id):
        if isinstance(id, numbers.Number) and route in self.routes:
            url = f'{self.tgt_url}/{route}/{id}'
            r = requests.get(url, headers=self.mepr_headers)
            return r.json()
        else:
            raise Exception("id must be integer")
    

    def create_item(self, route, data):
        if isinstance(data, dict) and route in self.routes:
            x = keys_match(data, route)
            if x:
                url = f'{self.tgt_url}/{route}'
                r = requests.post(url, headers=self.mepr_headers, data=json.dumps(data))
                return r.json()
            else:
                return Exception("Missing required key(s)")
        else:
            raise Exception("Error")


    def del_item(self, route, id):
        if isinstance(id, numbers.Number) and route in self.routes:
            url = f'{self.tgt_url}/{route}/{id}'
            r = requests.delete(url=url, headers=self.mepr_headers)
            return r.json()
        else:
            raise Exception("Error")