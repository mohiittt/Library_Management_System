from flask import Flask, render_template
from database import books  # Import the get_all_books function

app = Flask(__name__, template_folder='template')


@app.route('/')
def index():
    # Retrieve all books from the database using the get_all_books function
    all_books = books  # Call the function to get the books data

    # Render the HTML template and pass the books data to it
    return render_template('index.html', books=all_books)


if __name__ == '__main__':
    app.run(debug=True)
