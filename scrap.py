from data.spreadsheet import ExcelWriter
from feeds.el_vigia_scrapper import ElVigiaScrapper
import click
import logging
import os
from datetime import datetime


LOG_DIR = 'logs'


# Configuration to save the logs into a file
if not os.path.isdir(LOG_DIR):
    os.mkdir(LOG_DIR)
logging.basicConfig(filename='{0}/{1}.log'.format(LOG_DIR, datetime.now().strftime('%Y%m%d_%H%M')), level=logging.DEBUG)


@click.group()
def cli():
    pass

@cli.group()
def extract():
    pass

@extract.command()
def vigia():
    click.echo('Scraping from El Vigia feed...')
    scraper = ElVigiaScrapper()
    writer = ExcelWriter('news.xlsx')
    writer.write_headers(headers=[
        'ID',
        'Title',
        'Link',
        'Updated',
        'Summary',
        'Content',
        'Author name',
        'Author URI',
        'Author Email'
    ])
    for entry in scraper.scrap():
        writer.write_model(entry)
    writer.close()

if __name__ == "__main__":
    cli()