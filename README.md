# Library Management Web Application

This is a simple web application for managing a local library's operations. The application is designed to assist librarians in tracking books and their quantity, books issued to members, and book fees. It provides a user-friendly interface for managing the library's resources efficiently.

## Functionality

The Library Management Web Application includes the following key functionalities:

1. **Base Library System:**
   - Maintain a database of books with stock information.
   - Manage library members.
   - Record transactions related to book issues and returns.

2. **Librarian Operations:**
   - Perform Create, Read, Update, and Delete (CRUD) operations on books and members.
   - Issue a book to a library member.
   - Handle book returns from members.
   - Search for books by name and author.
   - Charge a rental fee on book returns.
   - Ensure that a member's outstanding debt does not exceed Rs. 500.

## Usage

https://frappe.io/api/method/frappe-library?page=2&title=and

### Prerequisites

Before running the application, make sure you have the following software installed:

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Database Management System] ([SQLite](https://www.sqlite.org/))

### Setup

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/library-management-webapp.git
   ```

2. Change to the project directory:

   ```bash
   cd library-management-webapp
   ```

3. Create a virtual environment :

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

6. Set up the database:

   - Modify the `config.py` file to configure your database settings (e.g., SQLite).
   - Create the database schema by running:

     ```bash
     flask db init
     flask db migrate
     flask db upgrade
     ```

### Running the Application

1. Start the Flask development server:

   ```bash
   flask run
   ```

2. Open a web browser and navigate to `http://localhost:5000` to access the library management application.

### Usage Notes

- Use the user interface to manage books, members, and transactions as a librabrian.
- Ensure that book fees and outstanding debts are handled correctly.

## Contributing

Contributions to this project are welcome! If you have any improvements, bug fixes, or new features to suggest, please open an issue or submit a pull request.

---

Note: This is a Frappe dev hiring test. You can find the details at - https://frappe.io/dev-hiring-test
