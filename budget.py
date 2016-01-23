#!/usr/bin/python3

import sqlite3
import os
import curses
import re
import datetime

## Need to convert month's in database to number, then edit displays to show month name instead of numbers ##

# Create Database
def createTable():
	c.execute('CREATE TABLE income(name TEXT, amount FLOAT, month TEXT, year INT)')
	c.execute('CREATE TABLE constantMonthly(name TEXT, amount FLOAT)')
	c.execute('CREATE TABLE constantYearly(name TEXT, amount FLOAT, month INT)')
	c.execute('CREATE TABLE varyingMonthly(name TEXT, amount FLOAT, month INT, year INT)')
	db.commit()

### Functions to edit database ###

def startFunc():
	screen.clear()
	screen.border(0)
	screen.refresh()

def convertMonth(month):
	if month == '1' or month == 'jan' or month == 'january':
		month = 'january'
	elif month == '2' or month == 'feb' or month == 'febuary':
		month = 'febuary'
	elif month == '3' or month == 'mar' or month == 'march':
		month = 'march'
	elif month == '4' or month == 'apr' or month == 'april':
		month = 'april'
	elif month == '5' or month == 'may':
		month = 'may'
	elif month == '6' or month == 'jun' or month == 'june':
		month = 'june'
	elif month == '7' or month == 'jul' or month == 'july':
		month = 'july'
	elif month == '8' or month == 'aug' or month == 'august':
		month = 'august'
	elif month == '9' or month == 'sep' or month == 'september':
		month = 'september'
	elif month == '10' or month == 'oct' or month == 'october':
		month = 'october'
	elif month == '11' or month == 'nov' or month == 'november':
		month = 'november'
	elif month == '12' or month == 'dec' or month == 'december':
		month = 'december'
	else:
		month = str(month) + ' is not valid, please update'
	return month

def getMonthNumber(num):
	if num == 'january':
		num = 1
	elif num == 'febuary':
		num = 2
	elif num == 'march':
		num = 3
	elif num == 'april':
		num = 4
	elif num == 'may':
		num = 5
	elif num == 'june':
		num = 6
	elif num == 'july':
		num = 7
	elif num == 'august':
		num = 8
	elif num == 'september':
		num = 9
	elif num == 'october':
		num = 10
	elif num == 'november':
		num = 11
	elif num == 'december':
		num = 12
	else:
		num = str(num) + ' is not valid, please update'
	return num

def getMonth():
	date = datetime.datetime.now()
	month = date.month
	return month

def getYear():
	date = datetime.datetime.now()
	year = date.year
	year = int(year)
	return year

def addIncome(income): # Add income values
	startFunc()
	if income == 'income':
		screen.addstr(4, 4, 'Source of income: ')
		name = screen.getstr(5, 4, 20).decode('utf8')
		name = str(name)
		name = str.lower(name)
		screen.refresh()
		screen.addstr(6, 4, 'Monthly Income:')
		screen.addstr(7, 4, '$')	
		income = screen.getstr(7, 5, 10)
		income = float(income)
		month = 'ALL'
		year = 1
		c.execute('INSERT INTO income VALUES (?, ?, ?, ?)', (name, income, month, year))
	elif income == 'bonus':
		screen.addstr(4, 4, 'Bonus amount:')
		screen.addstr(5, 4, '$')
		income = screen.getstr(5, 5, 10)
		income = float(income)
		name = 'bonus'
		month = getMonth()
		year = getYear()
		c.execute('INSERT INTO income VALUES (?, ?, ?, ?)', (name, income, month, year))
	else:
		pass

def editIncome(): # Edit income
	startFunc()
	showNames('income')
	screen.addstr(4, 4, 'Which income are you updating?: ')
	name = screen.getstr(5, 4, 20)
	name = str(name)
	name = str.lower(name)
	screen.refresh()
	screen.addstr(6, 4, 'New value: ')
	income = screen.getstr(7, 4, 10)
	income = float(income)
	c.execute('UPDATE income SET amount=(?) WHERE name=(?)', (income, name))

def addExpenseM(): # Add Monthly Expense
	startFunc()
	screen.addstr(4, 4, 'Monthly Expense name: ')
	name = screen.getstr(5, 4, 20).decode('utf8')
	name = str(name)
	name = str.lower(name)
	screen.addstr(6, 4, 'Monthly Expense amount: ')
	amount = screen.getstr(7, 4, 10)
	amount = float(amount)
	c.execute('INSERT INTO constantMonthly VALUES (?, ?)', (name, amount))

def editExpenseM(): # Edit Monthly Expense
	startFunc()
	showNames(constantMonthly)
	screen.addstr(4, 4, 'Expense name: ')
	name = screen.getstr(5, 4, 20).decode('utf8')
	name = str(name)
	name = str.lower(name)
	screen.addstr(6, 4, 'Monthly Expense amount: ')
	amount = screen.getstr(7, 4, 10)
	amount = float(income)	
	c.execute('UPDATE constantMonthly SET amount=(?) WHERE name=(?)' (amount, name))


