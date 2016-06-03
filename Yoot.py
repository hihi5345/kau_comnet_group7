import random

def enemy(player):
  if(player==1):
    return int(2)
  else:
    return int(1)

class game :
  def __init__(self) :
    self.mset = ('빽도','도','개','걸','윷','모')
    self.distance = [] #윷을 던져서 나온 목록
    self.combination = 0 #윷가락이 뒤집힌 횟수
    self.waiting = 4 #남은 말
    self.finish = 0 #통과한 말
    self.first = 0 #빽도가 표시된 윷가락

  def throw(self) :
    self.combination = 0 #초기화
    self.first = random.randint(0,1) #윷던짐
    second = random.randint(0,1) 
    third = random.randint(0,1)
    fourth = random.randint(0,1)
    self.combination += self.first #뒤집혔으면 갯수를 셈
    self.combination += second
    self.combination += third
    self.combination += fourth
    print (self.first, second, third, fourth)
    return (self.first, second, third, fourth)


  def move(self) :
    if (self.combination == 0): #모
      self.distance.append(5) #모의 거리를 추가
      print (self.mset[5]) #모라고출력
      self.play() #모니까 또던짐
    elif (self.combination == 1): #도
      if(self.first == 1): #빽도
        self.distance.append(-1) #빽도거리를 추가
        print (self.mset[0]) #빽도라고출력
      else :
        self.distance.append(1) #그냥도
        print (self.mset[1])     
    elif (self.combination == 2):#개
      self.distance.append(2)
      print (self.mset[2])   
    elif (self.combination == 3):#걸
      self.distance.append(3)
      print (self.mset[3])
    elif (self.combination == 4):#윷
      self.distance.append(4)
      print (self.mset[4]) 
      self.play() #윷이니까 또던짐
    else:
      None
    return None
    
  def printf(self):
    print (self.distance) #갈수있는거리를 출력
    return (self.distance)
    
  def getin(self):
    self.finish += 1 #통과말 증가
    return None
  
  def getout(self):
    self.waiting = self.waiting - 1 #대기말 감소
    return None
  
  def play(self): #던지고 거리계산
    self.throw()
    self.move()

class board:
  def __init__(self):
    self.route1 = [{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}]
    self.route2 = [{},{},{},{},{},{},{},{},{},{},{},{}]
    self.route3 = [{},{},{},{},{},{},{}]

  def newstart(self,player,d,waiting):
    if(waiting==0):
        print("남은 말이 없으므로 go로 갑니다!")
        return self.go(player,d)
   
    select = int(input("어떤것을 사용하실건가요? : "))
    if(select==-1):
      print('빽도는 newstart를 할수 없습니다.')
      return 0
    for i in d:
       if(i==select):
         self.route1[select]["P%d"%player] = self.route1[select].get("P%d"%player,0) + 1
    d.remove(select)

    self.check(player)
    
    return 1
  def go(self,player,d):
    select = int(input("어떤것을 사용하실건가요? : "))
    select_unit_route=int(input("어떤 말을 사용하실건가요?(루트입력) : "))
    select_unit_index=int(input("말 인덱스 입력"))
    select_unit_name="P%d"%player
    if(self.home_in(select_unit_route,select_unit_index,select)):
      if(select_unit_route==1):
        value=self.route1[select_unit_index].get("P%d"%player,0)
      elif(select_unit_route==3):
        value=self.route3[select_unit_index].get("P%d"%player,0)
      d.remove(select)
      return value
    else:
      if(select==-1 and select_unit_route==2 and select_unit_index==0):
        self.route1[4][select_unit_name] = self.route1[4].get("P%d"%player,0) + self.route2[0][select_unit_name]
        self.route2[0]={}
      elif(select==-1 and select_unit_route==3 and select_unit_index==0):
        self.route1[9][select_unit_name] = self.route1[9].get("P%d"%player,0) + self.route3[0][select_unit_name]
        self.route3[0]={}
      else:
        if(select_unit_route==1):
            self.route1[select_unit_index+select][select_unit_name] = self.route1[select_unit_index+select].get("P%d"%player,0) + self.route1[select_unit_index][select_unit_name]
            self.route1[select_unit_index].pop(select_unit_name)
        elif(select_unit_route==2):
            self.route2[select_unit_index+select][select_unit_name] = self.route2[select_unit_index+select].get("P%d"%player,0) + self.route2[select_unit_index][select_unit_name]
            self.route2[select_unit_index].pop(select_unit_name)
        elif(select_unit_route==3):
            self.route3[select_unit_index+select][select_unit_name] = self.route3[select_unit_index+select].get("P%d"%player,0) + self.route3[select_unit_index][select_unit_name]
            self.route3[select_unit_index].pop(select_unit_name)
    
      d.remove(select)

      self.check(player)
      return 0
        
  def eat(self,player):
    for i in range(3):
      if(i==0):
        for j in range(len(self.route1)):
          if(self.route1[j].get("P1",0) != 0 and self.route1[j].get("P2",0) != 0):
            temp=self.route1[j].get("P%d"%enemy(player))
            self.route1[j]={"P%d"%player:self.route1[j].get("P%d"%player)}
            return [player,temp]                

      elif(i==1):
        for j in range(len(self.route2)):
          if(self.route2[j].get("P1",0) != 0 and self.route2[j].get("P2",0) != 0):
            temp=self.route2[j].get("P%d"%enemy(player))
            self.route2[j]={"P%d"%player:self.route2[j].get("P%d"%player)}
            return [player,temp]
          
      else:
        for j in range(len(self.route3)):
          if(self.route3[j].get("P1",0) != 0 and self.route3[j].get("P2",0) != 0):
            temp=self.route3[j].get("P%d"%enemy(player))
            self.route3[j]={"P%d"%player:self.route3[j].get("P%d"%player)}
            return [player,temp]

    return [0,0]

  def home_in(self, route, index,d):
    if(route==1):
      if(index+d>20):
        self.route1[index]={}
        print("완주했습니다.")
        return 1
    elif(route==3):
      if(index+d>6):
        self.route3[index]={}
        print("완주했습니다.")
        return 1
    else:
      return 0

  def check(self, player):
    if self.route1[0]:
      self.route1[20]["P%d"%player] = self.route1[20].get("P%d"%player,0) +1
      self.route1[0]={}
    if self.route1[5]:
        self.route2[0]["P%d"%player] = self.route2[0].get("P%d"%player,0) +1
        self.route1[5] = {}
    if self.route1[10]:
        self.route3[0]["P%d"%player] = self.route3[0].get("P%d"%player,0) +1
        self.route1[10] = {}
    if self.route2[3]:
        self.route3[3]["P%d"%player] = self.route3[3].get("P%d"%player,0) +1
        self.route2[3] = {}
    if self.route3[6]:
        self.route1[20]["P%d"%player] = self.route1[20].get("P%d"%player,0) +1
        self.route3[6] = {}
    for i in range(6,12):
      if self.route2[i]:
        self.route1[i+9]["P%d"%player] = self.route1[i+9].get("P%d"%player,0) +1
        self.route2[i]={}
    

  def mapp(self):
    print(self.route1[20],self.route1[1], self.route1[2],'\t', self.route1[3], self.route1[4], self.route2[0] )
    print(self.route1[19],' ',self.route3[5],'\t ',self.route2[1],' ',self.route1[6])
    print(self.route1[18],'   ',self.route3[4],'     ',self.route2[2],'   ',self.route1[7])
    print(' \t  ',self.route3[3],'\t      ')
    print(self.route1[17],'   ',self.route2[4],'     ',self.route3[2],'   ',self.route1[8])
    print(self.route1[16],' ',self.route2[5],'\t ',self.route3[1],' ',self.route1[9])
    print(self.route1[15],self.route1[14],self.route1[13],'\t',self.route1[12],self.route1[11],self.route3[0])
    
    None
    

    
