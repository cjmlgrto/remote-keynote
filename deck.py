import markdown2

def parse(filename):
	keynote = []
	with open(filename) as file:
		slide = []
		content = file.readlines()
		for line in content:
			text = line.rstrip()
			if text != '' and text != '---' and text != '<pre><code>' and text != '</pre></code>' and text[:4] != '    ':
				slide.append(str(markdown2.markdown(text)))
			if text == '<pre><code>' or text == '</pre></code>' or text[:4] == '    ':
				slide.append(text)
			if text == '---':
				keynote.append(slide)
				slide = []
	return keynote

def display(slides, page):
	for line in slides[page]:
		print line