import markdown2

def deck(filename):
	keynote = []
	with open(filename) as file:
		slide = []
		content = file.readlines()
		code = False
		list = False
		for line in content:
			text = line.rstrip()
			if text == '```':
				code = not code
				if code:
					slide.append('<pre><code>')
				else:
					slide.append('</pre></code>')
			if text == '-':
				list = not list
				if list:
					slide.append('<ul>')
				else:
					slide.append('</ul>')
			if not code and not list:
				if not (text == '```' or text == '---' or text == '' or text == '-'):
					slide.append(str(markdown2.markdown(text)))
			else:
				if text != '```' and text != '-':
					if text[:2] == '* ':
						slide.append('<li>' + text[2:] + '</li>')
					else:
						slide.append(text)
			if text == '---':
				keynote.append(slide)
				slide = []
	return keynote