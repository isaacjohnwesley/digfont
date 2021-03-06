# Set the path
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import mongoengine
from flask.ext.script import Manager, Server
from main import create_app
from main.views import index, view_site, addnew, view_font, search, get_all_fonts
from main.models import db, Font

app = create_app()
# Add urls
app.add_url_rule('/', view_func=index, methods=['GET'])
app.add_url_rule('/<website>', view_func=view_site)
app.add_url_rule('/new', view_func=addnew, methods=["GET", "POST"])
app.add_url_rule('/font/<name>', view_func=view_font, methods=["GET"], defaults={'page': 1})
app.add_url_rule('/font/<name>/<int:page>', view_func=view_font, methods=["GET"])
app.add_url_rule('/search', view_func=search, methods=["POST"])

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
				print("{0} already exists.".format(url))
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
