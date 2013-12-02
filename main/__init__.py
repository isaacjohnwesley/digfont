# -*- coding: utf-8 -*-

import os

from flask import Flask
from flask.ext.assets import Environment , Bundle
from models import db
import main.views
import main.models


def create_app():
    app = Flask(__name__, instance_relative_config=True, static_folder='../static/', static_url_path='/static', template_folder='pages')
    app.config.from_pyfile('settings.py')
    assets = Environment(app)
    db.init_app(app)

    #Compress All Assets
    js = Bundle('javascripts/vendor/jquery-1.9.1.min.js',
                'javascripts/main.js',
                'javascripts/plugins.js',
                'javascripts/vendor/modernizr-2.6.2.min.js',
                'javascripts/vendor/Underscore-1.5.1.js',
                'javascripts/vendor/backbone-min.js',
                filters='jsmin', output='gen/packedjs.js')
    assets.register('js_all', js)

    css = Bundle('stylesheets/css/boilerplate_main.css',
                'stylesheets/css/normalize.css',
                'stylesheets/css/page.css',
                filters='cssmin', output='gen/packedcss.css')
    assets.register('css_all', css)
    return app
