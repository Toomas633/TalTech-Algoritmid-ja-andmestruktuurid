# https://www.geeksforgeeks.org/combinations-with-repetitions/

valikud =[]
index = []

def CombinationRepetitionUtil(chosen, arr, index, r, start, end):
    if index == r:
        valikud.append([])
        for j in range(r):
            if chosen[j] != " ":
                valikud[len(valikud)-1].append(chosen[j])
            else:
                return
        return
    if start > n:
        return
    chosen[index] = arr[start]
    CombinationRepetitionUtil(chosen, arr, index + 1, r, start, end)
    CombinationRepetitionUtil(chosen, arr, index, r, start + 1, end)

def CombinationRepetition(arr, n, r):
    chosen = [0] * r
    CombinationRepetitionUtil(chosen, arr, 0, r, 0, n)
 
def kontroll(valikud):
    for i in range(len(valikud)):
        if valikud[i][0] == valikud[i][1]:
            index.append(i)
        elif valikud[i][0] == valikud[i][2]:
            index.append(i)
        elif valikud[i][1] == valikud[i][2]:
            index.append(i)
    if len(index) != 0:
        for j in sorted(index, reverse=True):
           del valikud[j]

arr = [ 1, 2, 3, 4, 5]
r = 3
n = len(arr) - 1

CombinationRepetition(arr, n, r)
kontroll(valikud)
print(valikud)