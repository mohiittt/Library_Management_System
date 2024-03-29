import requests
import sqlite3

url = "https://frappe.io/api/method/frappe-library?page=2&title=and"

# Make an HTTP GET request to the URL
try:
    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        books = data.get("message", [])

        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          title TEXT,
                          authors TEXT,
                          isbn TEXT,
                          publisher TEXT,
                          page INTEGER)''')

        for book in books:
            title = book.get("title", "N/A")
            authors = book.get("authors", "N/A")
            isbn = book.get("isbn", "N/A")
            publisher = book.get("publisher", "N/A")
            num_pages = book.get("num_pages", "N/A")

            # Insert book data into the database
            cursor.execute("INSERT INTO books (title, authors, isbn, publisher, page) VALUES (?, ?, ?, ?, ?)",
                           (title, authors, isbn, publisher, num_pages))

        conn.commit()
        conn.close()

        print("Book data inserted into the database.")
    else:
        print("Failed to retrieve data. Status code:", response.status_code)
except requests.exceptions.RequestException as e:
    print("An error occurred during the HTTP request:", e)
except Exception as e:
    print("An error occurred:", e)