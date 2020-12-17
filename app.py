import os
from dotenv import load_dotenv
from cls import MemberPress

load_dotenv()

mepr_robo = MemberPress(os.getenv('WEBSITE_URL'), os.getenv('MEPR_API_KEY'))
given_name = "Richard"
surname = "Morose"
email = "richard@domain.com"
membership = 10 ## the membership id
duration = 12 ## in months
robo = mepr_robo.get_member(email=email)

try:
    if robo['status']:
        new_transaction = mepr_robo.create_transaction(userid=robo['response'][0]['id'], membership=membership, duration=duration)
        # print('Created a new transaction')
    else:
        new_member = mepr_robo.create_member(email=email, fname=given_name, lname=surname)
        new_transaction = mepr_robo.create_transaction(userid=new_member['id'], membership=membership, duration=duration)
        # print('Created a new member & transaction')
except Exception as e:
    print(e)