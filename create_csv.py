import sqlite3
import pandas as pd

db = sqlite3.connect("db.sqlite3")  #「hoge」を変更 
df = pd.read_sql_query("SELECT*FROM table", db) #「table」を変更 
db.close()
df.to_csv("hoge1.csv", index=None)