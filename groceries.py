
from sqlalchemy.sql import text
from db import db 

def add_grocery_func(name, amount): 
    sql = "SELECT visible FROM groceries WHERE name=:name"
    result = db.session.execute(text(sql), {"name":name})
    visible = result.fetchone()
    if visible == None:
        sql = "INSERT INTO groceries (name, amount, type, visible) VALUES (:name, :amount, 1, 1)" 
        db.session.execute(text(sql), {"name":name, "amount":int(amount)})
        db.session.commit()
    else: 
        if visible[0] == 1: 
            sql = "SELECT amount FROM groceries WHERE name=:name"
            result = db.session.execute(text(sql), {"name":name})
            new_amount = result.fetchone()
            amount += new_amount[0]
            sql = "UPDATE groceries SET amount=:amount WHERE name=:name" 
            db.session.execute(text(sql), {"amount":amount, "name":name})
            db.session.commit()
        elif visible[0] == 0: 
            sql = "UPDATE groceries SET visible=1 WHERE name=:name" 
            result = db.session.execute(text(sql), {"name":name}) 
            db.session.commit()
            sql = "UPDATE groceries SET amount=:amount WHERE name=:name" 
            db.session.execute(text(sql), {"amount":amount, "name":name})
            db.session.commit()
    
    
def list_groceries(): 
    sql = "SELECT id, name, amount, type FROM groceries WHERE visible=1 ORDER BY type, name" 
    result = db.session.execute(text(sql))
    grocery_list = result.fetchall()
    return grocery_list

def remove_grocery_func(id): 
    sql = "UPDATE groceries SET visible=0 WHERE id=:id" 
    db.session.execute(text(sql), {"id":id}) 
    db.session.commit() 

def increase_grocery(id): 
    sql = "SELECT amount FROM groceries WHERE id=:id" 
    result = db.session.execute(text(sql), {"id":id}) 
    amount = result.fetchone()[0]
    amount += 1
    sql = "UPDATE groceries SET amount=:amount WHERE id=:id"
    db.session.execute(text(sql), {"id":id, "amount":amount}) 
    db.session.commit() 

def decrease_grocery(id): 
    sql = "SELECT amount FROM groceries WHERE id=:id" 
    result = db.session.execute(text(sql), {"id":id}) 
    amount = result.fetchone()[0]
    amount -= 1
    sql = "UPDATE groceries SET amount=:amount WHERE id=:id"
    db.session.execute(text(sql), {"id":id, "amount":amount}) 
    db.session.commit() 

def add_as_grocery(id):
    sql = "SELECT name FROM foods WHERE id=:id;" 
    result = db.session.execute(text(sql), {"id":id})
    name = result.fetchone()[0]
    add_grocery_func(name, 1)

def empty_shopping_list():
    sql = "TRUNCATE TABLE groceries" 
    db.session.execute(text(sql))
    db.session.commit()

def increase_type(id): 
    sql = "SELECT type FROM groceries WHERE id=:id" 
    result = db.session.execute(text(sql), {"id":id})
    new_type = result.fetchone()[0] + 1
    sql = "UPDATE groceries SET type=:new_type WHERE id=:id" 
    db.session.execute(text(sql), {"new_type":new_type, "id":id})
    db.session.commit() 

def decrease_type(id): 
    sql = "SELECT type FROM groceries WHERE id=:id" 
    result = db.session.execute(text(sql), {"id":id})
    new_type = result.fetchone()[0] - 1
    sql = "UPDATE groceries SET type=:new_type WHERE id=:id" 
    db.session.execute(text(sql), {"new_type":new_type, "id":id})
    db.session.commit() 