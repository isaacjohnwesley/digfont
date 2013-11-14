from run import db

#Fonts Model
class fonts(db.Document):
    font_name = db.StringField()
    site_url = db.StringField()
    image_url = db.StringField()
    last_update = db.DateTimeField()