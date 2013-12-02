import lxml.html as parser
import requests
import sys

URL = "http://webcreme.com/page/"
WEBCREME_MAGIC_CLASS = "image"

def get_html(url):
    return requests.get(url).content

def get_links(html):
    tree = parser.fromstring(html)
    elements = tree.find_class(WEBCREME_MAGIC_CLASS)
    
    links = []
    
    for element in elements:
        links.append(element.getchildren()[0].attrib['href'])
    return links

def grab_from_webcreme():
	with open('urls.txt', 'w') as f:
		for i in range(1, 515):
			print 'Getting page', i
			page = get_html(URL + str(i))
			links = get_links(page)
			f.write('\n'.join(links))
			f.write('\n')

def grab_fonts(filename):
	pass

if __name__ == '__main__':
	if sys.argv[1] == 'scrape':
		grab_from_webcreme()
	elif sys.argv[1] == 'grab':
		grab_fonts()
	elif sys.argv[1] == 'grabfonts':