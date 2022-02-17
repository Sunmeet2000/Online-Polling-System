import sqlite3
import os.path
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

# @app.route("/login")
# def login():
#     return render_template("login.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        #print("andar")
        username = request.form.get("uname")
        password = request.form.get("pass")
        # print(username)
        # print(password)
        if not username or not password:
            return ("\n Enter username and password")
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "polling.db")
        with sqlite3.connect(db_path) as database:
            db=database.execute("SELECT * FROM user WHERE username = :username ",{"username":username})
            rows = db.fetchone()
            #print(generate_password_hash(password))
            if rows == None or rows[1] != password:
                return render_template("text_generator.html", message="Invalid username or password")
            return render_template("text_generator.html", message="Successfully Logged In")
    else:
        # print("bahar")
        return render_template("login.html")

@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        username = request.form.get("uname")
        password = request.form.get("pass")
        confirm_password = request.form.get("cpass")

        if password != confirm_password:
            return render_template("text_generator.html", message="Passwords do not match")

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "polling.db")

        with sqlite3.connect(db_path) as database:
            db = database.execute("SELECT * FROM user WHERE username = :username ", {"username": username})
            rows = db.fetchone()
            if rows != None:
                return render_template("text_generator.html", message="Username Already Exists")
            db = database.cursor()
            db.execute(
                """CREATE TABLE IF NOT EXISTS `user` ( `username` varchar(100) NOT NULL, `password` varchar(100) NOT NULL )""")
            db.execute("INSERT INTO user(username, password)" " VALUES( :username, :password)", {"username": username, "password": password})
            database.commit()

        return render_template("text_generator.html", message="Account Succesfully Created")
    else:
        return render_template("register.html")

@app.route("/temp", methods = ["POST", "GET"])
def temp():
    if request.method == "POST":
        # print("andar")
        return render_template("home.html")
    # print("bahar")
    return render_template("temp.html")

@app.route("/admin", methods=["POST", "GET"])
def admin():
    if request.method == "POST":
        #print("andar")
        username = request.form.get("uname")
        password = request.form.get("pass")
        # print(username)
        # print(password)
        if not username or not password:
            return ("\n Enter username and password")
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "polling.db")
        with sqlite3.connect(db_path) as database:
            db=database.execute("SELECT * FROM admin WHERE username = :username ",{"username":username})
            rows = db.fetchone()
            #print(generate_password_hash(password))
            if rows == None or rows[1] != password:
                return render_template("text_generator.html", message="Invalid username or password")
            return render_template("text_generator.html", message="Successfully Logged In")
    else:
        # print("bahar")
        return render_template("AdminLogin.html")