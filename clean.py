import numpy as np

n_tests = int(input())

with open("test.txt", "w") as myfile:
	myfile.write(str(n_tests) + "\n")

for _ in range(n_tests):
	n, m, opt = map(float, input().split())
	n, m = int(n), int(m)
	with open("test.txt", "a") as myfile:
		myfile.write(str(n) + " " + str(m) + " " + str(opt) + "\n")

	for i in range(m+1):
		line = np.array([])
		for l in range(int(n/7) + 1):
			a = list(map(int, input().split()))
			line = np.concatenate((line, a), axis=None)
		with open("test.txt", "a") as myfile:
			out = ""
			for j in range(len(line)):
				out += str(line[j]) + " "
			myfile.write(out + "\n")
    
	# b = list(map(int, input().split()))
	# with open("test.txt", "a") as myfile:
	# 	out = ""
	# 	for k in range(len(b)):
	# 		out += str(b[k]) + " "
	# 	myfile.write(out + "\n")
	line = np.array([])
	for l in range(5):
		a = list(map(int, input().split()))
		line = np.concatenate((line, a), axis=None)
	with open("test.txt", "a") as myfile:
		out = ""
		for j in range(len(line)):
			out += str(line[j]) + " "
		myfile.write(out + "\n")