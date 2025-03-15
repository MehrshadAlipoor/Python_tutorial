# python
# Date: 11/03/25

# =========================================================================

# ============================
# Python Modules Tutorial
# ============================

# A module in Python is a file containing Python code (functions, classes, variables) that can be reused in other programs.
# It helps in organizing code and avoiding redundancy.

# 1. Importing a Module
import math  # Built-in module
print(math.sqrt(16))  # Output: 4.0

# 2. Importing Specific Functions
from math import pi, sin
print(pi)  # Output: 3.141592653589793
print(sin(0))  # Output: 0.0

# 3. Importing with an Alias
import datetime as dt
print(dt.datetime.now())  # Prints current date and time

# 4. Creating a Custom Module
    # Save this code in a file named mymodule.py:
    # def greet(name):
    #     return f"Hello, {name}!"
    # 
    # x = 10

# Now, import and use it in another Python file:
    # import mymodule
    # print(mymodule.greet("Alice"))  # Output: Hello, Alice!
    # print(mymodule.x)  # Output: 10

# 5. Using the dir() Function
    # The dir() function lists all attributes and functions inside a module
print(dir(math))  # Shows all available functions in the math module

# 6. Installing and Using External Modules (via pip)
    # Example: Install requests module using pip
    # pip install requests
    # import requests
    # response = requests.get("https://www.example.com")
    # print(response.status_code)

# Summary:
    # - Modules help organize and reuse code.
    # - Use built-in, third-party, or custom modules.
    # - Import entire modules, specific functions, or use aliases.
    # - Install external modules using pip.

# Happy Coding!

# =====================================================================================

# ============================
# Python Packages Tutorial
# ============================

# A package in Python is a way of structuring related modules together in a directory.
# It allows better code organization and reuse.

# 1. Creating a Package (Folder Structure)
    # mypackage/         <-- This is the package
    # ├── __init__.py    <-- (Optional) Initializes the package
    # ├── module1.py     <-- First module in the package
    # ├── module2.py     <-- Second module in the package

# Example: mypackage/module1.py
    # def greet(name):
    #     return f"Hello, {name}!"

# Example: mypackage/module2.py
    # def add(a, b):
    #     return a + b

# 2. Importing from a Package
    # import mypackage.module1
    # print(mypackage.module1.greet("Alice"))  # Output: Hello, Alice!

# 3. Using 'from' to Import Specific Functions
    # from mypackage.module2 import add
    # print(add(3, 5))  # Output: 8

# 4. Using 'from package import *' (Requires __all__ in __init__.py)
    # Example: Inside mypackage/__init__.py:
    # __all__ = ["module1", "module2"]

# Now we can do:
    # from mypackage import *
    # print(module1.greet("Bob"))  # Output: Hello, Bob!

# 5. Installing and Using External Packages
    # Packages can be installed using pip (e.g., numpy, pandas)
    # pip install numpy
    # import numpy as np
    # print(np.array([1, 2, 3]))  # Output: [1 2 3]

# Summary:
    # - A package is a directory containing multiple related modules.
    # - __init__.py is optional but useful for package initialization.
    # - Import modules using different methods: full path, specific imports, or wildcard (*).
    # - External packages can be installed using pip.

# ==================================================================================================

# ============================
# Python Directories Tutorial
# ============================
import os  # The 'os' module helps in handling directories and files.

# 1. Getting the Current Working Directory
print(os.getcwd())  # Output: Current directory path

# 2. Changing the Working Directory
    # os.chdir("C:/Users/YourName/Documents")  # Changes the current directory (Windows)
    # os.chdir("/home/user/Documents")  # Changes directory (Linux/Mac)
print(os.getcwd())  # Verifies the change

# 3. Listing Files and Directories
print(os.listdir())  # Lists all files and folders in the current directory
    # print(os.listdir("C:/Users/YourName"))  # Lists files in a specific directory

# 4. Creating a New Directory
    # os.mkdir("new_folder")  # Creates a new folder in the current directory
    # os.makedirs("parent_folder/child_folder")  # Creates multiple nested directories

