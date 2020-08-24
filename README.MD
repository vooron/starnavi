# StarNavi 
A simple blog application.

## Meta
- Language: Python 3.6+
- Framework: Django, Django Rest Framework 
- Database: SQLite (Default)

This app is not tested with Unit-testing. Some points were simplified.
The server in development mode and not ready to be deployed (this wasn't specified in requirements).

## Installation
1) Download source code from GitHub
2) `python3 -m venv venv`
3) `source venv/bin/activate`
4) `pip install -r requirements.txt`
5) `./manage.py migrate`
6) `./manage.py runserver`

You can also create a superuser account if needed (admin part is available).

You can find a bot, that perform queries in _bot folder. 
NOTE: if your port:8000 is already in use, please, change the host address in _bot.main to a valid value.
