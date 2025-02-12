import logging
from .args import get_arguments
from .url_processor import process_url
from .id_processor import process_album_id

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    args = get_arguments()

    logger.info(f"Save Path: {args.path}")
    logger.info(f"Max Concurrent Requests: {args.concurrent_requests_max}")
    logger.info(f"Skip Images: {args.skip_images}")
    logger.info(f"Skip Videos: {args.skip_videos}")

    try:
        if args.url:
            logger.info(f"Processing album from URL: {args.url}")
            process_url(args.url, args.path, args.concurrent_requests_max, args.skip_images, args.skip_videos)

        elif args.album_id:
            logger.info(f"Processing album with ID: {args.album_id}")
            process_album_id(args.album_id, args.path, args.concurrent_requests_max, args.skip_images, args.skip_videos)
        else:
            logger.error("No URL or album ID provided. Exiting.")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        exit(1)

if __name__ == "__main__":
    main()
