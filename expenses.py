from sqlalchemy.sql import text
from db import db 
from datetime import date

# months_eng = ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
# months = ["Tammikuu","Helmikuu","Maaliskuu","Huhtikuu","Toukokuu","Kesäkuu","Heinäkuu","Elokuu","Syyskuu","Lokakuu","Marraskuu","Joulukuu"]
# data = [i.time.year,i.time.month, i.time.day, i.time.hour, i.time.minute, i.value] 


def list_expenses():
    sql = "SELECT time, value FROM expenses ORDER BY time DESC"
    result = db.session.execute(text(sql))
    info = result.fetchall()
    return info

def add_to_expenses(value):
    print("adding to expenses")
    sql = "INSERT INTO expenses (time, value) VALUES (NOW(), :value)"
    db.session.execute(text(sql), {"value":value}) 
    db.session.commit()
    print("added")



