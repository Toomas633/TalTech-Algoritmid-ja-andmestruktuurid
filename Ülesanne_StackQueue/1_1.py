# https://realpython.com/reverse-string-python/#reversing-strings-with-recursion

def reversed_string(text):
    if len(text) == 1:
        return text
    return reversed_string(text[1:]) + text[:1]

sõned = ["õun","riis","madu","konn"]
pööratud = []

for i in sõned:
    pööratud.append(reversed_string(i))
    
print(sõned)
print(pööratud)