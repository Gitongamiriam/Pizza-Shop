from flask import Flask
from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__)
app.config[ "SQLALCHEMY_DATABASE_URI"] ="sqlitte:///pizza.db"
db = SQLAlchemy(app)


from app.main.views import main


app.register_blueprint(main)