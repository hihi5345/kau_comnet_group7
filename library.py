from .models import Player1, Player2, Client, Yuut
import random

def count(player):				#통과한 말을 세는 함수 입니다.
	count=[]
	for i in player:	
		if(i.finish==1):
			count.append(i.order)	#플레이어가 가진 말중에 통과한 말이 있다면 리스트에 모아줍니다
	return sorted(count) 			#그 후 정렬된 리스트를 반환합니다.

def left(player):				#남은 말을 세는 함수 입니다.
	left=[]
	for i in player:
		if(i.finish==0):
			left.append(i.order)	#플레이어가 가진 말이 통과를 하지 않았다면 리스트에 모아줍니다.
	return sorted(left) 			#그 후 정렬된 리스트를 반환합니다.
	
def print_():						#숫자를 문자로 바꾸어 출력해주는 함수 입니다.
	temp=Yuut.objects.all()				#데이터 베이스에 저장된 윷의 정보들을 가져옵니다.
	list1=[]
	for i in temp:	 
		if(i.yut!=0):				#데이터베이스에 저장된 값이
			if(i.yut==1): 
				list1.append('도') 	#1일경우에는 도
			elif(i.yut==2):
				list1.append('개')	#2일경우에는 개
			elif(i.yut==3):
				list1.append('걸')	#3일경우에는 걸
			elif(i.yut==4):
				list1.append('윷')	#4일경우에는 윷
			elif(i.yut==5):
				list1.append('모')	#5일경우에는 모
			elif(i.yut==6):
				list1.append('빽도')	#6일경우에는 빽도를 리스트에 추가하여 반환합니다.
	return list1
				

def ip(self): 						#클라이언트의 ip를 저장하는 함수 입니다.
	temp_ip=self.META['REMOTE_ADDR'].split('.')	#.을 구분하지않고 숫자만을 저장해옵니다
	new_ip="".join(temp_ip)[:] 			#.없이 새로운 아이피 주소를 만들어 냅니다
	real_ip=int(new_ip) 				#type은 정수타입입니다.
	ip=Client.objects.get(ip=real_ip) 		#그리고 그 아이피 주소와 같은 클라이언트 정보를 데이터베이스로부터 가져옵니다
	return ip

def start(): 							#윷을 처음 초기화 하는 코드입니다.
	Player1.objects.all().delete()				#데이터 베이스를 비우고 시작합니다.
	Player2.objects.all().delete()
	a=Player1(x=0, y=0, finish=0, together=1, order=1)	#플레이어1,2의 말들의 정보를 좌표상위치 0,0로 초기화하여 저장합니다
	a.save()						#그리고 만약 겹친상태라면 말을 부르느 명령(order)를 통하여 겹친말의 수(together)를 구분할 수 있도록 합니다.
	a=Player1(x=0, y=0, finish=0, together=2, order=2)	
	a.save()
	a=Player1(x=0, y=0, finish=0, together=3, order=3)
	a.save()
	a=Player1(x=0, y=0, finish=0, together=4, order=4)
	a.save()
	
	b=Player2(x=0, y=0, finish=0, together=1, order=1)
	b.save()
	b=Player2(x=0, y=0, finish=0, together=2, order=2)
	b.save()
	b=Player2(x=0, y=0, finish=0, together=3, order=3)
	b.save()
	b=Player2(x=0, y=0, finish=0, together=4, order=4)
	b.save()
	
	c=Yuut(yut=0, count=0, next=1, to_move=0)	#count는 윷의 순서, next는 플레이어의 순서, to move는 움직일 말이고 이정보를 초기화하여 따로 저장합니다.
	Yuut.objects.all().delete()			#그 후 윷클래스의 데이터 베이스 정보를 비워둡니다.
	c.save()
	
