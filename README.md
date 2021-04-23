# Zerodha-Task

## Demo

https://zerodha-task-mahen.herokuapp.com/

## Task Description

BSE publishes a "Bhavcopy" (Equity) ZIP every day here: https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx

Write a standalone Python Django web app/server that:

- Downloads the equity bhavcopy zip from the above page every day at 18:00 IST for the current date.
- Extracts and parses the CSV file in it.
- Writes the records into Redis with appropriate data structures (Fields: code, name, open, high, low, close).
- Renders a simple VueJS frontend with a search box that allows the stored entries to be searched by name and renders a
  table of results and optionally downloads the results as CSV. Make this page look nice!
- The search needs to be performed on the backend using Redis.

## Solution

I have used `APScheduler` for downloading `Bhavcopy` daily at 6:00 PM IST. Frontend is made using Vue.js (cdn) and
Vuetify is used for Material-UI components.

## Setup (Local)

1. Clone this repository: `$ git clone https://github.com/imlegend19/Zerodha-Task.git`
2. Create a virtual environment:
    ```
    $ python3 -m venv venv
    $ source venv/bin/activate
    ```
3. Install the requirements: `$ pip install -r requirements.txt`
4. (Skip if already installed) Download & setup *Redis*:
    - Download: `$ wget https://download.redis.io/releases/redis-6.2.2.tar.gz`
    - Extract: `$ tar xzf redis-6.2.2.tar.gz`
    - `$ cd redis-6.2.2 && make`
5. Start Redis Server: `$ redis-server`
6. Check if redis is working:
    ```
    $ redis-cli ping
    PONG
    ```
7. Start `clock.py` tasks: `$ cd Zerodha-Task && python clock.py`
8. Run migrations:
    - `$ python manage.py makemigrations`
    - `$ python manage.py migrate`
9. Bingo! The setup is now complete.

Start the Django Server: `$ python manage.py runserver`
