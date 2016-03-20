import http.client
import json

def getboard(BID,UID):
    
    conn = http.client.HTTPConnection("172.17.183.204:80")

    headers = {
        'cache-control': "no-cache",
        'postman-token': "5e5caeea-7db4-040a-c246-62b9e37b6266"
        }

    conn.request("GET", "/api/board?board_id="+BID, headers=headers)

    res = conn.getresponse()
    data = res.read()
    
    #print(data.decode("utf-8"))
    return data.decode("utf-8")
