#!/usr/bin/python3

class arrdict():
	#true
	def ArrToDict(self, arr):
		dick = {}
		for item in arr:
			dick[item[0]] = item[1]
		return dick

	def DictToArr(dick):
		arr = []
		for key, value in dick.items():
			arr.append([key, value])
		return arr

class BinaryTree:
	#true
	def __init__(self):
		#name:[value, [parents]]
		self.value = {}
	def __getitem__(self, index):
		return {"value": self.value[index][0], "parents":  self.value[index][1]}

	def __setitem__(self, index, value):
		if index in self.value:
			self.value[index] = value
		else:
			self.value[index] = [value,[]]
	def __delitem__(self, index):
		del self.value[index]

	def __str__(self):
		 return str(self.value)

	def resetparents(self,index):
		self.value[index][1] = []

	def addparent(self,index, parent):
		if parent in self.value:
			self.value[index][1].append(parent)
		else:
			raise KeyError(f"no value named {index} founded")

	def deleteparent(self,index,parent):
		self.value[index][1].remove(parent)

	def searchallchilds(self,index):
		ret = []
		for i in self.value:
			if  index in self.value[i][1]:
				ret.append(i)
		return ret

class table():
	#true
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.value = []
		self.update(x,y)

	def __getitem__(self,key):
		return self.value[key]

	def __setitem__(self,key,value):
		self.value[key] = value
	
	def echo(self, ToPrint):
		print(ToPrint, end="")
	
	def MatPrint(self, Matrics):
		for i in range(len(Matrics)):
			for j in range(len(Matrics[i])):
				self.echo([Matrics[i][j]])
			print()
	
	def __str__(self):
		self.MatPrint(self.value)
		return ''
				

	def update(self,x,y):
		for i in range(x):
			self.value.append([])
			for j in range(y):
				self.value[i].append(0)
				
	def increaseX(self,num):
		for i in range(num):
			self.x+=1
			self.value.append([])
			for j in range(self.y):
					self.value[self.x-1].append(0)

	def decreaseX(self, num):
		for i in range(num):
			self.value.pop()
			self.x-=1

	def increaseY(self, num):
		for i in range(num):
			self.y+=1
			for j in range(self.x):
				self.value[j].append(0)
				
	def decreaseY(self,num):
		for i in range(num):
			self.y-=1
			for j in range(self.x):
				self.value[j].pop()

def echo(ToPrint):
	#true
	print(ToPrint, end="")
	
def MatPrint(Matrics):
	#true
	def echo(ToPrint):
		print(ToPrint, end="")
	
	for i in range(len(Matrics)):
		for j in range(len(Matrics[i])):
			echo([Matrics[i][j]])
		print()
		
#true
ev = lambda x: x%2 - x%2%1 <= 0

#true
LOXRIY = lambda x,y: [x for i in range(int(y/x - y/x%1))]

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

revernum = lambda x,y:y - x

def palindr(that):
        #true
	rev = ""

	for i in range(len(that)):
		rev = that[len(that) - i -1]

	return that == rev

def nonum(number):
	#true
	ev = lambda x: x%2 - x%2%1 <=0
	if ev(number):
		return number -1
	else:
		return number +1

#true
VFP = lambda x: x != x - x%1
