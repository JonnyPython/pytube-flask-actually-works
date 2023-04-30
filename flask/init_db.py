import os
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="flask_db",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'])

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS sites;')
cur.execute('CREATE TABLE sites (id serial PRIMARY KEY,'
                                 'url varchar (150) NOT NULL,'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);')


cur.execute('INSERT INTO sites (url)'
            'VALUES (%s)',
            ('https://www.youtube.com/watch?v=GAboygK-XhE',))

conn.commit()

cur.close()
conn.close()
