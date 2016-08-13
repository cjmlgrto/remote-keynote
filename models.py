from peewee import *

db = SqliteDatabase('counter.db')

class Counter(Model):
	id = PrimaryKeyField()
	counter = IntegerField()

	class Meta:
		database = db

def initialize_db():
	db.connect()
	db.create_tables([Counter], safe=True)