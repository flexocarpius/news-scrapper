import logging
from bs4 import BeautifulSoup
import requests
from models.item import Item


class ElDebateScraper():
    def __init__(self):
        logging.info('Initializing El Debate Scraper...')
        print('Initializing El Debate Scraper...')
        self.url = 'https://www.debate.com.mx/rss/feed.xml'

    def scrap(self):
        logging.info('Scraping El Debate feed...')
        print('Scraping El Debate feed...')
        page = requests.get(self.url)
        parsed = BeautifulSoup(page.text, 'html.parser')
        entries = parsed.find_all('item')
        logging.info('Found {0} entries.'.format(len(entries)))
        print('Found {0} entries.'.format(len(entries)))

        for entry in entries:
            parsed_entry = self.parse(entry)
            yield parsed_entry

    def parse(self, entry):
        media_text = ''
        media = entry.find('media:content')
        if media is not None:
            media_text = media.text

        return Item(
            guid=entry.find('guid').text,
            title=entry.find('title').text,
            link=entry.find('link').next_element,
            pub_date=entry.find('pubdate').text,
            description=entry.find('description').text.replace('\n', '').replace('\r', '').replace('\t', ''),
            creator=entry.find('dc:creator').text,
            content=BeautifulSoup(entry.find('content:encoded').text, 'html.parser').text.replace('\n', '').replace('\r', '').replace('\t', ''),
            media=media_text.replace('\n', '').replace('\r', '').replace('\t', ''),
        )
