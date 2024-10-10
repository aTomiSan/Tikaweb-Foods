
from flask import Flask 
from os import getenv

ap = Flask(__name__) 
ap.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
ap.secret_key = getenv("SECRET_KEY")

import routes

