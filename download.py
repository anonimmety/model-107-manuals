import logging
import os
import random
import time
from pathlib import Path

import requests
from bs4 import BeautifulSoup


base = "https://www.startekinfo.com/StarTek/outside/11883/PROGRAM"
start = "88560sl.html"
local_home = str(Path.home())
local_root = os.path.join(
    local_home,
    "Downloads",
    "mercedes"
)
# used to show progress when starting a new directory
prev = "" 

logging.basicConfig(level=logging.INFO)


if __name__ == "__main__":

    # download HTML page
    remote_url = "{}/{}".format(base, start)
    doc = requests.get(remote_url)

    # parse it
    soup = BeautifulSoup(doc.text, 'html.parser')

    # go through all links to PDF files
    for link in [ x for x in soup.find_all('a') if x.get('href').lower().endswith('.pdf') ]: # noqa

        # extract subdirectory and filename from remote dir structure
        # and use the same locally
        href = link.get('href')
        (remote_dir, local_file) = href.rsplit('/', 1)
        local_dir = os.path.join(
            local_root,
            remote_dir
        )

        # show progress when you start a new subdirectory
        if prev != remote_dir:
            logging.info("Downloading from {} into to {}".format(
                local_dir, 
                remote_dir
            ))
            prev = remote_dir

        # create target directory tree as needed
        try:
            os.makedirs(local_dir, 0o777, True)
        except:
            pass
        
        # download the file
        url = "{}/{}".format(base, href.lstrip("/"))
        logging.info("Downloading {}".format(url))
        r = requests.get(url, allow_redirects=True)
        # save it locally
        open(os.path.join(
            local_dir,
            local_file
        ), 'wb').write(r.content)

        # wait between requests because it's polite
        time.sleep(
            random.randrange(1, 5)
        )
