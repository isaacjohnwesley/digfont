# Set the path
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import mongoengine
from flask.ext.script import Manager, Server
from main import app, db
from main.views import get_all_fonts
from main.model import Font


manager = Manager(app)

@manager.command
def sync():
	for font in Font.objects.filter(is_processed=False):
		if not font.name and font.site_url:
			print(font.site_url)
			try:
				fonts = get_all_fonts(font.site_url)
			except Exception, e:
				print(e)
			if fonts:
				font.name = fonts
				font.is_processed = True
				try:
					font.save()
				except db.OperationFailure:
					pass
				print(u"Fetch fonts for site: {0}, {1}".format(font.site_url, fonts))


def yield_url(filename):
	with open(filename) as f:
		for line in f:
			# TODO: Check the line is url or not
			if line.startswith('http') or line.startswith('www'):
				yield line


@manager.command
def add_url_file(filename):
	try:
		for url in yield_url(filename):
			url = url.strip("\n")
			try:
				Font.objects.get(site_url=url)
			except db.DoesNotExist:
				font = Font(site_url=url)
				font.save()
				# TODO: Use logging library rather than print
				print("{0} url added.".format(url))
	except (IOError, mongoengine.errors.ValidationError) as e:
		print(e)


# Turn on debugger by default and reloader
manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = '0.0.0.0')
)


if __name__ == "__main__":
    manager.run()