from createuser import createuser
from getboard import getboard
from postboard import postboard
from deluser import deluser
import json
import time

userNum = 100

def createNusr(n):
    ulist = []
    for i in range(0,n):
        #print(i)
        ulist.append(json.loads(createuser(i)))
    return ulist

def parseboard(Bjson,UID):
    ps = Bjson["players"]
    for p in ps:
        if(p["id"] == UID):
            return (Bjson["round"],p,Bjson["goals"])
    

Ulist = createNusr(userNum)
roundList = []
playerList = []
#print(Ulist)
for i in range(0,userNum):
    rnd,ply,goals = parseboard(json.loads(getboard(Ulist[i]["boardId"],Ulist[i]["userId"])),Ulist[i]["userId"])
    roundList.append(rnd)
    playerList.append(ply)
    #print(rnd,ply)
try:
    while(True):
        for i in range(0,userNum):
            rnd,ply,goals = parseboard(json.loads(getboard(Ulist[i]["boardId"],Ulist[i]["userId"])),Ulist[i]["userId"])
            if(rnd > roundList[i]):
                postboard(Ulist[i]["boardId"],Ulist[i]["userId"],rnd,ply,goals)
                #postboard
            roundList[i] = rnd
            playerList[i] = ply
            #print(rnd,ply)
            print(ply)
        
        time.sleep(0.5)
except (KeyboardInterrupt):
    for U in Ulist:
        deluser(U["boardId"],U["userId"])
    rollback()
    raise
#print(parseboard(json.loads(getboard(Ulist[0]["boardId"],Ulist[0]["userId"])),Ulist[0]["userId"]))
#if round +1 then post
#else continue getboard
