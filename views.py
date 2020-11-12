from main import db
from main import app
from main import ma
from database import *
from flask_restful import reqparse, Api, abort, Resource
from datetime import datetime, date


api = Api(app)


# BOARD

class BoardSchema(ma.Schema):
	class Meta:
		fields = ("id", "name", "date_creation", "date_modification")

board_schema = BoardSchema()
boards_schema = BoardSchema(many=True)

parser = reqparse.RequestParser()
parser.add_argument('name') # board


class BoardList(Resource):
	def get(self):
		try:
			board = Board.query.all()
			return boards_schema.dump(board)

		except Exception as error:
			pass
			print(error)

			with open("error.txt", "a") as f:
				f.write(f"Error: {error}\ndatetime: {datetime.now()}\nError in: BoardList, get\n\n")

	def post(self):
		try:
			args = parser.parse_args()
			print(args['name'])
			new_board = Board(
				name=args['name'],
				date_creation=date.today(),
				date_modification=date.today()
			)
			db.session.add(new_board)
			db.session.commit()
			return 201

		except Exception as error:
			pass
			print(error)

			with open("error.txt", "a") as f:
				f.write(f"Error: {error}\ndatetime: {datetime.now()}\nError in: BoardList, post\n\n")


class BoardItem(Resource):
	def get(self, board_id):
		try:
			board = Board.query.get_or_404(board_id)
			return board_schema.dump(board)
		
		except Exception as error:
			pass
			print(error)

			with open("error.txt", "a") as f:
				f.write(f"Error: {error}\ndatetime: {datetime.now()}\nError in: BoardItem, get\n\n")

	def delete(self, board_id):
		try:
			db.session.delete(Board.query.get(board_id))
			db.session.commit()
			return '', 204

		except Exception as error:
			pass
			print(error)

			with open("error.txt", "a") as f:
				f.write(f"Error: {error}\ndatetime: {datetime.now()}\nError in: BoardItem, delete\n\n")

	def put(self, board_id):
		try:
			args = parser.parse_args()
			board = Board.query.get_or_404(board_id)
			board.name = args['name']
			board.date_modification = date.today()

			db.session.commit()
			return board_schema.dump(board)

		except Exception as error:
			pass
			print(error)

			with open("error.txt", "a") as f:
				f.write(f"Error: {error}\ndatetime: {datetime.now()}\nError in: BoardItem, put\n\n")


api.add_resource(BoardList, '/boards')
api.add_resource(BoardItem, '/board/<int:board_id>')


# TASK

class TaskSchema(ma.Schema):
	class Meta:
		fields = ("id", "header", "description", "status", "date_creation", "date_modification", "board_id")

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)


parser.add_argument('header')
parser.add_argument('description')
parser.add_argument('status', type=bool)
parser.add_argument('board_id', type=int)


class TaskList(Resource):
	def get(self):
		try:
			tasks = Task.query.all()
			return tasks_schema.dump(tasks)

		except Exception as error:
			pass
			print(error)

			with open("error.txt", "a") as f:
				f.write(f"Error: {error}\ndatetime: {datetime.now()}\nError in: TaskList, get\n\n")

	def post(self):
		try:
			args = parser.parse_args()
			new_task = Task(
				header=args['header'],
				description=args['description'],
				status=args['status'],
				date_creation=date.today(),
				date_modification=date.today(),
				board_id=args['board_id'],
			)
			db.session.add(new_task)
			db.session.commit()
			return 201

		except Exception as error:
			pass
			print(error)

			with open("error.txt", "a") as f:
				f.write(f"Error: {error}\ndatetime: {datetime.now()}\nError in: TaskList, post\n\n")


class TaskListInBoard(Resource):
	def get(self, board_id):
		try:
			tasks = Task.query.filter(Task.board_id==board_id).all()
			return tasks_schema.dump(tasks)

		except Exception as error:
			pass
			print(error)

			with open("error.txt", "a") as f:
				f.write(f"Error: {error}\ndatetime: {datetime.now()}\nError in: TaskListInBoard, get\n\n")

	def post(self, board_id):
		try:
			args = parser.parse_args()
			new_task = Task(
				header=args['header'],
				description=args['description'],
				status=args['status'],
				date_creation=date.today(),
				date_modification=date.today(),
				board_id=board_id,
			)
			db.session.add(new_task)
			db.session.commit()
			return 201

		except Exception as error:
			pass
			print(error)

			with open("error.txt", "a") as f:
				f.write(f"Error: {error}\ndatetime: {datetime.now()}\nError in: TaskListInBoard, post\n\n")


class TaskItem(Resource):
	def get(self, task_id):
		try:
			task = Task.query.get_or_404(task_id)
			return task_schema.dump(task)

		except Exception as error:
			pass
			print(error)

			with open("error.txt", "a") as f:
				f.write(f"Error: {error}\ndatetime: {datetime.now()}\nError in: TaskItem, get\n\n")

	def delete(self, task_id):
		try:
			db.session.delete(Task.query.get(task_id))
			db.session.commit()
			return '', 204

		except Exception as error:
			pass
			print(error)

			with open("error.txt", "a") as f:
				f.write(f"Error: {error}\ndatetime: {datetime.now()}\nError in: TaskItem, delete\n\n")

	def put(self, task_id):
		try:
			args = parser.parse_args()
			task = Task.query.get_or_404(task_id)
			task.header = args['header']
			task.description = args['description']
			task.status = args['status']
			task.date_modification = date.today()

			db.session.commit()
			return task_schema.dump(task)

		except Exception as error:
			pass
			print(error)

			with open("error.txt", "a") as f:
				f.write(f"Error: {error}\ndatetime: {datetime.now()}\nError in: TaskItem, put\n\n")


api.add_resource(TaskList, '/tasks')
api.add_resource(TaskListInBoard, '/tasks/board/<int:board_id>') # фільтрування по дошці
api.add_resource(TaskItem, '/task/<int:task_id>')