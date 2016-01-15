#!/usr/bin/python3

import sqlite3
import os
import curses
import re
import datetime

# Create Database
def createTable():
	c.execute('CREATE TABLE income(name TEXT, amount FLOAT)')
	c.execute('CREATE TABLE constantMonthly(name TEXT, amount FLOAT)')
	c.execute('CREATE TABLE constantYearly(name TEXT, amount FLOAT, month TEXT)')
	c.execute('CREATE TABLE varyingMonthly(name TEXT, amount FLOAT, month TEXT)')
	db.commit()

### Functions to edit database ###

def startFunc():
	screen.clear()
	screen.border(0)
	screen.refresh()

def convertMonth(month):
	if (month == 1) or (month == 'jan') or (month == 'january'):
		month = 'january'
	elif (month == 2) or (month == 'feb') or (month == 'febuary'):
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
	showNames('income')
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
	c.execute('INSERT INTO constantMonthly VALUES (?, ?)', (name, amount))

def editExpenseM(): # Edit Monthly Expense
	startFunc()
	showNames(constantMonthly)
	screen.addstr(10, 10, 'Expense name: ')
	name = screen.getstr(11, 10, 20)
	name = str(name)
	name = str.lower(name)
	screen.addstr(12, 10, 'Monthly Expense amount: ')
	amount = screen.getstr(13, 10, 10)
	amount = float(income)	
	c.execute('UPDATE constantMonthly SET amount=(?) WHERE name=(?)' (amount, name))


def addExpenseY(): # Add Yearly Expense
	startFunc()
	screen.addstr(10, 10, 'Expense name: ')
	name = screen.getstr(11, 10, 20)
	name = str(name)
	name = str.lower(name)
	screen.addstr(12, 10, 'Yearly Expense amount: ')
	amount = screen.getstr(13, 10, 10)
	amount = float(amount)
	screen.addstr(14, 10, 'Month of Payment: ')
	month = screen.getstr(15, 10, 10)
	month = str(month)
	month = str.lower(month)
	c.execute('INSERT INTO constantYearly VALUES (?, ?, ?)', (name, amount, month))

def editExpenseY(): # Edit Yearly Expense
	startFunc()
	showNames(constantYearly)
	screen.addstr(10, 10, 'Expense name: ')
	name = screen.getsr(11, 10, 20)
	name = str(name)
	name = str.lower(name)
	screen.addstr(12, 10, 'Monthly Expense amount: ')
	amount = screen.getstr(13, 10, 10)
	amount = float(income)	
	c.execute('UPDATE constantYearly SET amount=(?) WHERE name=(?)' (amount, name))

def addExpenseV(): # Add montly purchase
	startFunc()
	screen.addstr(10, 10, 'Purchase name: ')
	name = screen.getstr(11, 10, 20)
	name = str(name)
	name = str.lower(name)
	screen.addstr(12, 10, 'Purchase amount: ')
	amount = screen.getstr(13, 10, 10)
	amount = float(amount)
	screen.addstr(14, 10, 'Month: ')
	date = datetime.datetime.now()
	month = date.month
	month = convertMonth(month)
	month = str(month)
	c.execute('INSERT INTO varyingMonthly VALUES (?, ?, ?)', (name, amount, month))

def editExpenseV(): # Edit Monthly Purchase
	startFunc()	
	showNames(caryingMonthly)
	screen.addstr(10, 10, 'Purchase name: ')
	name = screen.getsr(11, 10, 20)
	name = str(name)
	name = str.lower(name)
	screen.addstr(12, 10, 'Purchase amount: ')
	amount = screen.getstr(13, 10, 10)
	amount = float(income)
	screen.addstr(14, 10, 'Purchase Month: ')
	month = screen.getstr(15, 10, 10)
	c.execute('UPDATE varyingMonthly SET amount=(?) WHERE name=(?) AND month = (?)' (amount, name, month))


### View Functions ###

def showNames(db):
	screen.addstr(10, halfx, 'Current Names: ')
	db = str(db)
	c.execute('SELECT * FROM %s' % (db))
	contents = c.fetchall()
	l = 10
	for row in contents:	
		n = 0
		for item in row:
			item = str(item)	
			if n == 0:
				item = item[1:]
				item = re.sub('[\']', '', item)
				screen.addstr(l, halfx, item )
				l = l + 1
			elif n == 1:
				screen.addstr(l, halfx, '%.2f' % float(item) + '\n')
				l = l + 1

