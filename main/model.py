from run import db

class Font(db.Document):
    name = db.StringField()
    site_url = db.URLField()
    image_url = db.StringField()
    updated = db.DateTimeField()