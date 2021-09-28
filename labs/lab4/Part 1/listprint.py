import filetolist

print("file to print")

file = input()

list  =  filetolist.filetolist("test.txt")
#print (list)
print("1 for whole list 2 for evey 3rd item")
k = int(input())

#k = 2


if k == 1: 
	print(list)
	exit()
elif k == 2:
	x = 1
	for i in list:
		#print (x)
		#print (i)
		
		if x % 3 == 0:
			print (i)
			#print (x)
			x += 1
		else:
			x += 1
			exit()
else:
	print("bad input use 1 or 2")
