mylist = [9,7,60,8,6]
n=len(mylist)
for i in range(1,n):
  current_val = mylist.pop(i)
  insert_index = i
  for j in range(i-1,-1,-1):
    if mylist[j] > current_val:
     insert_index = j
  mylist.insert(insert_index,current_val)
print(mylist)