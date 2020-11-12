from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
ma = Marshmallow(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres+psycopg2://root:root@localhost/api'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from views import *

if __name__ == '__main__':
	app.run(debug=True)