import markdown2

def parse(filename):
	keynote = []
	with open(filename) as file:
		slide = []
		content = file.readlines()
		for line in content:
			text = line.rstrip()
			if text != '' and text != '---':
				slide.append(str(markdown2.markdown(text)))
			if text == '---':
				keynote.append(slide)
				slide = []
	return keynote

def display(slides, page):
	for line in slides[page]:
		print line

if __name__ == '__main__':
	slides = parse('keynote.md')
	display(slides, 0)