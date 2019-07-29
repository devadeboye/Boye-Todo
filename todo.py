import psycopg2

class Todo:
    def __init__(self):
        self.qty_completed = 0
        self.qty_uncompleted = 0


    def insert_item(self, t):
        """
        insert an item into the db.

        Takes a single argument (t) which is the activity
        to be added.
        """

        # try to connect to db
        try:
            connection = psycopg2.connect(user = "postgres",
            password = "1b2u3s4t",
            host = "localhost",
            port = "5432",
            database = "todo")

            # create cursor object
            cursor = connection.cursor()

            # insertion statement
            insertion = """ INSERT INTO task (name) VALUES ('{}')
            """.format(t)

            print('checking validity')
            # check the validity of t
            if len(t) > 2:
                cursor.execute(insertion)

                # commit changes
                connection.commit()
                print('Record inserted successfully')
            else:
                print('input is empty, pls write something')

        except (Exception, psycopg2.Error) as error:
            print('operation failed', error)
        
        finally:
            # close connection if active
            if(connection):
                cursor.close()
                connection.close()
                #print('connection closed')


    def remove_item(self, idd):
        """Remove item from the db
        
        idd is the id of the item to removed
        """
        # try to connect to db
        try:
            connection = psycopg2.connect(user = "postgres",
            password = "1b2u3s4t",
            host = "localhost",
            port = "5432",
            database = "todo")

            # create cursor object
            cursor = connection.cursor()
            # delete statement
            del_stat = """ DELETE FROM task WHERE id = {}
            """.format(idd)
            # execute the delete statement
            cursor.execute(del_stat)
            connection.commit()
            #print('operation successful')

        except (Exception, psycopg2.Error) as error:
            print('operation failed', error)

        finally:
            # check if connection is active
            if(connection):
                cursor.close()
                connection.close()
                #print('connection closed')


    def edit_item(self, idd, nw):
        """
        idd = id of the task
        nw = the correction
        """
        # try to connect to db
        try:
            connection = psycopg2.connect(user = "postgres",
            password = "1b2u3s4t",
            host = "localhost",
            port = "5432",
            database = "todo")

            # create cursor object
            cursor = connection.cursor()
            # update statement
            update_stat = """ UPDATE task SET name = '{}' 
            WHERE id = {}""".format(nw, idd)
            # execute update statement
            cursor.execute(update_stat)
            connection.commit()
            print('success!, data has been updated')

        except (Exception, psycopg2.Error) as error:
            print('operation failed', error)

        finally:
            # check if connection is active
            if(connection):
                cursor.close()
                connection.close()
                #print('connection closed')


    def view_all(self):
        """Returns the element of the db"""
        # try to connect to db
        try:
            connection = psycopg2.connect(user = "postgres",
            password = "1b2u3s4t",
            host = "localhost",
            port = "5432",
            database = "todo")

            # create cursor object
            cursor = connection.cursor()
            # selection statement
            sel_stat = """ SELECT * FROM task """

            # execute the sel_stat
            cursor.execute(sel_stat)
            connection.commit()
            # fetch the db content
            activities = cursor.fetchall()
            return activities

        except (Exception, psycopg2.Error) as error:
            print('could not get content from db', error)

        finally:
            # check if connection is open
            if (connection):
                # close connection
                cursor.close()
                connection.close()
                #print('connection closed')