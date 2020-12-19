from datetime import date, datetime
import os
from utils import chars_generator, datetime_generator
from dotenv import load_dotenv
from cls import MemberPress
from data_templates import template_create_trans, template_create_member

load_dotenv()

mepr_robo = MemberPress(os.getenv('WEBSITE_URL'), os.getenv('MEPR_API_KEY'))
given_name = "Richard"
surname = "Morose"
email = "testing3@example.com"
membership = 10 ## the membership id
duration = 12 ## in months


#############################################
## Basic: Create member and/or transaction ##
#############################################

# robo = mepr_robo.get_member(email=email)
# try:
#     if robo['status']:
#         new_transaction = mepr_robo.create_transaction(userid=robo['response'][0]['id'], membership=membership, duration=duration)
#         # print('Created a new transaction')
#     else:
#         new_member = mepr_robo.create_member(email=email, fname=given_name, lname=surname, welcome_email=True, password_email=True)
#         new_transaction = mepr_robo.create_transaction(userid=new_member['id'], membership=membership, duration=duration)
#         # print('Created a new member & transaction')
# except Exception as e:
#     print(e)




##############
## Advanced ##
##############

params = {
    "search": email
}

robo2 = mepr_robo.get_items(route="members", params=params)

try:
    timing = datetime_generator(duration=duration)
    prefix = os.getenv("TRANS_PREFIX") if os.getenv("TRANS_PREFIX") else "trans"
    trans_num = f'{prefix}-{timing["created_at_tz"]}-{chars_generator()}'

    if robo2['status']:
        new_transaction = template_create_trans(member=robo2["response"][0]["id"],membership=membership,trans_num=trans_num,created_at=timing["created_at"],expires_at=timing["expires_at"])
        mepr_robo.create_item(route="transactions", data=new_transaction)
        # print('Created a new transaction')
    else:
        new_member = template_create_member(email=email, username=email, first_name=given_name, last_name=surname)
        create_member = mepr_robo.create_item(route="members", data=new_member)

        new_transaction = template_create_trans(member=create_member['id'],membership=10,trans_num=trans_num,created_at=timing["created_at"],expires_at=timing["expires_at"])
        mepr_robo.create_item(route="transactions", data=new_transaction)
        # print('Created a new member & transaction')
except Exception as e:
    print(e)





#####################
## Test Connection ##
#####################

# test = mepr_robo.test_authentication()
# print(test)





###################
#                 #
# Dynamic: Search #
#                 #
###################

#####################
## (1) Single Item ##
#####################

# search = mepr_robo.get_item(route="members", id=1)



########################
## (2) Multiple Items ##
########################

# items = {
#     "page": 1,
#     "per_page": 2,
#     "search": "testing@domain.com"
# }
# search2 = mepr_robo.get_items(route="members", params=items)






#####################
#                   #
#  Dynamic: Create  #
#                   #
#####################

################
## (1) Member ##
################

# data = {
#     "email": email,
#     "username": email,
#     "first_name": given_name,
#     "last_name": surname
# }
# create0 = mepr_robo.create_item(route="members", data=data)
# print(create0)


##############################
## (2) Transaction (Manual) ##
##############################

# timing = datetime_generator(12)
# prefix = os.getenv('TRANS_PREFIX') if os.getenv('TRANS_PREFIX') else "trans"

# data = {
#     'member': 666,
#     'membership': 10,
#     'trans_num': f'{prefix}-{timing["created_at_tz"]}-{chars_generator()}',
#     'status': 'complete',
#     'created_at': timing["created_at"],
#     'expires_at': timing["expires_at"],
#     'send_receipt_email': False
# }

# create2 = mepr_robo.create_item(route="transactions", data=data)
# print(create2)


################################
## (2) Transaction (Template) ##
################################

# timing = datetime_generator(12)
# prefix = os.getenv("TRANS_PREFIX") if os.getenv("TRANS_PREFIX") else "trans"
# trans_num = f'{prefix}-{timing["created_at_tz"]}-{chars_generator()}'

# data = template_create_trans(member=666,membership=10,trans_num=trans_num,created_at=timing["created_at"],expires_at=timing["expires_at"])
# create3 = mepr_robo.create_item(route="transactions", data=data)
# print(create3)





###################
#                 #
# Dynamic: Delete #
#                 #
###################

# rm_data = mepr_robo.del_item(route="transactions",id=148)
# print(rm_data)