#===== Bubble Sort =====#

mylist = [8,7,6,5,4,3,2,1]
n= len(mylist)
for i in range(n-1):
  for j in range(n-i-1):
    if mylist[j] > mylist[j+1]:
      mylist[j+1], mylist[j] = mylist[j], mylist[j+1]
print(mylist)  