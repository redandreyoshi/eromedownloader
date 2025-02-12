import argparse

def get_arguments():
    parser = argparse.ArgumentParser()

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-u", "--url", 
        help="Album URL", 
        type=str
    )
    group.add_argument("-id", "--album-id", 
        help="Album ID instead of URL", 
        type=str
    )

    parser.add_argument("-p", "--path", 
        help="Save destination path", 
        type=str, 
        default=None
    )
    parser.add_argument("-c", "--concurrent-requests-max", 
        help="Max number of concurrent requests to be made", 
        type=int, 
        default=4
    )
    parser.add_argument("-si", "--skip-images", 
        action="store_true",
        help="Skip downloading images"
    )
    parser.add_argument("-sv", "--skip-videos", 
        action="store_true", 
        help="Skip downloading videos"
    )

    return parser.parse_args()
