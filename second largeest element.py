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
##bubble sort
arr=eval(input("Enter the list"))
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i]<arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
            
print(arr)

     
