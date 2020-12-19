templates = {
    "create": {
        "transactions": {
            "required": ["member", "membership"],
            "optional": ["trans_num", "amount", "total", "tax_amount", "tax_rate", "tax_desc", "coupon", "status", "response", "gateway", "subscription", "created_at", "expires_at", "send_welcome_email", "send_receipt_email"]
        },
        "members": {
            "required": ["email", "username"],
            "optional": ["first_name", "last_name", "send_welcome_email", "send_password_email"]
        }
    }
}

def template_create_trans(member, membership, trans_num, created_at, expires_at,
                        amount=float(0.00), total=float(0.00), tax_amount=float(0.00), tax_rate=float(0.00), coupon=0, 
                        status="complete", gateway="manual", subscription=0, send_welcome_email=False, send_receipt_email=False):
    d = dict()
    d["member"] = member
    d["membership"] = membership
    d["trans_num"] = trans_num
    d["amount"] = amount
    d["total"] = total
    d["tax_amount"] = tax_amount
    d["tax_rate"] = tax_rate
    d["coupon"] = coupon
    d["status"] = status
    d["gateway"] = gateway
    d["subscription"] = subscription
    d["created_at"] = created_at
    d["expires_at"] = expires_at
    d["send_welcome_email"] = send_welcome_email
    d["send_receipt_email"] = send_receipt_email
    return d

def template_create_member(email, username, first_name="Richard", last_name="Morose",
                        send_welcome_email=False, send_password_email=False):
    d = dict()
    d["email"] = email
    d["username"] = username
    d["first_name"] = first_name
    d["last_name"] = last_name
    d["send_welcome_email"] = send_welcome_email
    d["send_password_email"] = send_password_email
    return d