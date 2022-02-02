import sqlite3
import pandas as pd

db = "imdb.db"


def getAnswer(db, sql):
    conn = sqlite3.connect(db)
    answer = pd.read_sql_query(sql, conn)
    conn.close()
    return answer
