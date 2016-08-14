import markdown2

def parse(filename):
	keynote = []

	with open(filename) as file:

		slide = []
		content = file.readlines()
		code = False

		for line in content:

			text = line.rstrip()

			if text == '```':
				code = not code
				if code:
					slide.append('<pre><code>')
				else:
					slide.append('</pre></code>')

			if not code:
				if not (text == '```' or text == '---' or text == ''):
					slide.append(str(markdown2.markdown(text)))
			else:
				if text != '```':
					slide.append(text)

			if text == '---':
				keynote.append(slide)
				slide = []

	return keynote

def display(slides, page):
	for line in slides[page]:
		print line

# print display(parse('keynote.md'), 0)