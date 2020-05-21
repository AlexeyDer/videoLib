from app import app
from app import db
from view import *

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
