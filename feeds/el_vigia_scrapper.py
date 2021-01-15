import logging
from bs4 import BeautifulSoup
import requests
from models.entry import Entry
from models.author import Author


class ElVigiaScrapper():
    def __init__(self):
        self.url = 'https://www.elvigia.net/rss/un_foto.html'

    def scrap(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.text, 'html.parser')
        entries = soup.find_all('entry')
        logging.info('Found {0} entries'.format(len(entries)))
        print('Found {0} entries'.format(len(entries)))
        for entry in entries:
            yield self.parse_entry(entry)
    
    def parse_entry(self, entry):
        return Entry(
            id=entry.find('id').text,
            title=entry.find('title').text,
            link=entry.find('link')['href'],
            updated=entry.find('updated').text,
            summary=entry.find('summary').text,
            content=entry.find('content').text.replace('\r', '').replace('\n', ''),
            author=Author(
                name=entry.find('author').find('name').text,
                uri=entry.find('author').find('uri').text,
                email=entry.find('author').find('email').text
            )
        )
