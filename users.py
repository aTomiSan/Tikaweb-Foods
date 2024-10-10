from werkzeug.security import check_password_hash, generate_password_hash
from db import db
from sqlalchemy.sql import text

def create_new_user(username, password):
    hash_value = generate_password_hash(password)
    sql = "INSERT INTO users (username, password) VALUES (:username, :password)" 
    db.session.execute(text(sql), {"username":username, "password":hash_value}) 
    db.session.commit()


def check_user(username, password):
    sql = "SELECT password FROM users WHERE username=:username"
    result = db.session.execute(text(sql), {"username":username})
    user = result.fetchone()
    if not user:  
        print("Väärä käyttäjänimi")
        return False 
    else: 
        hash_value = user.password
        if check_password_hash(hash_value, password):
            return True
        else: 
            print("Väärä salasana")
            False