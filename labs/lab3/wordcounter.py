import count
import removePunctuation

print("file to count")

file = input()

count =  count.readNameList(file)

count = removePunctuation.removePunctuation(str(count))

count = len(count.split()) 
 
print(count)



