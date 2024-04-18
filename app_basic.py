from flask import Flask, render_template
from pathlib import Path

import sqlite3
import pathlib



base_path = pathlib.Path.home() / "C:/Users/DELL/Documents/DAB111/python/krunal/krunal"

db_name = "housing.db"
db_path = base_path / db_name

# Define a file path
file_path = Path('/path/to/file.txt')

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index_links.html") 

@app.route("/defination")
def defination():
    return render_template("defination.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/Content")
def features():
    return render_template("Content.html")  

@app.route("/data")
def data():
    con = sqlite3.connect(db_path)
    cursor = con.cursor()
    housing = cursor.execute("SELECT * FROM housing LIMIT 10").fetchall()
    con.close()
    # print(housing)
    return render_template("data_table.html", housing = housing)

@app.route("/link")
def link():
    return render_template("link.html")


if __name__=="__main__":
    app.run(debug=True)