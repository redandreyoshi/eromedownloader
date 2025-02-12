# eromedownloader

A Python-based downloader for erome.com, allowing users to download media from albums on the platform.

## Features

- Download images and videos from erome.com albums.
- Support for concurrent requests to speed up downloads.
- Customizable options for skipping images or videos.

## Installation

### Prerequisites

- Python 3.11+ (recommended version).
- Poetry (for dependency management and packaging).

### 1. Install Dependencies

Follow the installation instructions from the [official Poetry website](https://python-poetry.org/docs/#installation).

On Linux/macOS, you can use the following command:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

On Windows, you can follow the [installation guide](https://python-poetry.org/docs/#installation) for respective steps.

### 2. Install Project dependencies
Once Poetry is installed, run the following command to install all project dependencies:

```bash
poetry install
```

This will create a virtual environment and install all the necessary packages specified in the `pyproject.toml` file, including `beautifulsoup4`, `requests`, `aiohttp`, and others.

### 3. Running the Application

After the environment is set up, you can run the application with:

```bash
poetry run python main.py --url <your_album_url> --path <your_save_path> --concurrent-requests-max <number> --skip-images <True/False> --skip-videos <True/False>
```
or
```bash
poetry run python main.py --album-id <your_album_id> --path <your_save_path> --concurrent-requests-max <number> --skip-images <True/False> --skip-videos <True/False>
```


### 4. Generating a `requirements.txt` (Optional)

If you need to generate a `requirements.txt` file (for example, for compatibility reasons), you can export it with:

```bash
poetry export --without-hashes --format=requirements.txt > requirements.txt
```

### 5. Directory Structure

```graphql
eromedownloader/
├── eromedownloader/                  # Main source folder
│   ├── __init__.py
│   ├── __main__.py                  # Entry point for the command line tool
│   ├── config.py                    # Configuration settings (e.g., user agent, default paths)
│   ├── downloader.py                # Handles downloading of media
│   ├── scraper.py                   # Scraping logic for extracting media URLs
│   ├── save_manager.py              # Manages the save directory and file saving
│   ├── url_processor.py             # Processes URLs for scraping
│   ├── album_id_processor.py        # Processes album IDs for scraping
│   └── logger.py                    # Logger setup for handling log messages
├── pyproject.toml                   # Poetry configuration
├── README.md                        # Project documentation
└── poetry.lock                      # Dependency lock file

```
- `eromedownloader/`: Contains all the source code files.
- `__main__.py`: This is the entry point for the command-line interface (CLI). It allows you to run the tool using python -m eromedownloader.
- `config.py`: Contains configuration details like the user agent and default save paths.
- `downloader.py`: Handles the actual downloading of media files from the URLs.
- `scraper.py`: Contains the scraping logic for extracting image and video URLs from the album.
- `save_manager.py`: Manages the directory where media is saved, handling path generation and folder creation.
- `url_processor.py`: Responsible for processing albums by URL.
- `album_id_processor.py`: Responsible for processing albums by album ID.
- `logger.py`: Configures the logger used across the app for consistent log management.
- `pyproject.toml`: The Poetry configuration file containing package and dependency details.
- `poetry.lock`: The file that locks the dependencies to specific versions for consistency.

## Notes
- **Dependencies:** The project uses aiohttp, beautifulsoup4, and other libraries. Poetry will automatically handle these dependencies when you run poetry install.
- **Concurrency:** The program allows setting the maximum number of concurrent requests for downloading media files. The default is 4, but you can change it using the --concurrent-requests-max argument.
- **Skipping Media:** You can choose to skip downloading images or videos with the `--skip-images` and `--skip-videos` flags.

## Usage
Once the package is installed, you can use it as a CLI tool to download media from erome.com.

### 1. Using URL
To download an album using its URL, run:

```bash
python -m eromedownloader --url <album_url>
```

This will scrape and download all the media from the specified album.

### 2. Using Album ID
You can also provide the album ID directly instead of the URL. For example:

```bash
python -m eromedownloader --album_id <album_id>
```

Where `<album_id>` is the ID of the album you want to download.

### Options
- `-u, --url <album_url>`: The URL of the album you want to download.
- `-id --album_id <album_id>`: The ID of the album you want to download.
- `-p --path <path>`: (Optional) Specify the download path. Default is a "downloads" folder in the current directory.
- `-c --concurrent_requests_max <number>`: (Optional) Max concurrent requests. Default is 5.
- `-si --skip_images`: (Optional) Skip downloading images.
- `-sv --skip_videos`: (Optional) Skip downloading videos.
