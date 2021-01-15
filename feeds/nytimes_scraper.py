import logging
from bs4 import BeautifulSoup
import requests
from models.item import Item


class NYTimesScraper():
    def __init__(self):
        logging.info('Initializing NY Times Scraper...')
        print('Initializing NY Times Scraper...')
        self.url = 'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml'

    def scrap(self):
        logging.info('Scraping NY Times feed...')
        print('Scraping NY Times feed...')
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
            guid=entry.find('guid').text,
            title=entry.find('title').text,
            link=entry.find('link').next_element,
            pub_date=entry.find('pubdate').text,
            description=entry.find('description').text.replace('\n', '').replace('\r', '').replace('\t', ''),
            creator=creator_str
        )
