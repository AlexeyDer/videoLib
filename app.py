from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy

from config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)
from models import *

app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
admin = Admin(app, name='VideoLib', template_mode='bootstrap3')

admin.add_view(UserAdmin(User, db.session))
admin.add_view(FilmInfoAdmin(FilmInfo, db.session))
admin.add_view(GivenAdmin(Given, db.session))