def board():					#말판을 구현하는 함수 입니다.
	def board_(self):
		a=0				#a,b,c,d는 각각 겹친말이 하나인 것의 개수 ~ 겹친말이 네개인 것의 개수를 의미합니다.
		b=0
		c=0
		d=0
		for i in self:			#만약에 자신의 정보값에 겹쳐있는말이 있다면 겹쳐진 말들의 세트만큼 a,b,c,d값을 올려줍니다
			if (i.together==1):
				a+=1
			elif (i.together==2):
				b+=1
			elif (i.together==3):
				c+=1
			elif (i.together==4):
				d+=1
		if (a==0):			#아무것도 들어가 있지 않을 때는 윷에 명령할 때 order1 을 적용할 수 있도록 처리해 줍니다 
			a=1
		if (b==0):
			b=1
		if (c==0):
			c=1
		if (d==0):
			d=1
		list=[]				#각각의 정보를 리스트에 담아서 그에 맞게 order값들을 가지고 있도록 합니다.
		list.append(a) 			#order -> 1 number
		list.append(b) 			#order -> 2 number
		list.append(c) 			#order -> 3 number
		list.append(d) 			#order -> 4 number
		return list

	route = [[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],	#말판입니다. 각각 순서대로 player number, 몇번째 말인지, 업힌 말의 수를 의미합니다.
	[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],
	[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],
	[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],
	[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],
	[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],
	[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],
	[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]]
	p_1=Player1.objects.all()							#각각의 플레이어들의 데이터 정보값을 받아옵니다.
	p_2=Player2.objects.all()
	
	count=0
	temp1=board_(p_1)								#플레이어1의 정보를 임시말판에 입력합니다.
	for i in p_1:									#말판에서 아직 도착처리가 되지 않은 말일경우
		if(i.finish!=0):
			if(i.x!=-1 and i.y!=-1):
				route[i.x][i.y][0]=1					#말판의 첫번째 원소에 플레이어 1이라는 표시와
				route[i.x][i.y][1]=i.order				#몇번 째 말인지를 입력합니다.
				if(i.together==i.order): 				#그 후 임시 말판으로 부터 겹쳐진 말의 개수를입력합니다.
					if(i.order==1): 
						if (temp1[0]>route[i.x][i.y][2]): 	#보드판에 말의 수를 입력합니다 
							route[i.x][i.y][2]=temp1[0]
					elif(i.order==2):
						if (temp1[1]>route[i.x][i.y][2]):
							route[i.x][i.y][2]=temp1[1]
					elif(i.order==3):
						if (temp1[2]>route[i.x][i.y][2]):
							route[i.x][i.y][2]=temp1[2]
					elif(i.order==4):
						if (temp1[3]>route[i.x][i.y][2]):
							route[i.x][i.y][2]=temp1[3]
	temp2=board_(p_2)								#플레이어2도 같은 처리를 해줍니다
	for j in p_2: 
		if(j.finish!=0):
			if(j.x!=-1 and j.y!=-1):
				route[j.x][j.y][0]=2
				route[j.x][j.y][1]=j.order
				if(j.together==j.order):
					if(j.order==1):
						if (temp2[0]>route[j.x][j.y][2]):
							route[j.x][j.y][2]=temp2[0]
					elif(j.order==2):
						if (temp2[1]>route[j.x][j.y][2]):
							route[j.x][j.y][2]=temp2[1]
					elif(j.order==3):
						if (temp2[2]>route[j.x][j.y][2]):
							route[j.x][j.y][2]=temp2[2]
					elif(j.order==4):
						if (temp2[3]>route[j.x][j.y][2]):
							route[j.x][j.y][2]=temp2[3]
				
	return route 									#최종적인 맵의 정보값을 반환합니다.
		
def throw(you):							#윷던지기를 처리하는 함수 입니다.
	tempyut=Yuut.objects.all()				#데이터베이스로부터 윷의 저장형태를 받아옵니다.
	for i in tempyut:					#도개걸윷모빽도는 1~6으로 표현할 것이기 때문에 0으로 된 값은 지워줍니다.
		if(i.yut==0):
			i.delete()
	
	counting=0 						#한번 더 던질 수 있는지 아닌지를 나타냅니다.
	yuut = 0 						#각각 랜덤함수를 통해서 윷을 던지고 뒤집혔다면 1로 판단하여 그 개수 더하여 저장합니다.
	first = random.randint(0,1)
	second = random.randint(0,1)
	third = random.randint(0,1)
	fourth = random.randint(0,1)
	yuut=first+second+third+fourth
	if(yuut==4 or yuut==0):					#만일 윷(4)또는 모(0)가 나왔을 경우 카운트를 증가시켜 다시 던질 수 있도록 합니다.
		counting=2
		if(yuut==0):					#그리고 실제로 모는 4로 윷은 5로 사용할 것이기 때문에 그에 맞게 바꾸어줍니다.
			yuut=4
		elif(yuut==4):
			yuut=5
	elif(yuut==1 and first==1):				#만약에 도가 나왔는데 첫번째 윷가락이 뒤집힌거면 빽도로 인식하여 사용하는 빽도 넘버인 6을 대입합니다
		yuut=6 
			
	temp=Yuut(yut=yuut, count=0, next=you.count, to_move=0) #이제 윷정보를 입력해서 저장후 다시던질 수 있는 지 여부를 반환합니다.
	
	temp.save() 
	return counting