# 5. Removing a Directory
    # os.rmdir("new_folder")  # Removes an empty directory
    # os.removedirs("parent_folder/child_folder")  # Removes directories recursively (if empty)

# 6. Checking if a Directory Exists
if os.path.exists("new_folder"):
    print("Directory exists")
else:
    print("Directory does not exist")

# 7. Renaming a Directory
# os.rename("old_folder", "new_folder_name")

# 8. Walking Through a Directory Tree
for dirpath, dirnames, filenames in os.walk("."):  # "." means current directory
    print("Directory Path:", dirpath)
 #   print("Subdirectories:", dirnames)
 #   print("Files:", filenames)

# 9. Working with File Paths (Using os.path)
file_path = os.path.join("folder", "file.txt")  # Creates a platform-independent file path
print(file_path)  # Output: folder/file.txt (Linux/Mac) or folder\file.txt (Windows)

print(os.path.abspath("file.txt"))  # Returns absolute path of a file
#print(os.path.basename("/home/user/file.txt"))  # Output: file.txt (Gets file name)
#print(os.path.dirname("/home/user/file.txt"))  # Output: /home/user (Gets directory name)

# 10. Deleting Files (Be Careful!)
    # os.remove("file.txt")  # Deletes a file if it exists

# Summary:
    # - Use `os` module for directory and file operations.
    # - `os.getcwd()` gets the current directory.
    # - `os.listdir()` lists files and folders.
    # - `os.mkdir()` and `os.makedirs()` create directories.
    # - `os.rmdir()` and `os.removedirs()` delete empty directories.
    # - `os.path` functions help with file path manipulations.

# ==================================================================================

# ====================================
# Selenium & Web Scraping Tutorial
# ====================================

# Web Scraping is the process of extracting data from websites.
# Selenium is a Python package used for automating web browsers and can be used for web scraping.

# -----------------------
# 1. Installing Selenium
# -----------------------
# First, install Selenium using pip:
# pip install selenium

# You also need a WebDriver for your browser:
# - Chrome: Download 'chromedriver' from https://chromedriver.chromium.org/downloads
# - Firefox: Download 'geckodriver' from https://github.com/mozilla/geckodriver/releases

# -----------------------
# 2. Importing Selenium and Setting Up WebDriver
# -----------------------

from selenium import webdriver  # Import WebDriver
from selenium.webdriver.common.by import By  # Helps in locating elements
from selenium.webdriver.common.keys import Keys  # Helps in keyboard interactions
import time  # For adding delays

# Set up the WebDriver (for Chrome, use "chromedriver.exe" in the same directory)
driver = webdriver.Chrome()  

# Open a Website
driver.get("https://www.google.com")

# -----------------------
# 3. Finding Elements
# -----------------------

# Find element by name and type into it
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python")  # Typing in search box
search_box.send_keys(Keys.RETURN)  # Pressing Enter

time.sleep(3)  # Wait for results to load

# Get search results
results = driver.find_elements(By.CSS_SELECTOR, "h3")
for result in results:
    print(result.text)  # Print result titles

# -----------------------
# 4. Clicking Elements
# -----------------------
first_result = results[0]
first_result.click()  # Clicks the first result

time.sleep(3)  # Wait for page to load

# -----------------------
# 5. Closing the Browser
# -----------------------
driver.quit()  # Closes the browser window

# ====================================
# Web Scraping vs Web Crawling
# ====================================

# Web Scraping:
# - Extracts specific data from web pages.
# - Focuses on one or multiple pages but does not go beyond a defined limit.
# - Example: Extracting product prices from an e-commerce website.

# Web Crawling:
# - Automatically follows links to discover and index multiple pages.
# - Used by search engines (Google, Bing) to index websites.
# - Example: A bot that navigates a website and extracts links.

# Summary:
# - Selenium automates browsers and can be used for scraping.
# - `find_element` and `find_elements` help locate webpage elements.
# - Scraping extracts specific data; crawling explores entire websites.

# Happy Scraping!
