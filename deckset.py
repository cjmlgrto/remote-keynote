def parse(filename):

	slides = []

	with open(filename, 'r') as file:
		lines = iter(file.readlines())

		while True:
			try:
				line = next(lines).rstrip()
				if line == '---':
					slide = []
					title = next(lines).rstrip()
					title = title[2:]
					slide.append(title)
					content = []
					while True:
						line = next(lines).rstrip()
						if line == "*":
							break
						else:
							content.append(line)
					slide.append(content)
					slides.append(slide)
			except(StopIteration):
				break

	display(slides)

def display(slides):
	for slide in slides:
		print(slide[0])
		for line in slide[1]:
			print "- " + line

parse('keynote.md')