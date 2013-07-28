import os
from flask import Flask
from flask.ext.assets import Environment , Bundle
from main.views import main
from webassets.loaders import PythonLoader

app = Flask(__name__)
assets = Environment(app)

app.register_blueprint(main)

#Compress All Assets
js = Bundle('javascripts/main.js',
            'javascripts/plugins.js',
            'javascripts/vendor/jquery-1.9.1.min.js',
            'javascripts/vendor/modernizr-2.6.2.min.js',

            filters='jsmin', output='gen/packedjs.js')
assets.register('js_all', js)

css = Bundle('stylesheets/css/main.css',
            'stylesheets/css/normalize.css',
            filters='sass,less,cssmin', output='gen/packedcss.css')
assets.register('css_all', css)


#App Configuration
app.config.from_pyfile('settings.py')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug= True)