a = game()
b = game()  
table = board()

table.mapp()
while (1):
    print('<player1>')
    input()
    a.play()
    #a.distance[0]=5
    #a.distance.append(-1)
    if(a.waiting==4 and a.printf()[0]==-1):
        print("첫 빽도는 꽝!!!")
        a.distance.pop()
    else:
        while len(a.distance):
            print("1.newstart\n2.go(나가있는말)")
            select = int(input("무엇을 하실건가요 : "))
            if(select==1):
              if(table.newstart(1,a.printf(),a.waiting)==1):
                a.getout()
            elif(select==2):
              value_f1=table.go(1,a.printf())
              print (value_f1)
              if(value_f1):
                a.finish+=value_f1

            t1 = table.eat(1)
            table.mapp()
            if(t1[0]!=0):
              a.play()
              b.waiting+=t1[1]
            
            
            print()
            print ('A팀의 남은 말 수 : ',a.waiting)
            print ('A팀의 완주한 말 수 : ',a.finish)
            print ('B팀의 남은 말 수 : ',b.waiting)
            print ('B팀의 완주한 말 수 : ',b.finish)
    print()
    if(a.finish==4):
      print("A팀이 승리했습니다.")
      break;
    print('<player2>')
    input()
    b.play()
    if(b.waiting==4 and b.printf()[0]==-1):
        print("첫 빽도는 꽝!!!")
        b.distance.pop()
    else:
        while len(b.distance):
            print("1.newstart\n2.go(나가있는말)")
            select = int(input("무엇을 하실건가요 : "))
            if(select==1):
              if(table.newstart(2,b.printf(),b.waiting)==1):
                b.getout()
            elif(select==2):
              value_f2=table.go(2,b.printf())
              if(value_f2):
                b.finish+=value_f2
            t2 = table.eat(2)
            table.mapp()
            if(t2[0]!=0):
              b.play()
              a.waiting+=t2[1]
            
            print()
            print ('A팀의 남은 말 수 : ',a.waiting)
            print ('A팀의 완주한 말 수 : ',a.finish)
            print ('B팀의 남은 말 수 : ',b.waiting)
            print ('B팀의 완주한 말 수 : ',b.finish)
            print()
    if(b.finish==4):
      print("B팀이 승리했습니다.")
      break;
    print('=========================================')





