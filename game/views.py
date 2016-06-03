from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Player
from .forms import SignUpForm

# Create your views here.
def IndexView(request):
    title = '윷놀이'
    print(request, Player.objects.values())
    form = SignUpForm(request.POST or None)
    context = {
        'title': title,
        'form': form,
    }

    if form.is_valid():
        instance = form.save(commit=False)
        nickname = form.clean_nickname()
        instance.nickname = nickname
        instance.save()
        board = BoardView()
        return board
        
    return render(request,'index.html', context)

class BoardView(generic.View):
    
    model = None
    template_name = 'board.html'

    def get(self):
        route1 = [{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}]
        route2 = [{},{},{},{},{},{},{},{},{},{},{},{}]
        route3 = [{},{},{},{},{},{},{}]
        context = {
            'route1': route1,
            'route2': route2,
            'route3': route3,
        }

        return render_to_response(context)







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
