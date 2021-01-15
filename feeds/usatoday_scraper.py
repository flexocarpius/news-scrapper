import logging
from bs4 import BeautifulSoup
import requests
from models.item import Item


class UsaTodayScraper():
    def __init__(self):
        logging.info('Initializing USA Today Scraper...')
        print('Initializing USA Today Scraper...')
        self.url = 'http://rssfeeds.usatoday.com/usatoday-newstopstories&x=1'

    def scrap(self):
        logging.info('Scraping USA Today feed...')
        print('Scraping USA Today feed...')
        page = requests.get(self.url)
        parsed = BeautifulSoup(page.text, 'html.parser')
        entries = parsed.find_all('item')
        logging.info('Found {0} entries.'.format(len(entries)))
        print('Found {0} entries.'.format(len(entries)))

        for entry in entries:
            parsed_entry = self.parse(entry)
            yield parsed_entry

    def parse(self, entry):
        creator_str = ''
        creator=entry.find('dc:creator')
        if creator is not None:
            creator_str = creator.text

        return Item(
            guid=entry.find('guid').text.replace('\n', '').replace('\r', '').replace('\t', ''),
            title=entry.find('title').text,
            link=entry.find('feedburner:origlink').next_element.replace('\n', '').replace('\r', '').replace('\t', ''),
            pub_date=entry.find('pubdate').text,
            description=entry.find('description').text.replace('\n', '').replace('\r', '').replace('\t', ''),
            creator=creator_str
        )
