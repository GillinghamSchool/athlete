from functools import wraps
from flask import session, url_for, redirect, abort

from athlete.alerts import set_alert


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "username" not in session:
            abort(403)
        return f(*args, **kwargs)
    return decorated_function


def keys_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "alert" not in session:
            set_alert()
        return f(*args, **kwargs)
    return decorated_function
