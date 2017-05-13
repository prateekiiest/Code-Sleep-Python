import pandas as pd
df  = pd.read_stata(data_filepath + "individual_characteristics.dta")
df1 = df[df.village == 1]
df2 = df[df.village == 2]

# Enter code here!
df1.head()


sex1      = {df1.pid[i] : df1.resp_gend[i] for i in range(len(df1.pid))}
caste1    = {df1.pid[i] : df1.caste[i] for i in range(len(df1.pid))}
religion1 = {df1.pid[i] : df1.religion[i] for i in range(len(df1.pid))}
# Continue for df2 as well.

j = 203
sex2      = {df2.pid[j] : df2.resp_gend[j] for j in range(203,406)}
caste2    = {df2.pid[j] : df2.caste[j] for j in range(203,406) }
religion2 = {df2.pid[j] : df2.religion[j] for j in range(203,406)}



from collections import Counter
def chance_homophily(chars):
    # Enter code here!
    z = set(chars.values())
    su = 0
    for c in z:
        
        su = su + pow((sum(x == c for x in chars.values())/len(chars) * 1.0),2)
    
    return su

favorite_colors = {
    "ankit":  "red",
    "xiaoyu": "blue",
    "mary":   "blue"
}

color_homophily = chance_homophily(favorite_colors)
print(color_homophily)


    
print("Village 1 chance of same sex:", chance_homophily(sex1))
# Enter your code here.
print("Village 1 chance of same caste:", chance_homophily(caste1))
print("Village 1 chance of same religion:", chance_homophily(religion1))

print("Village 2 chance of same sex:", chance_homophily(sex2))
print("Village 2 chance of same religion:", chance_homophily(religion2))
print("Village 2 chance of same caste:", chance_homophily(caste2))



def homophily(G, chars, IDs):
    """
    Given a network G, a dict of characteristics chars for node IDs,
    and dict of node IDs for each node in the network,
    find the homophily of the network.
    """
    num_same_ties, num_ties = 0, 0
    for n1 in G.nodes():
        for n2 in G.nodes():
            if n1 > n2:   # do not double-count edges!
                if IDs[n1] in chars and IDs[n2] in chars:
                    if G.has_edge(n1, n2):
                        # Should `num_ties` be incremented?  What about `num_same_ties`?
                        num_ties += 1
                        if chars[IDs[n1]] == chars[IDs[n2]]:


    return (num_same_ties / num_ties)
    
    
print("Village 1 observed proportion of same sex:", homophily(G1, sex1, pid1))
print("Village 1 observed proportion of same caste:", homophily(G1, caste1, pid1))
print("Village 1 observed proportion of same religion:", homophily(G1, religion1, pid1))
# Enter your code here!
print("Village 2 observed proportion of same sex:", homophily(G2, sex2, pid2))
print("Village 2 observed proportion of same caste:", homophily(G2, caste2, pid2))
print("Village 2 observed proportion of same religion:", homophily(G1, religion2, pid2))





