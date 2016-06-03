from django.db import models
##from django.contrib.auth.models import User as U


# Create your models here.
##class Board(models.Model):
##    route = models.CharField(max_length=128, default=('빽도','도','개','걸','윷','모'))
####    route1 = models.CharField(max_length=128, default=('빽도','도','개','걸','윷','모'))
####    route2 = models.CharField(max_length=128, default=('빽도','도','개','걸','윷','모'))
####    route3 = models.CharField(max_length=128, default=('빽도','도','개','걸','윷','모'))




class Player(models.Model):
##    Board = models.ForeignKey(Board, on_delete=models.CASCADE)
    
    nickname = models.CharField(max_length=30, default='')
    online = models.BooleanField(default = False)
    
    mset = models.CharField(max_length=128, default=('빽도','도','개','걸','윷','모'))
    combination = models.IntegerField(default=0)
    waiting = models.IntegerField(default=4)
    finish = models.IntegerField(default=0)

    def __str__(self):
        return self.nickname


class Distance(models.Model):
    Player = models.ForeignKey(Player, on_delete=models.CASCADE)
    distance = models.IntegerField(default=0)
