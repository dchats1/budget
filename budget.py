#!/usr/bin/python3

import sqlite3
import os
import curses
import re

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
	screen.clear()
	screen.border(0)
	screen.refresh()
	screen.addstr(10, 10, 'Monthly Expense name: ')
	name = screen.getstr(11, 10, 15)
	name = str(name)
	name = str.lower(name)
	screen.addstr(12, 10, 'Monthly Expense amount: ')
	amount = screen.getstr(13, 10, 10)
	amount = float(amount)
	screen.addstr(14, 10, 'Month: ')
	month = screen.getstr(15, 10, 10)
	month = str(month)
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

### View Functions ###

def listIncome():
	screen.clear()
	screen.border(0)
	screen.refresh()
	screen.addstr(9, 10, 'Income:')
	c.execute('select * from income')
	contents = c.fetchall()
	l = 10
	for row in contents:	
		n = 0
		for item in row:
			item = str(item)	
			if n == 0:
				item = item[1:]
				item = re.sub('[\']', '', item)
				screen.addstr(l, 10, 'Source of income: '+ item)
			elif n == 1:
				screen.addstr(l, 10, 'Monthly salary: $' + item)
			else:
				screen.addstr(l, 10, 'Derrr.... check the database')
			l = l + 1
			n = n + 1
	screen.addstr(l, 10, "Press Enter")
	pause = screen.getstr(l, 10, 1)

def listMonthlyC():
	screen.clear()
	screen.border(0)
	screen.refresh()
	screen.addstr(9, 10, 'Constant Monthly Expense:')
	c.execute('select * from constantMonthly')
	contents = c.fetchall()
	l = 10
	for row in contents:
		screen.addstr(l, 10, '---')
		n = 0
		for item in row:
			item = str(item)	
			if n == 0:
				item = item[1:]
				item = re.sub('[\']', '', item)
				screen.addstr(l, 10, 'Expense: '+ item)
			elif n == 1:
				screen.addstr(l, 10, 'Cost: $' + item)
			elif n == 2:
				item = item[1:]
				item = re.sub('[\']', '', item)
				screen.addstr(l, 10, 'Month: ' + item)
			else:
				screen.addstr(l, 10, 'Derrr.... check the database')
			l = l + 1
			n = n + 1
	screen.addstr(l, 10, "Press Enter")
	pause = screen.getstr(l, 10, 1)


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
	screen.addstr(7, 4, "4 - Add Monthly Expense")
	screen.addstr(8, 4, "5 - View Constant Monthly Expenses")

	screen.addstr(10, 4, "9 - Exit")

	x = screen.getch()

	if x == ord('1'):
		addIncome()
	if x == ord('2'):
		editIncome()
	if x == ord('3'):
		listIncome()
	if x == ord('4'):
		addExpenseM()
	if x == ord('5'):
		listMonthlyC()

screen.clear()
curses.endwin()

db.commit()
db.close()
