import re
import secrets
from datetime import datetime, timezone, timedelta
from dateutil.relativedelta import relativedelta
from data_templates import templates

def check(obj):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    return re.search(regex, obj)


def chars_generator():
    p = secrets.token_hex(12)
    return p


def datetime_generator(duration=1):
    x = datetime.now() ## can change to UTC time later
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


def validate_hs_property(action, data):
    if isinstance(data, list):
        try:
            if action == "create":
                for i in data:
                    if "email" in i.values():
                        return 1
                    else:
                        return 0
            else:
                return 1
        except:
            raise Exception("Error with data. List must have only -> {'property': 'email','value': email}")
    else:
        raise Exception("List/Array Only")


def hs_templates(data):
    d = dict()
    d["properties"] = data
    return d


## To customise the starting date, just modify year, month, day
def expiry_timestamp(duration, year=datetime.utcnow().year, month=datetime.utcnow().month, day=datetime.utcnow().day):
    start_dt = datetime(year,month,day)
    day = start_dt.day
    val_month = (start_dt.month + duration) % 12
    if val_month:
        exp_month = val_month
    else:
        exp_month = 12
    year = start_dt.year + (duration // 12)
    expired_at = round(datetime(year, exp_month, day, 00, 00, 00, tzinfo=timezone.utc).timestamp()) * 1000
    d = dict()
    d['expired_at'] = f"{year}-{exp_month}-{day} 00:00:00"
    d['expired_at_tmstp'] = expired_at
    return d