'''
'''
import database


class User():
	''''''
	@classmethod
	def load_from_db_by_email(cls, email):
		''''''
		user_data = None
		with database.CursorFromConnectionFromPool() as cursor:
			cursor.execute('SELECT * FROM users WHERE email = %s',
				(email,))
			user_data = cursor.fetchone()

		return cls(email=user_data[1], first_name=user_data[2],
			last_name=user_data[2], uid=user_data[0]) if user_data else None

	def __init__(self, email, first_name, last_name, uid):
		self.email = email
		self.first_name = first_name
		self.last_name = last_name
		self.uid = uid

	def __repr__(self):
		return '<User {}>'.format(self.email)

	def save_to_db(self):
		'''Using `with` statements to insert the appropriate data'''
		with database.CursorFromConnectionFromPool() as cursor:
			cursor.execute('INSERT INTO users (email, first_name, last_name) '
				' VALUES (%s, %s, %s)', (self.email, self.first_name,
					self.last_name))



