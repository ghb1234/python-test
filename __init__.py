from flask import Flask
from .views.login import login_page
from .views.bussiness import buss_page
from .extension import db
app = Flask('first_flask')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:11111111@localhost:3306/user2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "lalskskskskksksjsj"
db.init_app(app)

app.register_blueprint(login_page)
app.register_blueprint(buss_page)
