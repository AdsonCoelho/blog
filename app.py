from flask import Flask, render_template
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
 
app = Flask("hello")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Post(db.model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    title = db.Column(db.String(70), nullable=False)
    body = db.Column(db.String(500))
    author = db.Collumn(db.String(20))
    created = db.Collumn(db.Datetime, nullable=False, default=datetime.now)


@app.route("/")
def index():
    # Busca no banco os posts
    return render_template("index.html", posts=posts)
