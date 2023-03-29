import os
import requests
from bs4 import BeautifulSoup

# replace the username with the user you want to download the repls from
username = "codewithharry"

# create a directory to store the repls
os.makedirs(username)

# make a request to the user's profile page
url = f"https://replit.com/@{username}"
response = requests.get(url)

# parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# find all the repls on the page
repls = soup.find_all("div", {"class": "user-repl-item"})

# loop through each repl and download it
for repl in repls:
    # get the repl's name and URL
    repl_name = repl.find("a")["href"].split("/")[-1]
    repl_url = f"https://replit.com{repl.find('a')['href']}/archive.zip"

    # make a request to download the repl's source code
    response = requests.get(repl_url)

    # save the source code to a file
    with open(f"{username}/{repl_name}.zip", "wb") as f:
        f.write(response.content)

    print(f"Downloaded {repl_name}")
