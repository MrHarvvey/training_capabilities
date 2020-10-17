



stringa= "xxcaazzxxaaxxxaaaaxxaxxaxaxaxxa"
list2 = list()
for i in range(len(stringa)):
  nowa_zmienna = stringa[i:i+2]
  list2.append(nowa_zmienna)

list2 = list2[:-1]
count = 0
for w in list2:
  if w in stringa:
    count=+1
print(count)
