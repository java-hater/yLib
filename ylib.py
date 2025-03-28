import requests
import json

def getBookInfo(isbn):
    url = f"https://openlibrary.org/api/books?bibkeys={isbn}&format=json&jscmd=data"
    data = {}

    response = requests.get(url, headers = {"accept": "application/json"})
    book_data = response.text
    # turn json to dict
    data = json.loads(book_data)
    data = data[isbn]
    with open(f"{isbn}.json", "w") as file:
        file.write(book_data)
    
    parsed_data = {
        "isbn": isbn,
        "title": data["title"],
        "author": data["authors"][0]["name"],
        "pages": data["pagination"],
        "publisher": data["publishers"][0]["name"],
        "publish_date": data["publish_date"],
        "cover_url": data["cover"]
    }
    print(parsed_data)

isbn = "0441569595"
#isbn = "9781368098175"
getBookInfo(isbn)
getCover("isbn", isbn, "L")

#cover  #title
        #author
        #pages
        #publisher, year published
#isFav, haveRead
