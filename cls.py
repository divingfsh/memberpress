import os
import json
import secrets
import numbers
import requests
from dotenv import load_dotenv
from datetime import datetime
from dateutil.relativedelta import relativedelta
from utils import check

load_dotenv()

class MemberPress:
    def __init__(self, tgt_url, api_key):
        self.tgt_url = tgt_url
        self.mepr_headers = {
            'MEMBERPRESS-API-KEY': api_key,
            'Content-Type': 'application/json'
        }


    def get_member(self, email):
        if check(email):
            url = f'{self.tgt_url}/wp-json/mp/v1/members?search={email}'
            r = requests.get(url, headers=self.mepr_headers)
            d = dict()
            d['status'] = len(r.json())
            d['response'] = r.json()
            return d
        else:
            raise Exception("Please provide a valid email.")
            

    def create_member(self, email, fname="John", lname="Doe", welcome_email=False):
        if check(email):
            url = f'{self.tgt_url}/wp-json/mp/v1/members'
            data = {
                'first_name': fname,
                'last_name': lname,
                'email': email,
                'username': email,
                'send_password_email': welcome_email,
            }
            r = requests.post(url=url, headers=self.mepr_headers, data=json.dumps(data))
            return r.json()
        else:
            raise Exception("Please provide a valid email.")
    

    def create_transaction(self, userid, membership, duration=0, send_receipt=False):
        if isinstance(membership, numbers.Number):
            x = datetime.now()
            created_at = x.strftime('%Y-%m-%d %H:%M:%S')
            y = x + relativedelta(months=int(duration))
            expires_at = y.strftime('%Y-%m-%d %H:%M:%S')

            prefix = os.getenv('TRANS_PREFIX') if os.getenv('TRANS_PREFIX') else "trans"
            b = secrets.token_hex(12)
            trans_num = f'{prefix}-{int(x.timestamp())}-{b}'
            
            trans_url = f'{self.tgt_url}/wp-json/mp/v1/transactions'
            data = {
                'member': userid,
                'membership': membership,
                'trans_num': trans_num,
                'status': 'complete',
                'created_at': created_at,
                'expires_at': expires_at,
                'send_receipt_email': send_receipt
            }

            r = requests.post(trans_url, headers=self.mepr_headers, data=json.dumps(data))
            return r.json()
        else:
            raise Exception("Please provide a valid membership")
