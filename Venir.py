import matplotlib.pyplot as plt
import random
from Testbench import avgsplit
# making venir to the next safe level
lvl = 6
# number of sucessful attemps you want to simulate
n = 1000

#chance from 1 to 6
#item_chance= [50, 45, 40, 35, 50]
#chance from 6 to 12
item_chance= [45, 40, 35, 30, 25, 50]
#chance from 12 to 18 or 18 to 24
#item_chance= [35, 30, 25, 20, 15, 50]
# list to store the items used for each attempt that made to the desired lvl.
item_list = []

venir_frags = 0

for i in range(n):
    item_used = 1
    item_level = 0
    while item_level < lvl:
        item_used += 1
        if random.randrange(1,100) <= item_chance[item_level]:
            item_level += 1
        else:
            item_level = 0
    item_list.append(item_used)

# variables need for the histogram plot
item_list.sort()
maxlen = len(str(item_list[-1]))
rfactor = 10**(maxlen-2)/2-1
rnum = round(item_list[-1]+rfactor,-(maxlen-2))
bins = []
for i in range(round(rnum/(10**(maxlen-2)))):
    bins.append(i*10**(maxlen-2))

# calcaulating the average items used for sucessful attempts
totalused = 0
for i in range (n):
    totalused += item_list[i]

avgused = totalused/n

histplt = plt.hist(item_list,bins = bins)
#title = ("Average fragments used for Venir lvl1 - 6")
title = ("Average fragments used for Venir lvl6 - 12")
#title = ("Average fragments used for Venir lvl12-18 or 18-24")
plt.suptitle(title)
plt.title(avgused)

# piechart
labels = "Successful enchanting with below average items used", "Successful enchanting with above average items used"
sizes = [len(avgsplit(avgused,item_list,n)[0]),len(avgsplit(avgused,item_list,n)[1])]
colors = ['lightskyblue','lightcoral']

plt.figure(figsize=(10,5))
plt.pie(sizes,labels=labels,colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')

plt.show()


