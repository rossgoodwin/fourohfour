import make_url_endings
import json
import requests
from bs4 import BeautifulSoup

grammarDict = json.load( open('weird_grammar.json', 'r') )

urlsFile = open('urls.txt', 'r')
urls = [line.strip() for line in urlsFile.readlines()]
endings = make_url_endings.main(grammarDict, 3333).split('\n')

outLines = ["\\documentclass[10pt]{book}",
			"\\usepackage{hyperref}",
			"\\title{Four Oh Four}",
			"\\author{Ross Goodwin\\\\http://rossgoodwin.com/fourohfour}",
			"\\date{\\today}",
			"\\begin{document}",
			"\\maketitle"]

for i in range(3333):
	outLines.append("\\href{http://%s/%s}{%i. http://%s/%s}\\\\" % (urls[i].replace('_','\_'), endings[i].replace('_','\_'), i+1, urls[i].replace('_','\_'), endings[i].replace('_','\_')))

outLines.append("\\end{document}")

with open('fourohfour.tex', 'w') as outfile:
	outfile.write('\n'.join(outLines))
	
