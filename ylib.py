import requests
import json

def getBookInfo(isbn):
    url = f"https://openlibrary.org/isbn/{isbn}"
    data = {}

    response = requests.get(url, headers = {"accept": "application/json"})
    book_data = response.text
    # turn json to dict
    # data = json.loads(book_data)
    with open(f"{isbn}.json", "w") as file:
        file.write(book_data)
    

def getCover(key, value, size):
    # key = isbn, value = isbn number, size = s,m,or l
    url = f"https://covers.openlibrary.org/b/{key}/{value}-{size}.jpg"
    #this retrieves the actual image
    response = requests.get(url)
    with open(f"{value}.jpg", "wb") as file:
        file.write(response.content)

#isbn = "0441569595"
isbn = "9781368098175"
getBookInfo(isbn)
getCover("isbn", isbn, "L")

#cover  #title
        #author
        #pages
        #publisher, year published
#isFav, haveRead