def select(yuut, move, you):							#이동할 말을 고르는 함수 입니다.
	checking=Yuut.objects.all()						#먼저 데이터베이스로 부터 정보값을 가져옵니다.
	checking_num=0
	for i in checking: 							#플레이어가 사용할 수 있는 말을 골랐는지 판단을 합니다.
		if (i.yut == yuut):
			if (i.count==0):
				checking_num=1
	if (checking_num==0): 							#잘못 선택되었다면 반환값을 통하여 재선택을 할 수 있도록 합니다.
		return 1
	
	backdoe_check=0
	if(you.count==1 or you.count==3): 					#team1일 경우
		current=Player1.objects.get(order=move)				#말의 정보를 order를 통하여 비교하고 가져옵니다.
		if(current.finish==1): 						#완주한 말일경우 바로 리턴을 처리합니다.
			return 1
		elif (current.x==0 and current.y==0 and yuut==6): 
			for i in checking:					#첫 빽도가 나왔을 때 그것을 선택하지 못하게 처리합니다.
				if(i.to_move==current.order):
					backdoe_check=1
					break
			if(backdoe_check==0):
				return 1
		elif(current.together!=current.order): 				#말을 업은 상태가 되었을 때 together와 order가 다를수 있기 때문에 이상황에 대해 정의해 줍니다. 
			while(1):
				temp=Player1.objects.get(order=current.together)
				if(temp.together==temp.order):			#새로운 together값 정보를 계속 받아오고 같아지면 루프를 벗어납니다.
					move=temp.order
					break
	elif(you.count==2 or you.count==4): 					#team2도 같은 원리로 처리해 줍니다.
		current=Player2.objects.get(order=move)
		if(current.finish==1):
			return 1
		elif (current.x==0 and current.y==0 and yuut==6):
			for i in checking:
				if(i.to_move==current.order):
					backdoe_check=1
					break
			if(backdoe_check==0):
				return 1
		elif(current.together!=current.order):
			while(1):
				temp=Player2.objects.get(order=current.together)
				if(temp.together==temp.order):
					move=temp.order
					break
	
	templist=[]						#윷의 순서를 부여하는 코드입니다
	allyut=Yuut.objects.all()				#예를들어 사용자가 걸, 모 순서대로 사용할 때, 걸이 먼저 사용되도록 새롭게 배치합니다.
	tempnum=0
	all_yuut=Yuut.objects.all()
	for h in all_yuut:
		templist.append(h.count)
	for l in allyut:
		if(l.yut==yuut and l.count==0):
			for k in templist:
				if (k>tempnum):
					tempnum=k
			moved=Yuut(yut=l.yut, count=tempnum+1, next=l.next, to_move=move)
			l.delete()
			moved.save()
			break 					#새롭게 만들어진 순서를 저장하고 루프를 벗어납니다
	check=0
	to_check=Yuut.objects.all()
	for j in to_check: 					#잘못된 선택인지 검사를 하고 재선택여부를 결정합니다
		if (j.count==0):
			check=1
	if (check==1):
		return 2
	return 0
		
			
