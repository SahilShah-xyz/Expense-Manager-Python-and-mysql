import mysql.connector as my
import calendar

def connectNew():
    database = my.connect(host='localhost', user='root', password='')
    return database

def connectExisting():
    database = my.connect(host='localhost', user='root', password='', database='expense_manager')
    return database

def createDatabase():
    database = connectNew()
    cursor = database.cursor()
    cursor.execute('CREATE DATABASE IF NOT EXISTS expense_manager')

def createUserTable():
    database = connectExisting()
    cursor = database.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS clients(id INT AUTO_INCREMENT KEY, email VARCHAR(255), password VARCHAR(255), firstname VARCHAR(255), lastname VARCHAR(255), salary INT(10), daily INT (10))')

def createExpenseTable():
    database = connectExisting()
    cursor = database.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS expenses(id INT AUTO_INCREMENT KEY, date VARCHAR(255), email VARCHAR(255), cost INT(10), type VARCHAR(255), description VARCHAR(255))')


def addClient(email, password, firstname, lastname, salary, daily):
    database = connectExisting()
    cursor = database.cursor()
    query = 'INSERT INTO clients (email, password, firstname, lastname, salary, daily) VALUES (%s, %s, %s, %s, %s, %s)'
    values = (email, password, firstname, lastname, salary, daily)
    cursor.execute(query, values)

    database.commit()

def addExpense(date, email, cost, type, description):
    database = connectExisting()
    cursor = database.cursor()
    query = 'INSERT INTO expenses (date, email, cost, type, description) VALUES (%s, %s, %s, %s, %s)'
    values = (date, email, cost, type, description)
    cursor.execute(query, values)

    database.commit()

def returnName(email):
    database = connectExisting()
    cursor = database.cursor()
    query = 'SELECT firstname FROM clients WHERE email = %s'
    values = (email,)
    cursor.execute(query, values)
    fetchedData = cursor.fetchone()
    return fetchedData

def returnExpenses(email):
    database = connectExisting()
    cursor = database.cursor()
    query = 'SELECT * FROM expenses WHERE email=%s'
    values = (email,)
    cursor.execute(query, values)
    fetchedExpenses = cursor.fetchall()
    return fetchedExpenses

def returnAllExpenses(email):
    database = connectExisting()
    cursor = database.cursor()
    query = 'SELECT cost FROM expenses WHERE email=%s'
    values = (email,)
    cursor.execute(query, values)
    fetchedExpenses = cursor.fetchall()
    return fetchedExpenses

def returnExpensesType(email, type):
    database = connectExisting()
    cursor = database.cursor()
    query = 'SELECT cost FROM expenses WHERE email=%s AND type = %s'
    values = (email, type)
    cursor.execute(query, values)
    fetchedExpenses = cursor.fetchall()
    return fetchedExpenses

def returnExpensesPerDay(email, date):
    database = connectExisting()
    cursor = database.cursor()
    query = 'SELECT cost FROM expenses WHERE email=%s AND date=%s'
    values = (email, date)
    cursor.execute(query, values)
    fetchedExpenses = cursor.fetchall()
    return fetchedExpenses

def returnDates(email):
    database = connectExisting()
    cursor = database.cursor()
    query = 'SELECT date FROM expenses WHERE email=%s'
    values = (email)
    cursor.execute(query, values)
    fetchedDates = cursor.fetchall()
    return fetchedDates

def returnDaily(email):
    database = connectExisting()
    cursor = database.cursor()
    query = 'SELECT daily FROM clients WHERE email = %s'
    values = (email,)
    cursor.execute(query, values)
    fetchedDaily = cursor.fetchone()
    return fetchedDaily


def returnSalary(email):
    database = connectExisting()
    cursor = database.cursor()
    query = 'SELECT salary FROM clients WHERE email = %s'
    values = (email,)
    cursor.execute(query, values)
    fetchedSalary = cursor.fetchone()
    return fetchedSalary

def returnAll(email):
    database = connectExisting()
    cursor = database.cursor()
    query = 'SELECT date, email, cost, type, description FROM expenses WHERE email = %s'
    values = (email,)
    cursor.execute(query, values)
    fetchedData = cursor.fetchall()
    return fetchedData

def returnAllDate(email, date):
    database = connectExisting()
    cursor = database.cursor()
    query = 'SELECT date, email, cost, type, description FROM expenses WHERE email = %s AND date = %s'
    values = (email,date)
    cursor.execute(query, values)
    fetchedData = cursor.fetchall()
    return fetchedData

def returnAllType(email, type):
    database = connectExisting()
    cursor = database.cursor()
    query = 'SELECT date, email, cost, type, description FROM expenses WHERE email = %s AND type = %s'
    values = (email,type)
    cursor.execute(query, values)
    fetchedData = cursor.fetchall()
    return fetchedData

def returnDateType(email, type, date):
    database = connectExisting()
    cursor = database.cursor()
    query = 'SELECT date, email, cost, type, description FROM expenses WHERE email = %s AND type = %s AND date = %s'
    values = (email,type, date)
    cursor.execute(query, values)
    fetchedData = cursor.fetchall()
    return fetchedData

def updateSalary(salary, email):
    database = connectExisting()
    cursor = database.cursor()
    query = 'UPDATE clients SET salary = %s WHERE email = %s'
    values = (salary, email)
    cursor.execute(query, values)
    database.commit()

    query = 'UPDATE clients SET daily = %s WHERE email = %s'
    days = calendar.monthrange(2021, 10)[1]
    daily = salary//days
    values = (daily, email)
    cursor.execute(query, values)
    database.commit()

def returnPassword(email):
    database = connectExisting()
    cursor = database.cursor()
    query = 'SELECT password FROM clients WHERE email = %s'
    values = (email,)
    cursor.execute(query, values)
    fetchedPassword = cursor.fetchone()
    return fetchedPassword

def initialize():
    createDatabase()
    createExpenseTable()
    createUserTable()

