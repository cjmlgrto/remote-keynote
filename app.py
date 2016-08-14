from flask import Flask, render_template, redirect
from models import *

app = Flask(__name__)

@app.before_request
def before_request():
	initialize_db()

@app.teardown_request
def teardown_request(exception):
	db.close()

@app.route('/')
def display():
	slide = Counter.select()[0]
	return render_template('display.html', slide=slide.counter)

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

@app.route('/keynote')
def keynote():
	source = file('keynote.md', 'r')
	title = str(source.readline().rstrip())
	title = title[2:]
	content = source.readlines()
	return render_template('keynote.html', title=title, content=content)


if __name__ == '__main__':
	app.run(debug=True)