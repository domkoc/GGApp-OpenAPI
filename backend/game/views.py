from asyncio import tasks
import json

from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest,HttpResponse
import mysql.connector
from . import models
from django.views.decorators.csrf import csrf_exempt
from random import sample


lobbies=[]
nrounds=5

@csrf_exempt
def create_lobby(request):
    if request.method=='POST':
        body = json.loads(request.body)
        player=body['username']
        id=body['lobbyId']
        for l in lobbies:
            if id in l.get_id():
                return HttpResponseBadRequest('Lobby id is already taken')

        lobby = models.Lobby(id,nrounds)
        lobby.add_player(player)
        lobbies.append(lobby)
        task=[]
        db=connectToDB()
        taskns=sample(range(1,400),nrounds)
        c=db.cursor()
        c.execute('SELECT * FROM location')
        c=c.fetchall()
        db.close()
        for i in taskns:
            task.append({'lat':c[i][1],"long":c[i][2]})
        lobby.set_tasks(task)
        lobby={'username':player,'lobbyId':id}
        return JsonResponse(lobby)

    
    return HttpResponseBadRequest('Only POST requests are allowed')


    return JsonResponse(lobby)
@csrf_exempt
def start_lobby(request,lobby_id):
    if request.method=='POST':
        lobby=0
        for l in lobbies:
            if l.get_id()==lobby_id:
                lobby=l
        if lobby==0:
            return HttpResponseBadRequest('Non existing lobby')
        players=[]
        lobby.state='start'
        for p in lobby.get_players():
            players.append({'username':p,'score':0,'isPlaying':True})
        jobj={'state':'start','players':players}

        return JsonResponse(jobj)

    return HttpResponseBadRequest('Only POST requests are allowed')


@csrf_exempt
def join_lobby(request):
    if request.method=='POST':
        body = json.loads(request.body)
        player=body['username']
        id=body['lobbyId']
        for l in lobbies:
            if l.get_id()== id:
                l.add_player(player)
                players=[]
                for p in l.get_players():
                    players.append({'username':p,'score':0,'isPlaying':True})
                jobj={'username':player,'lobbyId':l.get_id(),'players':players}   
                return JsonResponse(jobj)

        lobby = models.Lobby(id)
        lobby.add_player(player)
        lobbies.append(lobby)
        lobby={'username':player,'lobbyId':id}
        return JsonResponse(lobby)
        
    return HttpResponseBadRequest('Only POST requests are allowed')


@csrf_exempt
def scoreboard(request):
    db=connectToDB()
    cursor=db.cursor()
    if request.method=='GET':
        cursor.execute("select * from scoreboard order by score desc")
        cursor=cursor.fetchall()
        scores=[]
        for x in cursor:
            scores.append({'username':x[0],'score':x[1]})
        return JsonResponse({'players':scores})
    if request.method=='POST':
        body = json.loads(request.body)
        player=body['username']
        id=body['lobbyId']
        for l in lobbies:
            if l.get_id()==id:
                cursor.execute('INSERT INTO scoreboard values(%s,%s)',(player,l.player_score(player)))
                db.commit()
                return HttpResponse('Inseretd into db')
    return HttpResponseBadRequest('No good')

@csrf_exempt
def game(request,id):
    if request.method=='GET':
        lobby=0
        for l in lobbies:
            if l.get_id()==id:
                lobby=l
        if lobby==0:
            return HttpResponseBadRequest(f'No lobby with id {id}')
        players=[]
        lobby.dropLastPlayer()
        state=lobby.state
        for p in lobby.get_players():
            playerdata=lobby.get_player_data(p)
            players.append({'username':p,'score':playerdata[0],'isPlaying':playerdata[1]})
        return JsonResponse({'state':state,'players':players})

    return HttpResponseBadRequest('Only GET requests are allowed')

@csrf_exempt
def round(request,id):
    lobby=0
    for l in lobbies:
        if l.get_id()==id:
            lobby=l
    if request.method=='POST':
        body = json.loads(request.body)
        player=body['username']
        ans=body['answers']
        coordinates=ans[0]['coordinates']
        lat=coordinates['lattitude']
        long=coordinates['longitude']
        l.calculate_score(lat,long,player)
        return HttpResponse('ok')
    if request.method=='GET':
        gtasks=[]
        task=l.get_task()
        gtasks.append({ 'title':'title',
                        'coordinates':{'lattitude':task['lat'],'longitude':task['long']},
                        'seconds':10
                        })
        return JsonResponse({'tasks':gtasks})
    
    return HttpResponseBadRequest('Only POST or GET requests are alloved')


def connectToDB():
    mydb = mysql.connector.connect( host="localhost",
                                    port="8889",
                                    user="root",
                                    password="root",
                                    database='geoguesser'
                                    )
    return mydb