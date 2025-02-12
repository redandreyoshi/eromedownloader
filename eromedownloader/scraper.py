import re
import requests

from bs4 import BeautifulSoup

from .config import _HOST_NAME, _USER_AGENT

def scrape_data(album_url, skip_images, skip_videos):         
    try:
        req = requests.get(album_url, headers=_USER_AGENT)
        req.raise_for_status()

    except requests.RequestException as e:
        raise ConnectionError(f"Request failed: {e}")

    soup = BeautifulSoup(req.content, "html.parser")

    album_id = _extract_album_id(album_url)

    title = soup.find("meta", property="og:title")
    album_title = title.get("content", "Unknown Album") if title else "Unknown Album"
    print(f"Scraping album title: {album_title}")

    urls = set()

    if not skip_images:
        image_urls = {img.get("data-src") for img in soup.find_all("img", class_="img-back") if img.get("data-src")}
        print(f"Found {len(image_urls)} Image(s)")
        urls.update(image_urls)

    if not skip_videos:
        video_urls = {video.get("src") for video in soup.find_all("source") if video.get("src")}
        print(f"Found {len(video_urls)} Video(s)")
        urls.update(video_urls)

    return album_id, album_title, list(urls)


def _extract_album_id(url: str) -> str:
    """Extract album ID from the URL (assuming it is the last part after a slash)."""
    match = re.search(r"/([^/]+)$", url)  # Matches the last part of the URL after the last "/"
    if match:
        return match.group(1)
    raise ValueError("Album ID not found in the URL")