def ev(num):
	bol = True
	for i in range(num):
		bol = not bol
	return(bol)

def without(what, without):
	RetArr = []
	Ret = 
	for i in what:
		RetArr.append(i)

	if without in range(len(what)):
		for i in range(len(RetArr)):
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
					for i in range(len(arr)):
						setattr(self, arr[i][0], arr[i][1])

			return retclass

		def ObjToArr(objname):
			ret = []
			name = list(objname.__dict__.keys())
			value = []
			for i in name:
				value.append(getattr(objname, i))

			for i in range(len(name)):
				ret.append([name[i], value[i]])

			return ret

			

	return arrtoobj	

	def arrdict():
		class ard:
			def __init__():

			def ArrToDict(arr):
				dick = {}
				value = []
				name = []

				for i in range(len(arr)):
					value.append([arr[i -1][1]]) 
					name.append([arr[i -1][0]])


				for i in range(len(arr)):
					dick.update(name[i -1]:value[i -1])



			def DictToArr(dict):
				arr = []
				value = list(dict.keys())
				name = list(dict.values())

				for i in range(len(dict)):
					arr.append([name[i -1], val[i -1]])

				return arr


		return ard
			
