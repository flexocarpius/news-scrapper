from feeds.usatoday_scraper import UsaTodayScraper
from feeds.nytimes_scraper import NYTimesScraper
from feeds.clarin_scraper import ClarinScraper
from feeds.debate_scraper import ElDebateScraper
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
    scrap_page(scraper=scraper, writer=writer, headers=[
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
    writer.close()

@extract.command()
def debate():
    click.echo('Scraping from El Debate feed...')
    scraper = ElDebateScraper()
    writer = ExcelWriter('debate.xlsx')
    scrap_page(scraper=scraper, writer=writer, headers=[
        'GUID',
        'Title',
        'Link',
        'Publication Date',
        'Description',
        'Creator',
        'Category',
        'Content',
        'Media'
    ])
    writer.close()

@extract.command()
def clarin():
    click.echo('Scraping from Clarin feed...')
    scraper = ClarinScraper()
    writer = ExcelWriter('clarin.xlsx')
    scrap_page(scraper=scraper, writer=writer, headers=[
        'GUID',
        'Title',
        'Link',
        'Publication Date',
        'Description',
        'Creator',
        'Category'
    ])
    writer.close()

@extract.command()
def nytimes():
    click.echo('Scraping from NY Times feed...')
    scraper = NYTimesScraper()
    writer = ExcelWriter('nytimes.xlsx')
    scrap_page(scraper=scraper, writer=writer, headers=[
        'GUID',
        'Title',
        'Link',
        'Publication Date',
        'Description',
        'Creator'
    ])
    writer.close()

@extract.command()
def usatoday():
    click.echo('Scraping from USA Today feed...')
    scraper = UsaTodayScraper()
    writer = ExcelWriter('usatoday.xlsx')
    scrap_page(scraper=scraper, writer=writer, headers=[
        'GUID',
        'Title',
        'Link',
        'Publication Date',
        'Description',
        'Creator'
    ])
    writer.close()

def scrap_page(scraper=None, writer=None, headers=None):
    writer.write_headers(headers=headers)
    for entry in scraper.scrap():
        writer.write_model(entry)

if __name__ == "__main__":
    cli()