## IDEAS
1. MemberPress is a user friendly WordPress membership plugin.
2. MemberPress Plus/Pro comes with REST API which is quite useful to automate the creation of new members and transactions.
3. I am using a third party LMS website to accept all the payments and host 90% of my membership contents.
4. The remaining 10% membership contents is published on WordPress website.
5. This python script is written to automate the creation of new member and transaction.
6. Although there are numbers of REST API comes with MemberPress, I commonly use get_member, create_member and create_transaction only.

## LOGICS
***Notes: Check out app.py for reference***

**1. Basic**
```
if get_member(email):
    create_transaction(userid,membership)
else:
    create_member(email)
    create_transaction(userid,membership)
```

**2. Dynamic**
```
if get_items(member):
    create_item(transactions,data)
else:
    create_item(member,data)
    create_item(transactions,data)
```

## INSTRUCTIONS
**Step 1(a)**
```
Setup a virtual environment
```

**Step 1(b): pip install required packages**
```
pip install -r requirements.txt
```

**Step 2: Create a .env file and included the following environment variables to this file**
```
WEBSITE_URL=https://example.domain.com/wp-json/mp/v1
MEPR_API_KEY=yourMemberPressAPIKey
TRANS_PREFIX=mepr_trans
```

##### Notes:
*MEPR_API_KEY*
- If you have MemberPress Plus/Pro, you will need to first activate the Developer Tools.
    - MemberPress > Add On > Developer Tools
- Then, get the API key.
    - MemberPress > Developer > REST API

*TRANS_PREFIX*
- Can be very useful to track the transactions based on the event
- Example, you can set it to bfcm2020
- Later, you can easily filter the transactions for marketing analysis

## CHANGELOG
***Notes: Example can be found on app.py***

##### _version 1.1.0_
- Updated at: Dec 19, 2020 11.52PM GMT+8
- Add in Dynamic Functions
    - get_item
    - get_items
    - create_item
    - del_item
    - Supported routes: transctions and members

##### _version 1.0.0_
- Updated at: Dec 18, 2020 3.16AM GMT+8
- Static Functions
    - get_member
    - create_member
    - create_transactions