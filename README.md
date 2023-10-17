# Loan api

## Description

A Loan basic application to request loans given the tax id, business name and the amount, this request should be accepted, declined or undecided based on the amount.

- if amount < 50000 is rejected
- if amount = 50000 is undecied
- if amount > 50000 is accepted

## Virtual environment

First of all make sure to create virtual environment

- `$ pip install virtualenv`
- `$ python3 -m venv venv`

Then activate the environemnt:

- windows: `. /venv/Scripts/activate`
- Unix system: `. venv/bin/activate`

Note: if you have any issues please refer to this documentation https://docs.python.org/3/library/venv.html

## Dependencies

Install every dependency with the next command

`$ pip install -r requirements.txt`

## Run the application

`$ python server.py`
