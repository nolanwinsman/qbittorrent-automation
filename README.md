# qbittorrent-automation
---
 Scripts to Automate Qbittorrent Tasks

## Disclaimer

This script uses the qbittorrent-api to interface with qBittorrent. It is intended for legal and ethical uses only, and I do not promote or condone piracy or illegal downloading.

Please use this script responsibly and only for its intended purposes. Any illegal or unethical use of this script is strictly prohibited and not supported by the author.

## Installation

1. Clone the repo

```sh
git clone https://github.com/nolanwinsman/Roll20AverageRolls.git
```

2. Install Pip Modules.
There is only one module, qbittorrent-api. 

Below are two methods to install qbittorrent-api. They both achieve the same result.

```sh
pip install qbittorrent-api

pip install -r requirements.txt
```

## Setup

Both Python scripts require a few changes before use. The default credentials for the Qbittorrent web-ui are used for this script. If you use different credentials, you will need to change it in both files.

```py
    qbt_client = qbittorrentapi.Client(
        host='localhost',
        port=8080,
        username='admin',
        password='adminadmin'
    )
```

# Scripts

Currently, there are two main scripts

## set_location.py

If you are torrenting several different things and want to organize them into seperate folders, this script makes it much easier.

When you give a torrent a tag, let's say **movies** then run this script, it will set the location of the torrent to your movies folder.

This does require a bit of setup though. I store all my folders inside **/mnt/mount/** so it's configured to that folder.

The script uses a dictionary to map the tags to a folder. My current dictionary is setup like this where the keys are the tags and the values are the path it should be saves in.

```py
PATHS = {
        "movie": f"{DIR}/movies/",
        "show": f"{DIR}/shows/",
        "anime": f"{DIR}/anime/",
        "cartoon": f"{DIR}/cartoons/",
        "cartoon-movie": f"{DIR}/cartoon-movies/",
        "anime-movie": f"{DIR}/anime-movies/",
        "special": f"{DIR}/specials/",
        "documentary": f"{DIR}/documentaries/"
}
```

## set_tags.py

This is a simple script to quickly set tags to all your torrents. It is primarily useful for when you have a lot of torrents that you want to quickly assign tags for the set_location.py script.

## Contact

Nolan Winsman - [@Github](https://github.com/nolanwinsman) - nolanwinsman@gmail.com

Project Link: [https://github.com/nolanwinsman/qbittorrent-automation](https://github.com/nolanwinsman/qbittorrent-automation)

## Contributers

- nolanwinsman