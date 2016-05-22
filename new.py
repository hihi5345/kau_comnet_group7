import random

class game:
	def __init__(self) :
		self.mset = ('back doe', 'doe', 'gae', 'girl', 'yoot', 'moe')
		self.position = [0,0]
		self.yuut =0
		self.finish=0
		self.together=[]
		self.eaten=[]
	def throw() :
		self.yuut = random.randint(0,5)
		if (self.yuut==0):
			self.yuut=-1
		print self.yuut
		return self.yuut

	def move(self):
		if (self.yuut==4 or self.yuut==5):
			count=1
		if (self.position[0]==0):
			if(self.position[1]==0):
				if(self.yuut!=-1):
					self.position[1]=self.yuut
			elif (self.position[1]==5):
				if(self.yuut==5):
					self.position[0]=7
					self.position[1]=1
				elif(self.yuut!=-1):
					self.position[1]=4
				else:
					self.position[0]=self.yuut
					self.position[1]=5-self.yuut
			elif(self.position[1]+self.yuut>4):
				self.position[0]=self.position[1]+self.yuut-5
				self.position[1]=5
			else:
				self.position[1]=self.position[1]+self.yuut
			
		elif (self.position[1]==5):
			if (self.position[0]==5):
				if (self.yuut==5):
					self.position[0]=7
					self.position[1]=7
				elif(self.yuut!=-1):
					self.position[0]=4
				else:
					self.position[0]=5-self.yuut
					self.position[1]=5-self.yuut
			elif (self.position[0]+self.yuut>4):
				self.position[1]=5-(self.position[0]+self.yuut-5)
				self.position[0]=5
			else:
				self.position[0]=self.position[0]+self.yuut
		
		elif (self.position[0]==5):
			if (self.position[1]==0):
				if(self.yuut!=-1):
					self.position[1]=1
				else:
					self.position[0]=5-self.yuut
			elif (self.position[1]-self.yuut<0):
				self.position[0]=5-self.yuut+self.position[1]
				self.position[1]=0
			else:
				self.position[1]=self.position[1]-self.yuut

		elif (self.position[1]==0):
			if (self.position[0]-self.yuut<0):
				self.position[1]=self.yuut-self.position[0]
				self.position[0]=0
			else:
				self.position[0]=self.position[0]-self.yuut
		
		else:
			if ((self.position[0]<3 and self.position[1]>2) or (self.position[0]>3 and self.position[1]<3)):
				if(self.position[0]+self.yuut>5):
					if (self.position[0]==7):
						if (self.yuut==-1):
							self.position[0]=4
							self.position[1]=1
						else:
							self.position[0]=5-(self.position[0]+self.yuut-8)
							self.position[1]=0
					else:									
						self.position[0]=5-(self.position[0]+self.yuut-6)
						self.position[1]=0
				else:
					if(self.position[0]+self.yuut==5):
						self.position[0]=7
						self.position[1]=1
					else:
						self.position[0]=self.position[0]+self.yuut
						self.position[1]=self.position[1]-self.yuut
			else:
				if(self.position[0]-self.yuut<0 or self.position[1]==7):
					if(self.position[1]==7):
						if(self.yuut==-1):
							self.position[0]=1
							self.position[1]=1
						else:
							self.position[0]=self.yuut-self.position[0]+6
							self.position[1]=0
					else:
						self.position[1]=self.yuut-self.position[0]-1
						self.position[0]=0
				else:	
					if(self.position[0]-self.yuut==0):
						self.position[0]=7
						self.position[1]=7
					else:
						self.position[0]=self.position[0]-self.yuut
						self.position[1]=self.position[1]-self.yuut
		
		if (self.position[0]==0 and self.position[1]==0):
			for i in self.together:
				i.finish=1
				i.eaten=[]
			self.finish=1
			self.together=[]
		
		return count
	
	
	def check(self, list):
		for x in list:
			for i in range(4):
				for j in range(4):
					if (self[i].position[0]==x[j].position[0] and self[i].position[1]==x[j].position[1]):
							if (self==x):
								if(i!=j):
									if(x[j].position[0]!=0 and x[j].position[1]!=0):
										self.together.append(x[j])
										x[j].eaten.append(self)
							else:
								for i in x[j].together:
									i.eaten=[]
								x[j].together=[]
							x[j].position[0]=0
							x[j].position[1]=0
		return None
			
			
if __name__ == '__main__':
	
	a[:3] = game()
	b[:3] = game()  
	c[:3] = game()
	d[:3] = game()

	list=[a,b,c,d]
	while (1):
		
		print('<player1>')
		while(1):
			if (a[0].finish==1 and a[1].finish==1 and a[2].finish==1 and a[3].finish==1):
				print ('Winner is player1')
			a.throw()
			while(1):
				select = input("which piece do you want to move? only 0~3")
				if (a[select].finish!=0):
					print ('You picked wrong piece.')
				else:
					break
			if(a[select].move()):
				a[select].check(list)
			else:
				a[select].check(list)
				break
	
		print('<player2>')
		while(1):
			if (b[0].finish==1 and b[1].finish==1 and b[2].finish==1 and b[3].finish==1):
				print ('Winner is player2')
			b.throw()
			while(1):
				select = input("which piece do you want to move? only 0~3")
				if (b[select].finish!=0):
					print ('You picked wrong piece.')
				else:
					break
			if(b[select].move()):
				b[select].check(list)
			else:
				b[select].check(list)
				break
	
		print('<player3>')
		while(1):
			if (c[0].finish==1 and c[1].finish==1 and c[2].finish==1 and c[3].finish==1):
				print ('Winner is player3')
			c.throw()
			while(1):
				select = input("which piece do you want to move? only 0~3")
				if (c[select].finish!=0):
					print ('You picked wrong piece.')
				else:
					break
			if(c[select].move()):
				c[select].check(list)
			else:
				c[select].check(list)
				break
	
		print('<player4>')
		while(1):
			if (d[0].finish==1 and d[1].finish==1 and d[2].finish==1 and d[3].finish==1):
				print ('Winner is player4')
			d.throw()
			while(1):
				select = input("which piece do you want to move? only 0~3")
				if (d[select].finish!=0):
					print ('You picked wrong piece.')
				else:
					break
			if(d[select].move()):
				d[select].check(list)
			else:
				d[select].check(list)
				break
		print('=========================================')
	





