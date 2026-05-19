def linearSearch(arr, target):

  for i in range(len(arr)):
    if arr[i] == target:
      return i
  return -1

mylist = list(map(int, input().split()))
target = 5

result = linearSearch(mylist, target)

if result != -1:
  print(f"Found at {result}")
else:
  print("Not Found")