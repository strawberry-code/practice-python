# Author: Cristiano Cavo
# Date: 2019-08-27
# From: http://www.practicepython.org/exercise/2014/11/30/21-write-to-a-file.html

# Take the code from the How To Decode A Website exercise (if you didn’t do it
# or just want to play with some different code, use the code from the
# solution), and instead of printing the results to a screen, write the results
# to a txt file. In your code, just make up a name for the file you are saving
# to.
# Extras:
# Ask the user to specify the name of the output file that will be saved.

# Notes: I decided to write on a file the output of the exercise number 19

""" # # # # -<( Bootcamp )>- # # # #

with open("file_to_save.txt", "w") as open_file:
    open_file.write("A string to write")

"""

from bs4 import BeautifulSoup
import requests
import re
import datetime

url = "https://www.ilpost.it/2019/08/24/weekly-beasts-270/"
how_many_weeks = 10
week = 270


def fetch_week(url):
    output = ""
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
        output = output + beastDescription + "\n"
    return output


def build_url(current_week, week):
    week_str = str(current_week).replace("-", "/")
    url = "https://www.ilpost.it/{}/weekly-beasts-{}/".format(week_str, week)
    return url


def fetch_weeks():
    output = ""
    startingDateRaw = re.search("[0-9]{4}\/[0-9]{2}\/[0-9]{2}", url).group()
    startingDate = datetime.datetime.strptime(startingDateRaw, "%Y/%m/%d").date()
    current_week = startingDate
    week = 270
    current_url = url
    for i in range(10):
        print("- - - - fetching ({} - {})...".format(current_week, current_url))

        current_url = build_url(current_week, week)
        output = output + fetch_week(current_url)

        print("done!".format(current_week))
        week_ago = current_week - datetime.timedelta(days=7)
        current_week = week_ago
        week = week - 1
    return output


def getFileName():
    filename = input("give the filename:\n> ")
    return filename


def main():
    filename = getFileName()
    text = fetch_weeks()
    with open("{}.txt".format(filename), "w") as open_file:
        open_file.write(text)


main()
