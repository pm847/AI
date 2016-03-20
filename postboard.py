import http.client
import random

def postboard(BID,UID,Round,player,goal,mode = 0):
    
    conn = http.client.HTTPConnection("172.17.183.204:80")
    if(mode == 0):
        direction = random.randrange(4)
    elif(mode == 1):
        ls = []
        if(player.x < goal.x):
            ls.append(2)
        else:
            ls.append(3)
        if(player.y <goal.y):
            ls.append(0)
        else:
            ls.append(1)
        direction = random.sample(ls,1)
            
    #print(direction)
    if(direction == 2):
        nextX = player["x"] + 1 if player["x"] <39 else 39
        nextY = player["y"]
    elif(direction == 3):
        nextX = player["x"] - 1 if player["x"]  > 0 else 0
        nextY = player["y"]
    elif(direction == 0):
        nextX = player["x"]
        nextY = player["y"] + 1 if player["y"] <39 else 39
    else:
        nextX = player["x"]
        nextY = player["y"] - 1 if player["y"] > 0 else 0
    payload = "{\n    \"boardId\": \""+BID+"\",\n    \"userId\": \""+UID+"\",\n    \"nextRound\": "+str(Round)+",\n    \"nextMoveX\": "+str(nextX)+",\n    \"nextMoveY\":"+str(nextY)+" \n}"

    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "933beb72-8f57-09f3-9739-4f3a742c1217"
        }

    conn.request("POST", "/api/board", payload, headers)

    res = conn.getresponse()
    data = res.read()

    #print(data.decode("utf-8"))
    #return data.decode("utf-8")
