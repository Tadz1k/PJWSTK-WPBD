import sys

for line in sys.stdin:
	line = line.strip()
	words = line.split()
	for word in words:
		word = word.lower()
		print('{0}\t{1}'.format(word, 1))
