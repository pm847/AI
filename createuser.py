import http.client

def createuser(name):
    conn = http.client.HTTPConnection("172.17.183.204")

    payload = "name="+str(name)

    headers = {
        'cache-control': "no-cache",
        'postman-token': "e102b6d6-bc1d-b386-4298-b333810e3390",
        'content-type': "application/x-www-form-urlencoded"
        }

    conn.request("POST", "/api/user", payload, headers)

    res = conn.getresponse()
    data = res.read()

    #print(data.decode("utf-8"))
    return data.decode("utf-8")
