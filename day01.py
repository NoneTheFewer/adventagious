import numpy

sampling = False
day = "1b"

sample = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""

if not sampling:
	sample = open("day1.txt", "r").read()

lines = sample.split("\n")

elves = []
curttl = 0

for line in lines:
	if len(line) == 0:
		elves.append(curttl)
		curttl = 0
	else:
		curttl += int(line)

if day == "1a":
	print(max(elves))
elif day == "1b":
	tops = [
		sorted(elves, reverse=True)[0],
		sorted(elves, reverse=True)[1],
		sorted(elves, reverse=True)[2]
	]
	print(numpy.sum(tops))
