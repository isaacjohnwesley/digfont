# -*- coding: utf-8 -*-

from flask import render_template, request, abort, redirect, url_for

# For scraping
from BeautifulSoup import BeautifulSoup
import cssutils
import requests
import urlparse

from main.models import db, Font

# Helpers 
# Todo: Move to separate file

def fetch_fonts(css):
    sheet = cssutils.parseString(css)
    fonts = []
    for rule in sheet:
        if rule.type == rule.STYLE_RULE:

        # find property
            for property in rule.style:
                if property.name == 'font-family':
                    fonts.extend([font.strip() for font in (unicode(property.value)).split(", ")])
    return fonts


def convert_relative_url(url, site_url):
    chopped_url = site_url.split("//")
    if url.startswith('//'):
        scheme = chopped_url[0]
        return scheme + url
    elif url.startswith("http"):
        return url
    else:
        return site_url + url


def fetch_css(url, site_url):
    full_url = convert_relative_url(url, site_url)
    resp  = requests.get(full_url)
    return resp.content


def fetch_css_links(site):
    resp = requests.get(site)
    if resp.ok:
        soup = BeautifulSoup(resp.content)
        return soup.findAll('link', rel='stylesheet')
    raise Exception(u"Unable to process because of status code: {0}".format(resp.status_code))


def clean_fonts(fonts):
    # Todo: Move this to settings file
    EXCLUDE = ('sans-serif', 'serif', 'inherit', 'monospace', '!important', '"', "'")
    for rule in EXCLUDE:
        if rule in fonts:
            fonts.remove(rule)
    return fonts


def get_all_fonts(site):
    css_urls = fetch_css_links(site)
    font_set = set([])
    for url in css_urls:
        css = fetch_css(url['href'], site)
        font_set.update(clean_fonts(fetch_fonts(css)))
    return list(font_set)


# Route functions
def index(foundFont=None):
    return render_template('index.html')


def view_site(website):
    try:
        font = Font.objects.get(site_url__icontains=website)
        return render_template('website.html', font=font)
    except db.DoesNotExist:
        abort(404)


def addnew():
    if request.method == "POST":
        if u'website' in request.form:
            website = request.form['website']
            try:
                font = Font.objects.get(site_url=website)
            except db.DoesNotExist:
                font = Font(site_url=website)
                font.name = get_all_fonts(font.site_url)
                q = urlparse.urlparse(font.site_url)
                font.save()
        return redirect(url_for('view_site', website=q.hostname), 302)
    return render_template('addnew.html')


def view_font(name, page, per_page=10):
    try:
        # TODO: check all possible options like "Arial", arial "\"arail\""
        pagination = Font.objects.filter(name__icontains=name).paginate(page=page, per_page=per_page)
        return render_template('font.html', pagination=pagination, name=name)
    except db.DoesNotExist:
        abort(404)
