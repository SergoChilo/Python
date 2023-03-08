file = open('./test.txt', "r")
z = []
for index, s in enumerate(file):
	t = s.split()
	count = 0
	for y in t:
		z += y[0]
		count += 1
		if len(t) is count:
			z += '\n'
		k = ''.join(z)
print(k)

file.close()