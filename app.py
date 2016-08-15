from flask import Flask, render_template, redirect
from models import *
from deck import *

app = Flask(__name__)
keynote = deck('build-your-own-website.md')
n = len(keynote)

@app.before_request
def before_request():
	initialize_db()

@app.teardown_request
def teardown_request(exception):
	db.close()

@app.route('/')
def display():
	slide = Counter.select()[0]
	index = slide.counter % n
	return render_template('keynote.html', content=keynote[index])
	# return redirect('http://indiecodeworkshop.com')

@app.route('/presentation/<name>')
def full(name=None):
	if name is not None:
		keynote = deck(name + '.md')
		return render_template('full.html', keynote=keynote)
	else:
		return redirect('http://indiecodeworkshop.com/')


@app.route('/start')
def reset():
	slide = Counter.select()[0]
	slide.counter = 0
	slide.save()
	return redirect('/')

@app.route('/init')
def init():
	slide = Counter.create(counter=0)
	return redirect('/')

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