"""
Data Acquisition Module

This module provides functions to acquire data from various sources:
- Web scraping
- Social media (X/Twitter and Reddit)
- Public datasets
- Local files

Each submodule contains specific functions for data acquisition from its respective source.
"""

from . import social_media
from . import local_files
from . import public_datasets
from . import web_scraping

__all__ = ['scrape_website', 'get_x_data', 'get_reddit_data', 'load_public_dataset', 'load_local_file']