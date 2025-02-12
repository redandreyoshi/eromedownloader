import asyncio
import logging

from .downloader import download_media
from .save_manager import get_save_dir
from .scraper import scrape_data

logger = logging.getLogger(__name__)

def process_album(album_url, path, concurrent_requests_max, skip_images, skip_videos):
    try:
        album_id, album_title, urls = scrape_data(album_url, skip_images, skip_videos)
        
        logger.info(f"Album ID: {album_id}, Title: \"{album_title}\"")
        
        save_dir = get_save_dir(path, album_title, album_id)
        
        logger.info(f"Downloading media for album \"{album_title}\"")
        asyncio.run(download_media(urls, album_url, concurrent_requests_max, save_dir))
    
    except ValueError as e:
        logger.error(f"Validation error: \"{e}\"")
    except Exception as e:
        logger.error(f"Error during processing album: \"{e}\"")
