#a program to remove the duplicates in a list
integers=[2,2,4,6,3,4,6,1]
uniques=[]
for integer in integers:
    if integer not in uniques:
        uniques.append(integer)
print(uniques)