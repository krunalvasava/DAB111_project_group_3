import sqlite3 
import csv 

conn = sqlite3.connect('housing.db')
cursor = conn.cursor()

create_table = """CREATE TABLE IF NOT EXISTS housing (
                    ID INT PRIMARY KEY,
                    price INT,
                    area INT,
                    bedrooms INT,
                    bathrooms INT,
                    stories INT,
                    mainroad TEXT,
                    guestroom TEXT,
                    basement TEXT,
                    hotwaterheating TEXT,
                    airconditioning TEXT,
                    parking INT,
                    prefarea TEXT,
                    furnishingstatus TEXT
                );"""

cursor.execute(create_table)

with open("Housing_Price_Data.csv") as f:
    data = csv.reader(f)
    for row in data:
        if row[0] == 'id': 
            continue
        cursor.execute("INSERT INTO housing (price, area, bedrooms, bathrooms, stories, mainroad, guestroom, basement, hotwaterheating, airconditioning, parking, prefarea, furnishingstatus) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12]))

results = cursor.execute("SELECT * FROM housing;").fetchall()

conn.commit()

conn.close() 
