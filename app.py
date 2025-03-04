from flask import Flask,render_template,url_for
from dotenv import load_dotenv
import mysql.connector
import os

load_dotenv()

host = os.getenv('host')
user = os.getenv('user')
password= os.getenv('password')
db = os.getenv('db')
database1=os.getenv('database1')
database2=os.getenv('database2')
database3=os.getenv('database3')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/about")
def welcome():
	return render_template("about.html")

@app.route('/contact')
def contact():
     return render_template('contact.html')

@app.route('/funds')
def fund():
    return render_template("funds.html")

@app.route("/schemes")
def schemes():
    conn = mysql.connector.connect(
    host=host,
    db=db,
    user=user,
    password=password)

    # cursor = conn.cursor()
    # query="SELECT * FROM fund_data"
    # cursor.execute(query)

    # sch_data=cursor.fetchall()
    # conn.close()
    
    # cursor = conn.cursor()
    # query="SELECT * FROM swap"
    # cursor.execute(query)
    
    # swap_data=cursor.fetchall()
    # conn.close()

    cursor = conn.cursor()
    query="SELECT * FROM smartcity"
    cursor.execute(query)
    smart_data=cursor.fetchall()

    cursor = conn.cursor()
    query="SELECT * FROM uids"
    cursor.execute(query)
    uids_data=cursor.fetchall()
    conn.close()
    
    return render_template("sch.html",data2=smart_data,data3=uids_data)

@app.route('/boardofdirectors')
def bod():
    conn = mysql.connector.connect(
    host=host,
    database=database1,
    user=user,
    password=password)

    cursor = conn.cursor()
    query="SELECT * FROM bod_data"
    cursor.execute(query)

    bod_data=cursor.fetchall()
    conn.close()
    return render_template('boardofdirectors.html', data=bod_data)

if __name__ == "__main__":
    app.run(debug=True)