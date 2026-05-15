my_list = [[] for _ in range(0,10)]

def addName(name):

  sum = 0
  for ch in name:
    sum += ord(ch)
    sum %= 10
  my_list[sum].append(name)

def findName(name):
  sum = 0
  for ch in name:
    sum += ord(ch)
    sum %= 10

  return name in my_list[sum]

addName('Naveen')
addName('Bob')
addName('Nishwa')
addName('Nithish')

print(findName('Naveen'))
print(findName('Bob'))