# Best Pharmacy Management System

## Description
A command-line application for a pharmacist to record medicines,
track stock and sales, and calculate profit/loss and tax owed.

## How to run
python pharmacy.py

## Features
1. Add a medicine and calculate results
2. View all medicines
3. Search by name
4. Exit

## Project structure
main.py            - entry point and menu loop
modules/validations.py  - input validation
modules/calculations.py - profit and tax maths
modules/records.py      - file loading and saving
modules/reports.py      - display output

## Requirements
Python 3.10 or newer. Standard library only.

## Data storage
Records are stored in data/medicine.txt, one medicine per line,
fields separated by "|".

## Github Link For Project Progress Tracking
[Github](https://github.com/gaks1/Pharmacy)