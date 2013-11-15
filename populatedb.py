from main.model import Font
from main.views import fetch_css
import requests
import datetime

SNAPSHOTTER_URL = "http://screenshoter.herokuapp.com/takescreenshot/"

def populate():
	with open('urls.txt', 'r') as f:
		urls = f.read().split('\n')[:10]

	for url in urls:
		print 'Processing', url, '...'
		font_string = fetch_css(url)
		if font_string:
			f = Font(name=font_string,
						site_url=url,
						image_url=get_snapshot(url),
						updated=datetime.datetime.now()
						)
			f.save()

def get_snapshot(url):
	return requests.get(SNAPSHOTTER_URL + '?url=' + url).content.replace('\n', '')

if __name__ == '__main__':
	populate()