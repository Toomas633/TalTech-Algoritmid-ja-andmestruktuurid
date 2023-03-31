words = {'Sõna': [],'Hash': []}

def word_hash(word):
    total_value = 0
    for char in word.lower():
        total_value += ord(char) - ord('a')  + 1
    words['Sõna'].append(word)
    t = True
    while(t):
        if total_value not in words['Hash']:
            words['Hash'].append(total_value)
            t = False
        else:
            total_value += 1
            t = True        
        
f = open('The_Last_of_the_Mohicans-James_Fenimore_Cooper.txt', 'r')
text = f.read()
f.close()
arr = text.split()

for i in arr:
    j = i
    if '.' in j:
         j = j.replace('.','')
    if ',' in j:
        j = j.replace(',','')
    if '?' in j:
        j = j.replace('?','')
    if '!' in j:
        j = j.replace('!','')
    if "'" in j:
        j = j.replace("'",'')
    if '-' in j:
        j = j.replace('-','')
    if ':' in j:
        j = j.replace(':','')
    arr[arr.index(i)] = j.lower()

arr = list(dict.fromkeys(filter(None,arr)))    

for word in arr:
    word_hash(word)
for i in range(len(words['Sõna'])):
    print (f'{words["Sõna"][i]}\t\t{words["Hash"][i]}')