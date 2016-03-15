from sys import argv
import fileinput

script, filename = argv

#txt = open(filename, "r")
#fileString = txt.read()

for line in open(filename):
	

	left_text = line.partition('\t')[2]
	final = left_text.strip('\n')
	#print left_text
	print final
