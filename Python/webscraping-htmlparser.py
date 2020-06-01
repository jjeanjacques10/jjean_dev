# Author: Jean J Barros
# Github: https://github.com/jjeanjacques10/

# --- Fazendo Web Scraping com HTMLParser ---
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Tag HTML:", tag)

    def handle_data(self, data):
        print("Dados:", data)

parser = MyHTMLParser()
parser.feed('<html><head><title>Hello World</title></head></html>')