def listIncome():
	startFunc()
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
	startFunc()
	screen.addstr(9, 10, 'Constant Monthly Expenses:')
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
			else:
				screen.addstr(l, 10, 'Derrr.... check the database')
			l = l + 1
			n = n + 1
	screen.addstr(l, 10, "Press Enter")
	pause = screen.getstr(l, 10, 1)

def listYearly():
	startFunc()
	screen.addstr(9, 10, 'Yearly Expense:')
	c.execute('select * from constantYearly')
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

def listPurchases():
	startFunc()
	#Get Month
	date = datetime.datetime.now()
	month = date.month
	month = convertMonth(month)
	month = str(month)
	screen.addstr(8, 10, month)
	screen.addstr(9, 10, 'Purchases This month:')
	c.execute('SELECT * FROM varyingMonthly WHERE month=(?)', (month,))
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
				screen.addstr(l, 10, 'Purchase: '+ item)
			elif n == 1:
				screen.addstr(l, 10, 'Amount: $' + "%.2f" % float(item))
			l = l + 1
			n = n + 1
	screen.addstr(l, 10, "Press Enter")
	pause = screen.getstr(l, 10, 1)



# Connect to DB file
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
	win = screen.getmaxyx()
	halfx = int(win[1]/2)
	halfy = int(win[0]/2)
	curses.noecho()
	screen.clear()
	screen.border(0)
	screen.addstr(2, 2, "Main Menu:")
	screen.addstr(4, 4, "1 - Income")	
	screen.addstr(5, 4, "2 - Constant Monthly Expenses")
	screen.addstr(6, 4, "3 - Constant Yearly Expenses")
	screen.addstr(7, 4, "4 - Purchases")

	screen.addstr(9, 4, "9 - Exit")

	x = screen.getch()
	
	curses.echo()

	#SubMenu
	
	if x == ord('1'):
		screen.addstr(4, halfx, '[A]dd Income')
		screen.addstr(5, halfx, '[E]dit Income')
		screen.addstr(6, halfx, '[V]iew Income')
		screen.addstr(7, halfx, '[B]ack')
		screen.refresh()
		x = screen.getch()	
			
		if x == ord('A') or x == ord('a'):
			addIncome()
		if x == ord('E') or x == ord('e'):
			editIncome()
		if x == ord('V') or x == ord('v'):
			listIncome()

	if x == ord('2'):
		screen.addstr(4, halfx, '[A]dd Constant Monthly Expense')
		screen.addstr(5, halfx, '[E]dit Constant Monthly Expense')
		screen.addstr(6, halfx, '[V]iew Constant Monthly Expenses')
		screen.addstr(7, halfx, '[B]ack')
		screen.refresh()
		x = screen.getch()	
			
		if x == ord('A') or x == ord('a'):
			addExpenseM()
		if x == ord('E') or x == ord('e'):
			editExpenseM()
		if x == ord('V') or x == ord('v'):
			listMonthlyC()

	if x == ord('3'):
		screen.addstr(4, halfx, '[A]dd Constant Yearly Expense')
		screen.addstr(5, halfx, '[E]dit Constant Yearly Expense')
		screen.addstr(6, halfx, '[V]iew Constant Yearly Expenses')
		screen.addstr(7, halfx, '[B]ack')
		screen.refresh()
		x = screen.getch()	
			
		if x == ord('A') or x == ord('a'):
			addExpenseY()
		if x == ord('E') or x == ord('e'):
			editExpenseY()
		if x == ord('V') or x == ord('v'):
			listYearly()

	if x == ord('4'):
		screen.addstr(4, halfx, '[A]dd Varying Monthly Expense')
		screen.addstr(5, halfx, '[E]dit Varying Monthly Expense')
		screen.addstr(6, halfx, '[V]iew Varying Monthly Expenses')
		screen.addstr(7, halfx, '[B]ack')
		screen.refresh()
		x = screen.getch()	
			
		if x == ord('A') or x == ord('a'):
			addExpenseV()
		if x == ord('E') or x == ord('e'):
			editExpenseV
		if x == ord('V') or x == ord('v'):
			listPurchases()


screen.clear()
curses.endwin()

db.commit()
db.close()
