# Author: Cristiano Cavo
# Date: 2019-08-20
# From: http://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html

# Use the BeautifulSoup and requests Python packages to print out a list of all
# the article titles on the New York Times homepage.
# Notes: Since something changed in the NYT website, I decided to use ansa.it

import requests
from bs4 import BeautifulSoup

base_url = "http://www.ansa.it/sito/notizie/mondo/mondo.shtml"
r = requests.get(base_url)
soup = BeautifulSoup(r.text, features="html.parser")

notizieUltimaOra = soup.find("ol", id="ultimaOra").find_all("li")
for notizia in notizieUltimaOra:
    print(notizia.find("em").text + " " + notizia.find("h3").text)
