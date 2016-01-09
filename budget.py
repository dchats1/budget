#!/usr/bin/python

import sqlite3
import os
import os.path

db = 'budget.db'
monthlyIncome = 'Monthly_Income'
knownBills = 'Known_Bills'

#Check if sqlite file exists
if os.path.isfile('budget.db'): # Connect to database
	conn = sqlite3.connect(db)
	c = conn.cursor()
	print 'Connecting to database'
else: # Build database
	conn = sqlite3.connect(db)
	c = conn.cursor()
	c.execute('''CREATE TABLE user
			(monthlyIncome integer)''')
	monthly = int(raw_input('What is your monthly income? '))
	c.execute('INSERT INTO user VALUES (?)', (monthly))
	c.execute('SELECT * FROM user')
	print (c.fetchone())
#	c.execute('SHOW TABLES;')
	print 'Created database'


#c.execute('CREATE TABLE {tn} ({nf} {ft})'\
#	.format(tn=knownBills, nf='' )


# Commit and close connection to database
conn.commit()
conn.close()
