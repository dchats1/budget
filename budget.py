#!/usr/bin/python3

import sqlite3
import os

db = sqlite3.connect(':memory:')

c = db.cursor()

shouldExit = False

#Create Database
def createTable():
	c.execute('CREATE TABLE income(name TEXT, amount FLOAT)')
	c.execute('CREATE TABLE constantMonthly(name TEXT, amount FLOAT, month TEXT)')
	c.execute('CREATE TABLE constantYearly(name TEXT, amount FLOAT, month TEXT)')
	c.execute('CREATE TABLE varyingMonthly(name TEXT, amount FLOAT, month TEXT)')
	db.commit()

createTable()

def addIncome():
	name = input('Source of income: ')
	name = str(name)
	income = input('Monthly Income: ')
	income = float(income)
	c.execute('INSERT INTO income VALUES (?, ?)', (name, income))
	db.commit()

def editIncome():
	name = input('Which income are you updating?: ')
	name = str(name)
	income = input('New value: ')
	income = float(income)
	c.execute('UPDATE income SET amount=(?) WHERE name=(?)', (income, name))
	db.commit()

def addExpenseM():
	name = input('Monthly Expense name: ')
	name = str(name)
	amount = input('Monthly Expense amount: ')
	amount = float(income)
	c.execute('INSERT INTO constantMonthly VALUES (?, ?)', (name, amount))
	db.commit()

def addExpenseY():
	name = input('Yearly Expense name: ')
	name = str(name)
	amount = input('Yearly Expense amount: ')
	amount = float(income)
	c.execute('INSERT INTO constantYearly VALUES (?, ?)', (name, amount))
	db.commit()

def listIncome():
	for i in c.execute('select * from income'):
		print(i)

def controls():
	global shouldExit
	print('Menu:')

db.commit()
db.close()
