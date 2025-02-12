import logging

from urllib.parse import urljoin

from eromedownloader.config import BASE_URL
from .album_processor import process_album

logger = logging.getLogger(__name__)

def process_album_id(album_id, path, concurrent_requests_max, skip_images, skip_videos):
    try:
        # Construct the URL from the album_id
        album_url = urljoin(BASE_URL, album_id)
        
        logger.info(f"Processing album with ID: {album_id}")
        
        # Delegate to the shared function for album ID processing
        process_album(album_url, path, concurrent_requests_max, skip_images, skip_videos)
    
    except ValueError as e:
        logger.error(f"Validation error: \"{e}\"")
    except Exception as e:
        logger.error(f"Error during processing album ID: \"{e}\"")