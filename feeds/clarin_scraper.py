import logging
from bs4 import BeautifulSoup
import requests
from models.item import Item


class ClarinScraper():
    def __init__(self):
        logging.info('Initializing Clarin Scraper...')
        print('Initializing Clarin Scraper...')
        self.urls = [
            { 'link': 'https://www.clarin.com/rss/lo-ultimo/', 'category': 'Lo Ultimo' },
            { 'link': 'https://www.clarin.com/rss/politica/', 'category': 'Politica' },
            { 'link': 'https://www.clarin.com/rss/mundo/', 'category': 'Mundo' },
            { 'link': 'https://www.clarin.com/rss/tecnologia/', 'category': 'Tecnologia' },
            { 'link': 'https://www.clarin.com/rss/economia/', 'category': 'Economia' }
        ]

    def scrap(self):
        logging.info('Scraping Clarin feed...')
        print('Scraping Clarin feed...')
        for url in self.urls:
            yield from self.scrap_page(url)

    def scrap_page(self, data):
        url = data['link']
        category = data['category']
        logging.info('From url {0}...'.format(url))
        print('From url {0}...'.format(url))
        page = requests.get(url)
        parsed = BeautifulSoup(page.text, 'html.parser')
        entries = parsed.find_all('item')
        logging.info('Found {0} entries.'.format(len(entries)))
        print('Found {0} entries.'.format(len(entries)))

        for entry in entries:
            parsed_entry = self.parse(entry)
            parsed_entry.category = category
            yield parsed_entry

    def parse(self, entry):
        return Item(
            guid=entry.find('guid').text,
            title=entry.find('title').text,
            link=entry.find('link').next_element,
            pub_date=entry.find('pubdate').text,
            description=entry.find('description').text.replace('\n', '').replace('\r', '').replace('\t', ''),
            creator=entry.find('dc:creator').text
        )
