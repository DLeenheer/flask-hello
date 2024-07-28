from flask import Flask
import psycopg2


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World from Dana Leenheer in 3308!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://hello_dana_user:2lIRg498XAKrdhUz9MWzGFGZ2ZWKr1Cb@dpg-cqjcbg6ehbks73c9kia0-a/hello_dana")
    conn.close()
    return 'Database Connection Successful'

@app.route('/db_create')
def creating():
    conn = psycopg2.connect("postgresql://hello_dana_user:2lIRg498XAKrdhUz9MWzGFGZ2ZWKr1Cb@dpg-cqjcbg6ehbks73c9kia0-a/hello_dana")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball (
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"

@app.route('/db_insert')
def inserting():
    conn = psycopg2.connect("postgresql://hello_dana_user:2lIRg498XAKrdhUz9MWzGFGZ2ZWKr1Cb@dpg-cqjcbg6ehbks73c9kia0-a/hello_dana")
    cur = conn.cursor()
    cur.execute('''
        Insert INTO Basketball (First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Populated"