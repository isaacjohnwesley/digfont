import peewee

#Database configurations
DATABASE_NAME = '' # Please use your own local database name
DATABASE_USER = '' # Please use your own local user name
DATABASE_PASSWORD = '' # Please use your own local user name
DATABASE_HOST = '' # Please use your own host
DATABASE_PORT = '' # Please use your own port

#Import secrets from the file the world should not see :P
try:
   from config import *
except ImportError:
   pass

#Database connection
mysql_db = peewee.MySQLDatabase(config["DATABASE_NAME"] , host=config["DATABASE_HOST"] , port=config["DATABASE_PORT"] , user=config["DATABASE_USER"] , passwd=config["DATABASE_PASSWORD"])

#Fonts Model
class fonts(peewee.Model):
    font_name = peewee.CharField()
    site_url = peewee.CharField()
    image_url = peewee.CharField()
    last_update = peewee.DateTimeField()

    class Meta:
        database = mysql_db

#connect database
mysql_db.connect()

#create table if not exist
fonts.create_table(True)