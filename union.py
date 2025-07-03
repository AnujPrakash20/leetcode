#Brute Force

# def union(arr1,arr2):
#     common = []
#     distinct = []
#     for i in arr1:
#         if i in arr2:
#             common.append(i)

#     for i in arr1:
#         if i not in arr2:
#             distinct.append(i)
    
#     for i in arr2:
#         if i not in arr1:
#             distinct.append(i)

#     final_array = common + distinct

#     return sorted(final_array)

# if __name__ == "__main__":
#     arr1 = [1,2,3,4,5,6,7,8,9,10]
#     arr2 = [2,3,4,4,5,11,12]
#     print(union(arr1,arr2))

# Optimal Approach

def union(arr1,arr2):
    final_array = []
    i,j = 0,0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j] and arr1[i] not in final_array:
            final_array.append(arr1[i])
            i+=1
        elif arr2[j] not in final_array:
            final_array.append(arr2[j])
            j+=1

    while i< len(arr1):
        if arr1[i] not in final_array:
            final_array.append(arr1[i])
            i+=1

    while j< len(arr2):
        if arr2[j] not in final_array:
            final_array.append(arr2[j])
            j+=1
     
    return final_array

if __name__ == "__main__":
    arr1 = [1,2,3,4,5,6,7,8,9,10]
    arr2 = [2,3,4,4,5,11,12]
    print(union(arr1,arr2))