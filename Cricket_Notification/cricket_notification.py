
# coding: utf-8

# In[2]:


url = "http://cricapi.com/api/matches?apikey=D18haZnedRZ3QijAQEJJV97U5r23"


# In[3]:


import requests


# In[4]:


import notify2


# In[5]:


r = requests.get(url)


# In[6]:


print(r)


# In[7]:


print r.text


# In[8]:


import json


# In[10]:


data = json.loads(r.text)
print data


# In[11]:


print(data['matches'][0])


# In[12]:


print (data['matches'][0]['team-1'])


# In[20]:


id=""
for item in data['matches']:
    if (item['team-1']=="India" or item["team-2"]=="India"):
        print item
        if item["matchStarted"]:
            id=item["unique_id"]


# In[14]:


print id


# In[18]:


if id:
    r = requests.get("http://cricapi.com/api/cricketScore?apikey=D18haZnedRZ3QijAQEJJV97U5r23&unique_id="+str(id))
    score = json.loads(r.text)
    print score


# In[19]:


print score['score'] 
print score['stat']


# In[17]:


notify2.init("Cric - Notify")
n = notify2.Notification(score["stat"],
                         score["score"],
                         "system"   # Icon name
                        )
n.show()

