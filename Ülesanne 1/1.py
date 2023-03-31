from random import randint
from time import time

def contains_duplicates(list_n):
    for i in range(len(list_n)):
        for j in range(len(list_n)):
            if (i != j):
                if list_n[i] == list_n[j]:
                    return True
    return False

def contains_duplicates2(list_n):
    for i in range(len(list_n)):
        j = i+1
        for j in range(len(list_n)):
                if list_n[i] == list_n[j]:
                    return True
    return False

a = [randint(1, 100) for _ in range(1000)]
set_a = list(set(a))

print(f'Sisaldab duplikaate: {contains_duplicates(set_a)}')
print(f'Sisaldab duplikaate: {contains_duplicates2(set_a)}')