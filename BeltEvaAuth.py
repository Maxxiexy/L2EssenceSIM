import matplotlib.pyplot as plt
import random
import statistics
from Testbench import avgsplit
# level of item you want to make
lvl = 5
# number of sucessful attemps you want to simulate
n = 1000

item_chance= [60, 50, 40, 35, 30, 28, 26, 24, 22, 20]
# list to store the items used for each attempt that made to the desired lvl.
item_list = []

for i in range(n):
    item_used = 1
    item_level = 0
    while item_level < lvl:
        if random.randrange(1,100) <= item_chance[item_level]:
            item_level += 1
        else:
            item_used += 1
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

print(statistics.stdev(item_list))

histplt = plt.hist(item_list,bins = bins)
title = ("Average item used for Belt/Eva/Auth level", lvl)
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


