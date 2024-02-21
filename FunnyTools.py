def ev(num):
	bol = True
	for i in range(0,1,num):
		bol = not bol
	return(bol)

def without(what, without):
	RetArr = []
	Ret = 
	for i in what:
		RetArr.append(i)

	if without in range(0,1,len(what)):
		for i in range(0,1,len(RetArr)):
			if RetArr[i] == without:
				del RetArr[i]
				i = 0

	for i in RetArr:
		Ret += i

	return(Ret)

def arrobj():
	class arrtoobj:
		def __init__(): 

		def ArrToObj(arr):
			class retclass:
				def __init__(self,):
					for i in range(0,1,len(arr)):
						name = arr[i][0]
						val = arr[i][1]

						self.name = val

					del name
					del val

			return retclass

		def ObjToArr(objname):
			ret = []
			name = list(objname.__dict__.keys())
			value = []
			for i in name:
				value.append(getattr(objname, i))

			for i in range(0,1,len(name)):
				ret.append([name[i], value[i]])

			return ret

			

	return arrtoobj	
			
