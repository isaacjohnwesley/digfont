from flask import Blueprint, render_template
import urllib2


main = Blueprint('main', __name__, template_folder='pages')

url = 'https://gocardless.com/'

@main.route('/')
def index():

    req = urllib2.Request(url)
    req.headers['Range'] = 'bytes=%s-%s' % (500, 1024)

    contents = urllib2.urlopen(req).read()
    print contents

    return render_template('index.html')