def play(you):
	temp_yuut=Yuut.objects.order_by('count')	
	
	
	
	
	for current_yuut in temp_yuut: 								#윷정보값에서
		if(you.count==1 or you.count==3):						#만약 team1일경우
			current=Player1.objects.get(order=current_yuut.to_move)			#이동값을 order에 대입한 player1의 데이터 형태로 받아옵니다. 
			tempnum=current_yuut.to_move
			if(current.together!=current.order):					#위에 select에서 처럼 order와 겹친말의 수가 같아질때까지 새로 정보를 받아오게 되고
				while(1):
					temp=Player1.objects.get(order=current.together)
					if(temp.together==temp.order):				#같아지면 루프를 벗어납니다.
						tempnum=temp.order
						break
			current_player=Player1.objects.get(order=tempnum) 			#선택한 말을 나타냅니다.
			
			if(move(current_player, current_yuut.yut, 1)): 				#움직이거나, 먹었을떄, 업었을때, 통과할 때 등등 새롭게 던질 수 있을때
				current_yuut.delete()
				zero=Yuut(yut=0, count=0, next=current_yuut.next, to_move=0) 	#초기화하고
				zero.save() 
				return 1							#다시 던집니다.


			count=0	
			j=Player1.objects.all()							#모든정보값을 가져옵니다
			for i in j:
				if (i.finish==1): 						#완주한 말이 있는지 체크합니다.(count변수 = 통과한 말의 수)
					count+=1
			if (count==4): 								#만약에 완주한 말이 4개가 된다면 
				Client.objects.all().delete()
				return 2							#team1이 승리임을 반환합니다
		
		elif(you.count==2 or you.count==4): 						#team2도 같은 원리를 이용하여 처리합니다.
			current=Player2.objects.get(order=current_yuut.to_move)
			tempnum=current_yuut.to_move
			if(current.together!=current.order):
				while(1):
					temp=Player2.objects.get(order=current.together)
					if(temp.together==temp.order):
						tempnum=temp.order
						break
			current_player=Player2.objects.get(order=tempnum)
			
			if(move(current_player, current_yuut.yut, 2)):
				current_yuut.delete()
				zero=Yuut(yut=0, count=0, next=current_yuut.next, to_move=0)
				zero.save()
				return 1
			
			count=0
			k=Player2.objects.all()
			for i in k:
				if (i.finish==1):
					count+=1
			if (count==4):
				Client.objects.all().delete()
				return 3
	
	num=you.count+1										
	q=0
	for p in Client.objects.all(): 								#턴을 바꾸는 코드입니다. num이 순서대로 1,2를 반복하도록합니다.
		q+=1
	if(num>q):
		num=1
	reyuut=Yuut(yut=0, count=0, next=num, to_move=0) 					#턴을넘길때는 불필요한 정보를 다 지우고 저장후 넘어갑니다.
	Yuut.objects.all().delete()
	reyuut.save()
	
	return 4 										#다음턴임을 나타냅니다.


	
