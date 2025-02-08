AirBnB Clone - Web Framework

Description

This project is part of the AirBnB Clone series, focusing on building a web framework using Flask. The goal is to understand the core concepts of web frameworks, routing, templating, and database integration.

Learning Objectives

By completing this project, you will:

Understand what a web framework is.

Learn how to build a web framework using Flask.

Define and manage routes in Flask.

Work with dynamic URL variables.

Create and use HTML templates with Jinja2.

Implement loops and conditions in templates.

Fetch and display data from a MySQL database in an HTML page.

Requirements

Python Scripts

Use Ubuntu 20.04 LTS and Python 3.4.3.

All scripts must start with #!/usr/bin/python3.

Follow PEP 8 coding style.

Each module, class, and function must be well-documented.

Python files must be executable.

HTML & CSS

HTML files should be W3C-compliant (except for Jinja templates).

Use CSS styles stored in the styles/ directory.

All images must be in the images/ folder.

No !important or id selectors allowed in CSS.

All tags must be uppercase.

Tested with Google Chrome 56.0.2924.87.

Project Structure

AirBnB_clone/
│── web_flask/
│   ├── __init__.py
│   ├── main.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   ├── static/
│   │   ├── styles/
│   │   │   ├── main.css
│   │   ├── images/
│── README.md
│── requirements.txt

Setup & Usage

1. Install Dependencies

Run the following command to install Flask:

pip install flask

2. Create a Simple Flask Application

Create a file named main.py inside the web_flask/ directory with the following content:

#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, AirBnB Clone!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

3. Run the Flask App

Execute the following command to start the server:

python3 web_flask/main.py

4. Access the Web Application

Open your browser and go to:

http://localhost:5000/

You should see the message "Hello, AirBnB Clone!" displayed on the page.

5. Creating Routes with Variables

Modify main.py to include a new route that accepts a variable:

@app.route('/user/<username>')
def show_user(username):
    return f"Hello, {username}!"

Restart the Flask server and access the following URL in your browser:

http://localhost:5000/user/Duncan

You should see "Hello, Duncan!" displayed on the page.

Author

Duncan Korir - ALX Software Engineering Program