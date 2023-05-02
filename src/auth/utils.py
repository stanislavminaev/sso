from jwt import decode, encode, InvalidSignatureError
from fastapi import Cookie, Form
from ldap3 import Connection
from ldap3.core.exceptions import LDAPException

from auth.constants import SECRET, AD_SERVER


def check_login_error(username: str = Form(None), password: str = Form(None)):
    errors = []

    if username is None:
        errors.append("Укажите логин")

    if password is None:
        errors.append("Укажите пароль")

    if username and password:
        try:
            with Connection(server=AD_SERVER, user=username, password=password) as conn:
                return errors
        except LDAPException:
            errors.append("Неверный логин/пароль")
    return errors


def create_token(username: str = Form()):
    return encode({"username": username}, SECRET, algorithm="HS256")


def check_token(sso_auth: str = Cookie(None)):
    if not sso_auth:
        return False

    try:
        payload = decode(jwt=sso_auth, key=SECRET, algorithms=["HS256"])
        return payload.get("username")
    except InvalidSignatureError:
        return ""