def move(self, yuut, team):						#말을 움직이는 코드입니다.
	if (yuut==6): 							#빽도의 경우 6칸이 아니라 -1칸을 가는 것이므로 수정합니다.			
		yuut=-1
	if(self.x==0 and self.y==0 and self.finish==-1): 		#0,0일때 말이 출발한 상태에서
		if(yuut==-1): 						#만약빽도이면 그냥 도 처리를 해줍니다.
			self.x=1
		else: 							#나머지 출발하지 않은 말은 -1,-1에 고정합니다.
			self.x=-1
			self.y=-1
	self.finish=-1 							#출발전 finish=-1, 아직도착안함 finish=0, 완주함 finished = 1
	
	if (self.x==0): 						#x축이 고정되고 y축이 변화해야할때
		if(self.y==0):
			self.y=yuut					#윷이 나온만큼 y축을 이동합니다
		elif (self.y==5): 					#만약에 꺾여서 대각선으로 이동하는 경우일때 각 윷의 종류에 따라 좌표상 어디로갈지 설정합니다.
			if(yuut==5): 					
				self.x=7 				
				self.y=1
			elif(yuut==-1):
				self.y=4
			else:
				self.x=yuut
				self.y=5-yuut
		elif(self.y+yuut>4):
			self.x=self.y+yuut-5
			self.y=5
		else:
			if(self.y==1 and yuut==-1):			#만약 도에서 빽도가 나오면 말을 회수합니다
				self.y=0
				self.finish=0
			else:
				self.y=self.y+yuut
	
	elif (self.y==5):						#마찬가지로 꺾이는 부분에서 예외 처리 하는데, 맵에서 사용하는 맵이 7by7 행렬이므로 그에 맞게 루트를 변경합니다.
		if (self.x==5):
			if (yuut==5):
				self.x=7
				self.y=7
			elif(yuut==-1):
				self.x=4
			else:
				self.x=5-yuut
				self.y=5-yuut
		elif (self.x+yuut>4):
			self.y=5-(self.x+yuut-5)
			self.x=5
		else:
			self.x=self.x+yuut
	
	elif (self.x==5):						#마찬가지로 모퉁이에서 말이 이동하는 작업입니다
		if (self.y==0):
			if(yuut==-1):
				self.y=1
			else:
				self.x=5-yuut
		elif (self.y-yuut<0):
			self.x=5-yuut+self.y
			self.y=0
		else:
			self.y=self.y-yuut
	elif (self.y==0):						#y축이 0일때 윷이나온만큼 이동후 0보다 작아진다면 다시 말을 회수시켜줍니다.
		if (self.x-yuut<0):		
			self.y=-1
			self.x=-1
		else:
			self.x=self.x-yuut				#아닐경우 그 만큼 거리를 이동합니다.
	
	else:
		if ((self.x<3 and self.y>2) or (self.x>3 and self.y<3)):	#세부 예외처리 부분입니다. 구간들을 나누어 상황을 분석하고. 말판이 7by7이므로 그에 맞게 이동시킵니다.
			if(self.x+yuut>5):
				if (self.x==7):
					if (yuut==-1):
						self.x=4
						self.y=1
					else:
						self.x=5-(self.x+yuut-8)
						self.y=0
				else:									
					self.x=5-(self.x+yuut-6)
					self.y=0
			else:
				if(self.x+yuut==5):
					self.x=7
					self.y=1
				else:
					self.x=self.x+yuut
					self.y=self.y-yuut
		else:
			if(self.x-yuut<-1 or self.y==7):
				if(self.y==7):
					if(yuut==-1):
						self.x=1
						self.y=1
					elif(yuut>1):
						self.x=-1
						self.y=-1
					else:
						self.x=0
						self.y=0
				else:
					self.y=-1
					self.x=-1
			else:	
				if(self.x-yuut==0):
					self.x=7
					self.y=7
				elif(self.x-yuut==-1):
					self.x=0
					self.y=0
				else:
					self.x=self.x-yuut
					self.y=self.y-yuut 		#어떤 예외처리에도 걸리지 않으면 그냥 움직입니다.

	if (self.x==3 and self.y==2): 					#가운데 부분을 3,2에서 2,2로 변경합니다.
		self.x=2					

	if (self.x==-1 and self.y==-1): 				#말이 -1,-1에 도착하면 도착한 상태로 바꾸어 줍니다.
		self.finish=1
	
	re=0
	
	if (team==1): 							#team1이 말을 먹고 얹을때 그 말들을 처리하는 코드입니다.
		all1=Player1.objects.all()
		for i in all1:
			if (i.together==self.order): 			#if the piece is eaten by self -> move to self
				temp_1=Player1(x=self.x, y=self.y, finish=self.finish, together=i.together, order=i.order)
				i.delete()
				temp_1.save() 
		to_save=Player1(x=self.x, y=self.y, finish=self.finish, together=self.together, order=self.order) #self save
		Player1.objects.get(order=self.order).delete()
		to_save.save()
		team_1=Player1.objects.all()
		for i in team_1: 					#만약 같은팀을 먹을 때(다시말해 얹을 때)
			if (i.x == self.x and i.y == self.y):
				if(i.together!=self.order): 		#아직 먹지 않은 말일 때
					if(i.finish==-1): 		#0,0이 아니고, 말판 위에 있는 상태일때
						temp3=Player1(x=self.x, y=self.y, finish=self.finish, together=self.order, order=i.order) #얹은 말을 order를 사용해 조정해 줍니다.
						i.delete()
						temp3.save() 
		team_2=Player2.objects.all()
		for j in team_2: 					#만약 다른팀을 먹을 때
			if (j.x == self.x and j.y == self.y):
				if (j.finish==-1): 			#0,0이 아니고, 말판 위에 있는 상태일때
					temp4=Player2(x=0, y=0, finish=0, together=j.order, order=j.order) #먹은 말을 0,0으로 보내고 출발하지 않은 상태로 처리합니다.
					j.delete()
					temp4.save() 
					re=1 				#말을 잡았으므로 한번 더 던질 수 있도록 합니다.
		
		
	elif(team==2): 							#team2에 경우에도 같은 원리로 처리합니다.
		all2=Player2.objects.all()
		for i in all2:
			if (i.together==self.order):
				temp_2=Player2(x=self.x, y=self.y, finish=self.finish, together=i.together, order=i.order)
				i.delete()
				temp_2.save()
		to_save=Player2(x=self.x, y=self.y, finish=self.finish, together=self.together, order=self.order)
		Player2.objects.get(order=self.order).delete()
		to_save.save()
		team_2=Player2.objects.all()
		for i in team_2:
			if (i.x == self.x and i.y == self.y):
				if(i.together!=self.order):
					if(i.finish==-1):
						temp3=Player2(x=self.x, y=self.y, finish=self.finish, together=self.order, order=i.order)
						i.delete()
						temp3.save()
		team_1=Player1.objects.all()
		for j in team_1:
			if (j.x == self.x and j.y == self.y):
				if (j.finish==-1):
					temp4=Player1(x=0, y=0, finish=0, together=j.order, order=j.order)
					j.delete()
					temp4.save()
					re=1
	
	return re
