import requests
import notify2
import json

url = "http://cricapi.com/api/matches?apikey=D18haZnedRZ3QijAQEJJV97U5r23"
r = requests.get(url)
print(r)
print(r.text)

data = json.loads(r.text)
print(data)
print(data['matches'][0])
print (data['matches'][0]['team-1'])

id=""
for item in data['matches']:
    if (item['team-1']=="India" or item["team-2"]=="India"):
        print(item)
        if item["matchStarted"]:
            id=item["unique_id"]
print(id)

if id:
    r = requests.get("http://cricapi.com/api/cricketScore?apikey=D18haZnedRZ3QijAQEJJV97U5r23&unique_id="+str(id))
    score = json.loads(r.text)
    print(score)
print(score['score'])
print(score['stat'])

notify2.init("Cric - Notify")
n = notify2.Notification(score["stat"], score["score"], "system")
n.show()
