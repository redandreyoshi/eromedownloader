from urllib.parse import urlparse
import logging

from .album_processor import process_album
from eromedownloader.config import _HOST_NAME

logger = logging.getLogger(__name__)

def process_url(album_url, path, concurrent_requests_max, skip_images, skip_videos):
    try:
        if urlparse(album_url).hostname != _HOST_NAME:
            raise ValueError(f"URL hostname must be {_HOST_NAME}")

        logger.info(f"Scraping data for URL: \"{album_url}\"")
        
        process_album(album_url, path, concurrent_requests_max, skip_images, skip_videos)
    
    except ValueError as e:
        logger.error(f"Validation error: \"{e}\"")
    except Exception as e:
        logger.error(f"Error during processing URL: \"{e}\"")
