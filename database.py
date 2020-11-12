from main import db
from sqlalchemy import Date


class Board(db.Model):
	id = db.Column(db.Integer(), primary_key=True)
	name = db.Column(db.String(255))
	date_creation = db.Column(db.Date)
	date_modification = db.Column(db.Date)
	
class Task(db.Model):
	id = db.Column(db.Integer(), primary_key=True)
	header = db.Column(db.String(255))
	description = db.Column(db.String())
	status = db.Column(db.Boolean)
	date_creation = db.Column(db.Date)
	date_modification = db.Column(db.Date)
	board_id = db.Column(db.Integer(), db.ForeignKey("board.id"))