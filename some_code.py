import copy
arr = [[1,2,3],[4,5,6]]
another_arr=copy.deepcopy(arr)

another_arr[0][0]='a'

print(id(arr))
print(id(another_arr))

print(arr)
print(another_arr)