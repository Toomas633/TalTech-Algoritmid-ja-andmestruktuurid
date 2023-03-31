# Ülesanne 2 Toomas Kirsing
# Damerau–Levenshtein distance: https://blog.paperspace.com/implementing-levenshtein-distance-word-autocomplete-autocorrect/
# Failis asendamine https://stackoverflow.com/questions/17140886/how-to-search-and-replace-text-in-a-file
#! pip install numpy 
import numpy

f = open('EnglishDictionary.txt','r')
sõnastik = f.read()
f.close()
sõnastik = sõnastik.split()

def import_text():
    f = open('The_Last_of_the_Mohicans-James_Fenimore_Cooper.txt', 'r')
    text = f.read()
    f.close()
    text = text.split()
    for i in text:
        j = i
        if '.' in j:
            j = j.replace('.','')
        if ',' in j:
            j = j.replace(',','')
        if '?' in j:
            j = j.replace('?','')
        if '!' in j:
            j = j.replace('!','')
        if ':' in j:
            j = j.replace(':','')
        text[text.index(i)] = j
    return text

def levenshteinDistanceDP(token1, token2):
    distances = numpy.zeros((len(token1) + 1, len(token2) + 1))
    for t1 in range(len(token1) + 1):
        distances[t1][0] = t1
    for t2 in range(len(token2) + 1):
        distances[0][t2] = t2
    a = 0
    b = 0
    c = 0
    for t1 in range(1, len(token1) + 1):
        for t2 in range(1, len(token2) + 1):
            if (token1[t1-1] == token2[t2-1]):
                distances[t1][t2] = distances[t1 - 1][t2 - 1]
            else:
                a = distances[t1][t2 - 1]
                b = distances[t1 - 1][t2]
                c = distances[t1 - 1][t2 - 1]
                
                if (a <= b and a <= c):
                    distances[t1][t2] = a + 1
                elif (b <= a and b <= c):
                    distances[t1][t2] = b + 1
                else:
                    distances[t1][t2] = c + 1
    return distances[len(token1)][len(token2)]

def calcDictDistance(word, sõnastik):
    numWords = 3 # Mitu sõna pakutakse
    lines = sõnastik
    dictWordDist = []
    wordIdx = 0
    for line in lines: 
        wordDistance = levenshteinDistanceDP(word, line.strip())
        if wordDistance >= 10:
            wordDistance = 9
        dictWordDist.append(str(int(wordDistance)) + "-" + line.strip())
        wordIdx = wordIdx + 1
    closestWords = []
    wordDetails = []
    currWordDist = 0
    dictWordDist.sort()
    for i in range(numWords):
        currWordDist = dictWordDist[i]
        wordDetails = currWordDist.split("-")
        closestWords.append(wordDetails[1])
    return closestWords

def salvesta_sõnastik(sõnastik):
    sõnastik.sort()
    f = open('EnglishDictionary.txt', 'w')
    f.seek(0)
    for i in sõnastik:
        f.write(f'\n{str(i)}')
    f.truncate()
    f.close()
    exit(0)

def kontroll(text, sõnastik):
    vigased = []
    for i in text:
        if i.lower() not in sõnastik:
            vigased.append(i)
    vigased = [x for x in vigased if not x.isdigit()]
    return vigased

def salvesta_faili(sõna, parandatav):
    with open('The_Last_of_the_Mohicans-James_Fenimore_Cooper.txt', 'r') as file:
        filedata = file.read()
    filedata = filedata.replace(parandatav, sõna, 1)
    with open('The_Last_of_the_Mohicans-James_Fenimore_Cooper.txt', 'w') as file:
        file.write(filedata)

def lähimad(sõna, sõnastik):
    check = True
    suur = any(ele.isupper() for ele in sõna)
    print(suur)
    tmp = sõna
    tmp = tmp.lower()
    lähimad = calcDictDistance(tmp, sõnastik)
    while check:
        print(f'\nVali sobiv asendus sõnale "{sõna}":')
        j = 1
        for i in lähimad:
            print(f'{j}) {i}')
            j += 1
        print('0) -- Tagasi --')
        try:
            sisend = int(input("> "))
            if sisend == 0:
                pass
                check = False
            elif sisend == 1:
                print(f'Sõna "{lähimad[0]}" asendatud faili!')
                if suur == True: 
                    salvesta_faili(lähimad[0].capitalize(), sõna)
                else:
                    salvesta_faili(lähimad[0], sõna)
                check = False
            elif sisend == 2:
                print(f'Sõna "{lähimad[1]}" asendatud faili!')
                if suur == True:     
                    salvesta_faili(lähimad[1].capitalize(), sõna)
                else:
                    salvesta_faili(lähimad[1], sõna)
                check = False
            elif sisend == 3:
                if suur == True:     
                    salvesta_faili(lähimad[2].capitalize(), sõna)
                else:
                    salvesta_faili(lähimad[2], sõna)
                check = False
            else:
                print('Sisesta number valikust!')
                check = True
        except ValueError:
            print('Sisesta number valikust!')
            check = True
    
def main(sõnastik):
    text = import_text()
    vigased = kontroll(text, sõnastik)
    while(len(vigased) != 0):
        check = True
        for i in vigased:
            while check:
                print(f'\nSõna "{i}" ei leitud sõnastikust!')
                print('1) Lisa sõnastikku')
                print('2) Paranada sõna tekstis')
                print('3) Salvesta ja välju')
                print('4) Välju salvestamata')
                sisend = input("> ")
                try:
                    sisend = int(sisend)
                    if sisend == 1:
                        sõnastik.append(i.lower())
                        print(f'Sõna "{i}" lisatud sõnastikku!')
                        vigased = kontroll(text, sõnastik)
                        check = False
                    elif sisend == 2:
                        lähimad(i, sõnastik)
                        text = import_text()
                        vigased = kontroll(text, sõnastik)
                        check = False
                    elif sisend == 3:
                        check = False
                        salvesta_sõnastik(sõnastik)
                    elif sisend == 4:
                        exit(0)
                    else:
                        print('Sisesta number valikust!')
                        check = True
                except ValueError:
                    print('Sisesta number valikust!')
                    check = True
    
main(sõnastik)