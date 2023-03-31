# https://www.geeksforgeeks.org/python-ways-to-remove-duplicates-from-list/
# Meetod 6 

sisend = [1, 4, 6, 7, 9, 9, 10]
print("Sisend: " + str(sisend).replace('[','').replace(']',''))
 
korrastatud = []
for i in sisend:
    if i not in korrastatud:
        korrastatud.append(i)
 
print("Korrastatud: " + str(korrastatud).replace('[','').replace(']',''))