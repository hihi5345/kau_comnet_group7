from django.db import models
##from django.contrib.auth.models import User as U


# Create your models here.
class Board(models.Model):
    P1 = models.IntegerField(default=-1)
    P2 = models.IntegerField(default=-1)
    
class Player(models.Model):
    nickname = models.CharField(max_length=30, default='')
    online = models.BooleanField(default = False)
    
    board = models.IntegerField(default=0)
    mset = models.CharField(max_length=128, default=('빽도','도','개','걸','윷','모'))
    combination = models.IntegerField(default=0)
    waiting = models.IntegerField(default=4)
    finish = models.IntegerField(default=0)

    def __str__(self):
        return self.nickname


class Distance(models.Model):
    Player = models.ForeignKey(Player, on_delete=models.CASCADE)
    distance = models.IntegerField(default=0)
    
    def __str__(self):
        return self.distance

