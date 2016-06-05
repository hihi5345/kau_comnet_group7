from django.shortcuts import render
from django.views import generic
import time

from .models import Player, Board
from .forms import SignUpForm

# Create your views here.
def IndexView(request):
    s_nickname = request.session.get('nickname',False)
    try:
        player = Player.objects.get(nickname = s_nickname)
        player.online = True
        player.save()
        request.session['online'] = True
    except:
        request.session.pop('nickname',None)
        request.session.pop('online',None)
        request.session.pop('board',None)

    online = request.session.get('online',False)
    if not online:
        form = SignUpForm(request.POST or None)
        context = {
            'form': form,
        }
        
        if form.is_valid():
            instance = form.save(commit=False)
            nickname = form.clean_nickname()
            instance.nickname = nickname
            request.session['nickname'] = nickname
            instance.online = True
            request.session['online'] = True
            instance.save()
            
            return IndexView(request)
            
        return render(request,'index.html', context)
        
    else:
        b_id = request.session.get('board',False)
        if b_id:
            return BoardView(request, b_id)
        else:
            return Waiting(request)


def BoardView(request, id, context=None):
    board = Board.objects.get(id=id)
    if context==None:
        route1 = [{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}]
        route2 = [{},{},{},{},{},{},{},{},{},{},{},{}]
        route3 = [{},{},{},{},{},{},{}]
        turn = 1
        context = {
            'route1': route1,
            'route2': route2,
            'route3': route3,
            'turn' : turn,
            
        }
    
    template_name = 'board_throw.html'
    
    return render(request, template_name, context)
    
def Waiting(request):
    waiters = Player.objects.filter(online=True, board=-1)
    print(waiters, len(waiters))
    if len(waiters)>=2:
        b = Board()
        b.P1 = waiters[0].id
        b.P2 = waiters[1].id
        b.save()
        waiters[0].board = b.id
        waiters[0].save()
        waiters[1].board = b.id
        waiters[1].save()
        request.session['board'] = b.id
        
        return BoardView(request, b.id)
    else:
        time.sleep(1)
        return Waiting(request)

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
        
def newstart(request, d):
    if request.session['waiting']==0:
        return go(request, player, d)
   
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




##class board:
##  def go(self,player,d):
##    select = int(input("어떤것을 사용하실건가요? : "))
##    select_unit_route=int(input("어떤 말을 사용하실건가요?(루트입력) : "))
##    select_unit_index=int(input("말 인덱스 입력"))
##    select_unit_name="P%d"%player
##    if(self.home_in(select_unit_route,select_unit_index,select)):
##      if(select_unit_route==1):
##        value=self.route1[select_unit_index].get("P%d"%player,0)
##      elif(select_unit_route==3):
##        value=self.route3[select_unit_index].get("P%d"%player,0)
##      d.remove(select)
##      return value
##    else:
##      if(select==-1 and select_unit_route==2 and select_unit_index==0):
##        self.route1[4][select_unit_name] = self.route1[4].get("P%d"%player,0) + self.route2[0][select_unit_name]
##        self.route2[0]={}
##      elif(select==-1 and select_unit_route==3 and select_unit_index==0):
##        self.route1[9][select_unit_name] = self.route1[9].get("P%d"%player,0) + self.route3[0][select_unit_name]
##        self.route3[0]={}
##      else:
##        if(select_unit_route==1):
##            self.route1[select_unit_index+select][select_unit_name] = self.route1[select_unit_index+select].get("P%d"%player,0) + self.route1[select_unit_index][select_unit_name]
##            self.route1[select_unit_index].pop(select_unit_name)
##        elif(select_unit_route==2):
##            self.route2[select_unit_index+select][select_unit_name] = self.route2[select_unit_index+select].get("P%d"%player,0) + self.route2[select_unit_index][select_unit_name]
##            self.route2[select_unit_index].pop(select_unit_name)
##        elif(select_unit_route==3):
##            self.route3[select_unit_index+select][select_unit_name] = self.route3[select_unit_index+select].get("P%d"%player,0) + self.route3[select_unit_index][select_unit_name]
##            self.route3[select_unit_index].pop(select_unit_name)
##    
##      d.remove(select)
##
##      self.check(player)
##      return 0
##        
##  def eat(self,player):
##    for i in range(3):
##      if(i==0):
##        for j in range(len(self.route1)):
##          if(self.route1[j].get("P1",0) != 0 and self.route1[j].get("P2",0) != 0):
##            temp=self.route1[j].get("P%d"%enemy(player))
##            self.route1[j]={"P%d"%player:self.route1[j].get("P%d"%player)}
##            return [player,temp]                
##
##      elif(i==1):
##        for j in range(len(self.route2)):
##          if(self.route2[j].get("P1",0) != 0 and self.route2[j].get("P2",0) != 0):
##            temp=self.route2[j].get("P%d"%enemy(player))
##            self.route2[j]={"P%d"%player:self.route2[j].get("P%d"%player)}
##            return [player,temp]
##          
##      else:
##        for j in range(len(self.route3)):
##          if(self.route3[j].get("P1",0) != 0 and self.route3[j].get("P2",0) != 0):
##            temp=self.route3[j].get("P%d"%enemy(player))
##            self.route3[j]={"P%d"%player:self.route3[j].get("P%d"%player)}
##            return [player,temp]
##
##    return [0,0]
##
##  def home_in(self, route, index,d):
##    if(route==1):
##      if(index+d>20):
##        self.route1[index]={}
##        print("완주했습니다.")
##        return 1
##    elif(route==3):
##      if(index+d>6):
##        self.route3[index]={}
##        print("완주했습니다.")
##        return 1
##    else:
##      return 0
##
##  def check(self, player):
##    if self.route1[0]:
##      self.route1[20]["P%d"%player] = self.route1[20].get("P%d"%player,0) +1
##      self.route1[0]={}
##    if self.route1[5]:
##        self.route2[0]["P%d"%player] = self.route2[0].get("P%d"%player,0) +1
##        self.route1[5] = {}
##    if self.route1[10]:
##        self.route3[0]["P%d"%player] = self.route3[0].get("P%d"%player,0) +1
##        self.route1[10] = {}
##    if self.route2[3]:
##        self.route3[3]["P%d"%player] = self.route3[3].get("P%d"%player,0) +1
##        self.route2[3] = {}
##    if self.route3[6]:
##        self.route1[20]["P%d"%player] = self.route1[20].get("P%d"%player,0) +1
##        self.route3[6] = {}
##    for i in range(6,12):
##      if self.route2[i]:
##        self.route1[i+9]["P%d"%player] = self.route1[i+9].get("P%d"%player,0) +1
##        self.route2[i]={}

