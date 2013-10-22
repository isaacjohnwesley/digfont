from flask import Blueprint, render_template, request

# For scraping
import urllib2
import httplib
from BeautifulSoup import BeautifulSoup
from urlparse import urlparse
import cssutils

main = Blueprint('main', __name__, template_folder='pages')

fonts_junk = []
newlist = []


@main.route('/')
def index():

    data = fetch_css("http://walletkit.com/")
    return render_template('index.html')


@main.route('/search', methods=['POST'])
def search(data=None):

    if request.method == 'POST':
        searchq = request.form['searchquery']

    return render_template('search_results.html', data=searchq)


@main.route('/addnew')
def addnew():

    return render_template('addnew.html')


def fetch_css(url):

    try:
        response = urllib2.urlopen(url)
        html_data = response.read()
        response.close()

        soup = BeautifulSoup(''.join(html_data))

        # Find all external style sheet references
        ext_styles = soup.findAll('link', rel="stylesheet")

        # Loop through all the found ext stylesheet, extract the relative URL,
        # append the base URL, and fetch all content in that URL
        # first, check to see if there are any results within ext_styles.
        ext_css_data = ''
        ext_found = 1
        if len(ext_styles) != 0:
            for i in ext_styles:
                # Check to see if the href to css style is absolute or relative
                o = urlparse(i['href'])
                if o.scheme == "":
                    css_url = url + '/' + i['href']  # added "/" just in case
                    print "Found external stylesheet: " + css_url
                else:
                    css_url = i['href']
                    print "Found external stylesheet: " + css_url

                response = urllib2.urlopen(css_url)
                ext_css_data += response.read()
                response.close()
        else:
            ext_found = 0
            print "No external stylesheets found"
        all_css_data = unicode(ext_css_data, errors='ignore')

        sheet = cssutils.parseString(all_css_data)

        # CSS PARSING ##
        for rule in sheet:
            if rule.type == rule.STYLE_RULE:

                # find property
                for property in rule.style:
                    if property.name == 'font-family':
                        fonts_junk.append(str(property.value))

                        # remove duplicate entries
                        for i in fonts_junk:
                            if i not in newlist:
                                newlist.append(i)

        return newlist

    except:
        return "", 0, 0
