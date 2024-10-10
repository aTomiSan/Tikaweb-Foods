from sqlalchemy.sql import text
from db import db 

def list_recipes(): 
    sql = "SELECT id, name FROM recipes ORDER BY name" 
    result = db.session.execute(text(sql))
    recipe = result.fetchall()
    return  recipe

def add_recipe_func(name, ingredients, additional): 
    print(ingredients)
    sql = "INSERT INTO recipes (name, ingredients, additional) VALUES (:name, :ingredients, :additional)" 
    db.session.execute(text(sql), {"name":name, "ingredients":ingredients, "additional":additional}) 
    db.session.commit() 

def get_recipe(id): 
    sql = "SELECT name, ingredients, additional FROM recipes WHERE id=:id" 
    result = db.session.execute(text(sql), {"id":id}) 
    info = result.fetchall() 
    name = info[0][0]
    i = info[0][1]
    ingredients = []
    for j in i.split():
        if check_stored(j):
            x = (j, 1)
            ingredients.append(x)
        elif check_groceries(j):
            x = (j, 2)
            ingredients.append(x)
        else:
            if (j, 1) not in ingredients:
                x = (j, 0)
                ingredients.append(x)
    additional = info[0][2]
    return name, ingredients, additional

def check_stored(i): 
    sql = "SELECT 1 FROM foods WHERE visible=1 AND stored=1 AND name LIKE :i" 
    result = db.session.execute(text(sql), {"i":i}) 
    r = result.fetchone()
    if r:
        return True
    return False

def check_groceries(i): 
    sql = "SELECT 1 FROM groceries WHERE visible=1 AND name LIKE :i" 
    result = db.session.execute(text(sql), {"i":i}) 
    r = result.fetchone()
    if r:
        return True
    return False



