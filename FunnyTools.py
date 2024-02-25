def ev(num):
	#true
	bol = True
	for i in range(num):
		bol = not bol
	return(bol)

def numeric(num):
	#true
	try:
		int(num)
		return True
	except ValueError:
		return False

def without(what, without):
	#true
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
	#true
	tct = [[],[]]
	ttct = []
	if len(fir) == len(sec):
		for i in range(len(fir)):
			tct[0].append(None)
			for j in sec:
				if fir[i] == j:
					tct[0][i] = True
					break 
			else:
				tct[0][i] = False

		for i in range(len(sec)):
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

def arrdict():
	#true
    class Ard:
        @staticmethod
        def ArrToDict(arr):
            dick = {}
            for item in arr:
                dick[item[0]] = item[1]
            return dick

        @staticmethod
        def DictToArr(dick):
            arr = []
            for key, value in dick.items():
                arr.append([key, value])
            return arr

    return Ard
			
