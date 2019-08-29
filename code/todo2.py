import sqlite3
import os
import getOs

class Todo:
    def __init__(self):
        self.qty_completed = 0
        self.qty_uncompleted = 0
        # check if directory exist
        try:
            if getOs.get_platform() == 'linux':
                # create a db
                self.db = sqlite3.connect('/home/ea/Documents/puta/task.db')
            elif getOs.get_platform() == 'windows':
                # create a db
                self.db = sqlite3.connect('c:/Documents/puta/task.db')

            # get a cursor object
            self.cur = self.db.cursor()

            # create a table if it doesn't exist
            self.cur.execute(""" CREATE TABLE IF NOT EXISTS 
            task(id INTEGER PRIMARY KEY, name TEXT )""")
            self.db.commit()
        except sqlite3.OperationalError:
            # check for os type
            if getOs.get_platform() == 'linux':
                # create a directory
                os.mkdir('/home/ea/Documents/puta/')
                # create a db
                self.db = sqlite3.connect('/home/ea/Documents/puta/task.db')
            elif getOs.get_platform() == 'windows':
                # create a directory
                os.mkdir('/home/ea/Documents/puta/')
                # create a db
                self.db = sqlite3.connect('c:/Documents/puta/task.db')

            # get a cursor object
            self.cur = self.db.cursor()

            # create a table if it doesn't exist
            self.cur.execute(""" CREATE TABLE IF NOT EXISTS 
            task(id INTEGER PRIMARY KEY, name TEXT )""")
            self.db.commit()


    def insert_item(self, t):
        """
        insert an item into the db.

        Takes a single argument (t) which is the activity
        to be added.
        """

        # try to connect to db
        try:
            if getOs.get_platform() == 'linux':
                # create a db
                self.db = sqlite3.connect('/home/ea/Documents/puta/task.db')
            elif getOs.get_platform() == 'windows':
                # create a db
                self.db = sqlite3.connect('c:/Documents/puta/task.db')

            # get a cursor object
            self.cur = self.db.cursor()
            #print('checking validity')
            # check the validity of t
            if len(t) > 2:
                # insertion statement
                self.cur.execute(" INSERT INTO task (name)\
                VALUES (?)", (t,))

                # commit changes
                self.db.commit()
                #print('Record inserted successfully')
            else:
                raise ValueError('input is empty, pls write something')
                # write a code later to handle this
                # exception by firing a pop-up box
                # containing the warning.
        except:
            print('operation failed')
            #raise Exception()
        
        finally:
            # close connection if active
            if(self.db):
                self.cur.close()
                self.db.close()
                #print('connection closed')


    def remove_item(self, idd):
        """Remove item from the db
        
        idd is the id of the item to removed
        """
        # try to connect to db
        try:
            if getOs.get_platform() == 'linux':
                # create a db
                self.db = sqlite3.connect('/home/ea/Documents/puta/task.db')
            elif getOs.get_platform() == 'windows':
                # create a db
                self.db = sqlite3.connect('c:/Documents/puta/task.db')

            # get a cursor object
            self.cur = self.db.cursor()

            # delete statement
            self.cur.execute(""" DELETE FROM task WHERE id = ?
            """, (idd,))
            self.db.commit()
            #print('operation successful')

        except:
            print('operation failed')

        finally:
            # check if connection is active
            if(self.db):
                self.cur.close()
                self.db.close()
                #print('connection closed')


    def edit_item(self, idd, nw):
        """
        idd = id of the task
        nw = the correction
        """
        # try to connect to db
        try:
            if getOs.get_platform() == 'linux':
                # create a db
                self.db = sqlite3.connect('/home/ea/Documents/puta/task.db')
            elif getOs.get_platform() == 'windows':
                # create a db
                self.db = sqlite3.connect('c:/Documents/puta/task.db')

            # get a cursor object
            self.cur = self.db.cursor()

            # update statement
            self.cur.execute(""" UPDATE task SET name =? 
            WHERE id = ?""", (nw, idd))
            self.db.commit()
            print('success!, data has been updated')

        except:
            print('operation failed')

        finally:
            # check if connection is active
            if(self.db):
                self.cur.close()
                self.db.close()
                #print('connection closed')


    def view_all(self):
        """Returns the element of the db"""
        # try to connect to db
        try:
            if getOs.get_platform() == 'linux':
                # create a db
                self.db = sqlite3.connect('/home/ea/Documents/puta/task.db')
            elif getOs.get_platform() == 'windows':
                # create a db
                self.db = sqlite3.connect('c:/Documents/puta/task.db')

            # get a cursor object
            self.cur = self.db.cursor()

            # selection statement
            self.cur.execute(""" SELECT * FROM task """)
            self.db.commit()
            # fetch the db content
            activities = self.cur.fetchall()
            return activities

        except:
            print('could not get content from db')

        finally:
            # check if connection is open
            if (self.db):
                # close connection
                self.cur.close()
                self.db.close()
                #print('connection closed')


    def dict_db_content(self):
        """
        stores the content of the db in a dictionary data
        structure.
        """
        db_cont = self.view_all()
        # created to store the db content in a dict format
        dict_format = dict()
        for n in db_cont:
            dict_format[n[1]] = n[0]
        return dict_format
