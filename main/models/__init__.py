# -*- coding: utf-8 -*-

import datetime

from flask.ext.mongoengine import MongoEngine
db = MongoEngine()


class Font(db.Document):
    name = db.ListField()
    site_url = db.URLField()
    image_url = db.StringField()
    is_processed = db.BooleanField(default=False)
    score = db.IntField(default=1)
    created_at = db.DateTimeField(default=datetime.datetime.now)
    updated_at = db.DateTimeField(default=datetime.datetime.now)

    meta = {
    	'indexes': ['name']
    }
