Overview

This project was developed as part of the Industrial Internship provided by Upskill Campus and The IoT Academy in collaboration with UniConverge Technologies Pvt Ltd (UCT). The internship focused on solving a project/problem statement provided by UCT within a 6-week time frame. My project involved creating a URL Shortener, which is a Python application that converts long URLs into shorter, more manageable links. The system accepts a long URL as input, generates a unique shortened URL, and redirects users to the original URL when the shortened link is accessed.

Features

Shorten URLs: Accepts long URLs and generates short, unique links.
Redirect: Redirects users to the original URL when accessing the shortened link.
REST API: Implements REST endpoints to easily integrate the URL shortener with other services.

Technologies Used

Python: The core programming language used for the project.
Flask: A lightweight web framework for handling HTTP requests.
SQLite: A simple, lightweight database to store the original and shortened URLs.

url_shortener/
├── url_shortener.py    # Main Python application
├── README.md           # Project documentation
├── requirements.txt    # Dependencies for the project
└── url_shortener.db    # SQLite database file (created automatically)
