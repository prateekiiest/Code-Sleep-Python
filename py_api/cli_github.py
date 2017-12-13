import requests as rq
import getpass
user=str(input("GitHub Username: "))
pwd=getpass.getpass('Password: ')
params={'page':2}
r=rq.get("https://api.github.com/users/"+user+"/received_events",auth=(user,pwd))
data=r.json()
r=rq.get("https://api.github.com/users/"+user+"/received_events",auth=(user,pwd),params=params)
data.extend(r.json())
print("\n")
for i in range(len(data)):
    print(data[i]['actor']['display_login'] +" "+ data[i]['type'].replace("Watch","Star").replace("Event","")+" "+ data[i]['repo']['name'][:20] +" at "+ data[i]['repo']['url'].replace("api","www").replace("/repos",""))
