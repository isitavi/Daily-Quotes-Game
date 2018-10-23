import requests
from time import sleep
from bs4 import BeautifulSoup
from random import choice
from csv import DictWriter

BASE_URL = "http://quotes.toscrape.com"


def collectQuotes():
    allInfo = []

    PAGES_URL = "/page/1/"
    while PAGES_URL:
        response = requests.get(f"{BASE_URL}{PAGES_URL}")
        print(f"Now crawling this {BASE_URL}{PAGES_URL} link....")
        htmlData = BeautifulSoup(response.text, 'html.parser')
        grabQuotes = htmlData.find_all(class_="quote")

        for quote in grabQuotes:
            allInfo.append({
                "eachQuote": quote.find(class_="text").get_text(),
                "author": quote.find(class_="author").get_text(),
                "bio-link": quote.find("a")["href"]

            })

        nextPage = htmlData.find(class_="next")
        PAGES_URL = nextPage.find('a')['href'] if nextPage else None

    return allInfo


# Write all quotes to CSV file
def writeCSVFile(allQuotes):
    with open('dailyQuotes.csv', 'w') as file:
        headerTitle = ["eachQuote", "author", "bio-link"]
        csvWriter = DictWriter(file, fieldnames=headerTitle)
        csvWriter.writeheader()
        for quote in allQuotes:
            csvWriter.writerow(quote)


allQuotes = collectQuotes()
writeCSVFile(allQuotes)
