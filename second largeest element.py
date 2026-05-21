def second_larget (arr):
  sorted_element=sorted(set(arr))
  if sorted_element <2:
    print("not having second largst element")
    return none
  return sorted_element[-2]

numbers=[1,3,2,6,6,7,8,8]
result=second_largest(numbers)
print("second largest eleement",result)
# 7
     