def addExpenseY(): # Add Yearly Expense
	startFunc()
	screen.addstr(4, 4, 'Expense name: ')
	name = screen.getstr(5, 4, 20).decode('utf8')
	name = str(name)
	name = str.lower(name)
	screen.addstr(6, 4, 'Yearly Expense amount: ')
	amount = screen.getstr(7, 4, 10)
	amount = float(amount)
	screen.addstr(8, 4, 'Month of Payment: ')
	month = screen.getstr(9, 4, 10).decode('utf8')
	month = str(month)
	month = str.lower(month)
	month = getMonthNumber(convertMonth(month))
	c.execute('INSERT INTO constantYearly VALUES (?, ?, ?)', (name, amount, month))

def editExpenseY(): # Edit Yearly Expense
	startFunc()
	showNames(constantYearly)
	screen.addstr(4, 4, 'Expense name: ')
	name = screen.getsr(5, 4, 20).decode('utf8')
	name = str(name)
	name = str.lower(name)
	screen.addstr(6, 4, 'Yearly Expense amount: ')
	amount = screen.getstr(7, 4, 10)
	amount = float(income)	
	c.execute('UPDATE constantYearly SET amount=(?) WHERE name=(?)' (amount, name))

def addExpenseV(): # Add montly purchase
	startFunc()
	screen.addstr(4, 4, 'Purchase name: ')
	name = screen.getstr(5, 4, 20).decode('utf8')
	name = str(name)
	name = str.lower(name)
	screen.addstr(6, 4, 'Purchase amount: ')
	amount = screen.getstr(7, 4, 10)
	amount = float(amount)
	month = getMonth()
	year = getYear()
	c.execute('INSERT INTO varyingMonthly VALUES (?, ?, ?, ?)', (name, amount, month, year))

def editExpenseV(): # Edit Monthly Purchase
	startFunc()	
	showNames(caryingMonthly)
	screen.addstr(4, 4, 'Purchase name:')
	name = screen.getsr(5, 4, 20).decode('utf8')
	name = str(name)
	name = str.lower(name)
	screen.addstr(6, 4, 'Purchase amount:')
	amount = screen.getstr(7, 4, 10)
	amount = float(income)
	screen.addstr(8, 4, 'Purchase Month:')
	month = screen.getstr(9, 4, 10)
	month = getMonthNumber(convertMonth(month))
	screen.addstr(9, 4, 'Purchase Year:')
	year = screen.getstr(10, 4, 4)
	c.execute('UPDATE varyingMonthly SET amount=(?) WHERE name=(?) AND month = (?) and year = (?)' (amount, name, month, year))


### View Functions ###

def showNames(db):
	screen.addstr(4, halfx, 'Current Names: ')
	db = str(db)
	c.execute('SELECT name FROM %s' % (db))
	contents = c.fetchall()
	l = 5
	for row in contents:	
		n = 0
		for item in row:
			item = str(item)	
			if n == 0:
				screen.addstr(l, halfx, item )
				l = l + 1
				
def listIncome():
	startFunc()
	# Income
	screen.addstr(2, 4, 'Income:')
	c.execute('SELECT * FROM income WHERE month="ALL"')
	contents = c.fetchall()
	l = 4
	for row in contents:	
		n = 0
		for item in row:
			item = str(item)	
			if n == 0:
				screen.addstr(l, 4, 'Source of income: '+ item)
			elif n == 1:
				screen.addstr(l, 4, 'Monthly salary: $' + "%.2f" % float(item))
			elif n == 2 or n == 3:
				pass
			else:
				screen.addstr(l, 4, 'Derrr.... check the database')
			l = l + 1
			n = n + 1
	# Bonus
	month = str(getMonth())
	month = convertMonth(month)
	year = getYear()
	screen.addstr(l, 4, month.title() + ' bonus:')
	c.execute('SELECT * FROM income WHERE month=(?) AND year=(?)', (month, year))
	contents2 = c.fetchall()
	for row in contents2:
			n = 0
			for item in row:
				item = str(item)	
			if n == 0:
				pass
			elif n == 1:
				if item == null:
					screen.addstr(l, 4, '$0.00')
				else:
					screen.addstr(l, 4, '$' + "%.2f" % float(item))
			elif n == 2 or n == 3:
				pass
			else:
				screen.addstr(l, 4, 'Derrr.... check the database')
			l = l + 1
			n = n + 1

	l = l + 2
	screen.addstr(l, 4, "Press Enter")
	pause = screen.getstr(l, 4, 1)

