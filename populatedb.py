from main.model import Font
from main.views import fetch_css
import requests
import datetime
import random
import string

SNAPSHOTTER_URL = "http://localhost:3000/"

def populate():
	with open('urls.txt', 'r') as f:
		urls = f.read().split('\n')[:10]

	for url in urls:
		print 'Processing', url, '...'
		font_string = fetch_css(url)
		if font_string:
			f = Font(name=font_string,
						site_url=url,
						image_url=get_snapshot_url(url),
						updated=datetime.datetime.now()
						)
			f.save()

def get_snapshot_url(url):
	lst = [random.choice(string.ascii_letters + string.digits) for n in xrange(12)]
	uniquid = "".join(lst)
	img = requests.get(SNAPSHOTTER_URL, params={'url' : url}).content
	with open('static/media/' + uniquid + '.jpg', 'w') as image:
		image.write(img)
	return '/static/media/' + uniquid + '.jpg'

if __name__ == '__main__':
	populate()