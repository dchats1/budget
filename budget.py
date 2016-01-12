#!/usr/bin/python3

import sqlite3
import os
import curses

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
	screen.clear()
	screen.border(0)
	screen.refresh()
	screen.addstr(10, 10, 'Source of income: ')
	name = screen.getstr(11, 10, 10)
	name = str(name)
	name = str.lower(name)
	screen.refresh()
	screen.addstr(12, 10, 'Monthly Income: ')
	income = screen.getstr(13, 10, 10)
	income = float(income)
	c.execute('INSERT INTO income VALUES (?, ?)', (name, income))

def editIncome(): # Edit income
	screen.clear()
	screen.border(0)
	screen.refresh()
	screen.addstr(10, 10, 'Which income are you updating?: ')
	name = screen.getstr(11, 10, 10)
	name = str(name)
	name = str.lower(name)
	screen.refresh()
	screen.addstr(12, 10, 'New value: ')
	income = screen.getstr(13, 10, 10)
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

def editExpenseY(): # Edit Yearly Expense
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
	screen.clear()
	screen.border(0)
	screen.refresh()
	screen.addstr(9, 10, 'Income:')
	n = 10
	for i in c.execute('select * from income'):
		a = i
		a = str(a)
		screen.addstr(n, 10, a)
		n = n + 1
	screen.addstr(n, 10, "Press Enter")
	pause = screen.getstr(n, 10, 1)

# Main Menu

createTable()

x = 0

while x != ord('9'):
	screen = curses.initscr()
	screen.clear()
	screen.border(0)
	screen.addstr(2, 2, "Main Menu:")
	screen.addstr(4, 4, "1 - Add Income")	
	screen.addstr(5, 4, "2 - Edit Income")
	screen.addstr(6, 4, "3 - View Income")

	screen.addstr(10, 4, "9 - Exit")

	x = screen.getch()

	if x == ord('1'):
		addIncome()
	if x == ord('2'):
		editIncome()
	if x == ord('3'):
		listIncome()

screen.clear()
curses.endwin()

db.commit()
db.close()
