

list='qwertyuiopasdfghjklzxcvbnm'
print ("enter any letter:")
a=str(input()) 
b=list.find(a)
if a == "m":
	print("q")
else:
	print(list[b+1])
