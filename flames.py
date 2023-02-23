Name1 = input("what is your name:").lower()
Name2 = input("waht is your partner name:").lower()
Name1 = Name1.replace(" ","")
Name2 = Name2.replace(" ","")
print(Name1)
print(Name2)

for k in Name1:
	for j in Name2:
		if k==j:
			Name1=Name1.replace(k,"",1)
			Name2=Name2.replace(j,"",1)
			break
count= len(Name1+Name2)
print(count)

if count>0:
	list=["friends","lovers","affectionate","marriage","enemies","siblings"]

	while len(list)>1:
		c= count%len(list)
		game= c-1

		if game>=0:
			left = list[:game]
			right=list[game+1:]
			list = right+left
		else:
			list = list[:len(list)-1]
	

print("relationship is",list[0])
		
	