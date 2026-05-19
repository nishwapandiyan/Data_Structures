

def binarySearch(arr, target):

  low = 0
  high = len(arr)-1

  while low <= high:
    mid = low +(high - low)//2
    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      low = mid+1
    else:
      high = mid-1
  return -1

mylist = list(map(int,input().split()))
target = 5
result = binarySearch(mylist, target)

if result != -1:
  print(f"Found at:{result}")
else:
  print("Not Found")