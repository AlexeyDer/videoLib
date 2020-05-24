from flask_admin.contrib import sqla

from app import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(250))
    address = db.Column(db.String(250))

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)


class UserAdmin(sqla.ModelView):
    column_display_pk = True
    form_columns = ['id', 'name', 'address']


class FilmInfo(db.Model):
    __tablename__ = 'film_info'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    genre = db.Column(db.String(250))
    producer = db.Column(db.String(250))
    studio = db.Column(db.String(250))
    actors = db.Column(db.String(250))
    brief_abstract = db.Column(db.String())

    def __init__(self, *args, **kwargs):
        super(FilmInfo, self).__init__(*args, **kwargs)


class FilmInfoAdmin(sqla.ModelView):
    column_display_pk = True
    form_columns = ['id', 'name', 'genre', 'producer', 'studio', 'actors', 'brief_abstract']
    column_searchable_list = ['genre', 'actors']


class Given(db.Model):
    __tablename__ = 'given'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    data = db.Column(db.String(250))
    film = db.Column(db.String(250))
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # user = db.relationship('User', backref=db.backref('given', lazy='dynamic'))

    def __init__(self, *args, **kwargs):
        super(Given, self).__init__(*args, **kwargs)


class GivenAdmin(sqla.ModelView):
    column_display_pk = True
    form_columns = ['id', 'name', 'data', 'film']
    can_export = True
