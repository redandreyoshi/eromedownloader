import re
import string
from pathlib import Path

def get_save_dir(parent: str | None, album_title: str, album_id: str) -> Path:
    if not album_title:
        raise ValueError("Album title cannot be empty.")
    
    album_title = _sanitize_album_title(album_title)

    print(f"Album ID: {album_id}")
    print(f"Album Title: {album_title}")

    save_dir = Path(parent or Path.cwd(), 'downloads', album_title)

    if save_dir.exists():
        save_dir = _get_unique_save_dir(save_dir)

    save_dir.mkdir(parents=True, exist_ok=True)

    return save_dir

def _sanitize_album_title(album_title: str) -> str:
    """Sanitize the album title by removing or replacing invalid characters."""
    invalid_chars = set(r'\/:*?"<>|')

    sanitized_title = ''.join(c if c not in invalid_chars else '_' for c in album_title)

    sanitized_title = sanitized_title[:255]

    return sanitized_title

def _get_unique_save_dir(save_dir: Path) -> Path:
    """Iteratively find a unique directory name by appending a counter."""
    counter = 1
    while save_dir.exists():
        save_dir = save_dir.with_name(f"{save_dir.name}({counter})")
        counter += 1
    return save_dir
