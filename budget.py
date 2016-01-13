#!/usr/bin/python3

import sqlite3
import os
import curses
import re

# Create Database
def createTable():
	c.execute('CREATE TABLE income(name TEXT, amount FLOAT)')
	c.execute('CREATE TABLE constantMonthly(name TEXT, amount FLOAT, month TEXT)')
	c.execute('CREATE TABLE constantYearly(name TEXT, amount FLOAT, month TEXT)')
	c.execute('CREATE TABLE varyingMonthly(name TEXT, amount FLOAT, month TEXT)')
	db.commit()

### Functions to edit database ###

def startFunc():
	screen.clear()
	screen.border(0)
	screen.refresh()

def convertMonth(month):
	if (month == '1') or (month == 'jan') or (month == 'january'):
		month = 'january'
	elif (month == '2') or (month == 'feb') or (month == 'febuary'):
		month = 'febuary'
	elif (month == 3) or (month == 'mar') or (month == 'march'):
		month = 'march'
	elif (month == 4) or (month == 'apr') or (month == 'april'):
		month = 'april'
	elif (month == 5) or (month == 'may'):
		month = 'may'
	elif (month == 6) or (month == 'jun') or (month == 'june'):
		month = 'june'
	elif (month == 7) or (month == 'jul') or (month == 'july'):
		month = 'july'
	elif (month == 8) or (month == 'aug') or (month == 'august'):
		month = 'august'
	elif (month == 9) or (month == 'sep') or (month == 'september'):
		month = 'september'
	elif (month == 10) or (month == 'oct') or (month == 'october'):
		month = 'october'
	elif (month == 11) or (month == 'nov') or (month == 'november'):
		month = 'november'
	elif (month == 12) or (month == 'dec') or (month == 'december'):
		month = 'december'
	else:
		month = 'Invalid Month, please update'
	return month

def addIncome(): # Add income values
	startFunc()
	screen.addstr(10, 10, 'Source of income: ')
	name = screen.getstr(11, 10, 20)
	name = str(name)
	name = str.lower(name)
	screen.refresh()
	screen.addstr(12, 10, 'Monthly Income: ')
	income = screen.getstr(13, 10, 10)
	income = float(income)
	c.execute('INSERT INTO income VALUES (?, ?)', (name, income))

def editIncome(): # Edit income
	startFunc()
	screen.addstr(10, 10, 'Which income are you updating?: ')
	name = screen.getstr(11, 10, 20)
	name = str(name)
	name = str.lower(name)
	screen.refresh()
	screen.addstr(12, 10, 'New value: ')
	income = screen.getstr(13, 10, 10)
	income = float(income)
	c.execute('UPDATE income SET amount=(?) WHERE name=(?)', (income, name))

def addExpenseM(): # Add Monthly Expense
	startFunc()
	screen.addstr(10, 10, 'Monthly Expense name: ')
	name = screen.getstr(11, 10, 20)
	name = str(name)
	name = str.lower(name)
	screen.addstr(12, 10, 'Monthly Expense amount: ')
	amount = screen.getstr(13, 10, 10)
	amount = float(amount)
	screen.addstr(14, 10, 'Month: ')
	month = screen.getstr(15, 10, 10)
	month = str(month)
	month = str.lower(month)
	month = convertMonth(month)
	c.execute('INSERT INTO constantMonthly VALUES (?, ?, ?)', (name, amount, month))

def editExpenseM(): # Edit Monthly Expense
	startFunc()
	screen.addstr(10, 10, 'Expense name: ')
	name = screen.getstr(11, 10, 20)
	name = str(name)
	name = str.lower(name)
	screen.addstr(12, 10, 'Monthly Expense amount: ')
	amount = screen.getstr(13, 10, 10)
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
				screen.addstr(l, 10, 'Monthly salary: $' + "%.2f" % float(item))
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
		l = l + 1
		n = 0
		for item in row:
			item = str(item)	
			if n == 0:
				item = item[1:]
				item = re.sub('[\']', '', item)
				screen.addstr(l, 10, 'Expense: '+ item)
			elif n == 1:
				screen.addstr(l, 10, 'Cost: $' + "%.2f" % float(item))
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

if os.path.isfile('./sqliteBudget.db'):
	db = sqlite3.connect('sqliteBudget.db')
	c = db.cursor()
else:	
	db = sqlite3.connect('sqliteBudget.db')
	c = db.cursor()
	createTable()
	
# Main Menu

x = 0

while x != ord('9'):
	screen = curses.initscr()
	curses.noecho()
	screen.clear()
	screen.border(0)
	screen.addstr(2, 2, "Main Menu:")
	screen.addstr(4, 4, "1 - Add Income")	
	screen.addstr(5, 4, "2 - Edit Income")
	screen.addstr(6, 4, "3 - View Income")
	screen.addstr(7, 4, "4 - Add Monthly Expense")
	screen.addstr(8, 4, "5 - Edit Constant Monthly Expenses")
	screen.addstr(9, 4, "6 - View Constant Monthly Expenses")

	screen.addstr(10, 4, "9 - Exit")

	x = screen.getch()
	
	curses.echo()
	
	if x == ord('1'):
		addIncome()
	if x == ord('2'):
		editIncome()
	if x == ord('3'):
		listIncome()
	if x == ord('4'):
		addExpenseM()
	if x == ord('5'):
		editExpenseM()
	if x == ord('6'):
		listMonthlyC()

screen.clear()
curses.endwin()

db.commit()
db.close()
