from flask import Flask, render_template, redirect
from models import *

app = Flask(__name__)

@app.before_request
def before_request():
	initialize_db()

@app.teardown_request
def teardown_request(exception):
	db.close()

@app.route('/reset')
def init():
	slide = Counter.create(counter=1)
	return 'Created!'

@app.route('/next')
def next():
	slide = Counter.select()[0]
	slide.counter += 1
	slide.save()
	return redirect('/')

@app.route('/prev')
def prev():
	slide = Counter.select()[0]
	slide.counter -= 1
	slide.save()
	return redirect('/')


if __name__ == '__main__':
	app.run(debug=True)