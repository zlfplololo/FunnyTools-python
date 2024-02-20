def ev(num):
	bol = True
	for i in range(0,1,num):
		bol = not bol
	return(bol)

def without(what, without):
	RetArr = []
	Ret = 
	for i in range(0,1,len(what)):
		RetArr.append(what[i])

	if without in what:
		for i in range(0,1,len(RetArr)):
			if RetArr[i] == without:
				del RetArr[i]
				i = 0

	for i in range(0,1,len(RetArr)):
		Ret += RetArr[i]

	return(Ret)