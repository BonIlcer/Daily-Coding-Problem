# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?

def subList(sourceList, num):
  subList = []
  for elem in sourceList:
    subList.append(num - elem)
  return subList

def checkDuplicates(listOfElems):
    setOfElems = set()
    for elem in listOfElems:
        if elem in setOfElems:
            return True
        else:
            setOfElems.add(elem)         
    return False

def bonus(sourceList, num):
  difList = []
  for elem in sourceList:
    print(difList)
    for dif in difList:
      print("dif: ", dif, " elem: ", elem)
      if dif == elem:
        return True
    difList.append(num - elem)
  return False

sourceList = [15, 10, 7, 3]
number = 17
subList = subList(sourceList, number)

print("sourceList: ", sourceList)
print("number: ", number)
print("subList: ", subList)
# print("expandedList: ", sourceList + subList)
# print(checkDuplicates(sourceList + subList))

print(bonus(sourceList, number))