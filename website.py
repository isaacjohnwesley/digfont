# -*- coding: utf-8 -*-

import os

from main import create_app
from main.views import index, view_site, addnew, view_font, search

app = create_app()

# Add urls
app.add_url_rule('/', view_func=index, methods=['GET'])
app.add_url_rule('/<website>', view_func=view_site)
app.add_url_rule('/new', view_func=addnew, methods=["GET", "POST"])
app.add_url_rule('/font/<name>', view_func=view_font, methods=["GET"], defaults={'page': 1})
app.add_url_rule('/font/<name>/<int:page>', view_func=view_font, methods=["GET"])
app.add_url_rule('/search', view_func=search, methods=["POST"])


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug= True)
