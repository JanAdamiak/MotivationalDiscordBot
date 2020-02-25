from bs4 import BeautifulSoup
import requests
import time

def parse_quotes(website):
    r = requests.get(website)
    soup = BeautifulSoup(r.content, 'html5lib')
    return soup.find_all(class_="quote")

start_page = "https://www.successories.com/iquote/category/39/inspirational-quotes/"
quotes_list = []

with open("quotes.txt", "w") as file:
    for i in range(1, 20):
        quotes = parse_quotes(start_page + str(i))
        for quote in quotes:
            file.write(quote.text + "\n")
