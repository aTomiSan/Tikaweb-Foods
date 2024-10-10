from sqlalchemy.sql import text
from db import db 
from groceries import add_grocery_func, add_as_grocery

def add_food_func(name, amount=1, stored=1): 
    name = name.strip()
    sql = "SELECT visible, stored FROM foods WHERE name=:name"
    result = db.session.execute(text(sql), {"name":name})
    info = result.fetchall()
    if len(info) == 0:
        sql = "INSERT INTO foods (name, amount, visible, stored) VALUES (:name, :amount, 1, :stored)"
        db.session.execute(text(sql), {"name":name, "amount":int(amount), "stored":int(stored)}) 
        db.session.commit()
    else:
        visible = info[0][0]
        stored = info[0][1]
        if visible == 1:
            if stored == 0:
                sql = "UPDATE foods SET stored=1 WHERE name=:name"
                result = db.session.execute(text(sql), {"name":name})
                db.session.commit()
            else: 
                sql = "SELECT id FROM foods WHERE name=:name"
                result = db.session.execute(text(sql), {"name":name})
                id = result.fetchone()[0]
                increase_amount(id, amount)
        elif visible == 0: 
            sql = "UPDATE foods SET visible=1 WHERE name=:name"
            result = db.session.execute(text(sql), {"name":name})
            db.session.commit()

def list_foods():
    sql = "SELECT id, name, amount FROM foods WHERE visible=1 AND stored=1 ORDER BY name;" 
    result = db.session.execute(text(sql)) 
    stored = result.fetchall() 
    sql = "SELECT id, name FROM foods WHERE visible=1 AND stored=0 ORDER BY name;" 
    result = db.session.execute(text(sql)) 
    foods = result.fetchall() 
    return stored, foods 

def finish(id):
    sql = "UPDATE foods SET stored=0 WHERE id=:id;" 
    db.session.execute(text(sql), {"id":int(id)})
    db.session.commit()

def hide_food(id): 
    sql = "UPDATE foods SET visible=0 WHERE id=:id;" 
    db.session.execute(text(sql), {"id":int(id)})
    db.session.commit()
    print("piilotettu")

def store_groceries():
    sql = "SELECT name, amount FROM groceries" 
    result = db.session.execute(text(sql))
    groceries = result.fetchall() 
    for g in groceries:
        add_food_func(g[0], g[1])

def move_to_store(id):
    sql = "UPDATE foods SET stored=1 WHERE id=:id"
    db.session.execute(text(sql), {"id":id})
    db.session.commit()

def increase_amount(id, n=1): 
    sql = "SELECT amount FROM foods WHERE id=:id" 
    result = db.session.execute(text(sql), {"id":id}) 
    amount = result.fetchone()[0]
    amount += n
    sql = "UPDATE foods SET amount=:amount WHERE id=:id"
    db.session.execute(text(sql), {"id":id, "amount":amount}) 
    db.session.commit() 

def decrease_amount(id): 
    sql = "SELECT amount FROM foods WHERE id=:id" 
    result = db.session.execute(text(sql), {"id":id}) 
    amount = result.fetchone()[0]
    amount -= 1
    sql = "UPDATE foods SET amount=:amount WHERE id=:id"
    db.session.execute(text(sql), {"id":id, "amount":amount}) 
    db.session.commit() 