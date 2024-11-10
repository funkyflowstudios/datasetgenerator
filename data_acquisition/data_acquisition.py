# data_acquisition/data_acquisition.py
from .public_datasets import load_public_dataset
from .social_media import collect_tweets
from .web_scraping import scrape_website
from .local_files import load_local_file

def acquire_data(source, **kwargs):
    if source == 'public_dataset':
        return load_public_dataset(kwargs['dataset_name'])
    elif source == 'social_media':
        return collect_tweets(kwargs['hashtag'])
    elif source == 'web_scraping':
        return scrape_website(kwargs['url'])
    elif source == 'local_files':
        return load_local_file(kwargs['file_path'])
