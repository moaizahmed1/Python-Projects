# ## Section 4 — Working with JSON

# 1. Create a dictionary representing a book (title, author, year, in_stock). Use the json module to write it to a file book.json.
# 2. Read book.json back into a Python dictionary and print the title and author.
# 3. Create a list of three book dictionaries, save them all to books.json, then read them back and print only the titles.


#1
import json

good = {
    "title": "Python Basics","author": "John Smith","year": 2024,"in_stock": True
}

with open("book.json", "w") as f:
    json.dump(good, f, indent=4)

#2

import json

with open("book.json", "r") as f:
    book = json.load(f)

print("Title:", book["title"])
print("Author:", book["author"])


#3
import json

books = [
    {
        "title": "Python Basics",
        "author": "John Smith",
        "year": 2024,
        "in_stock": True
    },
    {
        "title": "Learn Django",
        "author": "Alice Brown",
        "year": 2023,
        "in_stock": False
    },
    {
        "title": "Flask Guide",
        "author": "David Lee",
        "year": 2022,
        "in_stock": True
    }
]

with open("books.json", "w") as f:
    json.dump(books, f, indent=4)


with open("books.json", "r") as f:
    books = json.load(f)

for book in books:
    print(book["title"])