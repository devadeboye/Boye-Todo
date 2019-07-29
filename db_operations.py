import psycopg2

def db_operation(action, name):
    """
    CREATE or DROP a PostgreSQL database . it relies on psycopg2
    module to connect to postgreSQL.

    it recieves two parameters (action and name).
    
    PARAMETERS
    - action can be either 1 or 0. with 1 standing for 
      CREATE and 0 standing for DROP.

    - name is the name of the db.
    """

    # check if action command is valid
    if action == 1 or action == 0:
        # try to connect
        try:
            # connection parameters
            connection = psycopg2.connect(user = 'postgres',
            password = "1b2u3s4t",
            host = 'localhost',
            port = '5432')

            # create cursor object
            cursor = connection.cursor()

            # change isolation level
            connection.set_isolation_level(0)
            
            #-------------------------------------------------------
            # NOTE: the isolation level above was changed because
            # db creation and deletion will not occur without them 
            # because postgre doesn't create or delete db within a
            # transaction block
            #--------------------------------------------------------

            if action == 1:
                # execute the creation command
                cursor.execute('CREATE DATABASE {}'.format(name))
                connection.commit()
                print('db {} created successfully'.format(name))
            elif action == 0:
                # execute the creation command
                cursor.execute('DROP DATABASE {}'.format(name))
                connection.commit()
                print('db {} has been dropped'.format(name))

        except (Exception, psycopg2.Error) as error:
            print(error, 'operation failed')

        finally:
            if (connection):
                print('closing connection')
                cursor.close()
                connection.close()
                print('connectiion closed')

    # raise error for invalid command
    else:
        raise ValueError('action can only be 1 or 0')