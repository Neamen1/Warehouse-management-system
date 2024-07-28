# Warehouse Management System

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Running-application](#Running-application)
- [Running-Tests](#Running-Tests)
- [Usage](#usage)
- [File-Structure](#File-Structure)
- [Screenshots](#screenshots)

## Overview
This project is a Warehouse Management System (WMS) built using Flask for the backend and Docker for containerization. The system provides functionalities for managing inventory, orders, and warehouse operations efficiently.

## Features
- **Inventory Management**: Add, update, and delete inventory items.
- **Order Management**: Create, update, and track orders.
- **User Authentication**: Secure login and user management.

## Requirements
- Docker (or other COUCHDB, REDIS container)
- Python 3.x
- Python libs in requirements.txt 

## Installation
1. Clone the Repository:
```sh
git clone https://github.com/Neamen1/Warehouse-management-system.git
cd Warehouse-management-system
```

2. Install Dependencies:
```sh
pip install -r requirements.txt
```

3. Configure databases
- Configure SQL database file
- Configure containers for COUCHDB, REDIS

## Running-application

1. set env variables and Run the Application:
```sh
set FLASK_APP=flaskblog.py
set FLASK_ENV=development
set SQLALCHEMY_DATABASE_URI=sqlite:///storage.db
set SECRET_KEY=5791628bb0b13ce0c676fde280a245
set COUCHDB_SERVER=http://couchdb:couchdb@localhost:5984/
set COUCHDB_DATABASE=logs
set SESSION_TYPE=redis
set SESSION_REDIS=redis://localhost:6379/
flask run
```

2. Access the Application:
Open your web browser and go to http://localhost:5000.

## Running-Tests
To run the tests, use the following commands (with setting env variables):
```sh
set FLASK_APP=flaskblog.py
set FLASK_ENV=development
set SQLALCHEMY_DATABASE_URI=sqlite:///test.db
set SECRET_KEY=5791628bb0b13ce0c676fde280a245
set COUCHDB_SERVER=http://couchdb:couchdb@localhost:5984/
set COUCHDB_DATABASE=logs
set SESSION_TYPE=redis
set SESSION_REDIS=redis://localhost:6379/
pytest
```
or launch **quickstart-windows-testing.bat**

## Usage
- Admin Panel: Manage inventory, orders, and users.
- Customer Interface: Browse and select products.

## File-Structure
- flaskblog/: Main application code.
  - \_\_init\_\_.py: Initializes the Flask application and sets up configuration.
  - models.py: Contains the database models for the application.
  - config.py: Configuration settings for different environments.
  - static/: Static files (CSS, JavaScript, images).
  - templates/: HTML templates for rendering views.
  - tests/: test scripts for the application.
  - *other directories*/: Scripts that handle logic for Users, notifications, orders etc.
- instance/: SQL database files.
- run.py: Entry point for running the application.
- quickstart-windows.bat: Script for quick setup on Windows.
- requirements.txt: python project dependencies

## Screenshots
|![Log in page](https://github.com/user-attachments/assets/eedf726b-e248-4a8e-9dca-26b32a0a70fd) Log in page|![List of products](https://github.com/user-attachments/assets/d65e478a-ca20-4b79-93b4-b53816abd135) List of products|
|:---:|:---:|
|![Cart with some products](https://github.com/user-attachments/assets/eab042e6-3b0d-4c58-b9a2-f832027d1cbc) Cart with some products|![Orders list](https://github.com/user-attachments/assets/46f6d5aa-b30e-41ab-9f4c-37962358f6c2) Orders list|
|![Logs](https://github.com/user-attachments/assets/aa19eb24-2d15-4ced-aec8-9ccec67c6102) Logs|![Account page](https://github.com/user-attachments/assets/d790bc4d-7c54-4f40-bbb4-8d0a7bb3e0f2) Account page|

