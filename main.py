from createuser import createuser
from getboard import getboard
from postboard import postboard
from deluser import deluser
import json
import time
import random

userNum = 95

def createNusr(n):
    ulist = []
    print(n)
    for i in range(0,n):
        ulist.append(json.loads(createuser(i)))
    return ulist

def parseboard(Bjson,UID):
    ps = Bjson["players"]
    for p in ps:
        if(p != None and p["id"] == UID):
            return (Bjson["round"],p,Bjson["goals"])
    return None,None,None

Ulist = createNusr(userNum)
#print(userNum)
roundList = []
playerList = []
#print(Ulist)
for i in range(0,userNum):

    string = getboard(Ulist[i]["boardId"],Ulist[i]["userId"])
    b_json = json.loads(string)
    rnd,ply,goals = parseboard(b_json,Ulist[i]["userId"])
    if(rnd == None):
        continue
    roundList.append(rnd)
    playerList.append(ply)

try:
    while(True):
        for i in range(0,len(roundList)):
            string = getboard(Ulist[i]["boardId"],Ulist[i]["userId"])
            b_json = json.loads(string)
            rnd,ply,goals = parseboard(b_json,Ulist[i]["userId"])
            if(rnd  == None):
                continue
            if(rnd > roundList[i]):
                postboard(Ulist[i]["boardId"],Ulist[i]["userId"],rnd,ply)

            roundList[i] = rnd
            playerList[i] = ply
            

        
        #time.sleep(0.5)
except (KeyboardInterrupt):
    for U in Ulist:
        deluser(U["boardId"],U["userId"])
    rollback()
    raise

