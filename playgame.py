import requests
from time import sleep
from bs4 import BeautifulSoup
from random import choice
from csv import DictReader


BASE_URL = "http://quotes.toscrape.com"

# Read all quotes from dailyQuotes.csv file


def readQuotes(fileName):
    with open(fileName, 'r')as file:
        csvReader = DictReader(file)
        csvReader = list(csvReader)
        return csvReader
        # for quote in csvReader:
        #     return quote
        # TypeError: object of type 'DictReader' has no len()


# Call readQuotes function to redad all quotes
# readQuotes('dailyQuotes.csv')

# Guess Task


def playGame(allQuotes):
    selectQuote = choice(allQuotes)
    totalChances = 4
    print(selectQuote["eachQuote"])
    print(selectQuote['author'].lower())
    guess = ''

    while guess.lower() != selectQuote["author"].lower() and totalChances > 0:
        guess = input(f'Who said this quote? Guess remaining {totalChances}: ')
        totalChances -= 1
        if guess.lower() == selectQuote["author"].lower():
            print('Correct!!')
        else:
            def hintMsg(selectQuote, totalChances):
                if totalChances == 3:
                    authorAddress = requests.get(
                        f"{BASE_URL}{selectQuote['bio-link']}")
                    authorInfo = BeautifulSoup(
                        authorAddress.text, "html.parser")
                    bornDate = authorInfo.find(
                        class_="author-born-date").get_text()
                    bornLocation = authorInfo.find(
                        class_="author-born-location").get_text()
                    print(f"Hint: Author is born on {bornDate} {bornLocation}")
                elif totalChances == 2:
                    print(
                        f"Author first name first letter is {selectQuote['author'][0][0]}")
                elif totalChances == 1:
                    print(
                        f"Author Last name first letter is {selectQuote['author'].split(' ')[1][0]}")
                else:
                    print(
                        f"Chances are out. Author name  is {selectQuote['author'].lower()}")
            hintMsg(selectQuote, totalChances)
# Forget the actual reason to return False
# return False


# Play Again
# def requestPlay(): Play games doesn't return anything so disable this function
    againPlay = ''
    while againPlay.lower() not in ('y', 'yes', 'n', 'no'):
        againPlay = input("Would you like to play again? (y/n)")
        if againPlay.lower() in ('yes', 'y'):
            playGame(allQuotes)
        else:
            print('Hope see you again to play this game :D')


# allQuotes holds all quotes from dailyQuotes.csv
allQuotes = readQuotes('dailyQuotes.csv')
playGame(allQuotes)


# Play again again function executes
# trueParam = playGame(allQuotes)
# requestPlay(trueParam)