def listMonthlyC():
	startFunc()
	screen.addstr(2, 4, 'Constant Monthly Expenses:')
	c.execute('SELECT * FROM constantMonthly')
	contents = c.fetchall()
	l = 4
	for row in contents:
		screen.addstr(l, 4, '---')
		l = l + 1
		n = 0
		for item in row:
			item = str(item)	
			if n == 0:
				item = item[1:]
				item = re.sub('[\']', '', item)
				screen.addstr(l, 4, 'Expense: '+ item)
			elif n == 1:
				screen.addstr(l, 4, 'Cost: $' + "%.2f" % float(item))
			else:
				screen.addstr(l, 4, 'Derrr.... check the database')
			l = l + 1
			n = n + 1
	screen.addstr(l, 4, "Press Enter")
	pause = screen.getstr(l, 4, 1)

def listYearly():
	startFunc()
	screen.addstr(2, 4, 'Yearly Expense:')
	c.execute('SELECT * FROM constantYearly')
	contents = c.fetchall()
	l = 4
	for row in contents:
		screen.addstr(l, 4, '---')
		l = l + 1
		n = 0
		for item in row:
			item = str(item)	
			if n == 0:
				screen.addstr(l, 4, 'Expense: '+ item)
			elif n == 1:
				screen.addstr(l, 4, 'Cost: $' + "%.2f" % float(item))
			elif n == 2:
				screen.addstr(l, 4, 'Month: ' + item)
			else:
				screen.addstr(l, 4, 'Derrr.... check the database')
			l = l + 1
			n = n + 1
	screen.addstr(l, 4, "Press Enter")
	pause = screen.getstr(l, 4, 1)

def listPurchases():
	startFunc()
	month = getMonth()
	screen.addstr(2, 4, 'Purchases from ' + month)
	c.execute('SELECT * FROM varyingMonthly WHERE month=(?)', (month,))
	contents = c.fetchall()
	l = 4
	for row in contents:
		screen.addstr(l, 4, '---')
		l = l + 1
		n = 0
		for item in row:
			item = str(item)	
			if n == 0:
				item = item[1:]
				item = re.sub('[\']', '', item)
				screen.addstr(l, 4, 'Purchase: '+ item)
			elif n == 1:
				screen.addstr(l, 4, 'Amount: $' + "%.2f" % float(item))
			l = l + 1
			n = n + 1
	screen.addstr(l, 4, "Press Enter")
	pause = screen.getstr(l, 4, 1)


### DB Queries ###

def totalMonth():
	month = getMonth()
	c.execute('SELECT SUM(amount) FROM constantMonthly')
	totalCM = c.fetchone()[0]
	if totalCM == None:
		totalCM = 0
	c.execute('SELECT SUM(amount) FROM constantYearly WHERE month LIKE (?)', (month,))
	totalCY = c.fetchone()[0]
	if totalCY == None:
		totalCY = 0
	c.execute('SELECT SUM(amount) FROM varyingMonthly WHERE month LIKE (?)', (month,))
	totalVM = c.fetchone()[0]
	if totalVM == None:
		totalVM = 0
	totalM = totalCM + totalCY + totalVM
	totalM = "$"+ "%.2f" % float(totalM)
	return str(totalM)

def totalYear(): # NEEDS UPDATE
	# Get month

	 
	
	c.execute('SELECT SUM(amount) FROM constantMonthly')
	totalCM = c.fetchone()[0]
	if totalCM == None:
		totalCM = 0
	c.execute('SELECT SUM(amount) FROM constantYearly')
	totalCY = c.fetchone()[0]
	if totalCY == None:
		totalCY = 0
	c.execute('SELECT SUM(amount) FROM varyingMonthly WHERE month LIKE (?)', (month,))
	totalVM = c.fetchone()[0]
	if totalVM == None:
		totalVM = 0
	totalM = totalCM + totalCY + totalVM
	totalM = "$"+ "%.2f" % float(totalM)
	return str(totalM)

# App Starts here:

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
	screen.addstr(8, 4, "5 - Goals")
	screen.addstr(10, 4, "9 - Exit")

	screen.addstr(12, 4, "Total Spent This month:")
	screen.addstr(13, 4, totalMonth())



	x = screen.getch()
	
	curses.echo()

	#SubMenu
	
	if x == ord('1'):
		screen.addstr(4, halfx, '[A]dd Income')
		screen.addstr(5, halfx, '[E]dit Income')
		screen.addstr(6, halfx, '[V]iew Income')
		screen.addstr(7, halfx, '[C] Bonus')
		screen.addstr(8, halfx, '[B]ack')
		screen.refresh()
		x = screen.getch()	
			
		if x == ord('A') or x == ord('a'):
			addIncome('income')
		if x == ord('E') or x == ord('e'):
			editIncome()
		if x == ord('V') or x == ord('v'):
			listIncome()
		if x == ord('C') or x == ord('c'):
			addIncome('bonus')

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
		screen.addstr(4, halfx, '[A]dd Purchase')
		screen.addstr(5, halfx, '[E]dit Purchase')
		screen.addstr(6, halfx, '[V]iew Purchase')
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
