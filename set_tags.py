# Script that enables you to quickly apply torrent tags to any torrents
# that do not have tags

# Author : Nolan Winsman
# Date : 10-17-2022
import os

import qbittorrentapi # pip install qbittorrent-api

# documentation to API
# https://qbittorrent-api.readthedocs.io/en/latest/introduction.html

# list of possible tags
TAGS = [
        "movie",
        "show",
        "anime",
        "cartoon",
        "cartoon-movie",
        "anime-movie",
]



def which_tag():
    s = f"\nType the correct number for which tag you want to apply to this torrent\n"
    for i, elem in enumerate(TAGS):
        s += f"{i} for {elem}\n"
    return s

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():

    # instantiate a Client using the appropriate WebUI configuration
    # change information to fit your login
    qbt_client = qbittorrentapi.Client(
        host='localhost',
        port=8080,
        username='admin',
        password='adminadmin'
    )

    # the Client will automatically acquire/maintain a logged in state in line with any request.
    # therefore, this is not necessary; however, you many want to test the provided login credentials.
    try:
        qbt_client.auth_log_in()
    except qbittorrentapi.LoginFailed as e:
        print(e)


    tag_msg = which_tag()

    # retrieve all torrents and set their download folder to the corresponding tag
    for torrent in qbt_client.torrents_info():

        # no torrent tag
        if len(torrent.tags) == 0:
            clear_screen()
            print(torrent.name)
            print(tag_msg)
            
            # cast the input to an int
            try:
                resp = int(input())
            except ValueError:
                continue

            # user input valid response
            if resp >= 0 and resp < len(TAGS):
                tag = TAGS[resp] # the tag corres
                print(f"Setting tag to {TAGS[resp]}")
                torrent.add_tags(tags=tag)


if __name__ == "__main__":
    main()
