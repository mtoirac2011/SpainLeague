![banner-readme](img/laliga_banner.png)

A Python Data Analyst Code-Louisville Project.

##### Version 1.0

## Welcome to the official repository of the Spain Soccer League!

The Spain Soccer League, is a Python Data Analyst CodeLouisville project, where
you can find some data and analysis of the Spain soccer league and Real Madrd soccer team as well. You can also find unit converter and string operation mudules. This project will be part of our go-to tool to show off to potential employers and demonstrate we know what we’re talking about.

## Requirements
    - Python 3.10.2 (older 3.3+ versions may work, but no promises)
    - Most recent version of Google Chrome
    - To use pyodbc for connect and execute SQL Server coammands:
      -  Go to Python installation folder Ex: C:\Users\minar\AppData\Local\Programs\Python\Python310
      -  Copy pyodbc-4.0.32-cp310-cp310-win_amd64.whl file from /data/ folder in project
      -  Run python -m pip install pyodbc-4.0.32-cp310-cp310-win_amd64.whl command
      -  Run python -m pip install pyodbc
    
## Setup
    - Run git clone https://github.com/mtoirac2011/SpainLeague.git to clone the repository.

## Instructions
    - From SpainLeague directory, run setup.py to execute the application.

## The Spain Soccer League pretents to give you a brief view about the soccer spain league, and this project is made up of the following pages:

* ###   Welcome screen 
* ###   Main menu
* ###   La Liga Menu 
* ###   Real Madrid Menu
* ###   Converter Menu 
* ###   Utilities Menu 

### Welcome screen
It welcomes the site and describes what the app will bring for us. 

### Main menu
Shows the diffrent menues that the application has to be used.

### La Liga Menu
Reports some kind of information about 2018 La liga soccer in Spain. Do some analyst as well in jupyter notebooks.

### Real Madrid Menu
Reports some kind of information about Real Madrid soccer team. Do some analyst as well specifically with the real madrid soccer team data. Do some analyst as well in jupyter notebooks.

### Converter Menu 
Converts an user input number to a several units.

### Utilities menu
Reads data from SQL Server and create a dictionary with data from a table. Also it shows operations over string fields.

### Feature list implemented

1. **Category 1: Python Programming Basics**:
    - Implement a “master loop” console application 
        (**setup.py**)
    - Create and call at least 3 functions or methods 
        (**All methods**)
    - Implement a regular expression (regex) 
        (**Convert module**)
    - Build a conversion tool that converts user input to another type and displays it (**Convert module**)
    - Create a dictionary or list, populate it with several values
        (**Utilities module**)
    - Analyze text and display information about it.
    - *( Not yet)*     
        - Create a class and create at least one object of that class and populate it.
        - Calculate and display data based on an external factor (ex: get the   current date, and display how many days remain until some event).
         (ex: how many words in a
            paragraph).

2. **Category 2: Utilize External Data**:
    - Read data from an external file, such as text, JSON, CSV, etc
        (**laliga and realmadrid modules**)
    - Connect to a database and read data using SQL. 
        (**Utilities module**)
    - *(Not yet)*
        - Connect to an external/3rd party API and read data into your app
        
3. **Category 3: Data Display**:
    - Visualize data in a graph, chart, or other visual representation of data.
        (**Laliga.ipynb and real_madrid.ipynb jupyter notebooks**)
    - Display data in tabular form.
        (**real_madrid.ipynb and Laliga.ipynb jupyter notebooks**)

4. **Category 4: Best Practices**:
    - Implement a log that records errors, invalid inputs.
        (**ligatools module**)
    - Create 3 or more unit tests for your application.
        (**test_ligatools.py**)
    - *(Not yet)*
        - The program should utilize a virtual environment and document library
        dependencies in a requirements.txt file.