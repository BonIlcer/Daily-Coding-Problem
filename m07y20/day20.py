print("20/07/2020")
# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?

def solution(sourceList):
  result = []
  for elem in sourceList:
    tmpList = list(sourceList)
    tmpList.remove(elem)
    #print(tmpList)
    count = 1
    for tmpElem in tmpList:
      count *= tmpElem
    result.append(count)
  return result

sourceList = [1, 2, 3, 4, 5]

result = solution(sourceList)
print("sourceList: ", sourceList)
print("result: ", result)