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
			if text[:3] == '```':
				code = not code
				if code:
					if text[3:] == '':
						slide.append('<pre><code>')
					else:
						lang = text[3:]
						slide.append('<pre><code class="language-' + lang + '">')
				else:
					slide.append('</pre></code>')
			if text == '-':
				list = not list
				if list:
					slide.append('<ul>')
				else:
					slide.append('</ul>')
			if not code and not list:
				if not (text[:3] == '```' or text == '---' or text == '' or text == '-'):
					slide.append(str(markdown2.markdown(text)))
			else:
				if text[:3] != '```' and text != '-':
					if text[:2] == '* ':
						slide.append('<li>' + text[2:] + '</li>')
					else:
						slide.append(text)
			if text == '---':
				keynote.append(slide)
				slide = []
	return keynote

# def display(slides, page):
# 	for line in slides[page]:
# 		print line

# print display(deck('keynote.md'), 0)