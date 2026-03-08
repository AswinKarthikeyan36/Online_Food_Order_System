ONLINE FOOD ORDER SYSTEM

The Online Food Order System is a simple command‑line application developed using Python and SQLite that allows users to browse food items, place orders, and store order information in a database. The system simulates the basic functionality of an online food ordering platform where customers can view available menu items and order food through a terminal interface.

This project is designed to demonstrate how Python can be used to build a small real‑world application using modular programming and database integration. The application is organized into multiple Python modules, where each file is responsible for a specific functionality such as managing the database, handling menu items, and processing customer orders.

The system uses SQLite, a lightweight database that comes built into Python, to store information about food items and customer orders. This ensures that the data is saved and can be accessed whenever the program runs.

The program runs through a menu‑driven command‑line interface (CLI) where users can select different options such as viewing available food items, adding items to the menu, and placing an order. This type of interface is simple but effective for demonstrating how interactive applications work.

This project is mainly created for learning purposes and helps beginners understand important programming concepts such as Python modules, database operations, and command‑line application design.

🎯 Purpose of the Project
The main objectives of this project are:

To build a simple online food ordering system

To understand modular programming in Python

To integrate SQLite database with Python

To practice basic CRUD operations (Create, Read, Update, Delete)

To create an interactive command‑line application

🧠 Concepts Demonstrated
This project demonstrates several important programming concepts:

Python modular programming using multiple files

Database management using SQLite

Command‑line interface development

Data storage and retrieval

Basic application structure and organization

📂 Project Structure
online-food-order-system/
│
├── database.py    # Handles database connection and table creation
├── menu.py        # Manages food menu operations
├── orders.py      # Handles food order placement
├── main.py        # Main program that runs the application
└── README.md
