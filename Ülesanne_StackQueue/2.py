from random import randint
from time import sleep

järjekorrad = 3
ostja_arv = 10
ostjad = []
järjekord = []
run = True

for i in range(järjekorrad):
    järjekord.append([])

def ostja(ostja_arv):
    for i in range(ostja_arv):
        n = randint(1, 5)
        ostjad.append(n)
    
def jagamine(ostjad, järjekord, järjekorrad):
    for i in range(järjekorrad):
        järjekord[i].append(ostjad[i])
        del ostjad[i]
    for j in ostjad:    
        if sum(järjekord[0]) > sum(järjekord[1]):
            if sum(järjekord[1]) > sum(järjekord[2]):
                järjekord[2].append(j)
            else:
                järjekord[1].append(j)
        else:
            järjekord[0].append(j)

def eemaldamine(num, järjekord):
    for i in range(num):
        if sum(järjekord[i]) == 0:
            del järjekord[i]
        elif järjekord[i][0] == 0:
            del järjekord[i][0]
            if sum(järjekord[i]) == 0:
                del järjekord[i]
        else:
            järjekord[i][0] -= 1
            if järjekord[i][0] == 0:
                del järjekord[i][0]
                if sum(järjekord[i]) == 0:
                    del järjekord[i]
            elif sum(järjekord[i]) == 0:
                del järjekord[i]

ostja(ostja_arv)
jagamine(ostjad, järjekord, järjekorrad)

while(run):
    num = 0
    for i in järjekord:
        num += 1
    eemaldamine(num, järjekord)
    num = 0
    for i in järjekord:
        num += 1
    if num != 0:
        print("==================================")
        for i in range(num):
            print("järejekord", i+1,": ", järjekord[i])
        sleep(1)
        run = True
    else:
        run = False