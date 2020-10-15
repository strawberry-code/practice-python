# Author: Cristiano Cavo
# Date: 2019-08-27
# From: http://www.practicepython.org/exercise/2014/07/14/19-decode-a-web-page-two.html

# Using the requests and BeautifulSoup Python libraries, print to the screen the
# full text of the article on this website:
# http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.
#
# The article is long, so it is split up between 4 pages. Your task is to print
# out the text to the screen so that you can read the full article without
# having to click any buttons.
#
# (Hint: The post here describes in detail how to use the BeautifulSoup and
# requests libraries through the solution of the exercise posted here.)
#
# This will just print the full text of the article to the screen. It will not
# make it easy to read, so next exercise we will learn how to write this text to
# a .txt file.  Notes: Since the original webpage has been changed, I decided to
# make a similar exercise with some differences. The website that I will use is
# ilpost.it (a very great website!). Every week ilpost.it publishes a set of
# images about animals in the World. My script starts from 2019/08/24 (that is
# the week number 270) and go bakwards for 10 weeks. For each week the scripts
# opens each image page, read its description and take it showing it int he
# console output. So, at the end, in the console output will be printed all the
# images description of 10 weeks.

from bs4 import BeautifulSoup
import requests
import re
import datetime

url = "https://www.ilpost.it/2019/08/24/weekly-beasts-270/"
how_many_weeks = 10
week = 270


def do_it(url):
    webpage = requests.get(url)
    soup = BeautifulSoup(webpage.text, "html.parser")
    beasts = soup.findAll("div", class_="gallery-icon landscape")

    beastsDescriptions = []

    for beast in beasts:
        beastUrl = beast.find("a")["href"]
        beastWebpage = requests.get(beastUrl)
        beastSoup = BeautifulSoup(beastWebpage.text, "html.parser")
        beastDescriptionRaw = (
            beastSoup.find("span", id="gallery-description").find("p").text
        )
        beastDescriptionRaw = re.sub("\(.*\)", "", beastDescriptionRaw).replace(
            "\n", ""
        )
        beastDescription = re.sub("^\ ", "", beastDescriptionRaw)
        print(beastDescription)


def build_url(current_week, week):
    week_str = str(current_week).replace("-", "/")
    url = "https://www.ilpost.it/{}/weekly-beasts-{}/".format(week_str, week)
    return url


def main():
    startingDateRaw = re.search("[0-9]{4}\/[0-9]{2}\/[0-9]{2}", url).group()
    startingDate = datetime.datetime.strptime(startingDateRaw, "%Y/%m/%d").date()
    current_week = startingDate
    week = 270
    current_url = url
    for i in range(10):
        print("- - - - fetching ({} - {})...".format(current_week, current_url))

        current_url = build_url(current_week, week)
        do_it(current_url)

        print("done!".format(current_week))
        week_ago = current_week - datetime.timedelta(days=7)
        current_week = week_ago
        week = week - 1


main()
