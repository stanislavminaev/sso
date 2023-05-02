from os import environ


SECRET = environ.get("JWT_SECRET", "")
AD_SERVER = environ.get("AD_SERVER", "")
