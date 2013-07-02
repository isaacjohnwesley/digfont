import os
from flask import Flask
#from flask.ext.assets import Environment
from main.views import main
from webassets.loaders import PythonLoader

app = Flask(__name__)
#assets = Environment(app)
app.register_blueprint(main, url_prefix='/')

app.config.from_pyfile('settings.py')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug= True)