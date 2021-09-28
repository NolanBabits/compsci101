import filetolist

print("file to print")

file = input()



list  =  filetolist.filetolist("test.txt")
x = 0

for i in list:
	if int (i) - int(x) < 0:
	 x = i

print(x)