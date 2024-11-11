"""
Data Acquisition Module

This module provides functions to acquire data from various sources:
- Web scraping
- Social media (X/Twitter and Reddit)
- Public datasets
- Local files

Each submodule contains specific functions for data acquisition from its respective source.
"""

from .web_scraping import scrape_website
from .social_media import fetch_x_data, fetch_reddit_data
from .public_datasets import load_public_dataset
from .local_files import load_local_file

__all__ = ['scrape_website', 'get_x_data', 'get_reddit_data', 'load_public_dataset', 'load_local_file']