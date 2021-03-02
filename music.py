import http.client

conn = http.client.HTTPSConnection("deezerdevs-deezer.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "bcd47eac68mshe3ce8d7db0f5cf2p1cbc65jsn4367b30fca5b",
    'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com"
    }

conn.request("GET", "/search?q=Jazz", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
#This code leads too my Dezzer api. This Api is used too pull muisc from a database.