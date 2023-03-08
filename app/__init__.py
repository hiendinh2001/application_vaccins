from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = '12#^&*+_%&*)(*(&(*^&^$%$#((*65t87676'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:%s@localhost/hellohien3?charset=utf8mb4' % quote('123456')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['MY_CART'] = 'cart'

db = SQLAlchemy(app=app)
