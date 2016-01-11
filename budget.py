#!/usr/bin/python3

import sqlite3
import os

db = sqlite3.connect(':memory:')

c = db.cursor()

shouldExit = False

# Create Database
def createTable():
	c.execute('CREATE TABLE income(name TEXT, amount FLOAT)')
	c.execute('CREATE TABLE constantMonthly(name TEXT, amount FLOAT, month TEXT)')
	c.execute('CREATE TABLE constantYearly(name TEXT, amount FLOAT, month TEXT)')
	c.execute('CREATE TABLE varyingMonthly(name TEXT, amount FLOAT, month TEXT)')
	db.commit()

### Functions to edit database ###

def addIncome(): # Add income values
	name = input('Source of income: ')
	name = str.lower(name)
	income = input('Monthly Income: ')
	income = float(income)
	c.execute('INSERT INTO income VALUES (?, ?)', (name, income))

def editIncome(): # Edit income
	name = input('Which income are you updating?: ')
	name = str.lower(name)
	income = input('New value: ')
	income = float(income)
	c.execute('UPDATE income SET amount=(?) WHERE name=(?)', (income, name))

def addExpenseM(): # Add Monthly Expense
	name = input('Monthly Expense name: ')
	name = str.lower(name)
	amount = input('Monthly Expense amount: ')
	amount = float(income)	
	month = input('Month: ')
	month = str.lower(month)
	c.execute('INSERT INTO constantMonthly VALUES (?, ?, ?)', (name, amount, month))

def editExpenseM(): # Edit Monthly Expense
	name = input(' Expense name: ')
	name = str.lower(name)
	amount = input('Monthly Expense amount: ')
	amount = float(income)	
	c.execute('UPDATE constantMonthly SET amount=(?) WHERE name=(?)' (amount, name))


def addExpenseY(): # Add Yearly Expense
	name = input('Yearly Expense name: ')
	name = str.lower(name)
	amount = input('Yearly Expense amount: ')
	amount = float(income)
	month = input('Month: ')
	month = str.lower(month)
	c.execute('INSERT INTO constantYearly VALUES (?, ?, ?)', (name, amount, month))

def editExpenseYM(): # Edit Yearly Expense
	name = input(' Expense name: ')
	name = str.lower(name)
	amount = input('Monthly Expense amount: ')
	amount = float(income)	
	c.execute('UPDATE constantMonthly SET amount=(?) WHERE name=(?)' (amount, name))


def addExpenseV(): # Add montly purchase
	name = input('Purchase name: ')
	name = str.lower(name)
	amount = input('Purchase amount: ')
	amount = float(income)
	month = input('Month: ')
	month = str.lower(month)
	c.execute('INSERT INTO varyingMonthly VALUES (?, ?, ?)', (name, amount, month))

###

def listIncome():
	for i in c.execute('select * from income'):
		print(i)

def controls():
	global shouldExit
	print('Menu:')

db.commit()
db.close()
