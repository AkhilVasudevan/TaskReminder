import sqlite3
from sqlite3 import Error

def getConn():
    try:
        sqliteConnection = sqlite3.connect('./DB/Task_Reminder.db')
        sqlite_create_table_query = """CREATE TABLE IF NOT EXISTS Task_Master (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                title TEXT NOT NULL,
                                alert_date datetime NOT NULL,
                                alert_time datetime NOT NULL);"""
        cursor = sqliteConnection.cursor()
        cursor.execute(sqlite_create_table_query)
        sqliteConnection.commit()
        cursor.close()
        return sqliteConnection
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)

def InsertTask(title,alert_date,alert_time):
    try:
        sqliteConnection = getConn()
        cursor = sqliteConnection.cursor()
        sqlite_insert_query = """INSERT INTO Task_Master(title,alert_date,alert_time) 
                            VALUES (?,?,?)"""
        parameters=(title,alert_date,alert_time)
        count = cursor.execute(sqlite_insert_query,parameters)
        sqliteConnection.commit()
        cursor.close()
        return True
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
        return False
    finally:
        if (sqliteConnection):
            sqliteConnection.close()

def GetAllTasks():
    try:
        sqliteConnection = getConn()
        cursor = sqliteConnection.cursor()
        sqlite_select_query = """SELECT * from Task_Master"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        cursor.close()
        return records
    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
        return []
    finally:
        if (sqliteConnection):
            sqliteConnection.close()

def GetTasksByDateTime(cur_date,cur_time):
    try:
        sqliteConnection = getConn()
        cursor = sqliteConnection.cursor()
        sqlite_select_query = """SELECT * from Task_Master where alert_date<=? and alert_time<=?"""
        parameter=(cur_date,cur_time)
        cursor.execute(sqlite_select_query,parameter)
        records = cursor.fetchall()
        cursor.close()
        return records
    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
        return []
    finally:
        if (sqliteConnection):
            sqliteConnection.close()

def GetTasksByGreaterDate(cur_date):
    try:
        sqliteConnection = getConn()
        cursor = sqliteConnection.cursor()
        sqlite_select_query = """SELECT * from Task_Master where alert_date>=?"""
        parameter=(cur_date,)
        cursor.execute(sqlite_select_query,parameter)
        records = cursor.fetchall()
        cursor.close()
        return records
    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
        return []
    finally:
        if (sqliteConnection):
            sqliteConnection.close()

def EditTask(id,title,alert_date,alert_time):
    try:
        sqliteConnection = getConn()
        cursor = sqliteConnection.cursor()
        sql_update_query = """Update Task_Master set title=?,alert_date=?,alert_time=? where id = ?"""
        parameters=(title,alert_date,alert_time,id)
        cursor.execute(sql_update_query,parameters)
        sqliteConnection.commit()
        cursor.close()
        return True
    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
        return False
    finally:
        if (sqliteConnection):
            sqliteConnection.close()

def DeleteTask(id):
    try:
        sqliteConnection = getConn()
        cursor = sqliteConnection.cursor()
        sql_delete_query = """DELETE from Task_Master where id = ?"""
        parameters=(id,)
        cursor.execute(sql_delete_query,parameters)
        sqliteConnection.commit()
        cursor.close()
        return True
    except sqlite3.Error as error:
        print("Failed to delete record from sqlite table", error)
        return False
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
