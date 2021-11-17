import sqlite3
con = sqlite3.connect(r'G:\sqlite\gui\valorantLineups')
cur = con.cursor()
cur.execute("select * from Agent")
agents = cur.fetchall()

cur.execute("select * from Map")
maps = cur.fetchall()

#Prompting agent selection.
from typing import TYPE_CHECKING

print("What agent are you playing?")
while True:
    selectedAgent = input(" ").lower() 
    agent = list(filter(lambda x: x[1] == selectedAgent, agents))
    if len(agent) > 0: 
        print("You selected", selectedAgent,)
        break
    else:
       print("That agent is not supported") 

 
#Prompting map selection

print("What map are you on?")
while True:
    selectedMap = input(" ").lower()
    map = list(filter(lambda x: x[1].lower() == selectedMap, maps))
    if len(map) > 0:
        print("You selected", selectedMap,)
        break
    else:
        print("That map is not supported")

#sqlite database accessing possible agent/map combos

lineupssql = "select * from Lineup where AgentID=? and MapID=?"
args = (agent[0][0], map[0][0])
cur.execute (lineupssql, args) 
lineups = cur.fetchall()
print(lineups)
print(lineups[1][4])
print("egg")
