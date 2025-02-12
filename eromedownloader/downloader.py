import aiohttp
import asyncio
import aiofiles
from pathlib import Path
from tqdm import tqdm
from urllib.parse import urlparse
from typing import Iterable
import logging
import random
import time

from .config import _USER_AGENT, DEFAULT_HEADERS

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

MAX_RETRIES = 3
RETRY_BACKOFF = 1  # seconds

async def download_media(urls: Iterable[str], album_url: str, concurrent_requests_max: int, dst_dir: Path):
    """Download media from a list of URLs with a limit on concurrent requests."""
    semaphore = asyncio.Semaphore(concurrent_requests_max)

    async with aiohttp.ClientSession(headers=DEFAULT_HEADERS) as session:
        tasks = []
        for url in urls:
            task = asyncio.create_task(_download_url_content(url, dst_dir, session, semaphore))
            tasks.append(task)
        
        await asyncio.gather(*tasks)

async def _download_url_content(url: str, dst_dir: Path, session: aiohttp.ClientSession, semaphore: asyncio.Semaphore):
    """Download a single URL's content to the specified destination directory."""
    file_name = Path(urlparse(url).path).name
    file_path = dst_dir / file_name
    CHUNK_SIZE = 1024

    for attempt in range(MAX_RETRIES):
        try:
            async with semaphore, session.get(url, timeout=30) as response:
                if response.ok:
                    logger.info(f"Downloading {file_name}...")

                    # Display progress bar during download
                    total_size = int(response.headers.get("content-length", 0))
                    pbar = tqdm(
                        desc=f"[+] Downloading {file_name}",
                        total=total_size,
                        unit="iB",
                        unit_scale=True,
                        unit_divisor=CHUNK_SIZE,
                        colour="green"
                    )

                    async with aiofiles.open(file_path, "wb") as f:
                        async for chunk in response.content.iter_chunked(CHUNK_SIZE):
                            await f.write(chunk)
                            pbar.update(len(chunk))

                    logger.info(f"Download complete: {file_name}")
                    return  # Exit if download is successful
                else:
                    raise ValueError(f"Failed to download {url} with status code {response.status}")
        except (aiohttp.ClientError, asyncio.TimeoutError, ValueError) as e:
            # Retry on error with backoff
            if attempt < MAX_RETRIES - 1:
                wait_time = RETRY_BACKOFF * (2 ** attempt) + random.uniform(0, 1)
                logger.warning(f"\nError downloading {file_name}: {e}. Retrying in {wait_time:.2f}s...")
                await asyncio.sleep(wait_time)
            else:
                logger.error(f"Failed to download {file_name} after {MAX_RETRIES} attempts. Skipping.")
                break  # Max retries reached, skip to the next file

