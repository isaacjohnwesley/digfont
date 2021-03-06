"""
Flask application settings.
"""
import os


DEBUG = True

# Output un-merged files in debug mode.
#ASSETS_DEBUG = DEBUG

SECRET_KEY = os.environ.get('SECRET_KEY', None)
MY_VAR = os.environ.get('MY_VAR', None)

#: Mongodb settings
MONGODB_SETTINGS = {'DB' : 'digfont'}

#: CSRF key
SECRET_KEY = "dig.font.s3cr3t"
