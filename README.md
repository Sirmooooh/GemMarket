# GemMarket
My portfolio project 
GemMarket is a web application designed to connect miners with buyers and investors in the world of precious gemstones and minerals. This app is built with Python using the Flask framework for the backend, HTML, JavaScript, and CSS for the frontend, and MySQL for database storage.
Table of Contents

    Features
    Installation
    Usage
    Project Structure
    API Routes
    Database Schema
    Dependencies
    Contributing
    License
Features

    User Roles:
        Miners: Create and manage listings for mineral resources and gemstones.
        Buyers: Browse and purchase mineral resources and gemstones.
        Investors: Explore investment opportunities in the gem market.

    Messaging System:
        Users can communicate with each other through a messaging system.

    Secure Authentication:
        User authentication is securely handled through the backend.

    Responsive Design:
        The web application is designed to be accessible on various devices.
Installation
Prerequisites

Make sure you have the following installed:

    Python
    Flask
    MySQL
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py


Configure the database:

    Create a MySQL database and update the database configuration in config.py.

PROJECT STRUCTURE


GemMarket/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── forms.py
│   └── templates/
│       ├── index.html
│       ├── register.html
│       ├── login.html
│       ├── dashboard.html
│       ├── listings.html
│       ├── messages.html
│       └── success.html
│
├── config.py
├── run.py
└── venv/
    └── ...  # Your virtual environment files

API Routes

    /api/listings
        GET: Returns a list of mineral resource and gemstone listings.
        POST: Allows miners to create new listings with details.

    /api/messages
        GET: Retrieves user-specific messages and conversations.
        POST: Enables users to send messages to each other.

Database Schema

The database schema includes tables such as users, listings, messages, etc. Refer to models.py for details.

Database Schema

The database schema includes tables such as users, listings, messages, etc. Refer to models.py for details.
Dependencies

    Flask
    Flask-Login
    Flask-WTF
    MySQL Connector

	LICENSED BY SIRMOOH
