import http.client

def deluser(BID,UID):
    conn = http.client.HTTPConnection("172.17.183.204:80")

    headers = {
        'cache-control': "no-cache",
        'postman-token': "68bf90e9-6ab7-c0a6-1e69-ca2231238177",
        'content-type': "application/x-www-form-urlencoded"
        }

    conn.request("DELETE", "/api/user?user_id="+UID+"&board_id="+BID, headers=headers)

    res = conn.getresponse()
    data = res.read()

    #print(data.decode("utf-8"))
