from hubspot import HubSpot
from utils import expiry_timestamp

hubspot = HubSpot()

email = "example@mail.com"
first_name = "example001"
new_email = "example2@mail.com"
new_first_name = "example002"
selected_property = "membership_expiry_date" ## Get the internal val of the property from HubSpot's account

findEmail = hubspot.get_contact_by_email(email=email)

##################
#                #
# Create Contact #
#                #
##################

# data = [
#     {"property": "email", "value": email},
#     {"property": "firstname", "value": first_name}
# ]
# p = hubspot.create_contact(arr=data)
# print(p)




##################
#                #
# Update Contact #
#                #
##################

# x = expiry_timestamp(duration=12)
# data2 = [
#     {"property": selected_property, "value": x["expired_at_tmstp"]},
# ]

# p2 = hubspot.update_property(email=email, arr=data2)
# print(p2)




##################
#                #
# Delete Contact #
#                #
##################


# if findEmail:
#     id = findEmail.json()["vid"]
#     x = hubspot.del_contact(id)
#     print(x)
# else:
#     print("Record not found")



############
#          #
# Combined #
#          #
############

if findEmail:
    exp_dt = expiry_timestamp(duration=16,year=2021,month=1,day=1)
    data2 = [
        {"property": selected_property, "value": exp_dt["expired_at_tmstp"]},
    ]
    req = hubspot.update_property(email=email, arr=data2)
    print(req)
    # print("Updated expiry date")
else:
    exp_dt = expiry_timestamp(duration=12)
    # 1: create properties list
    data = [
        {"property": "email", "value": email},
        {"property": "firstname", "value": first_name},
        {"property": selected_property, "value": exp_dt["expired_at_tmstp"]}
    ]

    # 2. Create contact
    req = hubspot.create_contact(arr=data)
    print(req)
    # print("Created contact && updated expiry date")
