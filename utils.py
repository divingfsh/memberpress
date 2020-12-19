import re
import secrets
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from data_templates import templates

def check(obj):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    return re.search(regex, obj)


def chars_generator():
    p = secrets.token_hex(12)
    return p


def datetime_generator(duration=1):
    x = datetime.now()
    created_at = x.strftime('%Y-%m-%d %H:%M:%S')
    y = x + relativedelta(months=int(duration))
    expires_at = y.strftime('%Y-%m-%d %H:%M:%S')
    d = dict()
    d['created_at_tz'] = int(x.timestamp())
    d['created_at'] = created_at
    d['expires_at'] = expires_at
    return d


## confirm whether there are enough required keys before posting to database
def keys_match(obj, route):
    counter = 0
    compare_obj = obj.items()
    base_template = templates["create"][route]["required"]

    for i,j in compare_obj:
        for a in base_template:
            if i == a:
                counter += 1

    if counter == len(base_template):
        return 1
    else:
        return 0