def ev(num):
	bol = True
	for i in range(num):
		bol = not bol
	return(bol)

def numeric(num):
	try:
		int(num)
		return True
	except ValueError:
		return False

def without(what, without):
	RetArr = []
	Ret = ""
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

def anagr(fir,sec):
	tct = [[],[]]
	ttct = []
	if len(fir) == len(sec):
		for i in range(fir):
			tct[0].append(None)
			for j in sec:
				if fir[i] == j:
					tct[0][i] = True
					break 
			else:
				tct[0][i] = False

		for i in len(sec):
			tct[1].append(None)
			for j in fir:
				if sec[i] == j:
					tct[1][i] = True
					break 
			else:
				tct[1][i] = False

		ttct.append(None)
		ttct.append(None)

		for i in tct[0]:
			if i == True:
				ttct[0] = True
				continue

			else:
				ttct[0] = False
				break

		for i in tct[1]:
			if i == True:
				ttct[1] = True
				continue

			else:
				ttct[1] = False
				break

		if ttct[0] & ttct[1]:
			return True
		else:
			return False

	else:
		return False

def objdict():
	class OBDI:
		def __init__():

		def ObjToDict(objname):
			ret = {}
			value = []
			name = list(objname.__dict__.keys())

			for i in name:
				value.append(getattr(objname, i))

			for i in range(len(value)):
				ret.update(name[i]:value[i])

		def DictToObj(dick):
			value = []
			name = list(dick.keys())

			for i in value:
				value.append(dick.get(i))

			class retclass:
				def __init__(self):
					for i in range(len(name)):
						setattr(self, name[i], value[i])


			return retclass

	return OBDI

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
					value.append([arr[i][1]]) 
					name.append([arr[i][0]])


				for i in range(len(arr)):
					dick.update(name[i]:value[i])



			def DictToArr(dict):
				arr = []
				value = list(dict.keys())
				name = list(dict.values())

				for i in range(len(dict)):
					arr.append([name[i], val[i]])

				return arr


		return ard
			
