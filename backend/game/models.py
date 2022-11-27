from asyncio import tasks
import math
from mimetypes import init
from django.db import models

class Lobby():
    
    def __init__(self,_id,nrounds) -> None:
        self.id=_id
        self.players={}
        self.state='waitingForPlayers'
        self.task=[]
        self.round=0
        self.nrounds=nrounds

    def set_tasks(self, task):
        self.task=task
    
    def get_task(self):
        i=self.round%self.nrounds
        self.round+=1
        return self.task[i]
        

    def get_player_data(self, player):
        return self.players[player]

    def dropLastPlayer(self):
        points=[]
        for p in self.players:
            points.append(self.players[p][0])
        lowestscore=min(points)
        for p in self.players:
            if self.players[p][0] == lowestscore:
                self.players[p][1]=False
                return


    def calculate_score(self,lat,long,player):
        i=self.round-1
        task=self.task[i]
        diff1=lat-task['lat']
        diff2=long-task['long']
        distance=(diff1**2+diff2**2)
        score=int(100*math.log(100+10000/max(1,distance),2))
        print(distance)
        print(score)
        self.players[player][0] += score

    def add_player(self,player):
        self.players[player]=[0,True]

    def size(self):
        return len(self.players)

    def get_players(self):
        return self.players.keys()

    def get_id(self):
        return self.id

    def player_score(self, player):
        return self.players[player]