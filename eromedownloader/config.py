
_USER_AGENT = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

_HOST_NAME = "www.erome.com"
BASE_URL = "https://www.erome.com/a/"

DEFAULT_HEADERS = {
    "Referer": _HOST_NAME,
    **_USER_AGENT
}
